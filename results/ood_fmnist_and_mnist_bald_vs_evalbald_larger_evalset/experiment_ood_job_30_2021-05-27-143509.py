store = {}
store['timestamp']=1622122509
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=30']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=30
store['worker_id']=30
store['num_workers']=80
store['config']={'seed': 1265, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.3686461448669434})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6116089820861816})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.68684983253479})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.938610553741455})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.060115098953247})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.079051971435547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.3708319664001465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.45975399017334})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6847, 'crossentropy': 2.67766171875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 23388], ['id', 41561], ['id', 32409], ['id', 4727], ['id', 25309]], 'labels': [7, 6, 3, 8, 2], 'scores': [1.290740574904908, 2.3767417668695012, 3.2275203707005398, 3.800389990942107, 4.171534021980893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.024111270904541})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.181853771209717})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.504258155822754})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.582566976547241})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7202, 'crossentropy': 1.8134033203125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36661], ['id', 46926], ['id', 42687], ['id', 50930], ['id', 48653]], 'labels': [5, 0, 5, 0, 4], 'scores': [1.1875078673790136, 2.139072943383776, 2.911730843470526, 3.499456377507925, 3.903310305760246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8516466617584229})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.029390811920166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.10072922706604})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.3997960090637207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.4197146892547607})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7549, 'crossentropy': 1.60835634765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 11505], ['id', 12342], ['id', 5474], ['id', 826], ['id', 37044]], 'labels': [5, 9, 8, 9, 6], 'scores': [1.2180301845745232, 2.261197978922464, 3.042510073836427, 3.6222004645964425, 4.007234265301076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4101355075836182})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.7891689538955688})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.6842665672302246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.9866653680801392})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.8767361640930176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.048048496246338})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7621054649353027})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.1723084449768066})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7862, 'crossentropy': 1.63187119140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 32712], ['id', 8033], ['id', 37407], ['id', 37574], ['id', 47723]], 'labels': [8, 8, 5, 5, 8], 'scores': [1.2675449925610218, 2.3715455680067885, 3.236816165476652, 3.846452729302489, 4.190000404144346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4908406734466553})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.8291873931884766})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.8089311122894287})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.8305370807647705})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8254399299621582})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.9106214046478271})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.0557267665863037})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.0301949977874756})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.995612621307373})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7789, 'crossentropy': 1.7037}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 57307], ['id', 1812], ['id', 56233], ['id', 12497], ['id', 41348]], 'labels': [2, 4, 7, 0, 2], 'scores': [1.2414943518781927, 2.305011739709281, 3.2027944326207383, 3.821808873733313, 4.180228937987817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2895848751068115})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.390285849571228})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.49155592918396})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.501042127609253})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.616097331047058})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.6656043529510498})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.671375036239624})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.92038893699646})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.8259317874908447})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.76817786693573})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.9239352941513062})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7541658878326416})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.096942901611328})
store['active_learning_steps'][5]['training']['best_epoch']=10
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8199, 'crossentropy': 1.5502125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 23140], ['id', 13705], ['id', 17131], ['id', 54461], ['id', 28371]], 'labels': [7, 2, 3, 5, 3], 'scores': [1.3210418877254653, 2.486340733514037, 3.422764624442248, 3.9963365032744296, 4.308348957560335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1585791110992432})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.396032691001892})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.5075865983963013})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.5624502897262573})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.6781164407730103})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.8331161737442017})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8139, 'crossentropy': 1.30133642578125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 42037], ['id', 47608], ['id', 9180], ['id', 27403], ['id', 59280]], 'labels': [2, 4, 3, 5, 8], 'scores': [1.1580259124093397, 2.197933620057357, 3.043323752541026, 3.6448549787679205, 4.021321553759406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.175649881362915})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.131195306777954})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1828486919403076})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2633252143859863})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.300525188446045})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5404155254364014})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8491, 'crossentropy': 1.02283916015625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 16532], ['id', 26358], ['id', 19276], ['id', 49992], ['id', 59339]], 'labels': [2, 3, 6, 5, 1], 'scores': [1.1673392596459116, 2.1407428257461927, 2.961570013303337, 3.579980960374373, 3.991854438864113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9901602268218994})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2116450071334839})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2073495388031006})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3398826122283936})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2695491313934326})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3436124324798584})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5549588203430176})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5435389280319214})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8494, 'crossentropy': 1.0687091796875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 32622], ['id', 32880], ['id', 16957], ['id', 55280], ['id', 42678]], 'labels': [8, 0, 6, 4, 3], 'scores': [1.1714327106089393, 2.21813028728162, 3.0730602008081354, 3.701504106955369, 4.080193090900215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9127997756004333})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0198365449905396})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9937292337417603})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2361935377120972})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.134032964706421})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1963143348693848})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.861, 'crossentropy': 0.895731640625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 30932], ['id', 54885], ['id', 48365], ['id', 58560], ['id', 37048]], 'labels': [0, 6, 4, 0, 9], 'scores': [1.0767625172586142, 2.0031249918958376, 2.8175212373447014, 3.440320130828641, 3.878448397177431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0190372467041016})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9564712643623352})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0020527839660645})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.03603196144104})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2382452487945557})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0810363292694092})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0642355680465698})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1700201034545898})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1934349536895752})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8625, 'crossentropy': 1.007012109375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 50343], ['id', 20641], ['id', 18001], ['id', 41578], ['id', 1423]], 'labels': [6, 9, 3, 8, 0], 'scores': [1.1733147772185086, 2.216359635454531, 3.0707851640301236, 3.675343667559533, 4.066142822307251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8595675230026245})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.800970196723938})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8527634143829346})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9999295473098755})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.892243504524231})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.063904047012329})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0782570838928223})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0309478044509888})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8767, 'crossentropy': 0.82852255859375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 29298], ['id', 46640], ['id', 37974], ['id', 12984], ['id', 14896]], 'labels': [7, 5, 2, 8, 8], 'scores': [1.0981735884495818, 2.0599043862630517, 2.887021640376645, 3.5084733583517957, 3.9471632794705984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9533734917640686})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9411669969558716})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9553823471069336})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.058960199356079})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.052316665649414})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.065690517425537})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0943443775177002})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2907973527908325})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8693, 'crossentropy': 0.968472265625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 52086], ['id', 28675], ['id', 38397], ['id', 22772], ['id', 32776]], 'labels': [5, 7, 8, 9, 4], 'scores': [1.1661156791086493, 2.2092278463919572, 3.0504554790637446, 3.6593597041071853, 4.052097048730193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.900474488735199})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8018912076950073})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8678807020187378})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8858648538589478})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9273048639297485})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9019883871078491})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0100560188293457})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.8381736328125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 27335], ['id', 8691], ['id', 43796], ['id', 22915], ['id', 16909]], 'labels': [4, 2, 7, 9, 2], 'scores': [1.1536569731946686, 2.2060893996925826, 3.0677959690392553, 3.6680987761858788, 4.070626543851657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8158153891563416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6813870668411255})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6543979644775391})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7253583669662476})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7141871452331543})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7153500914573669})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7569183111190796})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8403422832489014})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7834621071815491})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8103103041648865})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8988691568374634})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.896787703037262})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8172985315322876})
store['active_learning_steps'][14]['training']['best_epoch']=10
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.7848455078125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 11565], ['id', 47926], ['ood', 50403], ['id', 37293], ['id', 29922]], 'labels': [3, 8, -1, 3, 4], 'scores': [1.2656164728931207, 2.369942180217455, 3.2765245064389434, 3.8813971834538794, 4.238045245442779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9517351388931274})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.755490243434906})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7331856489181519})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.765997588634491})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8883380889892578})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8809622526168823})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8903, 'crossentropy': 0.70615390625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 26184], ['id', 470], ['id', 11202], ['id', 14062], ['id', 49202]], 'labels': [0, 1, 9, 8, 5], 'scores': [1.0849138267285277, 2.0149082086497097, 2.8103890056429153, 3.411390690582669, 3.841906491363546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9202976822853088})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7934414148330688})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8507054448127747})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9077689051628113})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.990943431854248})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9226106405258179})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9010730981826782})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8911, 'crossentropy': 0.77797275390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49537], ['id', 30884], ['id', 24479], ['id', 10038], ['id', 49474]], 'labels': [2, 2, 8, 9, 2], 'scores': [1.1227115821243778, 2.1335231984383665, 2.9840011469461, 3.591248364478128, 4.007174042638217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9242900013923645})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7360341548919678})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7392621040344238})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8346261978149414})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9248765707015991})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8699566125869751})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.882, 'crossentropy': 0.742216552734375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 33812], ['id', 50317], ['id', 1239], ['id', 53854], ['id', 9304]], 'labels': [6, 3, 8, 8, 9], 'scores': [1.043338133719494, 1.9769611471324549, 2.7516624103471674, 3.37287395598001, 3.826845426488937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9584735035896301})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6857215166091919})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6810953617095947})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6981277465820312})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7759367823600769})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7394148707389832})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.901, 'crossentropy': 0.6269197265625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 10256], ['id', 22083], ['id', 15942], ['id', 29132], ['id', 50743]], 'labels': [2, 2, 4, 8, 7], 'scores': [0.9703414617680075, 1.8491001511334244, 2.5820943632642575, 3.176427312437225, 3.626317014843572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9140456914901733})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6961490511894226})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7058295011520386})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7372288703918457})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7170097231864929})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8412380218505859})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.825143575668335})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8077638149261475})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.665389501953125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 16756], ['id', 52140], ['id', 46616], ['id', 59574], ['id', 13516]], 'labels': [7, 4, 8, 5, 3], 'scores': [1.0373496405042009, 2.000802629148579, 2.820696857356319, 3.4449385474125176, 3.8776556380166785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9983437061309814})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7157911062240601})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6856441497802734})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7246527671813965})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7430849075317383})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7375723123550415})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7484403848648071})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.729546308517456})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8283739686012268})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8147375583648682})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8399014472961426})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.724312451171875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 47475], ['id', 57728], ['id', 52462], ['id', 37794], ['id', 53640]], 'labels': [5, 9, 9, 4, 8], 'scores': [1.2340462991174226, 2.3637789718745443, 3.1777303166243307, 3.7717204217232023, 4.132142448221453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0933552980422974})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7004642486572266})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6737207174301147})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.713246762752533})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6999253034591675})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6781781911849976})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.659087451171875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52785], ['id', 21880], ['id', 47910], ['id', 59314], ['id', 11569]], 'labels': [3, 2, 1, 9, 5], 'scores': [0.9566201463639754, 1.85519524198134, 2.6706523981374355, 3.3114545273039653, 3.7621779291734274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.077524185180664})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6028767228126526})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5698697566986084})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5727599859237671})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6090797781944275})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5665918588638306})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6794105768203735})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.547518603515625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 12786], ['id', 4955], ['id', 21023], ['id', 12089], ['id', 58258]], 'labels': [4, 2, 2, 3, 7], 'scores': [1.078923903488123, 2.0398395634438637, 2.8350276073641156, 3.464710723166177, 3.899216179751998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0686774253845215})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6566959619522095})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6467479467391968})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5714238882064819})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6076894998550415})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6826109886169434})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6483519077301025})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.570683251953125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 38644], ['id', 16628], ['id', 41169], ['id', 41453], ['id', 34916]], 'labels': [-1, 9, 2, 3, 7], 'scores': [0.9682206092719183, 1.8689406424207542, 2.644762346391638, 3.255668649749035, 3.7113714264731703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9822086691856384})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5874166488647461})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5527536869049072})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5697435140609741})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5273815393447876})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5162672996520996})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5609776973724365})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5862623453140259})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.487527880859375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 32276], ['id', 8104], ['ood', 59081], ['id', 42078], ['ood', 7949]], 'labels': [3, 5, -1, 4, -1], 'scores': [1.0755875785552367, 2.0437612715262943, 2.899410557592409, 3.530697678209197, 3.957922821355499]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9757371544837952})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.528490424156189})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5432071089744568})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5319013595581055})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5221965312957764})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5281900763511658})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.562559962272644})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5833945274353027})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5994573831558228})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.520176887512207})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5291755199432373})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6075121164321899})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7071981430053711})
store['active_learning_steps'][25]['training']['best_epoch']=10
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.487176708984375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 27316], ['ood', 57416], ['id', 15855], ['id', 31308], ['id', 9036]], 'labels': [3, -1, 5, 8, 2], 'scores': [1.1221778871032106, 2.1341294086623375, 3.0036498891249277, 3.6394233115883896, 4.0446864508648845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0761122703552246})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6156667470932007})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.577245831489563})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5510380268096924})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5489325523376465})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5893579125404358})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.5398345703125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 31090], ['id', 52294], ['id', 36818], ['id', 39480], ['id', 33484]], 'labels': [4, 0, 7, 9, 6], 'scores': [0.9453587485949644, 1.7778778856999762, 2.5163693501549886, 3.1018814173966174, 3.5539487570104713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0422468185424805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6432965993881226})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5103644728660583})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5097075700759888})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5708006024360657})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5898160338401794})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.5051708984375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 5679], ['id', 11708], ['id', 33162], ['id', 33224], ['id', 36000]], 'labels': [3, 3, 8, 1, 9], 'scores': [0.9426591999224221, 1.8029610905098439, 2.5730266295751845, 3.1761918931719553, 3.623155058773352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0750036239624023})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6212193965911865})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5343457460403442})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.565352737903595})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5925852060317993})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5620440244674683})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5976893901824951})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.591774582862854})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6515198945999146})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6659094095230103})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.531569242477417})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.53368076171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 19868], ['id', 59726], ['id', 37906], ['id', 33594], ['ood', 39164]], 'labels': [5, 5, 9, 3, -1], 'scores': [1.1475549682393889, 2.2209207362134875, 3.0741864519495037, 3.6834283946316084, 4.076638239427085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2147784233093262})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6611466407775879})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5524840354919434})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5568482279777527})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5986859798431396})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5174257755279541})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6226714253425598})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5830445289611816})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5623642206192017})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.624411404132843})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6164451837539673})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.499248974609375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 40066], ['id', 34946], ['id', 38623], ['id', 41478], ['id', 43575]], 'labels': [4, 8, 8, 2, 2], 'scores': [1.1763180154775745, 2.2247728967389486, 3.110199120188904, 3.7392994875834606, 4.128096453517956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1650265455245972})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6237065196037292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5423526763916016})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5503491163253784})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5416316390037537})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5843072533607483})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5675311088562012})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5564415454864502})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6469436883926392})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6795137524604797})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.525393359375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 23870], ['id', 16248], ['id', 56454], ['id', 3634], ['id', 11292]], 'labels': [5, 7, 0, 5, 1], 'scores': [1.0719907298921094, 2.057950760179475, 2.8912780678355627, 3.521981497989133, 3.9490764649686616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.159271240234375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6046388149261475})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6341151595115662})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5484778881072998})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5268051624298096})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6058107614517212})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5712409019470215})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6445848345756531})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.46281689453125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 41608], ['id', 39561], ['id', 14201], ['id', 50320], ['id', 9677]], 'labels': [-1, 2, 7, 5, 0], 'scores': [1.0749152191283071, 2.0939937338499424, 2.9497832730824616, 3.5856765285233827, 4.004161608217779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0991199016571045})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5900809168815613})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5038159489631653})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.514392077922821})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5625329613685608})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.501732587814331})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5296918153762817})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5455125570297241})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5576910376548767})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.448067626953125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 45887], ['id', 2761], ['id', 2381], ['id', 45666], ['id', 24740]], 'labels': [6, 8, 7, 1, 8], 'scores': [1.0605572110709318, 2.0220179246096706, 2.833259712466427, 3.479552701230837, 3.9175198433869216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0742186307907104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5296272039413452})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48416972160339355})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44343072175979614})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4731743335723877})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44867944717407227})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5206351280212402})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5222349166870117})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.435040869140625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 59294], ['id', 27576], ['id', 18487], ['id', 4820], ['id', 39942]], 'labels': [8, 5, 4, 5, 9], 'scores': [1.017386860775423, 1.9681138893400303, 2.7727630132122147, 3.407938271999008, 3.8677017474231583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.265923023223877})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6977896094322205})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5567022562026978})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47907572984695435})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4981047809123993})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5435216426849365})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5571006536483765})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.469579541015625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 37469], ['id', 5740], ['id', 33222], ['id', 11616], ['ood', 7949]], 'labels': [2, 9, 5, 7, -1], 'scores': [0.9263990597343619, 1.767225981349303, 2.5190259061937743, 3.1267104152768503, 3.583901389660361]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0653953552246094})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5618867874145508})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4587429165840149})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47755879163742065})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48794883489608765})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47735875844955444})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5178675055503845})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4624252915382385})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.526949405670166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5440260171890259})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5055146217346191})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.4151755859375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 48681], ['id', 9118], ['ood', 48824], ['id', 17895], ['ood', 57221]], 'labels': [2, 9, -1, 2, -1], 'scores': [1.138802914133298, 2.1294190424088937, 2.9806488828205513, 3.6206576970896185, 4.0325560615281635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.275815725326538})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6088860034942627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5614446997642517})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48301005363464355})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4291713237762451})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46194887161254883})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4495772421360016})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4718630313873291})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45257705450057983})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47618409991264343})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5600526332855225})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5060280561447144})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.946, 'crossentropy': 0.4408333984375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 42317], ['id', 17178], ['id', 18324], ['id', 48102], ['id', 4646]], 'labels': [5, 8, 0, 7, 2], 'scores': [1.1361482251308577, 2.1965856809698145, 3.0797548629210905, 3.701294837290023, 4.099594947959097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2203879356384277})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6714048385620117})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4749930500984192})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4607575535774231})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49698156118392944})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49967026710510254})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.550499439239502})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.48073193430900574})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46064943075180054})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6001772284507751})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49057865142822266})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.951, 'crossentropy': 0.423504541015625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 8117], ['id', 42438], ['id', 13969], ['ood', 49253], ['id', 46316]], 'labels': [4, 9, 3, -1, 9], 'scores': [1.1072038156475104, 2.1134044833436625, 2.953032050389817, 3.5792734588180153, 4.008353316020215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0731267929077148})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.594333291053772})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5159127116203308})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4574544429779053})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5659414529800415})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4595212936401367})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5167392492294312})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5251840353012085})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5515185594558716})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.425398486328125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 14001], ['id', 44143], ['id', 59468], ['ood', 7949], ['id', 59747]], 'labels': [1, 2, 7, -1, 5], 'scores': [1.0099307563467663, 1.938880809833039, 2.74697919386563, 3.3958500169425996, 3.8491844486980664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2848107814788818})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6714410781860352})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5116170644760132})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5468084812164307})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4936791956424713})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.504821240901947})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.539533257484436})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.558908224105835})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5621212720870972})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.441409814453125}
