import fasttext
import gensim
import numpy
import flask
import spacy
import argparse
import os


app = flask.Flask(__name__)
scores = {}


def file_exists(x):
    if not os.path.isfile(x):
        import argparse
        raise argparse.ArgumentTypeError("{0} is not a file".format(x))
    return x


def init(args):
	global model
	global nlp
	model = fasttext.load_model(args.model)
	nlp = spacy.load(args.language)
	

@app.route('/fasttext', methods=['POST'])
def fasttext_sim():
	if not flask.request.json or not 'entities' in flask.request.json or not 'text' in flask.request.json or not 'mention' in flask.request.json:
		flask.abort(400)

	clean_text = [token.orth_ for token in nlp(flask.request.json['text']) if not (token.is_punct or token.is_stop or token.is_space or token.orth_ == flask.request.json['mention'])]

	for entity in flask.request.json['entities']:
		clean_entity = [token.orth_ for token in nlp(entity) if not (token.is_punct or token.is_stop or token.is_space)]
		v1 = [model[word] for word in clean_entity]
		v2 = [model[word] for word in clean_text]
		scores[entity] = numpy.dot(gensim.matutils.unitvec(numpy.array(v1).mean(axis=0)), gensim.matutils.unitvec(numpy.array(v2).mean(axis=0)))
    
	return flask.jsonify({flask.request.json['mention']: scores}), 200

def main():
	parser = argparse.ArgumentParser(description="Webapp for entity linking using fastText in a given language", prog="fasttext_app")
	parser.add_argument("-l", "--language", required=True, help="Set the language")
	parser.add_argument("-m", "--model", required=True, type=file_exists, help="Set the fastText model")
	parser.add_argument("-p", "--port", required=True, type=int, help="Set the port")
	parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

	args = parser.parse_args()

	init(args)

	app.run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
	main()
