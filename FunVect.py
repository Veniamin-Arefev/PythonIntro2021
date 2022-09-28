def superposition(funmod, funseq):
    return [(lambda x, i=i: funmod(funseq[i](x))) for i in range(len(funseq))]
