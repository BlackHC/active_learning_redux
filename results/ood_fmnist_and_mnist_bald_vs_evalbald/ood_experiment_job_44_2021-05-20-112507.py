store = {}
store['timestamp']=1621506307
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=44']
store['commit']='35841c01d6111c8009c59adebde0572fb40fe6d5'
store['github_url']='35841c01d6111c8009c59adebde0572fb40fe6d5'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=44
store['worker_id']=44
store['num_workers']=80
store['config']={'seed': 1280, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.294921398162842})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.518319606781006})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6294047832489014})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.172921657562256})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7933828830718994})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 2.302290625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 1981], ['id', 50740], ['id', 36826], ['id', 5728], ['id', 22845]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2443921996342016, 2.27698101432187, 3.0838843214831737, 3.6819913091949363, 4.062834075773779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.8629777431488037})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.218903064727783})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.481114387512207})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4094045162200928})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.674856185913086})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7264, 'crossentropy': 1.9365412109375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 23315], ['id', 11711], ['id', 45203], ['id', 12059], ['id', 41931]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.3189697002204817, 2.2921738584814255, 3.0999941390947514, 3.69044368799557, 4.0492849079991835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6505192518234253})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9314690828323364})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.202813148498535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.0370326042175293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.2106215953826904})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.381302833557129})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.1036148071289062})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.3609278202056885})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.243527889251709})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.2953288555145264})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.713, 'crossentropy': 2.259309765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 56258], ['id', 27641], ['id', 39963], ['id', 30996], ['id', 207]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2783799310995168, 2.343395142421189, 3.190708091215658, 3.7566927100882577, 4.126321654059026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5610833168029785})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.45426344871521})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.9653204679489136})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.820011854171753})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.9025025367736816})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7722, 'crossentropy': 1.4205306640625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 12668], ['id', 49824], ['id', 40025], ['id', 5259], ['id', 1239]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1396221279152163, 2.135082450054955, 2.934296622648791, 3.5205355951527153, 3.922210186805879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.165252685546875})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.333740234375})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.7409766912460327})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.7589865922927856})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.561903715133667})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.690856695175171})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.7432162761688232})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.7219452857971191})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 2.0034306049346924})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8042, 'crossentropy': 1.649046484375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 42487], ['id', 55643], ['id', 58560], ['id', 42366], ['id', 54880]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.3369639697936915, 2.467386103372841, 3.3042627845447576, 3.8584301612440646, 4.202070396053945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.086578369140625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.246144413948059})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2486021518707275})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.4883322715759277})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.4916383028030396})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4614014625549316})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8251, 'crossentropy': 1.2422755859375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 48952], ['id', 45845], ['id', 28413], ['id', 17540], ['id', 49616]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1624884300365521, 2.210304862215363, 3.0653243420244767, 3.658569516431734, 4.051227944091526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1014351844787598})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1843581199645996})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.4006470441818237})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5500727891921997})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.6529194116592407})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.836, 'crossentropy': 1.07251435546875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 59747], ['id', 25765], ['id', 48102], ['id', 29712], ['id', 24902]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1820818080217537, 2.204948360802864, 3.0113252276572577, 3.5808108884637893, 3.965219080527218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0829720497131348})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2790186405181885})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2743324041366577})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.28831148147583})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.303200125694275})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3644275665283203})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.6425056457519531})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4678083658218384})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.4041423797607422})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4976792335510254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.4611321687698364})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.4061763286590576})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.6998107433319092})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.5902495384216309})
store['active_learning_steps'][7]['training']['best_epoch']=11
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8343, 'crossentropy': 1.5028708984375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 35445], ['id', 15562], ['id', 50461], ['id', 12196], ['id', 43043]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.3528466423506753, 2.569892121964911, 3.4707623370110063, 4.006785529442526, 4.312292796869446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9705967903137207})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1231458187103271})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2130606174468994})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1482396125793457})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1543453931808472})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1783874034881592})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1979942321777344})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8578, 'crossentropy': 1.0278888671875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 23104], ['id', 1149], ['id', 50317], ['id', 20641], ['id', 51903]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1807352424489737, 2.2445120490155444, 3.068637682038819, 3.661753421215325, 4.051414074169959]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8828197717666626})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9583810567855835})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1259593963623047})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.326746940612793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.096824049949646})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3921828269958496})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8481, 'crossentropy': 1.06741533203125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 53316], ['id', 13096], ['id', 48681], ['id', 49537], ['id', 14715]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0751279499672641, 2.051557972799508, 2.90397956985934, 3.5433004529766325, 3.9601784183024176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0280354022979736})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0324403047561646})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3554555177688599})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2139395475387573})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2906973361968994})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.235222578048706})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3085179328918457})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8462, 'crossentropy': 1.07261494140625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 36744], ['id', 45024], ['id', 2000], ['id', 32323], ['id', 34052]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1457285008416214, 2.1557683859097647, 3.0071436806001035, 3.6165406708135546, 4.025021674897855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0202358961105347})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0261715650558472})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1196479797363281})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.168057918548584})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1808503866195679})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8557, 'crossentropy': 0.91324453125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 20057], ['id', 5474], ['id', 30083], ['id', 21880], ['id', 49880]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.01601944326846, 1.9663886898869407, 2.7829543262815495, 3.3978060908341003, 3.8309953794178995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.954714298248291})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9832689762115479})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9667237997055054})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.111690878868103})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0976371765136719})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.145043969154358})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1422674655914307})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.2420108318328857})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8732, 'crossentropy': 0.96025205078125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 6920], ['id', 15723], ['id', 31988], ['id', 17043], ['id', 12497]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.218477125502894, 2.314910168804256, 3.1742440394855453, 3.771193433969808, 4.147492405770509]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8369231224060059})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8347746133804321})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8724246025085449})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8566226959228516})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8935360908508301})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9783651828765869})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0165996551513672})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 1.0549930334091187})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.86265302734375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 17756], ['id', 9180], ['id', 1248], ['id', 11708], ['id', 40702]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1384105950314147, 2.1807195376826534, 3.0242258369346002, 3.632339171808197, 4.037196230880667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.938186526298523})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8169206976890564})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8310050964355469})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9729363918304443})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9904062747955322})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9631915092468262})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8996444940567017})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9703272581100464})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9375587105751038})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 1.0655511617660522})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8946, 'crossentropy': 0.8338580078125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 40066], ['id', 13709], ['id', 31014], ['id', 49607], ['id', 13045]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.170285590046022, 2.267098188863845, 3.132326785013322, 3.7381209819606642, 4.1113208791889075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.963810384273529})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7889764904975891})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7870444059371948})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8919522762298584})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8214384317398071})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0597014427185059})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9828574657440186})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9624260663986206})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.1242951154708862})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 1.0170108079910278})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 1.0063974857330322})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8896, 'crossentropy': 0.89815458984375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 26184], ['id', 59381], ['id', 45456], ['id', 21436], ['id', 21315]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1925377780306614, 2.2423856748572994, 3.097108346167877, 3.709617466767476, 4.101516904476238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9002821445465088})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7193278670310974})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7200988531112671})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8358629941940308})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8890607953071594})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8267847299575806})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.936690628528595})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9294956922531128})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.165470838546753})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9233508110046387})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8962, 'crossentropy': 0.85047958984375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 57510], ['id', 43782], ['id', 39405], ['id', 14295], ['id', 35401]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1606191262214618, 2.2362277759251765, 3.1339381011339364, 3.7747554466394533, 4.161942773184865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9205602407455444})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.678117036819458})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7818236351013184})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7532171010971069})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7486355304718018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9420218467712402})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8529613018035889})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7902045249938965})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8652068376541138})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8146974444389343})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8459150791168213})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.71627177734375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 33812], ['id', 14405], ['id', 5308], ['id', 7168], ['id', 2856]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2187065033700295, 2.305339386107083, 3.214166454156137, 3.816113419294619, 4.173840314059005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9867697358131409})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7389242649078369})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.790000855922699})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8012978434562683})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7747907042503357})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.816737174987793})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9089030623435974})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9325132369995117})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.696884228515625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 41254], ['id', 5684], ['id', 2192], ['id', 36704], ['id', 1075]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1623730549939701, 2.215873760545949, 3.0502527359496856, 3.6667624402421337, 4.06997714043243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0132384300231934})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7814689874649048})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7243297696113586})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7614668011665344})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.784846842288971})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7901463508605957})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7672480344772339})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9060450792312622})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7806273698806763})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8209602236747742})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8246750831604004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8339424133300781})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.673440576171875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 59314], ['id', 43126], ['id', 36984], ['id', 57985], ['id', 22591]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2127865116604286, 2.310039271928185, 3.1681745043368466, 3.797562498797962, 4.1750343844013225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9381893873214722})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6933812499046326})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6757060885429382})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6777843236923218})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6821762323379517})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.603827490234375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 29132], ['id', 49200], ['id', 20002], ['id', 56457], ['id', 25004]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9367857874815371, 1.723918589478246, 2.435978206594065, 3.009679014677693, 3.4672777813627125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0253775119781494})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6142045855522156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7083126306533813})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7335546016693115})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6876208782196045})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7865177392959595})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7390397191047668})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6853067278862})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.8292834758758545})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7765182256698608})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7446502447128296})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9261, 'crossentropy': 0.62619638671875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 39668], ['id', 32776], ['id', 4153], ['id', 51464], ['id', 16070]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.263956111606208, 2.437699016941641, 3.3256976729378493, 3.9045862291828186, 4.232440836533203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9465528130531311})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5751135945320129})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6329182386398315})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5712202787399292})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6299710273742676})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6693978309631348})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6823223829269409})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.622005045413971})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7054473161697388})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6623821258544922})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.51736669921875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 24457], ['id', 43745], ['id', 24620], ['id', 49242], ['id', 15771]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1151245717134137, 2.1282071824442963, 3.009599261940245, 3.6413133247360747, 4.04402220133436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0344960689544678})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5717108249664307})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5594440698623657})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5898202657699585})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.630225419998169})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5847817063331604})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.631731390953064})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6553151607513428})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6956470012664795})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5685515403747559})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6745048761367798})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.795080304145813})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7443311214447021})
store['active_learning_steps'][23]['training']['best_epoch']=10
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.557957861328125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 39208], ['id', 5175], ['id', 15848], ['id', 29476], ['id', 7949]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.2081540923289826, 2.3131504339621802, 3.221958363133428, 3.8692329982595624, 4.2379879880038445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.148240089416504})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6931825280189514})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7066822648048401})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5846062898635864})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6841123104095459})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6551554799079895})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7060723900794983})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.54179912109375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34847], ['id', 14385], ['id', 22824], ['id', 33362], ['id', 21700]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0478737915746907, 1.9536678026524585, 2.7422877015522484, 3.367319249974358, 3.811651151343842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.057183027267456})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6703215837478638})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5914773941040039})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5763738751411438})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5841767191886902})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6173514127731323})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6915295124053955})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7959877848625183})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7172213196754456})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.54532451171875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 3691], ['id', 58036], ['id', 20183], ['id', 24424], ['id', 37383]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0566559242870954, 2.0369660938381253, 2.8344562634375645, 3.4578232172031207, 3.892117936083693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0196266174316406})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6369615793228149})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5832244753837585})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6060523986816406})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5516368746757507})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6429171562194824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6193915009498596})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6541987657546997})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.506399609375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 33358], ['id', 11482], ['id', 3030], ['id', 2381], ['id', 55128]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0685915062619333, 2.0504250387851504, 2.853411997417801, 3.4704146203221455, 3.9244139017606807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1061089038848877})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.601978063583374})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5731105804443359})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5417489409446716})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5888317227363586})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6473519802093506})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6064224243164062})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.514009912109375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 23886], ['id', 22915], ['id', 35864], ['id', 33222], ['id', 42020]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9506175060839079, 1.8458561156892705, 2.626547279133109, 3.239586660794801, 3.706313549280024]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.112399935722351})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6216413974761963})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6845139265060425})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6063855886459351})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6052638292312622})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.613760232925415})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5675473213195801})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.532068701171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42428], ['id', 27874], ['id', 54316], ['id', 2761], ['id', 37489]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0611480220080862, 1.9655581264765472, 2.7561667136561407, 3.371614873883013, 3.8080255430893786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.045741081237793})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5742435455322266})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5182116031646729})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5092425346374512})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5237605571746826})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5332889556884766})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.505534291267395})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5832184553146362})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.449823876953125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20169], ['id', 52169], ['id', 57728], ['id', 38052], ['id', 2352]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.009498389413442, 1.951822103975199, 2.7599936989737905, 3.3675445241835265, 3.7998442049483687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1369366645812988})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.601886510848999})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5307713150978088})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49202632904052734})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4962771236896515})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5437881350517273})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.467773046875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 33057], ['id', 8449], ['id', 52086], ['id', 22193], ['id', 40976]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8787488384537521, 1.7065641694066844, 2.433878796408548, 3.0357890388861204, 3.487228734449859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1221954822540283})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6191896200180054})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5008329153060913})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5214046835899353})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5159868597984314})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5540754199028015})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5455759167671204})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5837023854255676})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9437, 'crossentropy': 0.428077099609375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 31308], ['id', 52012], ['id', 32880], ['id', 55241], ['id', 670]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0284001404464849, 1.9833888327172229, 2.809179466660474, 3.4355622387707516, 3.86719821937339]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1097543239593506})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6035047769546509})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5226705074310303})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5109013319015503})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5172791481018066})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5031786561012268})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.472723974609375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 43176], ['id', 37347], ['id', 19590], ['id', 5548], ['id', 24462]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0301340161425059, 1.8873750675706331, 2.63103193601796, 3.22396235435816, 3.6708931645953946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2741484642028809})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6249418258666992})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5044968724250793})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5240804553031921})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5674437284469604})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5124266743659973})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5172059535980225})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5395546555519104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5238379836082458})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9422, 'crossentropy': 0.44113212890625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 7886], ['id', 50236], ['id', 46132], ['id', 27429], ['id', 29662]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1050485763782523, 2.10493467191741, 2.9555358533338794, 3.575243991814542, 4.0033614253033445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2235227823257446})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.699415922164917})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6064124703407288})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5637695789337158})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5379925966262817})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5394296050071716})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5782579183578491})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.500943896484375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 44342], ['id', 39320], ['id', 52686], ['id', 18598], ['id', 34328]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9393514835699557, 1.7914650825471021, 2.5539603202108676, 3.1781381599565153, 3.6415717256618967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2796050310134888})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5646527409553528})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5405222177505493})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5301671028137207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.495460569858551})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4894411861896515})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5060492753982544})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49507981538772583})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5283700823783875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5488249063491821})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5799408555030823})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4842381477355957})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9487, 'crossentropy': 0.46702998046875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 49563], ['id', 18398], ['id', 48360], ['id', 17010], ['id', 38142]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1555006960145602, 2.2376165093742624, 3.106683973229954, 3.7032382550615317, 4.08420319515322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2156083583831787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5534603595733643})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5322846174240112})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4426509737968445})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4850435256958008})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4508547782897949})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5282157063484192})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9491, 'crossentropy': 0.3952493408203125}
