store = {}
store['timestamp']=1621478330
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=54']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=54
store['worker_id']=54
store['num_workers']=80
store['config']={'seed': 1291, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.0695018768310547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4104385375976562})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.591769218444824})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.607023239135742})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.76212215423584})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.1025476455688477})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.833822011947632})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.0202903747558594})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7620272636413574})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7005, 'crossentropy': 2.60809375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1348762512207031})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1502047777175903})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0844218730926514})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0979777574539185})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 35151], ['id', 30738], ['id', 38211], ['id', 39309], ['id', 55850]], 'labels': [5, 8, 0, 0, -1], 'scores': [1.1240525380105355, 2.0009395351340746, 2.577597391397254, 2.935037903372022, 3.141412431437457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3624563217163086})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5887255668640137})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.999969720840454})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.713907241821289})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0112838745117188})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6958, 'crossentropy': 2.17269609375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1746001243591309})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1569714546203613})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.188185691833496})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1282451152801514})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 27195], ['id', 13051], ['id', 3362], ['id', 34708], ['id', 23077]], 'labels': [8, 8, 2, 0, 8], 'scores': [0.8965907499499937, 1.6673345118560925, 2.2430737106731717, 2.6048664735588103, 2.807131840458358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4788501262664795})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.6752357482910156})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9657654762268066})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.995243549346924})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.0941104888916016})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.133543014526367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.2737877368927})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.0560755729675293})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6868, 'crossentropy': 2.6573607421875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3379039764404297})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2621525526046753})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1885573863983154})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2162431478500366})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2308825254440308})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2302470207214355})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 34495], ['id', 15947], ['id', 56482], ['id', 48653], ['id', 22789]], 'labels': [2, 3, 7, 4, 6], 'scores': [1.003258052365494, 1.8009880441397303, 2.4089805923947285, 2.827869104289915, 3.0504758358056527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.6250392198562622})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9356141090393066})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.2021684646606445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.2646069526672363})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.349722385406494})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7649, 'crossentropy': 1.746375390625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9453698396682739})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9499460458755493})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.884422779083252})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.8719394207000732})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 18247], ['id', 24479], ['id', 50378], ['id', 53048], ['id', 3531]], 'labels': [0, 8, 3, 3, 7], 'scores': [0.9189708121448261, 1.6437024264185793, 2.1596608707065075, 2.4924145112728837, 2.6964348760318098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.6732726097106934})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.9591119289398193})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9833641052246094})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 2.2884840965270996})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.3836538791656494})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.556745767593384})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.497584342956543})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7678, 'crossentropy': 2.1107923828125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0107643604278564})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.0131642818450928})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.987404465675354})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0067691802978516})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9456371068954468})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9701343774795532})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 14125], ['id', 58467], ['id', 18018], ['id', 10811], ['id', 44551]], 'labels': [2, 8, 5, 5, 0], 'scores': [0.9361571794921462, 1.7603272802638443, 2.321199117914305, 2.6852399594941128, 2.9208303811734613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.4707884788513184})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6330478191375732})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.897325873374939})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.2367305755615234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.121241569519043})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.1257524490356445})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 2.408323049545288})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.2464451789855957})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.45212459564209})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.372342586517334})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7723, 'crossentropy': 2.2868392578125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1271913051605225})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0451323986053467})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9701721668243408})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0910935401916504})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0141394138336182})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0080398321151733})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9969254732131958})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0608782768249512})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0322961807250977})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 17486], ['id', 14697], ['id', 19276], ['id', 10504], ['id', 20993]], 'labels': [7, 8, 6, 4, 2], 'scores': [0.9767830545637959, 1.7953684235672025, 2.437410711533988, 2.8364686226031717, 3.0226997178444996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2598414421081543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.488478660583496})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.712109088897705})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.7619774341583252})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.7784637212753296})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 2.0474724769592285})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.8182072639465332})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8099, 'crossentropy': 1.59123544921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9281200766563416})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8813866972923279})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8419228792190552})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8302723169326782})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8202375173568726})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8222957849502563})
store['active_learning_steps'][6]['eval_training']['best_epoch']=6
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 54490], ['id', 3494], ['id', 17467], ['id', 12757], ['id', 6388]], 'labels': [6, 7, 3, 7, 6], 'scores': [0.8878705174066417, 1.667993195531559, 2.232974675786113, 2.6198898890004436, 2.837398570450147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1948964595794678})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4777235984802246})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.594128131866455})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.651356816291809})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.9952601194381714})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 2.132875442504883})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.691396951675415})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 2.2685890197753906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.9267579317092896})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 2.1976184844970703})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8136, 'crossentropy': 1.6607244140625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9637119770050049})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8415101766586304})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8440427780151367})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8266329765319824})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8024706244468689})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 46640], ['id', 21660], ['id', 19501], ['id', 13085], ['id', 23734]], 'labels': [5, 3, 3, 6, 5], 'scores': [0.8348221002163365, 1.582701969670012, 2.1645797572228123, 2.534856597515091, 2.7460178363014194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.2040996551513672})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.650071382522583})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.8258495330810547})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.9288506507873535})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8893263339996338})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 2.0895419120788574})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.9401936531066895})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 2.2923455238342285})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 2.262348175048828})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 2.146084785461426})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.9745393991470337})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 2.1234235763549805})
store['active_learning_steps'][8]['training']['best_epoch']=9
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8177, 'crossentropy': 2.0081833984375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.899544358253479})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8632608652114868})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8372942805290222})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8006285429000854})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8077124953269958})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.78481525182724})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8571242094039917})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.7880871295928955})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 51736], ['id', 17362], ['id', 48811], ['id', 34771], ['id', 29483]], 'labels': [5, 8, 2, 0, 3], 'scores': [0.9110370435674924, 1.6902343842774976, 2.2715421920286545, 2.625123222030882, 2.786434760464524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2865886688232422})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.5586724281311035})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.8126401901245117})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.5675461292266846})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.9293943643569946})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.911799430847168})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 2.068934202194214})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8135, 'crossentropy': 1.503161328125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9161494970321655})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8954386711120605})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.8367547988891602})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8326560258865356})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8039482831954956})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8090026378631592})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 55064], ['id', 47613], ['id', 57913], ['id', 43212], ['id', 8200]], 'labels': [9, 7, 9, 5, 3], 'scores': [0.8835307312546945, 1.5866997612580969, 2.098688462545322, 2.4357252271781196, 2.6447269007350513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.185388207435608})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.4524116516113281})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.601822018623352})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.8169193267822266})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.7434632778167725})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.7940260171890259})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.8897068500518799})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.7309017181396484})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7985544204711914})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.88267982006073})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.8668237924575806})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.801, 'crossentropy': 1.6740673828125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8618175983428955})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8112801313400269})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8042534589767456})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.7695921659469604})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.7398530840873718})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.7558745741844177})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.7485135793685913})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.738489031791687})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 36122], ['id', 31301], ['id', 8622], ['id', 42125], ['id', 37767]], 'labels': [9, 5, 4, 7, 4], 'scores': [0.973987371617445, 1.7746617951044055, 2.34597510041928, 2.718521744266039, 2.8800931610490705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0134814977645874})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1660890579223633})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1757303476333618})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.236883521080017})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.227067232131958})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.4196267127990723})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2881011962890625})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5277315378189087})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 1.2120576171875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8571505546569824})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7228704690933228})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6948543190956116})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6579488515853882})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6536042094230652})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 14210], ['id', 46247], ['id', 22861], ['id', 28466], ['id', 28657]], 'labels': [-1, 3, 2, 0, 5], 'scores': [0.8573847232626686, 1.5557072800669318, 2.107490695696084, 2.433220276338016, 2.6462251575519327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1113860607147217})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1688947677612305})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.404652714729309})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3721569776535034})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.4732295274734497})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.657712459564209})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.446373462677002})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.5972198247909546})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.5120471715927124})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.6305570602416992})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.747294306755066})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8415, 'crossentropy': 1.35918173828125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8526524305343628})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7637833952903748})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.666603147983551})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6627966165542603})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.6670982837677002})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6201802492141724})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.6142746806144714})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6153320670127869})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6013218760490417})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 59377], ['id', 48102], ['id', 7533], ['id', 43424], ['id', 22719]], 'labels': [5, 7, 1, 6, 9], 'scores': [0.9570527508710525, 1.7799365380689176, 2.425694998948414, 2.821532663328619, 3.043360464279864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9224279522895813})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8258424997329712})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0756065845489502})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0779063701629639})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0984176397323608})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8624, 'crossentropy': 0.8385634765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7731384634971619})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6280407905578613})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6327832937240601})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5792118310928345})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37974], ['id', 5247], ['id', 8661], ['id', 55218], ['id', 33497]], 'labels': [2, 2, 8, 8, 6], 'scores': [0.7175626162819988, 1.335570699781789, 1.8260467692175295, 2.1751016249050945, 2.3790965421882637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0200889110565186})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9427802562713623})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9875137805938721})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.083467960357666})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.960869550704956})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1856505870819092})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.1412246227264404})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.2144978046417236})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8773, 'crossentropy': 0.876253515625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7373746633529663})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6162455677986145})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5672327280044556})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5172848701477051})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5191918015480042})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5586691498756409})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5264069437980652})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 28477], ['id', 7923], ['id', 47283], ['id', 55268], ['id', 46291]], 'labels': [5, 8, 8, 8, 1], 'scores': [0.8106527913236925, 1.5505740482902275, 2.125365650461117, 2.489751432446404, 2.683068530162976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.936626672744751})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9156838655471802})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1809000968933105})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0811302661895752})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.009542465209961})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2890105247497559})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2919100522994995})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2877813577651978})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.920291796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8240123391151428})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6482388973236084})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6589739918708801})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5895134806632996})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5536946058273315})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.5793628692626953})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5481654405593872})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14655], ['id', 53873], ['id', 47927], ['id', 2379], ['id', 26910]], 'labels': [3, 4, -1, 3, -1], 'scores': [0.807181806482014, 1.4732121084550345, 1.9970005659242176, 2.3509710605974945, 2.556106786674535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.952975869178772})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9218549728393555})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0816712379455566})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0615425109863281})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1799875497817993})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0821409225463867})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1814374923706055})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.2264366149902344})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1729851961135864})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0844104290008545})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.2314503192901611})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.3797647953033447})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2301857471466064})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.3076307773590088})
store['active_learning_steps'][16]['training']['best_epoch']=11
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8702, 'crossentropy': 1.04319501953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7308430671691895})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6201155185699463})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.5792708396911621})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5560659170150757})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5260356664657593})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5359125733375549})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5247027277946472})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5516085624694824})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46530], ['id', 19324], ['id', 52169], ['id', 15549], ['id', 57838]], 'labels': [4, 2, 2, 5, 2], 'scores': [0.9868970651959064, 1.7815236744887666, 2.4022141052514883, 2.7367732902408193, 2.887953201106308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8599625825881958})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8092761635780334})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8395293951034546})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9217057824134827})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9314593076705933})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8962, 'crossentropy': 0.70860888671875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.649300217628479})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5850590467453003})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5471869111061096})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5113070011138916})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 56004], ['id', 34052], ['id', 7160], ['id', 13099], ['id', 4970]], 'labels': [8, 9, 1, 3, 1], 'scores': [0.8063034776119191, 1.4483884685446355, 2.0035542436281553, 2.370829602428307, 2.597430647745954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.905312716960907})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.800716757774353})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7572252750396729})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.836588978767395})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8462016582489014})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9125977754592896})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.726270703125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7281742691993713})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5473819971084595})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5438074469566345})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5157595872879028})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4825456142425537})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 24608], ['id', 19824], ['id', 3710], ['id', 53522], ['id', 44105]], 'labels': [5, 9, 2, 2, 4], 'scores': [0.7530032152892234, 1.4088065498929896, 1.9618007089792, 2.344570064820047, 2.5661392924872324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9483412504196167})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7108848094940186})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7477730512619019})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7830728888511658})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8174909353256226})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.85285884141922})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8515664935112})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9276590943336487})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.720706640625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7736028432846069})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5156269073486328})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5139166116714478})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.46677497029304504})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4695306420326233})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.446390300989151})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.4816615879535675})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 41734], ['id', 37048], ['id', 59380], ['id', 511], ['id', 55314]], 'labels': [9, 9, 8, 7, 6], 'scores': [0.8426576875574951, 1.5810941343781053, 2.1509589733659453, 2.5205622103738072, 2.733281261777276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8569785356521606})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.707231342792511})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.666643500328064})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6829885244369507})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7443565130233765})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8024955987930298})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7832883596420288})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8171766400337219})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.760323166847229})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8501296043395996})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8221009969711304})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.722733203125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6743283271789551})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5142536163330078})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.4730430543422699})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4362216889858246})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.47116586565971375})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42703], ['id', 40646], ['id', 7705], ['id', 43952], ['id', 57965]], 'labels': [0, 8, -1, -1, -1], 'scores': [1.0051481673289564, 1.789744097064529, 2.3602071611708926, 2.741591799384681, 2.9743301821969954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8961319327354431})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6736608743667603})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6817618608474731})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7661130428314209})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7894672155380249})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8438478708267212})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8899848461151123})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.816696047782898})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9487811326980591})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8029258251190186})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8630571365356445})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9594736099243164})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8931084871292114})
store['active_learning_steps'][21]['training']['best_epoch']=10
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.7735333984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.721095085144043})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5396028757095337})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4800107479095459})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4788433909416199})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4638700783252716})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4577507972717285})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 26472], ['id', 11406], ['id', 30574], ['id', 48935], ['id', 32662]], 'labels': [-1, 8, 3, 3, 7], 'scores': [0.8302313502922942, 1.5586143982763625, 2.128987614894584, 2.537600739966339, 2.7878199764693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.009539008140564})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.744233250617981})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7634459137916565})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7155605554580688})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7668488025665283})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7701789736747742})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.884110689163208})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.646579541015625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7061814665794373})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5602715015411377})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.49664196372032166})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4553315341472626})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4707292318344116})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4446793794631958})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 50632], ['id', 44570], ['id', 35985], ['id', 58344], ['id', 24927]], 'labels': [1, 7, -1, 9, -1], 'scores': [0.7908377797446042, 1.5092260746156456, 2.057623024052866, 2.4102954685557076, 2.6286718851248416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8845410346984863})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7145218849182129})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6305810213088989})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6551855802536011})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7283393144607544})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7257118821144104})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.584589990234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7007898688316345})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5242739915847778})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.49967074394226074})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47030848264694214})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4655110239982605})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 1075], ['id', 26444], ['id', 13650], ['id', 56742], ['id', 50202]], 'labels': [7, 1, 4, 9, 5], 'scores': [0.7103159428118322, 1.3278991696429738, 1.8272607156744893, 2.1708040115971157, 2.3962098699661905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9541530013084412})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6938352584838867})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7222498655319214})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6704044342041016})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.744640588760376})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.737849235534668})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7696191072463989})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.600667138671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6601724624633789})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5262508988380432})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5048796534538269})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.46960487961769104})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.47305482625961304})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4532760977745056})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 5063], ['id', 14210], ['id', 44624], ['id', 49157], ['id', 9966]], 'labels': [9, 3, 8, 3, 0], 'scores': [0.7140644029287135, 1.3660094248109305, 1.921959885697131, 2.290486953589557, 2.5231901434351762]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9253708124160767})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6874437928199768})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6575142741203308})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7136767506599426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6908900737762451})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7435733079910278})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.566182470703125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6478813886642456})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5238146781921387})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4318614602088928})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4706774055957794})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4542773962020874})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 55743], ['id', 22139], ['id', 21023], ['id', 31347], ['id', 38890]], 'labels': [3, 2, 2, 3, -1], 'scores': [0.68261109871897, 1.3137969865541388, 1.8292687955812719, 2.177884552412193, 2.409284627600128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8740133047103882})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6456988453865051})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5572659969329834})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6382822394371033})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6182976961135864})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6555097103118896})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.485928662109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6820379495620728})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5327078104019165})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42615169286727905})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4327201843261719})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41611209511756897})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 5188], ['id', 29132], ['id', 9380], ['id', 50461], ['id', 32507]], 'labels': [5, 8, 3, 7, 5], 'scores': [0.7439365009186736, 1.3431913042748005, 1.8277705581758354, 2.164619109996943, 2.3605880108096544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9039968252182007})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6348326802253723})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5898283123970032})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6195489168167114})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6649526357650757})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6323285698890686})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6726862788200378})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6992975473403931})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7198880910873413})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6678981781005859})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.58778046875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7701520919799805})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5240200757980347})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45544764399528503})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4253878593444824})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3960886001586914})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4022521376609802})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3749004304409027})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3756854236125946})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 7415], ['id', 14650], ['id', 21287], ['id', 21527], ['id', 41587]], 'labels': [-1, 4, 4, 2, -1], 'scores': [0.7889064465114732, 1.5209043491516545, 2.098047239277556, 2.497304268134293, 2.7203310321991827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.026307225227356})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6102120876312256})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6005258560180664})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5540695190429688})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5858227014541626})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5879451036453247})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5797149538993835})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5657604932785034})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5707458257675171})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5833334922790527})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6588869094848633})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6263556480407715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6590242981910706})
store['active_learning_steps'][28]['training']['best_epoch']=10
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9335, 'crossentropy': 0.577187646484375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7149639129638672})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5222941637039185})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45318615436553955})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4162447154521942})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40047308802604675})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39109376072883606})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3870208263397217})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36987632513046265})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3575770854949951})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 13259], ['id', 18031], ['id', 8520], ['id', 36482], ['id', 11208]], 'labels': [1, 4, 8, -1, 9], 'scores': [0.9409588700683056, 1.693729834429257, 2.264430414570498, 2.6445489098559705, 2.8643282543145503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0188782215118408})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6171355247497559})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5712499022483826})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5929278135299683})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6965236663818359})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7123147249221802})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6064521074295044})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.5278548828125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6846675872802734})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.480998158454895})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4360552430152893})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4501268267631531})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4052441418170929})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3949189782142639})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 30351], ['id', 49563], ['id', 59747], ['id', 59927], ['id', 59684]], 'labels': [5, 8, 5, 9, 2], 'scores': [0.7779079398808513, 1.430073735277035, 1.943955303439532, 2.3039478356008223, 2.520215900155228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9807370901107788})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6566454172134399})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5574920773506165})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.630333662033081})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5747373700141907})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5613705515861511})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.526645361328125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7587276697158813})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.533288300037384})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5518924593925476})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4530063271522522})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4105362296104431})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 35864], ['id', 31557], ['id', 43648], ['id', 6311], ['id', 47479]], 'labels': [5, -1, 5, 1, -1], 'scores': [0.7844230829001826, 1.457829253994917, 1.9854146938588286, 2.346748810402305, 2.5829217941895326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0632437467575073})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6435242891311646})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6615687608718872})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5515233278274536})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5796220302581787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5485574007034302})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5701776742935181})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6425920724868774})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5827572345733643})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6321424841880798})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.528796142578125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7208261489868164})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5058334469795227})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4107162356376648})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3945975601673126})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3871801495552063})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.39326709508895874})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3747040629386902})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.37351155281066895})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 47597], ['id', 43952], ['id', 6174], ['id', 36072], ['id', 483]], 'labels': [8, -1, 9, 2, 7], 'scores': [0.7659039017768738, 1.4554629594717983, 1.9957932038827293, 2.360065453316089, 2.5960507085625952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0391559600830078})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5880809426307678})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5629938244819641})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5512744188308716})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5773184299468994})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6863301992416382})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6350239515304565})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9256, 'crossentropy': 0.510630224609375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7828689813613892})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5382827520370483})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4926372468471527})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40213823318481445})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43174028396606445})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4136485159397125})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 18487], ['id', 29839], ['id', 44286], ['id', 18598], ['id', 19675]], 'labels': [4, 2, 8, 9, 3], 'scores': [0.7600236238730265, 1.454882093384763, 1.9702938437080384, 2.299443708626969, 2.5019323523248342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9327861666679382})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6011258959770203})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6384475231170654})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5859183073043823})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6024148464202881})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5792863368988037})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5897223353385925})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6580133438110352})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7278690338134766})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7034705877304077})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.5644134765625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7332521677017212})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5088033676147461})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43334853649139404})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.401073157787323})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4004858136177063})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3741272985935211})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38017311692237854})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 20641], ['id', 54933], ['id', 26358], ['id', 43952], ['id', 33340]], 'labels': [9, 6, 3, -1, 5], 'scores': [0.807754159912415, 1.5485010720574794, 2.072663474240257, 2.4273139827345673, 2.5999356629089343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9940539598464966})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5588685274124146})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5568170547485352})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5213494896888733})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6385047435760498})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6953645348548889})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5413818359375})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.4935375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7166084051132202})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5158935189247131})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4465651512145996})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41168731451034546})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4432077407836914})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.412375807762146})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 48507], ['id', 11539], ['id', 23086], ['id', 46524], ['id', 31757]], 'labels': [6, -1, 8, 6, 2], 'scores': [0.7235596069917944, 1.3517113770647433, 1.8502315553074746, 2.204061298115402, 2.4097551216038573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2265390157699585})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6396373510360718})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5912929773330688})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5405087471008301})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6229428052902222})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5770522952079773})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7204653024673462})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.50555048828125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7727510929107666})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5197227001190186})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.49378928542137146})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45933443307876587})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4131212830543518})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40602582693099976})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 49624], ['id', 10746], ['id', 38275], ['id', 14641], ['id', 37168]], 'labels': [6, 9, 2, 6, 7], 'scores': [0.8321011927775019, 1.5183798741913943, 2.082667987216392, 2.4439236341641255, 2.6671644925554254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0566253662109375})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.59078049659729})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5329586863517761})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5329920053482056})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5864783525466919})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6335289478302002})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.486488623046875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8155075311660767})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5595564246177673})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5234160423278809})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45212322473526})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4421497583389282})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 22272], ['id', 33669], ['id', 15450], ['id', 42828], ['id', 34849]], 'labels': [5, -1, 6, 7, -1], 'scores': [0.6641993664987507, 1.229086683357941, 1.6789025072272787, 2.013658677685253, 2.225556426034734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0837953090667725})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6276620626449585})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5117815732955933})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5231653451919556})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.573184609413147})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5277257561683655})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5545350313186646})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5877331495285034})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6014381647109985})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.4880654296875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6895179748535156})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5128902196884155})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4117794632911682})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.39707648754119873})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37247979640960693})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35939592123031616})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3485141396522522})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3549604117870331})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 39909], ['id', 34133], ['id', 56773], ['id', 33035], ['id', 8628]], 'labels': [3, -1, 9, -1, -1], 'scores': [0.7554140709921799, 1.4223344423672581, 1.936324389835792, 2.288175991992399, 2.5080724964084133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.07613205909729})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6222849488258362})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6229029893875122})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5517011880874634})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.652541995048523})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5392457246780396})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5828755497932434})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5908874273300171})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5823554396629333})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.544508695602417})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6054584980010986})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5646592378616333})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6867715716362})
store['active_learning_steps'][38]['training']['best_epoch']=10
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.491706689453125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7245341539382935})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47990453243255615})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4012489914894104})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3743250370025635})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34973227977752686})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3501238226890564})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 34665], ['id', 21601], ['id', 51121], ['id', 16011], ['id', 3518]], 'labels': [9, 1, -1, 5, 7], 'scores': [0.7938232114549193, 1.5076270198172854, 2.1021974423137433, 2.5275457967422463, 2.7665771119507836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2154490947723389})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5818982720375061})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.55499267578125})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5406148433685303})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5647788643836975})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.555886447429657})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5698463916778564})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5729734897613525})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5690561532974243})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.454519921875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6920380592346191})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5067000389099121})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.453734815120697})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.41353029012680054})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3676947057247162})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35128122568130493})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35272714495658875})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3289448022842407})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 7287], ['id', 31557], ['id', 5553], ['id', 43952], ['id', 22194]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9094598787765085, 1.6113799345349844, 2.1698982765825487, 2.537520240188557, 2.760022816908285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0969116687774658})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.637236475944519})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4946415424346924})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5048975348472595})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6134142279624939})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5347273945808411})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.43254013671875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8208072185516357})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5646510124206543})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4982661306858063})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45112860202789307})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42335063219070435})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 38698], ['id', 2236], ['id', 39605], ['id', 28350], ['id', 38866]], 'labels': [5, 4, -1, -1, 8], 'scores': [0.6917774180925251, 1.306664403122972, 1.800552578589862, 2.1537503343688122, 2.410603600428728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1722729206085205})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6168189644813538})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5507088899612427})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.542356550693512})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5649082660675049})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5527174472808838})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5016775727272034})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6424597501754761})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5872980356216431})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5934426784515381})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.4211763671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.741192102432251})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4691266417503357})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4208630621433258})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3919372856616974})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34501025080680847})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33919578790664673})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36200135946273804})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3397480249404907})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31661027669906616})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 7851], ['id', 6130], ['id', 11196], ['id', 45774], ['id', 15899]], 'labels': [8, 7, 9, 3, 9], 'scores': [0.813685544914571, 1.5344382470826718, 2.038924910809812, 2.3851169598938133, 2.570271570547379]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0487163066864014})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6250898838043213})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46134740114212036})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5083876848220825})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.573644757270813})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5508254170417786})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6207088828086853})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6416453123092651})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.463055029296875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.745948076248169})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5185424089431763})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45615148544311523})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44871312379837036})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38618162274360657})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39679545164108276})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.42660367488861084})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 20110], ['id', 28860], ['id', 7847], ['id', 39314], ['id', 52092]], 'labels': [4, 4, -1, -1, 7], 'scores': [0.7229394396431568, 1.3642232673779255, 1.8969273220939478, 2.3016938823820743, 2.57536537519976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0653669834136963})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5994577407836914})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5296047329902649})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5088432431221008})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5215712785720825})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5817945003509521})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6425704956054688})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9435, 'crossentropy': 0.424053662109375}
