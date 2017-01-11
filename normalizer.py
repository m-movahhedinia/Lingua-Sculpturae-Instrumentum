def normal(action, element, source, corpus):
    if action is "replace":
        corpus = corpus.replace(source, element)
    elif action is "remove":
        corpus = corpus.strip(element)
    elif action is "split":
        corpus = corpus.split(element)
    else:
        pass
    return corpus
