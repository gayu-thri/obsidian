#### Installation
- Links
	- https://docs.lilacml.com/getting_started/installation.html
	- https://docs.lilacml.com/deployment/self_hosted.html
	  
- **From pypi, via command line**
	- $ *pip install lilac[all]*
	  
- **From existing Lilac project, via docker**
	- **ISSUE**: On using the command, opens only a nginx server page
	- $ *docker pull lilacai/lilac*
	- OR
	- $ *git clone https://github.com/lilacai/lilac.git*
	  $ *docker build -t lilac .*
	```bash
	  docker run -it \
  -p 5432:80 \
  --volume /host/path/to/data:/data \
  -e LILAC_PROJECT_DIR="/data" \
  lilac
	```
	- To use all GPUs
		```bash
		 --gpus all 
		```
	- To use a specific GPU
		```bash
		--gpus device=0
		```

- **Command I used and is hosting the application correctly** 
	- http://172.21.168.254:5432/
	```bash
	docker run -it --platform=linux/amd64 -p 5432:80 --volume /media/data/gayu/workspace/llm/lilac/:/data -e LILAC_PROJECT_DIR="/data" lilacai/lilac
	```

- #### Hosting using docker
	- Computing embedding
		- Example: **Dialogsum**
			- Without GPU: **11 mins 25 secs**
			- With GPU: **1 min 18 secs**
		- Approximately, 90% drop in time when using single GPU instead of CPU
		- ![[Pasted image 20240301125750.png]]
	- Loading from a file path works fine
		- Example: parquet, zst, etc
			- ![[Pasted image 20240301082824.png]]
	
	- ### LOADING FROM HF ISSUE
		- When hosting using docker, on loading a dataset from HuggingFace, an error occurs
			```bash
			Fatal Python error: PyGILState_Release: 
			thread state 0x55d9282d0b80 must be current when releasing
			Python runtime state: finalizing (tstate=0x00007fe7c79851f8)
			Thread 0x00007fe7c714b740 (most recent call first):
			  <no Python frame>
			```
			- When num_proc in load_dataset is set from CPU count to 1, error is gone but the server gets killed anyway
				- ![[Pasted image 20240301084051.png]]
	- Full error trace back
