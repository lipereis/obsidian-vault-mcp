"""Varre configurações do reranker: qualidade (paráfrases+exatos) x latência."""
import itertools, sys, time, io, contextlib
import server as s, semantic
with contextlib.redirect_stdout(io.StringIO()):
    sys.argv = ["x"]; import eval_semantic as e
notes = s._semantic_notes()
semantic.hybrid_search("aquecimento", notes, s.VAULT, 3)
import numpy as np
chunks, _, _ = semantic.build(notes, s.VAULT)
L = [len(c["text"]) for c in chunks]
print("chunks", len(L), "chars p50/p90/max", int(np.percentile(L,50)), int(np.percentile(L,90)), max(L))
def run(**kw):
    out = []
    for cases in (e.CASES, e.EXACT):
        hit = top1 = 0; mrr = 0.0
        for q, exp in cases:
            st = [c["path"].rsplit("/",1)[-1][:-3] for _, c in semantic.hybrid_search(q, notes, s.VAULT, 3, **kw)]
            r = next((i+1 for i, x in enumerate(st) if x in exp), 0)
            hit += bool(r); top1 += r == 1; mrr += 1/r if r else 0
        out.append(f"{hit}/{top1}/{mrr/len(cases):.2f}")
    return out
print("pool batch  parafr(r3/t1/mrr)  exatos  ms", flush=True)
for pool, bs in ((30, 0), (30, 16), (30, 8), (30, 4), (30, 2), (40, 4)):
    t = time.time(); a, b = run(pool=pool, batch_size=bs)
    print(f"{pool:>4} {bs:>5}  {a:>12}  {b:>12}  {(time.time()-t)/25*1000:.0f}", flush=True)
