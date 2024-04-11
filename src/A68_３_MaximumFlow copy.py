import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
400 399
78 39 2253
76 351 2341
35 84 205
66 116 2418
135 169 4463
204 295 577
155 93 3944
370 59 4730
277 372 4499
357 156 711
185 350 1160
289 288 2035
245 251 2472
327 30 2729
358 20 3342
312 378 864
356 63 1035
176 279 1806
310 267 2458
70 21 2732
93 326 1165
352 131 4485
282 236 820
211 3 2087
92 17 802
290 200 2748
308 354 1149
248 174 407
151 10 1274
286 379 2766
160 224 3702
140 389 692
53 121 3256
266 344 2522
239 342 775
94 137 3420
231 47 1966
107 151 231
182 283 1602
40 316 884
316 33 2361
330 190 2263
349 253 4950
81 138 1404
69 118 982
49 280 2521
68 69 2890
301 309 2828
383 387 1539
208 336 3272
112 213 2718
119 85 3269
133 250 1669
186 9 367
134 339 2896
198 321 1875
321 191 837
15 386 2964
285 301 2345
34 38 1529
230 269 1467
294 46 377
307 198 3275
351 23 2072
265 376 2379
353 181 73
97 196 380
130 41 1899
80 134 1742
121 277 1096
212 340 3077
269 32 2208
48 144 3029
227 136 3757
141 233 3601
363 90 2486
367 368 1088
194 65 1312
240 55 4670
126 320 4968
337 124 3050
104 317 410
83 232 597
118 26 3174
292 150 3868
179 194 2471
41 254 4285
273 299 3147
25 78 1686
63 357 1991
192 58 3595
167 159 3040
102 293 2551
38 155 4796
116 310 2820
16 361 3377
11 175 2436
338 305 4823
32 330 266
188 380 1240
270 48 4736
13 75 2123
280 312 4986
365 366 3548
254 145 487
196 221 85
85 54 1681
163 227 3639
75 282 2410
399 276 1667
332 202 4710
147 129 781
387 114 4440
26 315 4500
191 238 1497
224 235 2215
396 29 3398
108 109 3619
54 307 2211
124 212 4665
384 234 4309
261 122 2678
175 338 686
10 334 547
334 95 1905
398 5 3744
203 373 2108
73 298 1818
3 381 3097
74 132 2635
132 157 1495
157 104 2433
146 154 4215
317 256 3642
207 14 803
379 360 3871
299 270 4557
89 81 3635
172 197 4121
260 385 4809
244 222 1674
278 89 4779
27 125 3474
17 176 3698
181 66 3263
217 115 4767
375 264 4015
279 70 3933
86 195 4971
393 284 1284
195 341 2200
341 34 3908
28 303 3459
193 99 4852
333 2 816
249 171 1567
326 278 4191
395 375 2215
283 135 3199
1 76 4942
329 185 366
380 252 3959
234 167 2703
306 328 3827
199 162 4355
162 43 396
43 148 720
148 369 750
348 105 1448
20 325 4614
288 143 4390
255 149 2298
158 117 2594
19 27 2167
71 199 4617
90 297 4579
127 147 1155
222 377 2638
183 247 2873
324 153 1098
378 261 3689
51 96 378
180 248 2626
319 263 4522
190 87 4211
344 285 2099
111 142 443
243 244 4839
318 346 2170
202 259 2657
284 395 1958
247 220 4209
64 240 2087
100 57 4874
59 217 587
328 128 3772
237 210 4171
169 158 3675
331 11 1621
117 201 4087
229 6 3420
136 15 2722
109 271 503
206 35 4082
295 314 4632
320 396 3463
105 400 4814
14 209 3655
213 16 608
381 152 2048
18 231 2090
373 100 3027
276 327 520
174 286 3501
150 119 3317
275 112 1657
233 25 3032
364 205 4043
67 68 3709
228 370 1190
214 343 1928
303 359 4435
201 56 158
4 292 4443
350 61 714
221 108 2984
335 31 854
137 218 2280
215 94 902
342 382 4167
223 71 2953
304 102 4778
343 333 2871
129 74 447
110 97 2139
65 308 2966
142 226 359
264 348 4096
302 331 1229
219 50 2000
153 64 4612
242 243 1048
361 318 1532
313 355 428
178 183 69
171 397 2935
220 51 2296
145 300 2214
272 36 4160
205 60 4480
45 349 1043
345 204 2038
164 91 461
323 371 2559
241 311 1639
37 130 4269
271 249 2346
216 392 3263
392 260 410
62 107 4553
79 206 1820
6 329 3287
166 246 1097
144 111 493
369 170 3331
52 223 978
252 268 289
120 18 4394
382 374 2398
258 82 3617
225 290 3948
297 391 2620
84 83 3516
355 40 887
354 347 2695
7 245 3294
251 77 1109
103 110 3422
99 53 331
115 294 2790
152 362 1146
50 304 2089
173 215 1669
122 139 459
139 133 2350
236 383 3519
250 187 2903
187 98 2295
98 388 4676
259 306 3683
138 52 2025
101 7 1989
113 358 664
210 160 506
24 179 2151
154 168 4342
31 165 3534
91 274 916
268 44 2886
170 287 4207
347 28 3954
33 230 578
388 113 3913
359 266 2467
257 103 688
339 203 616
238 106 85
263 186 3529
281 45 1211
366 367 2332
9 332 2663
200 163 2929
360 141 4666
298 184 1697
44 258 984
156 324 1597
22 239 2822
394 192 3396
389 302 3649
47 173 1694
114 322 3265
322 193 2775
218 219 268
87 4 3282
30 49 1765
391 140 656
293 12 2845
390 189 1187
72 161 764
42 394 1089
96 319 4411
12 225 3176
267 86 829
325 24 2898
296 172 4714
336 337 3352
184 13 3166
235 242 4451
21 22 2234
61 101 3369
209 120 4047
161 398 2569
2 296 3886
149 19 2321
189 265 4172
374 180 1100
77 92 3545
197 228 2552
340 123 1491
314 207 1241
309 241 654
23 229 3984
385 262 146
5 323 123
46 356 1166
55 365 1424
305 291 4085
60 177 2384
397 275 798
159 237 887
125 8 3193
128 88 4828
315 37 1007
274 399 3067
287 255 1915
56 345 3505
123 214 4499
29 363 3902
131 364 2324
346 62 337
246 188 4606
57 146 2693
168 211 4325
376 67 1956
8 178 4361
371 208 3672
58 216 4891
300 79 4364
262 166 4999
291 257 619
377 289 489
368 80 2182
362 335 3975
232 126 4099
106 272 1091
165 352 922
88 182 425
36 390 4399
253 42 2553
143 281 1871
386 384 4383
177 393 4336
372 72 2117
226 353 3423
95 127 1455
311 73 56
82 164 3311
39 313 2198
256 273 2605
"""
sys.stdin = io.StringIO(_INPUT)
"""
N 個のタンクと M 本のパイプがあります、j 本目のパイプはタンク A j​  からタンク B j​  の方向に毎秒 C j​  リットルまで水を流すことができます。
タンク 1 からタンク N まで毎秒最大何リットルの水を流すことができますか。ただし、タンクに水を貯めることはできないと考えてかまいません。

#全探索で実現してみる。
#この問題用のライブラリがあるのでそれを利用。
#graph構築でmaxFlowが算出できる
"""
from atcoder.maxflow import MFGraph

n, m = map(int, input().split())
graph = MFGraph(n)
for i in range(m):
    a, b, c = map(int, input().split())
    #グラフ構築 解答も出る
    graph.add_edge(a - 1, b - 1, c)
print(graph.flow(0, n - 1))
"""
from typing import NamedTuple, Optional, List, cast


class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited
"""
