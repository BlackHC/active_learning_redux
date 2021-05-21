store = {}
store['timestamp']=1621471709
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=22']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=22
store['worker_id']=22
store['num_workers']=80
store['config']={'seed': 1257, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0981626510620117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5664453506469727})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.75738525390625})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6366114616394043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7301831245422363})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1704764366149902})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.938950538635254})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2018537521362305})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6859, 'crossentropy': 2.4918671875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1984866857528687})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1381592750549316})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1813955307006836})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1343822479248047})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1180894374847412})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1604878902435303})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1502556800842285})
store['active_learning_steps'][0]['eval_training']['best_epoch']=5
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47889], ['id', 34678], ['id', 25680], ['id', 40555], ['id', 50538]], 'labels': [5, 8, 6, 3, 2], 'scores': [1.2067657204618083, 2.07847202818622, 2.734818668347547, 3.1577147165641763, 3.401736650825992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2668089866638184})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4357786178588867})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.7752392292022705})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.1938490867614746})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.9235987663269043})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.718, 'crossentropy': 2.0365345703125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1186727285385132})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1005500555038452})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.103912591934204})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0973191261291504})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 23190], ['id', 55218], ['id', 6965], ['id', 49926], ['id', 34304]], 'labels': [8, 8, 7, 3, 8], 'scores': [0.9565703645864885, 1.7869866997157882, 2.397798505173907, 2.8124358877285838, 3.0511076091234948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6589369773864746})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8251230716705322})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.184628963470459})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.3379523754119873})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7557, 'crossentropy': 1.53782451171875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0493736267089844})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.002023458480835})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9437457323074341})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 28898], ['id', 45094], ['id', 36577], ['id', 39527], ['id', 16035]], 'labels': [6, 2, 4, 0, 9], 'scores': [0.8464469378330517, 1.5551892111973875, 2.15888081163538, 2.5288075667370125, 2.7738292327474605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5558226108551025})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.8861603736877441})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.8930097818374634})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.998654842376709})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.1649155616760254})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.234736919403076})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.34293270111084})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.355353593826294})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.370967388153076})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7893, 'crossentropy': 1.9680931640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0033212900161743})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.859866201877594})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9133278727531433})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8482591509819031})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8662775754928589})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8530592918395996})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.884667158126831})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 14669], ['id', 30011], ['id', 19643], ['id', 41485], ['id', 32896]], 'labels': [8, 3, 1, 0, -1], 'scores': [1.046693780057151, 1.9509501839658445, 2.6188241289272502, 3.0222884406581727, 3.243876329251396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.431563138961792})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6865301132202148})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.7571911811828613})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 2.0227298736572266})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.9010701179504395})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.8487262725830078})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 2.1165337562561035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 2.0713624954223633})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 2.0804405212402344})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 2.0175364017486572})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.2701754570007324})
store['active_learning_steps'][4]['training']['best_epoch']=8
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8071, 'crossentropy': 1.885104296875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9374042749404907})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9065003395080566})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.83436119556427})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9049034118652344})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9098479747772217})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8493659496307373})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8208773136138916})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8474142551422119})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8405311107635498})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8414542078971863})
store['active_learning_steps'][4]['eval_training']['best_epoch']=9
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 6898], ['id', 51614], ['id', 3782], ['id', 26358], ['id', 51342]], 'labels': [3, 2, 7, 3, 5], 'scores': [1.1268198880321445, 2.0076431258239786, 2.68189864119522, 3.051708878687167, 3.2441707759640366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3608200550079346})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.6297675371170044})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 2.087270498275757})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7557231187820435})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.9997022151947021})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8108, 'crossentropy': 1.41547919921875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8962427377700806})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8676872253417969})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8127281665802002})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8168989419937134})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 23137], ['id', 18049], ['id', 53045], ['id', 37974], ['id', 13803]], 'labels': [5, 3, 9, 2, 8], 'scores': [0.9473492832088288, 1.7117805940807695, 2.32358339525688, 2.709837978842426, 2.9167779065254784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0382006168365479})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.135688066482544})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2118611335754395})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3538117408752441})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.397902488708496})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.619519829750061})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8422, 'crossentropy': 1.17726376953125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8155189156532288})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6806089878082275})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.675987958908081})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.6398212313652039})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6302922964096069})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 47115], ['id', 37074], ['id', 16751], ['id', 33321], ['id', 8200]], 'labels': [5, 4, 9, 5, 3], 'scores': [0.9282724409839807, 1.7819903721302919, 2.4224211858347307, 2.782635854587843, 2.9492493740041326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9742445945739746})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1057301759719849})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1270313262939453})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2394012212753296})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.302565097808838})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.2030560970306396})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.173913836479187})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.3478710651397705})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.590681791305542})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8695, 'crossentropy': 1.0495650390625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7122470736503601})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6321072578430176})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5513981580734253})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5607917308807373})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5573575496673584})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5503411293029785})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5344419479370117})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5182962417602539})
store['active_learning_steps'][7]['eval_training']['best_epoch']=8
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 9180], ['id', 4058], ['id', 39415], ['id', 1278], ['id', 56340]], 'labels': [3, 8, 3, 5, 2], 'scores': [0.9641065103239719, 1.790965512604418, 2.4277897882927455, 2.8229481947024375, 3.0288443520825723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8944308757781982})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0709848403930664})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0711822509765625})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1745972633361816})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2740756273269653})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.2276983261108398})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.3179363012313843})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2759416103363037})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.2917519807815552})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8811, 'crossentropy': 0.98854072265625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7184008359909058})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6247076988220215})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5691441297531128})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.5859841108322144})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5583962798118591})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5406738519668579})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.5419870615005493})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.522017240524292})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 16376], ['id', 8924], ['id', 35246], ['id', 2231], ['id', 38890]], 'labels': [1, 2, 8, 8, -1], 'scores': [0.9436737655172016, 1.7648663502252613, 2.4126596945455914, 2.8216593959928566, 3.030536690249888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0301252603530884})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.034366488456726})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1103417873382568})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1112911701202393})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1813688278198242})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2902618646621704})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8641, 'crossentropy': 0.9994025390625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7709496021270752})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6425235271453857})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6170254945755005})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6274446249008179})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5958824157714844})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 37326], ['id', 53116], ['id', 16913], ['id', 56107], ['id', 11482]], 'labels': [9, 0, 4, 7, 8], 'scores': [0.8035085347756226, 1.4800219907997727, 2.0294108797103014, 2.44253366585529, 2.6845480216267017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8488024473190308})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9707999229431152})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0040581226348877})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0388001203536987})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1526951789855957})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8683, 'crossentropy': 0.85331943359375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7341111898422241})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6371891498565674})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6425952911376953})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6182796359062195})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 31347], ['id', 36122], ['id', 5194], ['id', 39618], ['id', 22992]], 'labels': [3, 9, 0, 3, 4], 'scores': [0.7962770566574306, 1.4665989422710841, 2.001996618531904, 2.3779363132177638, 2.599378479355293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9651352167129517})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9992526173591614})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9603397846221924})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9126504063606262})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9203264117240906})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0172817707061768})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0671923160552979})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0941746234893799})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.81954921875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6662856340408325})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6453778147697449})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5702869296073914})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5477412939071655})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5336395502090454})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5139034986495972})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37778], ['id', 8715], ['id', 54908], ['id', 25715], ['id', 44756]], 'labels': [8, 6, 2, 8, 7], 'scores': [0.7767310524065663, 1.4673819621107436, 2.0319431124175313, 2.4180742086966545, 2.66710966086203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.947563648223877})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8204261064529419})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8619329929351807})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9110559225082397})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9964928030967712})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9419840574264526})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9556676149368286})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0580735206604004})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.1907298564910889})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.85304501953125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6679403185844421})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5597892999649048})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5106135606765747})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.523165762424469})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48114317655563354})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.49108004570007324})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.46917831897735596})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4941653907299042})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 44149], ['id', 41324], ['id', 54909], ['id', 23406], ['id', 38593]], 'labels': [2, 7, 8, 4, 3], 'scores': [0.8689530671288352, 1.6645057678146378, 2.2615382674567712, 2.651712301298261, 2.870169339539075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8539057970046997})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7058898210525513})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8933314681053162})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8788975477218628})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.010604739189148})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9881521463394165})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 1.038832187652588})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8925, 'crossentropy': 0.784132421875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7001214027404785})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5666204690933228})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5266843438148499})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5135853290557861})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5000642538070679})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4677671194076538})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 20996], ['id', 57764], ['id', 8678], ['id', 26703], ['id', 56053]], 'labels': [7, 6, 1, 9, 3], 'scores': [0.9008576999654371, 1.5964935869070631, 2.1604313646227657, 2.528423309986378, 2.7417535190246625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8522588610649109})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6622519493103027})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8076350688934326})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7502691745758057})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8245842456817627})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.651864306640625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6833086013793945})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5543406009674072})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5701009035110474})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5272585153579712})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 32880], ['id', 19942], ['id', 48102], ['id', 3273], ['id', 26892]], 'labels': [0, 5, 7, 8, -1], 'scores': [0.7248406435684069, 1.346137704866396, 1.8022698949407516, 2.1313766797868663, 2.3206436368568557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8443408608436584})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7650830745697021})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8308085203170776})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8559988737106323})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8546788692474365})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9111099243164062})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.885360836982727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.0035362243652344})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.795218896484375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7164926528930664})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5511064529418945})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.506162166595459})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4918097257614136})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.49119189381599426})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.47991567850112915})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.46950656175613403})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 46325], ['id', 15713], ['id', 50734], ['id', 24715], ['id', 12151]], 'labels': [4, 1, 5, 0, 3], 'scores': [0.8804778873438313, 1.6450451654028022, 2.268435042079699, 2.6473845137707377, 2.871902996575301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8193479776382446})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6522080898284912})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7325664162635803})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6688173413276672})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7648785710334778})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.767757773399353})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.83167564868927})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8584776520729065})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.709686279296875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6880629062652588})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46730467677116394})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.46180474758148193})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.47649863362312317})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4329301416873932})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 4822], ['id', 25281], ['id', 47220], ['id', 45212], ['id', 14819]], 'labels': [4, 2, 6, 5, 2], 'scores': [0.792701882347377, 1.471184285101061, 2.0439649666742445, 2.438169900939016, 2.6723129934922962]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7548850774765015})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6277602910995483})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6643941402435303})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6393039226531982})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.696492612361908})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7520545721054077})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.609930615234375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6849384307861328})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4940637946128845})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.46935737133026123})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43880048394203186})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4531662166118622})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 47885], ['id', 58464], ['id', 40636], ['id', 49487], ['id', 49489]], 'labels': [9, 8, 3, 8, 9], 'scores': [0.8024782800721768, 1.4827099503219086, 2.0212144804760808, 2.4101136043679485, 2.6030076525275394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9696967601776123})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.703869640827179})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7641988396644592})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7405612468719482})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8031604290008545})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6928562521934509})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8035562038421631})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7234418392181396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.773375391960144})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8189500570297241})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7939627170562744})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8430408239364624})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.7202939453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6426787376403809})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45179468393325806})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44060036540031433})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3796929717063904})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4012482762336731})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.38200509548187256})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37078720331192017})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42274], ['id', 23262], ['id', 57575], ['id', 21189], ['id', 46259]], 'labels': [5, 9, 0, -1, 2], 'scores': [0.9229433111332848, 1.702290746065703, 2.262242612284509, 2.5581670763011903, 2.714344717185652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8815151453018188})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5859886407852173})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6359319090843201})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6579249501228333})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7018460631370544})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7022343873977661})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7062424421310425})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7179062366485596})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8038782477378845})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7115461826324463})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.7115798828125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7032086849212646})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4882124960422516})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4385527968406677})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4160158038139343})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4087020754814148})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 42799], ['id', 18720], ['id', 4638], ['id', 42892], ['id', 17431]], 'labels': [2, 7, 3, 7, 2], 'scores': [0.8665937272213236, 1.5424596881093335, 2.065730818489614, 2.4152582409222996, 2.598087183267399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8525224924087524})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6123193502426147})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5895810127258301})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6009002327919006})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6510832905769348})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6845488548278809})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6536394357681274})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6734878420829773})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6776353716850281})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.8198868036270142})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.583344189453125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6598539352416992})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47036007046699524})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4469609260559082})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4223922789096832})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40380218625068665})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4260302186012268})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37563997507095337})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3762628436088562})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3755438029766083})
store['active_learning_steps'][20]['eval_training']['best_epoch']=9
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 39130], ['id', 56838], ['id', 42216], ['id', 8693], ['id', 27527]], 'labels': [6, 5, 4, 3, 3], 'scores': [0.8579495233739847, 1.5783055285111338, 2.161538191784496, 2.5513106488622332, 2.8014626029771312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0141043663024902})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7364005446434021})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6712498664855957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6286793351173401})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7786984443664551})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.700272798538208})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7169917225837708})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.74021315574646})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7908045053482056})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8940688371658325})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7376192808151245})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9234, 'crossentropy': 0.617492333984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7323786616325378})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5221374034881592})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4593910574913025})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4547293484210968})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4197794198989868})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.40282589197158813})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.38564616441726685})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 18150], ['id', 35946], ['id', 13969], ['id', 10972], ['id', 43184]], 'labels': [8, 4, 3, 2, 2], 'scores': [0.9354772981738033, 1.7245640168907301, 2.3374717637264006, 2.679485038906016, 2.880110840650927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9988702535629272})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6283074617385864})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.614403486251831})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.528389573097229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.602999210357666})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6157283186912537})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.5333328125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7557928562164307})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5274868011474609})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46388640999794006})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42685627937316895})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4540976881980896})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 59312], ['id', 53854], ['id', 38890], ['id', 40530], ['id', 47113]], 'labels': [4, 8, -1, 2, 2], 'scores': [0.7621114978316801, 1.409020184201374, 1.9188581143944434, 2.284700757737901, 2.516284927562511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9689880013465881})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6236746311187744})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6084141731262207})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6107325553894043})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6106430292129517})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7001262903213501})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6504033803939819})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7881410717964172})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6293139457702637})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7963590621948242})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.59941884765625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6868433356285095})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45944467186927795})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4204595386981964})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4142667055130005})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3935885727405548})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.37572216987609863})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3689255118370056})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3738735318183899})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36575770378112793})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 2803], ['id', 22169], ['id', 29340], ['id', 39265], ['id', 44595]], 'labels': [3, 2, 4, 1, 7], 'scores': [0.8914282345469715, 1.6004667321160317, 2.1482152822466185, 2.543320138390092, 2.774216074152327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.030195951461792})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6187076568603516})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5869665145874023})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6381958723068237})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6447703242301941})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6213011145591736})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.554026123046875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6644076108932495})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5097475051879883})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5032464265823364})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42828476428985596})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40051376819610596})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4948], ['id', 12059], ['id', 12830], ['id', 52358], ['id', 30083]], 'labels': [5, 9, 4, 2, 6], 'scores': [0.7484943465203016, 1.377345834831993, 1.901115123349408, 2.281488289626858, 2.535844819690909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9096468091011047})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5448273420333862})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5381253957748413})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5496061444282532})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5520855188369751})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6122274398803711})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5651552677154541})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5426278114318848})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5932282209396362})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5871022939682007})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6064629554748535})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.48221474609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6811747550964355})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4582602381706238})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4414769411087036})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40030932426452637})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3758901357650757})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37092530727386475})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3579726815223694})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3525036871433258})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3644082546234131})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33817681670188904})
store['active_learning_steps'][25]['eval_training']['best_epoch']=10
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 31782], ['id', 45972], ['id', 45456], ['id', 16022], ['id', 106]], 'labels': [5, 2, 7, 8, 6], 'scores': [0.7705663065265997, 1.475865560676791, 2.005676081186248, 2.379601215348809, 2.6114928776028483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9413771629333496})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5841484665870667})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.528516948223114})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5904492139816284})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5595654249191284})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6121803522109985})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.50686201171875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7079493403434753})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5222116708755493})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46930623054504395})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43228644132614136})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4284582734107971})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 55302], ['id', 56649], ['id', 9096], ['id', 10736], ['id', 17190]], 'labels': [0, 9, 5, 4, 9], 'scores': [0.7357218695680634, 1.3677278955619934, 1.885824791710105, 2.2713269429021548, 2.4768034941409605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0068730115890503})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6344183683395386})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5274266004562378})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5525587797164917})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5647953748703003})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.583987832069397})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5699050426483154})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.510333642578125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7070450782775879})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4804416298866272})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4306008219718933})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.38588911294937134})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3895854353904724})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3610176742076874})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 19590], ['id', 45917], ['id', 20120], ['id', 23956], ['id', 15893]], 'labels': [5, 9, 5, 4, 5], 'scores': [0.7513242547206647, 1.362253382514854, 1.8632474407019473, 2.1967531537954006, 2.4027717348431246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8310195207595825})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5546645522117615})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4925972819328308})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5777771472930908})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5412304401397705})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5638501644134521})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5345755815505981})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5642315149307251})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5722405910491943})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6552849411964417})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5787598490715027})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5846607685089111})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.5126580078125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7423094511032104})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45861831307411194})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4072846472263336})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3744756877422333})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.37839001417160034})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33563005924224854})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3526915907859802})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.33770066499710083})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3372182250022888})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 27984], ['id', 55438], ['id', 13428], ['id', 44853], ['id', 24061]], 'labels': [7, 8, 9, 7, -1], 'scores': [0.8211363941118595, 1.5243236202482402, 2.025199725071025, 2.3624441534378704, 2.580775136703785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9884473085403442})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5523326396942139})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5482628345489502})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5177552103996277})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.516232967376709})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5326521396636963})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5948656797409058})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6031994819641113})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.48462294921875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7453687787055969})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5072200298309326})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.46821415424346924})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.423265278339386})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.39871877431869507})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.37226617336273193})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3997514247894287})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 125], ['id', 48306], ['id', 22994], ['id', 916], ['id', 18864]], 'labels': [-1, 1, 2, 5, -1], 'scores': [0.7442744072250389, 1.3995180329417924, 1.942828670622493, 2.335523415606229, 2.574075107378124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0015671253204346})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7034512758255005})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6168757677078247})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6104697585105896})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.582781195640564})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6674095988273621})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.688245415687561})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.527034716796875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6878286600112915})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4799429476261139})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4677768051624298})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4268220365047455})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42307448387145996})
store['active_learning_steps'][30]['eval_training']['best_epoch']=2
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 43126], ['id', 36686], ['id', 29713], ['id', 26882], ['id', 30016]], 'labels': [3, 6, 0, 7, 4], 'scores': [0.6563947488485544, 1.2560387377957696, 1.763763076849333, 2.1378738807986704, 2.388479828483275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9813913106918335})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5935665369033813})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4895358681678772})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5622419118881226})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.543281078338623})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5666643977165222})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.46384140625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7457871437072754})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5598787069320679})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4652041792869568})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45891210436820984})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43209153413772583})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 44948], ['id', 125], ['id', 37347], ['id', 18322], ['id', 13769]], 'labels': [9, -1, 2, 7, 0], 'scores': [0.6750297010225081, 1.207957183883372, 1.6232037365465537, 1.93333879829125, 2.138114674771292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9673507213592529})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6081644296646118})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.567794680595398})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5704854726791382})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.652378499507904})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6080470085144043})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6856001615524292})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.478601318359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6599358320236206})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49632954597473145})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4331445097923279})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40490639209747314})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3727627396583557})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42088818550109863})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 38316], ['id', 42337], ['id', 30474], ['id', 13149], ['id', 3303]], 'labels': [4, 5, 6, 7, -1], 'scores': [0.6962943096408989, 1.3346316155478184, 1.8775066753216265, 2.3032158618954313, 2.5593475434733577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1256060600280762})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5615723729133606})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5155333876609802})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5371296405792236})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.523182213306427})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5566494464874268})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.45234833984375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7739964723587036})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5005820989608765})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43071508407592773})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.43862396478652954})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4134909510612488})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 48384], ['id', 24296], ['id', 54950], ['id', 55648], ['id', 55314]], 'labels': [9, 4, 8, 9, 6], 'scores': [0.6300702895473553, 1.1612302896860567, 1.6375942220573085, 1.9921581932396482, 2.250460392535371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9686165452003479})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5557330250740051})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5079001188278198})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4920288920402527})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4698704779148102})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5204073786735535})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5588338375091553})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5674890279769897})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.425207568359375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.715919017791748})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41503602266311646})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4179864823818207})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4172443747520447})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38157039880752563})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3562544584274292})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34356677532196045})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 20641], ['id', 9677], ['id', 40022], ['id', 30545], ['id', 39605]], 'labels': [9, 0, 8, 8, -1], 'scores': [0.7310874201346529, 1.3434535310185929, 1.8315988674473758, 2.191957846336466, 2.4025159089773975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.99623042345047})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5447636842727661})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5093680620193481})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5056729912757874})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4563496708869934})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5130195617675781})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5619449615478516})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5319376587867737})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5557456612586975})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6049185991287231})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.62375408411026})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9476, 'crossentropy': 0.4451173828125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6923081874847412})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4845043122768402})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39713525772094727})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3600846529006958})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3633151054382324})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.333122193813324})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3274654150009155})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34119290113449097})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3358904719352722})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32060128450393677})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 21066], ['id', 2198], ['id', 38524], ['id', 42746], ['id', 43952]], 'labels': [0, -1, 4, 2, -1], 'scores': [0.8294574633706986, 1.493306597876649, 2.058187059392761, 2.472429633822493, 2.743744999666042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0814149379730225})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5488147735595703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.570656418800354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5342180728912354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4898657202720642})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6082949638366699})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5437315702438354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5895049571990967})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.457740185546875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7968218326568604})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5293670892715454})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5038653612136841})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.398481547832489})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3926229476928711})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36321213841438293})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37485823035240173})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 2845], ['id', 26745], ['id', 31883], ['id', 2761], ['id', 47910]], 'labels': [8, 1, 4, 8, 1], 'scores': [0.7408302179402557, 1.3879111253328889, 1.9404343686946675, 2.3462192878191575, 2.615491763519678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9956554174423218})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6231021881103516})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5271157622337341})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5596140623092651})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5697134733200073})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5100407004356384})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.512173056602478})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5712142586708069})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5532540082931519})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6126126050949097})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.461458203125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.766069769859314})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5145475268363953})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4092424511909485})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3948800563812256})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3823825418949127})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3533957600593567})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 46878], ['id', 46441], ['id', 39208], ['id', 46440], ['id', 32368]], 'labels': [5, 6, 5, 6, -1], 'scores': [0.8168874779545485, 1.4994276962355673, 2.010566212106757, 2.382069080910682, 2.562712076123197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.096634864807129})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4778267741203308})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4542742371559143})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49889564514160156})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4888550043106079})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4870012700557709})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4721919298171997})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45495033264160156})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.482136607170105})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49610841274261475})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4847361445426941})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.403937451171875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6710872650146484})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44027233123779297})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3525104820728302})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35253003239631653})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3547212481498718})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.32690203189849854})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 28512], ['id', 1356], ['id', 32918], ['id', 27458], ['id', 7283]], 'labels': [5, 5, 2, 2, 3], 'scores': [0.7980257295921431, 1.5126922797026854, 2.002885071601977, 2.297836383685727, 2.484084210347638]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9364603757858276})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4980562627315521})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4224272072315216})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4635353088378906})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4750199317932129})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5118799209594727})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.3895394775390625}
