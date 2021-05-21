store = {}
store['timestamp']=1621483472
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=76']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=76
store['worker_id']=76
store['num_workers']=80
store['config']={'seed': 1314, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.0122885704040527})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4222729206085205})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.901320457458496})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8313562870025635})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6684, 'crossentropy': 1.882403125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 28520], ['id', 34708], ['id', 5499], ['id', 39494], ['id', 21650]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1103269964080364, 2.1298496230064536, 2.889763167924783, 3.4364032824310424, 3.8268753430348186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.1023712158203125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7423391342163086})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0261850357055664})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5031213760375977})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.065828323364258})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0350723266601562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.53025484085083})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.2192163467407227})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.357076406478882})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6767, 'crossentropy': 2.6302380859375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 28424], ['id', 45012], ['id', 25294], ['id', 41217], ['id', 14397]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.3209147144218667, 2.4338140565208075, 3.2512076904575604, 3.824917934020913, 4.167426115266342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.394947052001953})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.887578010559082})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.009777545928955})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.360827922821045})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6906821727752686})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6699, 'crossentropy': 2.226530859375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43205], ['id', 35340], ['id', 11213], ['id', 28953], ['id', 29422]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0984248388972049, 2.10161204665997, 2.916879028000004, 3.5295102260097835, 3.9280097172724098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9960310459136963})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.090881824493408})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4351916313171387})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2656798362731934})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.5548624992370605})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.1441292762756348})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.727, 'crossentropy': 1.85907109375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 14290], ['id', 4909], ['id', 46329], ['id', 31253], ['id', 33304]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.279638328073188, 2.300514441942411, 3.1297763191424757, 3.703527747859403, 4.0655750471681875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9481759071350098})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.133035182952881})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.1772284507751465})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5078604221343994})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.587344169616699})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.7916970252990723})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7174, 'crossentropy': 1.9111095703125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 3300], ['id', 17131], ['id', 23183], ['id', 29132], ['id', 11711]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1563451151676205, 2.116852583394211, 2.900958653473639, 3.5173703890881285, 3.9482489104581786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.6074159145355225})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0108120441436768})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.253329277038574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3036255836486816})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.483167886734009})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.4364142417907715})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2619476318359375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.661457061767578})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.7208919525146484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.630336046218872})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.3330307006835938})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.7097511291503906})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.7326767444610596})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.7337522506713867})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 3.018336057662964})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.834686279296875})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 3.040432929992676})
store['active_learning_steps'][5]['training']['best_epoch']=14
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7507, 'crossentropy': 2.3062240234375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 52686], ['id', 41006], ['id', 22579], ['id', 32555], ['id', 21270]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2926934491715663, 2.4133929768318554, 3.3316500753514458, 3.94571294936671, 4.279595667869044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6590893268585205})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.0605430603027344})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.4478282928466797})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.1129729747772217})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.1601650714874268})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.7047929763793945})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.5662643909454346})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.227924346923828})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.591948986053467})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.324746608734131})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.6223526000976562})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7746, 'crossentropy': 1.7845638671875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 52462], ['id', 54065], ['id', 19868], ['id', 34188], ['id', 55897]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.21492483802199, 2.331935050817476, 3.259418449706825, 3.8218228590234204, 4.171313097449463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.281081199645996})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3023688793182373})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6077901124954224})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6479039192199707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6419100761413574})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.9754652976989746})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.768188714981079})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.788415789604187})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8201, 'crossentropy': 1.34083603515625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 15899], ['id', 55021], ['id', 41572], ['id', 15562], ['id', 57334]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1559616979526592, 2.170816900600804, 2.9957662768819446, 3.627698914778562, 4.019469858402415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2623612880706787})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.4612685441970825})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3954464197158813})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.5497503280639648})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.8105974197387695})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.697648286819458})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8126, 'crossentropy': 1.23892255859375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 14164], ['id', 16584], ['id', 57632], ['id', 20641], ['id', 44901]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.144139842321703, 2.116196569997385, 2.915484782774036, 3.5162692698146767, 3.918636470864346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1391234397888184})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2672276496887207})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2943874597549438})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.4608224630355835})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4012136459350586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.4868755340576172})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8361, 'crossentropy': 1.0905021484375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 23849], ['id', 19605], ['id', 48681], ['id', 35903], ['id', 33593]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.056959346896313, 2.0456061899945452, 2.885371378387214, 3.495141290676938, 3.9211496749559105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0510343313217163})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9731994867324829})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9206885695457458})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1064941883087158})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0826212167739868})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.118193507194519})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2168992757797241})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8619, 'crossentropy': 0.96581650390625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 3070], ['id', 43042], ['id', 51492], ['id', 59321], ['id', 35401]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1226510513245433, 2.145281813266846, 2.9777754866468955, 3.601965271917715, 4.008886135423058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0271317958831787})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.049957275390625})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1745977401733398})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1884983777999878})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.143923044204712})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.2285465002059937})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2011566162109375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1801789999008179})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2925965785980225})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8679, 'crossentropy': 1.01545634765625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 6169], ['id', 40012], ['id', 4243], ['id', 21507], ['id', 38038]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.3516652900642245, 2.4391198694487217, 3.2525004062547644, 3.8315118830613564, 4.1952004382887145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0884591341018677})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.927625834941864})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1185433864593506})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0437748432159424})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1292574405670166})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.153641939163208})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.180341124534607})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3617380857467651})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2848525047302246})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2863342761993408})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.869, 'crossentropy': 1.02536806640625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 46580], ['id', 23104], ['id', 21421], ['id', 9331], ['id', 53872]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2155439389125935, 2.307071648237418, 3.180422496484125, 3.81030501409378, 4.175175669862057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0463647842407227})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8893625736236572})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9922257661819458})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9998729228973389})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9885995388031006})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9772185683250427})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0335615873336792})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0815062522888184})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0696766376495361})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0892707109451294})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9475752115249634})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.926125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 36417], ['id', 14619], ['id', 18589], ['id', 10044], ['id', 22083]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2566203199563386, 2.346324885724055, 3.250614311430752, 3.850716518874078, 4.210368610433559]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9245752096176147})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7518473863601685})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8488803505897522})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8143572211265564})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9088827967643738})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.66816279296875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24426], ['id', 5684], ['id', 17043], ['id', 8958], ['id', 25315]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9413595591249788, 1.8170868299894942, 2.5801951846985514, 3.19227149725851, 3.638412765226069]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9235676527023315})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6969577074050903})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8220566511154175})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8267014026641846})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.828504204750061})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8667092323303223})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8114392161369324})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8035445809364319})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8587650060653687})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8487050533294678})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9493038058280945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.928141176700592})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8777481317520142})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.931546688079834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7897622585296631})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8579802513122559})
store['active_learning_steps'][15]['training']['best_epoch']=13
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.717978564453125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 53181], ['id', 49202], ['id', 45800], ['id', 18398], ['id', 37129]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1628664115761191, 2.230276029420491, 3.1239114805224837, 3.763478752673195, 4.157012934459677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.837345540523529})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6512497663497925})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6675277948379517})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.721868634223938})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7211161851882935})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7135322690010071})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.549470068359375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 56940], ['id', 9180], ['id', 5013], ['id', 44143], ['id', 32776]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.005480964888325, 1.9187388870421787, 2.719396238375454, 3.3287226502234644, 3.776582223793582]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8882173299789429})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.713727593421936})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7402517795562744})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7926089763641357})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7751116752624512})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7752615809440613})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7888285517692566})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7703707218170166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.0286318063735962})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8888601064682007})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.65369853515625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 1423], ['id', 26444], ['id', 53120], ['id', 22648], ['id', 11747]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2133714312193542, 2.2797333032059703, 3.0977478283235804, 3.7271552303802276, 4.1209196819422775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.050113558769226})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6819438338279724})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6776794195175171})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6839179396629333})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7738059759140015})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7820955514907837})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8118106126785278})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.58847216796875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 1674], ['id', 8116], ['id', 15472], ['id', 10997], ['id', 2148]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0845822350778935, 2.066824663799286, 2.8700037746426164, 3.4929791228934572, 3.9078073638096082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9299346208572388})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6621500253677368})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5984154939651489})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6322070360183716})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6560837030410767})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7391314506530762})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6836541891098022})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7231025695800781})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.531925341796875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 39526], ['id', 40312], ['id', 31090], ['id', 2803], ['id', 4652]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0439949490793952, 2.0009647260921626, 2.8323707528457556, 3.4957254935877478, 3.9375465565564696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9361188411712646})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6253803968429565})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6208040118217468})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6028835773468018})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5816089510917664})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6340353488922119})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6355630159378052})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6751232147216797})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7120391130447388})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7170976400375366})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7740938663482666})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.58247080078125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 50916], ['id', 29472], ['id', 8709], ['id', 52697], ['id', 48540]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.160709182257553, 2.206916663266203, 3.0764925279126043, 3.7081817393961227, 4.119513086938228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9122570753097534})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5286003351211548})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6022453308105469})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5258803367614746})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6496556401252747})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6456015110015869})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5592398047447205})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.487369580078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 49890], ['id', 37347], ['id', 37696], ['id', 48158], ['id', 36818]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9692117422081856, 1.8535247221973306, 2.632627930842519, 3.2628148704418507, 3.7429829569213853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9996466636657715})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6020439863204956})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5734941363334656})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.600594162940979})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6758109331130981})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.542223974609375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 34524], ['id', 7833], ['id', 22272], ['id', 34328], ['id', 41239]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8340958991172838, 1.5924576573570248, 2.2631205893414235, 2.828999493837877, 3.2822248622214723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0103232860565186})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7091881632804871})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6201752424240112})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6340938806533813})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6722326278686523})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7301333546638489})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.596219539642334})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6091593503952026})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6869028806686401})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7062444686889648})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.548790673828125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 966], ['id', 41924], ['id', 59726], ['id', 51718], ['id', 14726]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.141853041093107, 2.174986658340906, 3.0437702001698606, 3.6835606941356716, 4.09376613163761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0183875560760498})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5927184820175171})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5930628776550293})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48831841349601746})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5871200561523438})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.605125904083252})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5894134044647217})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.436503515625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 517], ['id', 21700], ['id', 16825], ['id', 33222], ['id', 13998]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9535942270883013, 1.8056306794558683, 2.5659144970044556, 3.18625606508672, 3.6508107463714765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.171128749847412})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5557674765586853})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.570297360420227})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5772266387939453})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5240141749382019})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.522682666015625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 49826], ['id', 1239], ['id', 2761], ['id', 32323], ['id', 3810]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8292475818781337, 1.6235554050875574, 2.2655248839361475, 2.797720309859928, 3.2382183461918554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0668959617614746})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6103641986846924})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5595687627792358})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5400487184524536})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5431455373764038})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5454725027084351})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6508330702781677})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.576599657535553})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.44647607421875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 27427], ['id', 18487], ['id', 33162], ['id', 19501], ['id', 58832]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0692789424733427, 2.033314732307275, 2.8170068697463675, 3.4203823438348095, 3.845136752175131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2376604080200195})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.666301965713501})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.522136926651001})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5634058117866516})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5875914096832275})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5199267268180847})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.48517763671875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59309], ['id', 54885], ['id', 23112], ['id', 21390], ['id', 31706]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8311372931338894, 1.6063048842248047, 2.3182161981316067, 2.900795122806474, 3.3708417001951023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0418213605880737})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6330130100250244})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5046859979629517})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5498769879341125})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5121128559112549})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5468028783798218})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5243244171142578})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5675948262214661})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9442, 'crossentropy': 0.448355859375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 38698], ['id', 3010], ['id', 7437], ['id', 56014], ['id', 45443]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9814871261649034, 1.9147300687006537, 2.6932648394083474, 3.322584913494288, 3.7630359963518467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2115099430084229})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6384841203689575})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5425278544425964})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5873449444770813})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6338754296302795})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.505214273929596})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5633418560028076})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.579308032989502})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6246176958084106})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.428033251953125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 43745], ['id', 1134], ['id', 12934], ['id', 49200], ['id', 11292]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0993039307771184, 2.043497015907654, 2.8251721067015616, 3.4225757515228254, 3.8673775501429226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0530617237091064})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6492998600006104})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.546894907951355})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5560027956962585})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5829000473022461})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5778669118881226})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.483188427734375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 59314], ['id', 24860], ['id', 25803], ['id', 58560], ['id', 25945]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8907223251221417, 1.712058498818926, 2.435703606882374, 3.043775905501338, 3.5008546515083045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.10780668258667})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6294997930526733})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5658838748931885})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5852950215339661})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5741602182388306})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.662723958492279})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6074079275131226})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6522171497344971})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.4778115234375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 57628], ['id', 3136], ['id', 17855], ['id', 52169], ['id', 36704]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9779061207782038, 1.8641076848427973, 2.6392928035065246, 3.271109270873186, 3.7281499761390133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1729280948638916})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6337512731552124})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5769529342651367})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5743481516838074})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.584797739982605})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5369740724563599})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5407823324203491})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.611678957939148})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6805223822593689})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6594828367233276})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.457918603515625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 10012], ['id', 39305], ['id', 34916], ['id', 30900], ['id', 34847]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0298690772000545, 1.9806807877669241, 2.799745610407089, 3.4265600522593367, 3.885999982701575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0857758522033691})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.57839035987854})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5178631544113159})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.492737352848053})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5037773847579956})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5638796091079712})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5013265013694763})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5038661956787109})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.547448992729187})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5293151140213013})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5280982255935669})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.423500830078125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 36642], ['id', 7886], ['id', 19576], ['id', 2352], ['id', 27431]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.095944195992566, 2.1180062249756855, 2.9259553851141327, 3.533420633148012, 3.9517497229925658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1875125169754028})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6320885419845581})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5162070393562317})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.490028440952301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4654691517353058})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44914329051971436})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48648566007614136})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5165812373161316})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46670326590538025})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9468, 'crossentropy': 0.3867770263671875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 13942], ['id', 54195], ['id', 42799], ['id', 59286], ['id', 12211]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0734422056231183, 1.9920568755418882, 2.7921610223746303, 3.4197979477008396, 3.888953893138213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.197045922279358})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5868240594863892})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5176078081130981})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4423339366912842})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5060411095619202})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4803638458251953})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47697728872299194})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4797687828540802})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5471173524856567})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5775997638702393})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4533992111682892})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9528, 'crossentropy': 0.3937214599609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 36118], ['id', 30844], ['id', 55906], ['id', 7498], ['id', 32427]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1238838503438988, 2.1292290697568603, 2.972432984375999, 3.6012679661080877, 4.030285883425309]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2747406959533691})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6147038340568542})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.498873770236969})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5052119493484497})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47479456663131714})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5134683847427368})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.445302294921875}
