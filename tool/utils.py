from lib_pickle import pickle


def isFile(args, a, path):
    if args.file == 1:
        with open(path, "wb") as f:
            pickle.dump(a, f)
