store = {}
store['timestamp']=1622124704
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=36']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=36
store['worker_id']=36
store['num_workers']=80
store['config']={'seed': 1272, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.177926540374756})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.4888577461242676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.854431629180908})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8724935054779053})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6897, 'crossentropy': 1.9757427734375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.105800747871399})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1115844249725342})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1291710138320923})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47605], ['id', 12369], ['id', 30162], ['id', 22685], ['id', 49149]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0739529823016096, 1.9039867769886007, 2.4588906779494133, 2.844180243084046, 3.052063043452213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1618895530700684})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.888770341873169})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7741951942443848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.8973755836486816})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.1735339164733887})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0888442993164062})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.1881794929504395})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.1919426918029785})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.51981258392334})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.289295196533203})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.577575206756592})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6995, 'crossentropy': 2.8839548828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2470054626464844})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2282047271728516})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.183701753616333})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1452958583831787})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1771776676177979})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1946966648101807})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 22603], ['id', 10210], ['id', 1020], ['id', 12305], ['ood', 40241]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1801418286661414, 2.1840324797653166, 2.8815687076390413, 3.2461257538208343, 3.421705673064471]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.705610752105713})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9213545322418213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.090817928314209})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.133863925933838})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.5837721824645996})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.52901029586792})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.395740032196045})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.526093006134033})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.6645116806030273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.416141986846924})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7195, 'crossentropy': 2.221644140625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.04446542263031})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0323816537857056})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0870647430419922})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0076720714569092})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0315030813217163})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 41887], ['id', 776], ['id', 21042], ['id', 54007], ['ood', 13979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0441572517978064, 1.8405782579608765, 2.4272775763587626, 2.7885436240580246, 2.971911704863812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4668340682983398})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.6694074869155884})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.9346368312835693})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.8847482204437256})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.1019468307495117})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.174686908721924})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.766, 'crossentropy': 1.661595703125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0413353443145752})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.9478344917297363})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9294462203979492})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.942972719669342})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8987863063812256})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 34428], ['id', 4530], ['id', 492], ['id', 8419], ['id', 16737]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9249271896322682, 1.7484261528667258, 2.3781341046818785, 2.810381065884793, 3.0689736443274374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2791703939437866})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3529167175292969})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.4464246034622192})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5886764526367188})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5935521125793457})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.7003474235534668})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8196, 'crossentropy': 1.2677736328125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8421448469161987})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.757345974445343})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.7452043294906616})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7162635326385498})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7284518480300903})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 8893], ['id', 51761], ['id', 39409], ['id', 51599], ['id', 8883]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8134529827001191, 1.5609866399059413, 2.1344131911544686, 2.5034606213736588, 2.7141305847847743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1244105100631714})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3323898315429688})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3349525928497314})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5144870281219482})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.634713888168335})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.713797926902771})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.6784764528274536})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.5129685401916504})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.817, 'crossentropy': 1.27517119140625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8146818280220032})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7408884763717651})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7199638485908508})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7067004442214966})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7200304269790649})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7222099304199219})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.6706993579864502})
store['active_learning_steps'][5]['eval_training']['best_epoch']=7
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 8887], ['id', 25246], ['id', 9499], ['id', 54646], ['id', 11853]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8858952833648397, 1.6892474177652232, 2.300173108158871, 2.714016222714603, 2.9647424925252785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0203056335449219})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0344305038452148})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2268061637878418})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.287855625152588})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.3512187004089355})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.409409523010254})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3473281860351562})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.44807767868042})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3859241008758545})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4415414333343506})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6173670291900635})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.852, 'crossentropy': 1.20560302734375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8041049242019653})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6319080591201782})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6441842317581177})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.610803484916687})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.5872116684913635})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.5925335884094238})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.5934945940971375})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.5982998609542847})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 27904], ['id', 50499], ['id', 17535], ['id', 3051], ['id', 2519]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9529659570504472, 1.7279903804383698, 2.286990037189198, 2.6732985555480617, 2.883598722124085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9799622297286987})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9632796049118042})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0477834939956665})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0191419124603271})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.10701584815979})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.2095015048980713})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.198700189590454})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1926624774932861})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2648224830627441})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8645, 'crossentropy': 1.02672314453125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7712938785552979})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6658003330230713})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6194121837615967})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6241298317909241})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6172772645950317})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 41078], ['id', 1535], ['id', 2018], ['id', 31404], ['id', 27986]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.875648685600678, 1.5901029020991055, 2.0965560699860104, 2.4381209301566917, 2.5970039930773394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9129490852355957})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0408332347869873})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0313142538070679})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0822031497955322})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.066429615020752})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1150877475738525})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.2815861701965332})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1576731204986572})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.3272641897201538})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8809, 'crossentropy': 0.9499251953125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8152198791503906})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6190049648284912})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6022864580154419})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5938024520874023})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5650838613510132})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5671675205230713})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5607610940933228})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5693849325180054})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 4564], ['id', 53239], ['id', 24853], ['id', 19792], ['ood', 38100]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9642767186526708, 1.7507934730037942, 2.285839110632481, 2.631192519198203, 2.793115323430297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7806756496429443})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8247106075286865})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8396309614181519})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.993824303150177})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.028061032295227})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9824672937393188})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0233656167984009})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.058668613433838})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0194473266601562})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8884, 'crossentropy': 0.86225673828125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7003062963485718})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5579551458358765})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.564132809638977})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5450965762138367})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5180078744888306})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5039360523223877})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5096604824066162})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.4983363151550293})
store['active_learning_steps'][9]['eval_training']['best_epoch']=7
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 15739], ['id', 54142], ['id', 21242], ['id', 48540], ['id', 16820]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9096157330371095, 1.6896850250527091, 2.301050737982274, 2.7384142870632857, 2.977446243615714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8142768740653992})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8322151899337769})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9478588104248047})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8721873760223389})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9776365160942078})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0171928405761719})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1099542379379272})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0328044891357422})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.770182666015625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7462918758392334})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5847132802009583})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.55386883020401})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5221906900405884})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5122712850570679})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5248374938964844})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5201418995857239})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 2803], ['id', 6174], ['id', 24457], ['id', 34829], ['id', 25962]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8921759971652428, 1.6088395392052894, 2.2014833428058838, 2.5435963312582084, 2.7273999874748256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8789368867874146})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8848400115966797})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8346736431121826})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8864107728004456})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.985222578048706})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0336288213729858})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9934185743331909})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8922, 'crossentropy': 0.753064453125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7247164249420166})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5987218618392944})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5542008876800537})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.507412314414978})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5088708400726318})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4890923500061035})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 46288], ['id', 49992], ['id', 41325], ['id', 19423], ['id', 5163]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7736080919777946, 1.4633546090032956, 2.013963341538873, 2.392188520728661, 2.5857993273397373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8263036608695984})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7203329801559448})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7686859369277954})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7323818802833557})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8189400434494019})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7661560773849487})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8444766998291016})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7318395376205444})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8666431903839111})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9876278042793274})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9540629386901855})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9014265537261963})
store['active_learning_steps'][12]['training']['best_epoch']=9
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.7718423828125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6375235915184021})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5469517707824707})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.45907747745513916})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4827944338321686})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4676387906074524})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.42027273774147034})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.44122833013534546})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4392193555831909})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.42535412311553955})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.43142059445381165})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 37778], ['id', 13079], ['id', 9608], ['id', 17269], ['id', 17700]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8645270771679157, 1.6741905555977898, 2.3181418905834485, 2.701913599770906, 2.8719268312148722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9383323192596436})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6916751861572266})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.758741021156311})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8217312097549438})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9445346593856812})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8277050256729126})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8993, 'crossentropy': 0.679945703125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6837573051452637})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5477239489555359})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.49087274074554443})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5011312961578369})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.4935545027256012})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 58422], ['id', 23642], ['id', 29900], ['id', 59257], ['id', 23386]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7424929462617038, 1.4103294384531124, 1.9643119427234215, 2.3149564230152757, 2.523370015270289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8903082609176636})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7374769449234009})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8413369655609131})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7395057678222656})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8305490016937256})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7569313049316406})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8942116498947144})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 1.006460428237915})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.672305322265625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7067935466766357})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5769340395927429})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.52765953540802})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.45987555384635925})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.46947187185287476})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43706822395324707})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.42997807264328003})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 54556], ['id', 38960], ['id', 10332], ['id', 19870], ['id', 46441]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.79629200401233, 1.5128762939518117, 2.0519047929603893, 2.475638175524999, 2.752506276443656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8448168039321899})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7533355951309204})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7020653486251831})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7176094651222229})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.769210696220398})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7910312414169312})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7692402005195618})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7556624412536621})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7940173149108887})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8574609756469727})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.636837109375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.658403754234314})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5040223598480225})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4653952121734619})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.46697184443473816})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4527108371257782})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4361690878868103})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4291883409023285})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4184380769729614})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.41696569323539734})
store['active_learning_steps'][15]['eval_training']['best_epoch']=8
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 54], ['id', 14070], ['id', 41383], ['id', 14681], ['id', 20097]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7775007527998274, 1.4723104338743886, 2.0635414863782024, 2.4663684685924734, 2.704902403707096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8382580876350403})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6659730672836304})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6462470889091492})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6570144295692444})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7233065962791443})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6773968935012817})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7938746213912964})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8054766654968262})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7846623659133911})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7853009700775146})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8388009071350098})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9243308305740356})
store['active_learning_steps'][16]['training']['best_epoch']=9
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.662195654296875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6207837462425232})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5152164697647095})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.45710957050323486})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4408426582813263})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4402068555355072})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.41253724694252014})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.40718555450439453})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 5545], ['id', 46435], ['id', 45732], ['id', 43337], ['id', 46895]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8794951859740614, 1.5507327641130928, 2.0936316539905873, 2.482776417940457, 2.71673646111221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7942231893539429})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7097724676132202})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7080522775650024})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7186404466629028})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7874104976654053})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7050366401672363})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7147635221481323})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7498547434806824})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7806843519210815})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.60357724609375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7104997634887695})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5310847759246826})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4830450415611267})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.45417946577072144})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.410444051027298})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4327887296676636})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40323618054389954})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.39727693796157837})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 23104], ['id', 8200], ['id', 19576], ['id', 13705], ['id', 26338]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8299047673143822, 1.5235111539322328, 2.059814875280937, 2.458046986231066, 2.6986250721581735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9215835928916931})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6900156736373901})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7205970883369446})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7644656300544739})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7638702392578125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7966923713684082})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7447490096092224})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7641170024871826})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7697551250457764})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7413762807846069})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.628901318359375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6907863020896912})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5058485269546509})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.480070024728775})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.46858492493629456})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4438123404979706})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4564807713031769})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 1423], ['id', 57270], ['id', 45175], ['id', 9098], ['id', 30865]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8351574740763001, 1.4272183481359084, 1.9000694085592889, 2.2086232704716107, 2.4027833078921716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8807839155197144})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7064234018325806})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6342910528182983})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6566038727760315})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7510873079299927})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7338255643844604})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.777074933052063})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6945351362228394})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6857751607894897})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6807295680046082})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8215066194534302})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8318673372268677})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.853053092956543})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.621506640625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6723408102989197})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4911075830459595})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.46976733207702637})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4309205412864685})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4269993305206299})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.41377341747283936})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14540], ['id', 7784], ['id', 3827], ['id', 59286], ['id', 57486]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.809601308438761, 1.5168577651234982, 2.039032810275435, 2.388449427666062, 2.5674285929996357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7646986842155457})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6370944976806641})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6812291145324707})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5833556652069092})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6531758308410645})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7945208549499512})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7687100172042847})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.495838232421875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.755888819694519})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5540783405303955})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4521782398223877})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4409385025501251})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.43352755904197693})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40292972326278687})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 48384], ['id', 3010], ['id', 48102], ['id', 20989], ['id', 16155]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6249360924842609, 1.183930546228658, 1.6381810088786706, 1.9765902988395894, 2.2018643815266827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0288841724395752})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5997856855392456})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5935719013214111})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.593395471572876})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6340957283973694})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.570172131061554})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7210805416107178})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7349011301994324})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7074202299118042})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.54875947265625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6460458636283875})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4857833981513977})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4395020306110382})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4096938967704773})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.38372811675071716})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.37430107593536377})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3771612048149109})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3793412148952484})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 23490], ['id', 16084], ['id', 23746], ['id', 36810], ['id', 34071]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7939446304843862, 1.458402115259946, 1.9861756884941606, 2.3455343792974563, 2.5931799312586508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0231376886367798})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5768832564353943})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6172112226486206})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.48920369148254395})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6138246059417725})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.568769097328186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6447497606277466})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6523704528808594})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6076587438583374})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.486327685546875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6420446634292603})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.499985933303833})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4094492793083191})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3913087844848633})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.3997843563556671})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3776736855506897})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40434348583221436})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 9227], ['id', 52140], ['id', 32386], ['id', 30214], ['id', 5000]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7418633324962665, 1.3844521051893683, 1.8901878994563086, 2.221624919875799, 2.4328717411807546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8781872987747192})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5301864147186279})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5022875666618347})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5094012022018433})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5381131172180176})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5777006149291992})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5448282957077026})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.479655078125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7335389256477356})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.48892971873283386})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4687455892562866})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.44292891025543213})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.414157509803772})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.40467891097068787})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 14164], ['id', 53873], ['id', 53693], ['id', 45407], ['id', 37469]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7826365112498503, 1.4476605184184264, 1.9483591322973908, 2.3048610379645966, 2.5262194277124586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8348903656005859})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4947921931743622})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4900347590446472})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5239827632904053})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5172659158706665})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5402394533157349})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5702290534973145})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5802854299545288})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.4463447265625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6996160745620728})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47451138496398926})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4350833296775818})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3854812979698181})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3938302993774414})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37971654534339905})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.34912607073783875})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 29832], ['id', 15855], ['id', 57392], ['id', 47387], ['id', 16722]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.677922774098759, 1.296601689274615, 1.7691700794685197, 2.1056686011601506, 2.2866764955970442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8638830184936523})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5895434021949768})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5570310354232788})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5548375248908997})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5420461297035217})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5715007185935974})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5580252408981323})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7204570174217224})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.45865107421875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7183709740638733})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4891050457954407})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4582093358039856})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4062036871910095})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3577905595302582})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3575320839881897})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37108734250068665})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 59726], ['id', 4165], ['id', 47870], ['id', 20110], ['id', 28652]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7796168762888855, 1.4059599799155702, 1.8885837882137988, 2.2351726112752894, 2.460119214681672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8323631286621094})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5485590100288391})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5788711309432983})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5392245650291443})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5910619497299194})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6116204261779785})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5732491612434387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5572010278701782})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5683319568634033})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5440689325332642})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6173170208930969})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.49085224609375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6829470992088318})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.47941339015960693})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38104110956192017})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40008699893951416})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3874698877334595})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3692384362220764})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 17227], ['id', 5315], ['id', 42199], ['id', 59718], ['id', 4747]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.739909749614795, 1.3844076767409121, 1.920739498075812, 2.3023725072735157, 2.513966812841687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9272192716598511})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6209486126899719})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5319685935974121})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5595024824142456})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5495404601097107})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5988171100616455})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5675537586212158})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6250120997428894})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.46659892578125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7939568758010864})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48970139026641846})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4398813843727112})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38513606786727905})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38666942715644836})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3711971044540405})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37360453605651855})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 3672], ['id', 52697], ['id', 14896], ['id', 17358], ['id', 42001]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6668992832119407, 1.2429455611369282, 1.733349101881437, 2.073528858647106, 2.3048044870231017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.055336356163025})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.631363034248352})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5081652402877808})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5610657930374146})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5818980932235718})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5714284181594849})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6063616871833801})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5109339952468872})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6192493438720703})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5919184684753418})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6000006198883057})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.478271923828125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6483838558197021})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4766949415206909})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.43150192499160767})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4233133792877197})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.42081403732299805})
store['active_learning_steps'][28]['eval_training']['best_epoch']=2
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 24263], ['id', 32173], ['id', 38389], ['id', 53906], ['id', 52201]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8991542114637481, 1.6571234367048175, 2.1214253478437435, 2.420305735534602, 2.585401282386126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.13429856300354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6638323664665222})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5507739186286926})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5476073026657104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5861846208572388})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5268340110778809})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5267254710197449})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5970360040664673})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5735555291175842})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5208680629730225})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9327, 'crossentropy': 0.514211328125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6757751107215881})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4875996708869934})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38379693031311035})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4088062047958374})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3475300371646881})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36827635765075684})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3717004954814911})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3666679859161377})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3234044015407562})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 32419], ['id', 47234], ['id', 7281], ['id', 14096], ['ood', 33781]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7871061023483996, 1.4946025117077393, 2.053072556921091, 2.4329600680885983, 2.6076202442638277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8340038061141968})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5555504560470581})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5333500504493713})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5651953220367432})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5521596670150757})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6318750977516174})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5288333892822266})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49546322226524353})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5781494379043579})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5720205307006836})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.501939697265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6952985525131226})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48156097531318665})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4371456503868103})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.385640412569046})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3787631392478943})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3821386694908142})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3866989016532898})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3496010899543762})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.36117175221443176})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 19868], ['id', 44494], ['ood', 3932], ['id', 32747], ['id', 43442]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9062673698378987, 1.5422717008718894, 2.0551562616926384, 2.4003651066635268, 2.613837990783191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0128031969070435})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.531353235244751})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4780656695365906})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5277936458587646})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4941762685775757})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.532809853553772})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5115321278572083})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4854589104652405})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.458041455078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.703685998916626})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.47637489438056946})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.43683749437332153})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4118694067001343})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3847334384918213})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3992326259613037})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 8045], ['id', 35401], ['id', 52236], ['id', 13774], ['ood', 38890]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6738616234293104, 1.3025633930648928, 1.8196721455153906, 2.222894020875242, 2.4398161643781604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0827211141586304})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5549038648605347})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5069015622138977})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46804437041282654})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.457309752702713})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5327742099761963})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4904255270957947})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9428, 'crossentropy': 0.4155728515625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7378931045532227})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49168896675109863})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39263516664505005})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3988097608089447})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37198370695114136})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.387260377407074})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 40654], ['id', 31310], ['id', 7840], ['id', 55503], ['id', 41334]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6451453641775968, 1.2500514546573367, 1.7457735153116287, 2.1389464895600208, 2.364777807080415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0156223773956299})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5236796140670776})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5183279514312744})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4814297556877136})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5288125872612})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5001345872879028})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5034778714179993})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9425, 'crossentropy': 0.4197537109375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6860908269882202})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.45783236622810364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3977833390235901})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40447282791137695})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3901173770427704})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39124706387519836})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 1248], ['id', 49252], ['id', 47247], ['id', 17817], ['id', 31505]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6844789475867354, 1.2690181343256905, 1.7568026728123538, 2.134329338666614, 2.3548772997703624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0287415981292725})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5155184268951416})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45408427715301514})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49956822395324707})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4551628828048706})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45835334062576294})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4473567008972168})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4450497031211853})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46837273240089417})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5165539979934692})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.373231640625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7457277774810791})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4874735474586487})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44292694330215454})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3919510245323181})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3711310029029846})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34421318769454956})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34198546409606934})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.342265784740448})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.33534789085388184})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 57764], ['id', 27576], ['ood', 4285], ['id', 51903], ['id', 41072]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5918925518705223, 1.1113544164370621, 1.5683871332185682, 1.9216656404146928, 2.1859083428104196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0382275581359863})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5969992876052856})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4428192973136902})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4824277460575104})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4827328324317932})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4533118009567261})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.417802197265625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6924731731414795})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5229557156562805})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44814085960388184})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39325258135795593})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.414469838142395})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 26358], ['id', 44927], ['id', 56695], ['id', 37118], ['id', 36818]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5688666537151885, 1.095724177397556, 1.5436786741646698, 1.873970770761912, 2.113100035036739]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0913609266281128})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5633887052536011})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46047741174697876})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.454426109790802})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46224749088287354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.47124359011650085})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4311610460281372})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.944, 'crossentropy': 0.395766845703125}