```bash
Downloading readme: 100%|█████████████████████████████████████████████████████████████████| 6.03k/6.03k [00:00<00:00, 15.7MB/s]
					Downloading data: 100%|███████████████████████████████████████████████████████████████████| 3.61M/3.61M [00:00<00:00, 7.84MB/s]
					Downloading data: 100%|███████████████████████████████████████████████████████████████████| 3.66M/3.66M [00:00<00:00, 4.23MB/s]
					Downloading data: 100%|███████████████████████████████████████████████████████████████████| 38.3M/38.3M [00:02<00:00, 13.8MB/s]
					Setting num_proc from 24 back to 1 for the train split to disable multiprocessing as it only contains one shard.0:00, 17.9MB/s]
					Generating train split:   0%|                                                                 | 0/23652 [00:00<?, ? examples/s]INFO:     Shutting down
					INFO:     Finished server process [1]
					Fatal Python error: PyGILState_Release: thread state 0x55d9282d0b80 must be current when releasing
					Python runtime state: finalizing (tstate=0x00007fe7c79851f8)
					
					Thread 0x00007fe7c714b740 (most recent call first):
					  <no Python frame>
					
					Extension modules: uvloop.loop, httptools.parser.parser, httptools.parser.url_parser, websockets.speedups, numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, psutil._psutil_linux, psutil._psutil_posix, sklearn.__check_build._check_build, scipy._lib._ccallback_c, scipy.sparse._sparsetools, _csparsetools, scipy.sparse._csparsetools, scipy.linalg._fblas, scipy.linalg._flapack, scipy.linalg.cython_lapack, scipy.linalg._cythonized_array_utils, scipy.linalg._solve_toeplitz, scipy.linalg._flinalg, scipy.linalg._decomp_lu_cython, scipy.linalg._matfuncs_sqrtm_triu, scipy.linalg.cython_blas, scipy.linalg._matfuncs_expm, scipy.linalg._decomp_update, scipy.sparse.linalg._dsolve._superlu, scipy.sparse.linalg._eigen.arpack._arpack, scipy.sparse.csgraph._tools, scipy.sparse.csgraph._shortest_path, scipy.sparse.csgraph._traversal, scipy.sparse.csgraph._min_spanning_tree, scipy.sparse.csgraph._flow, scipy.sparse.csgraph._matching, scipy.sparse.csgraph._reordering, scipy.spatial._ckdtree, scipy._lib.messagestream, scipy.spatial._qhull, scipy.spatial._voronoi, scipy.spatial._distance_wrap, scipy.spatial._hausdorff, scipy.special._ufuncs_cxx, scipy.special._ufuncs, scipy.special._specfun, scipy.special._comb, scipy.special._ellip_harm_2, scipy.spatial.transform._rotation, scipy.ndimage._nd_image, _ni_label, scipy.ndimage._ni_label, scipy.optimize._minpack2, scipy.optimize._group_columns, scipy.optimize._trlib._trlib, scipy.optimize._lbfgsb, _moduleTNC, scipy.optimize._moduleTNC, scipy.optimize._cobyla, scipy.optimize._slsqp, scipy.optimize._minpack, scipy.optimize._lsq.givens_elimination, scipy.optimize._zeros, scipy.optimize._highs.cython.src._highs_wrapper, scipy.optimize._highs._highs_wrapper, scipy.optimize._highs.cython.src._highs_constants, scipy.optimize._highs._highs_constants, scipy.linalg._interpolative, scipy.optimize._bglu_dense, scipy.optimize._lsap, scipy.optimize._direct, scipy.integrate._odepack, scipy.integrate._quadpack, scipy.integrate._vode, scipy.integrate._dop, scipy.integrate._lsoda, scipy.special.cython_special, scipy.stats._stats, scipy.stats.beta_ufunc, scipy.stats._boost.beta_ufunc, scipy.stats.binom_ufunc, scipy.stats._boost.binom_ufunc, scipy.stats.nbinom_ufunc, scipy.stats._boost.nbinom_ufunc, scipy.stats.hypergeom_ufunc, scipy.stats._boost.hypergeom_ufunc, scipy.stats.ncf_ufunc, scipy.stats._boost.ncf_ufunc, scipy.stats.ncx2_ufunc, scipy.stats._boost.ncx2_ufunc, scipy.stats.nct_ufunc, scipy.stats._boost.nct_ufunc, scipy.stats.skewnorm_ufunc, scipy.stats._boost.skewnorm_ufunc, scipy.stats.invgauss_ufunc, scipy.stats._boost.invgauss_ufunc, scipy.interpolate._fitpack, scipy.interpolate.dfitpack, scipy.interpolate._bspl, scipy.interpolate._ppoly, scipy.interpolate.interpnd, scipy.interpolate._rbfinterp_pythran, scipy.interpolate._rgi_cython, scipy.stats._biasedurn, scipy.stats._levy_stable.levyst, scipy.stats._stats_pythran, scipy._lib._uarray._uarray, scipy.stats._ansari_swilk_statistics, scipy.stats._sobol, scipy.stats._qmc_cy, scipy.stats._mvn, scipy.stats._rcont.rcont, scipy.stats._unuran.unuran_wrapper, sklearn.utils._isfinite, sklearn.utils.murmurhash, sklearn.utils._openmp_helpers, sklearn.utils._random, sklearn.utils._seq_dataset, sklearn.utils.sparsefuncs_fast, sklearn.metrics.cluster._expected_mutual_info_fast, sklearn.preprocessing._csr_polynomial_expansion, sklearn.preprocessing._target_encoder_fast, sklearn.metrics._dist_metrics, sklearn.metrics._pairwise_distances_reduction._datasets_pair, sklearn.utils._cython_blas, sklearn.metrics._pairwise_distances_reduction._base, sklearn.metrics._pairwise_distances_reduction._middle_term_computer, sklearn.utils._heap, sklearn.utils._sorting, sklearn.metrics._pairwise_distances_reduction._argkmin, sklearn.metrics._pairwise_distances_reduction._argkmin_classmode, sklearn.utils._vector_sentinel, sklearn.metrics._pairwise_distances_reduction._radius_neighbors, sklearn.metrics._pairwise_distances_reduction._radius_neighbors_classmode, sklearn.metrics._pairwise_fast, sklearn.linear_model._cd_fast, sklearn._loss._loss, sklearn.utils.arrayfuncs, sklearn.svm._liblinear, sklearn.svm._libsvm, sklearn.svm._libsvm_sparse, sklearn.utils._weight_vector, sklearn.linear_model._sgd_fast, sklearn.linear_model._sag_fast, pyarrow.lib, pyarrow._hdfsio, charset_normalizer.md, yaml._yaml, pandas._libs.tslibs.ccalendar, pandas._libs.tslibs.np_datetime, pandas._libs.tslibs.dtypes, pandas._libs.tslibs.base, pandas._libs.tslibs.nattype, pandas._libs.tslibs.timezones, pandas._libs.tslibs.fields, pandas._libs.tslibs.timedeltas, pandas._libs.tslibs.tzconversion, pandas._libs.tslibs.timestamps, pandas._libs.properties, pandas._libs.tslibs.offsets, pandas._libs.tslibs.strptime, pandas._libs.tslibs.parsing, pandas._libs.tslibs.conversion, pandas._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.lib, pyarrow._compute, pandas._libs.ops, pandas._libs.hashing, pandas._libs.arrays, pandas._libs.tslib, pandas._libs.sparse, pandas._libs.internals, pandas._libs.indexing, pandas._libs.index, pandas._libs.writers, pandas._libs.join, pandas._libs.window.aggregations, pandas._libs.window.indexers, pandas._libs.reshape, pandas._libs.groupby, pandas._libs.json, pandas._libs.parsers, pandas._libs.testing, google._upb._message, multidict._multidict, yarl._quoting_c, aiohttp._helpers, aiohttp._http_writer, aiohttp._http_parser, aiohttp._websocket, frozenlist._frozenlist, pyarrow._parquet, pyarrow._fs, pyarrow._hdfs, pyarrow._gcsfs, pyarrow._s3fs, xxhash._xxhash, pyarrow._json, regex._regex, markupsafe._speedups, _cffi_backend, scipy.io.matlab._mio_utils, scipy.io.matlab._streams, scipy.io.matlab._mio5_utils (total: 217)
```
#### References
- https://github.com/lilacai/lilac/issues/737
	- Above docker run command taken from this issue