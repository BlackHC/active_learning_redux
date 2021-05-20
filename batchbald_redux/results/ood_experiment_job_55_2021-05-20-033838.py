store = {}
store['timestamp']=1621478318
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=55']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=55
store['worker_id']=55
store['num_workers']=80
store['config']={'seed': 1292, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.750518321990967})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.920135021209717})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.4163498878479004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.894437313079834})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.5746541023254395})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5894, 'crossentropy': 3.274939453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3838746547698975})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.424283504486084})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4346003532409668})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.4998960494995117})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 50571], ['id', 30295], ['id', 13455], ['id', 54482], ['id', 44686]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0491423554682247, 1.8638358381160907, 2.4198111189288607, 2.751524992657788, 2.9355036100406107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.517332077026367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.249253749847412})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.4968485832214355})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.503678798675537})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.56667423248291})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.8758232593536377})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.14130973815918})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5937, 'crossentropy': 3.82569140625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.5041929483413696})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5674304962158203})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.5549159049987793})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5298947095870972})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6568620204925537})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5168604850769043})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 603], ['id', 56481], ['id', 58264], ['id', 22395], ['id', 6612]], 'labels': [-1, -1, 2, 8, -1], 'scores': [1.1283241862067874, 1.952889347338647, 2.4893194754088963, 2.8034221948963793, 2.965128659832115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.5645244121551514})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.234679698944092})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2710161209106445})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2753713130950928})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.316619634628296})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.909972906112671})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6242, 'crossentropy': 3.385353125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5136630535125732})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4762756824493408})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5374295711517334})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4331820011138916})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.6111829280853271})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 42365], ['id', 46467], ['id', 45942], ['id', 13476], ['id', 50144]], 'labels': [-1, -1, -1, 8, 3], 'scores': [1.1770644102215544, 2.002712415561963, 2.5246735497997568, 2.824180983009655, 2.993480122364244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.155827760696411})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7907567024230957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0461792945861816})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.343846321105957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5144896507263184})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6205, 'crossentropy': 2.924347265625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3455407619476318})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.283153772354126})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3170857429504395})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.318198561668396})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27643], ['id', 27471], ['id', 9304], ['id', 10444], ['id', 16979]], 'labels': [-1, -1, -1, 9, 4], 'scores': [1.0976804711237276, 1.9327705605342675, 2.4878978921822537, 2.839337456954058, 2.9992960410476224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.7820826768875122})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2491984367370605})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.714078426361084})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7981979846954346})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6453, 'crossentropy': 1.87662734375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1628915071487427})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1254427433013916})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1019858121871948})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 28135], ['id', 18412], ['id', 39342], ['id', 22501], ['id', 19695]], 'labels': [-1, -1, -1, 7, -1], 'scores': [1.0444067121619733, 1.6970668420026875, 2.180460061445399, 2.4973684701394827, 2.677288934511605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.1835689544677734})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5345726013183594})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.555622100830078})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1284546852111816})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.2147879600524902})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4761900901794434})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.158416271209717})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1776580810546875})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6289, 'crossentropy': 3.443878125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3314378261566162})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2602320909500122})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2783257961273193})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2255382537841797})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2349298000335693})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3177522420883179})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2804652452468872})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 4530], ['id', 56476], ['id', 56936], ['id', 59828], ['id', 22693]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.2444338653541644, 2.173634730397392, 2.7127866372626936, 2.9755942674829976, 3.082098653756759]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9509304761886597})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.291933059692383})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6385931968688965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.9348697662353516})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.8483662605285645})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.103870391845703})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.123535633087158})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.3322653770446777})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.144178867340088})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6594, 'crossentropy': 3.266090234375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2897504568099976})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.361036777496338})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2643954753875732})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3408514261245728})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.360670566558838})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.370928168296814})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 36050], ['id', 53796], ['id', 3875], ['id', 14159], ['id', 50554]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.064382223315952, 1.9286809403732779, 2.482001403780835, 2.7136222004715833, 2.8119896493224976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.200376510620117})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.403736114501953})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9818108081817627})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0216281414031982})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.084827423095703})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.412360906600952})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.4129843711853027})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.262376308441162})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6329, 'crossentropy': 3.1721474609375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3272712230682373})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3279523849487305})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.448843002319336})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2873880863189697})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2571749687194824})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3713126182556152})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3253151178359985})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 48963], ['id', 54488], ['id', 52578], ['id', 8616], ['id', 31301]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1232221769692692, 2.029485992413261, 2.622799137472011, 2.9546762162250984, 3.1157874538227555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.138105630874634})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.072763681411743})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.9213459491729736})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.45849609375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.916863203048706})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5349135398864746})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6065, 'crossentropy': 3.325189453125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.29827880859375})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2851636409759521})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2412981986999512})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4166350364685059})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.387437343597412})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 59788], ['id', 22167], ['id', 32641], ['id', 15126], ['id', 58591]], 'labels': [-1, -1, 0, -1, 6], 'scores': [0.9160326644934162, 1.626889425631938, 2.181296632567606, 2.454209609905794, 2.5936337317525595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.1025867462158203})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.653350591659546})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.923394203186035})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2689638137817383})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1017088890075684})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5859198570251465})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6161, 'crossentropy': 3.081384765625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3014039993286133})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.174320936203003})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2951133251190186})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.254441499710083})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2564404010772705})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 42942], ['id', 28757], ['id', 14781], ['id', 40269], ['id', 18003]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.1473181983514844, 2.004614386267312, 2.595790454791376, 2.9382091896529285, 3.117281130670891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8508222103118896})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.4689712524414062})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.497441530227661})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6141517162323})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7740917205810547})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3916239738464355})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7456490993499756})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6393, 'crossentropy': 2.8110228515625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3334884643554688})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2596365213394165})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1841599941253662})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2995649576187134})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2275415658950806})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2757816314697266})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 24941], ['id', 31744], ['id', 24422], ['id', 32376], ['id', 16413]], 'labels': [-1, -1, -1, 5, 7], 'scores': [1.1227119109777897, 1.9495466712255065, 2.46329981363138, 2.739667371202363, 2.8380557927228605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9408159255981445})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.16359806060791})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8063178062438965})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3280768394470215})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1696934700012207})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.419344663619995})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.4788970947265625})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.598768711090088})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4342877864837646})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.6627674102783203})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.427279472351074})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6278, 'crossentropy': 3.800520703125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2247018814086914})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3625707626342773})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3425376415252686})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4339261054992676})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59422], ['id', 8047], ['id', 49481], ['id', 47840], ['id', 39749]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.105579810083512, 1.9820360546318851, 2.5019840311694677, 2.8058554186778144, 2.903576128728478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.814769983291626})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.3847744464874268})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7472686767578125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.923549175262451})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9983909130096436})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6034, 'crossentropy': 2.6343150390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2185120582580566})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2990185022354126})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3548104763031006})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2662842273712158})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 10620], ['id', 40262], ['id', 17129], ['id', 33735], ['id', 13179]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.9964375813563007, 1.8325552903546023, 2.4141810108283632, 2.75859885090033, 2.933230833192712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.8476290702819824})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.265209436416626})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.8877031803131104})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2011449337005615})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 1.88485}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2691706418991089})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.177255392074585})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2078883647918701})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 38515], ['id', 36089], ['id', 2019], ['id', 42521], ['id', 3929]], 'labels': [8, 8, -1, 8, 3], 'scores': [0.7392176227422702, 1.3811130088391428, 1.8529500163129855, 2.181157923126764, 2.396356158600744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.8242195844650269})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 2.720545768737793})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.1193113327026367})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.704972267150879})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6009058952331543})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.595060348510742})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.92911958694458})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5662546157836914})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.7901346683502197})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.739088535308838})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.4472312927246094})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5879, 'crossentropy': 4.011346484375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.4290997982025146})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.436863899230957})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.4302254915237427})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4613947868347168})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.5883034467697144})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20098], ['id', 34277], ['id', 50887], ['id', 12399], ['id', 5707]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.080445200366134, 1.9757088315005298, 2.6162009290958093, 2.9368513228842397, 3.072620932368033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.9402282238006592})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.7556138038635254})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.181694507598877})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.226869583129883})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.630669355392456})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.673795223236084})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.9299111366271973})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5842, 'crossentropy': 3.754155859375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.436282992362976})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.4885742664337158})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.5136059522628784})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4251172542572021})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5092612504959106})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4746887683868408})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 44378], ['id', 10359], ['id', 38960], ['id', 5587], ['id', 54134]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0161710665779589, 1.8773770280930804, 2.4851028930265446, 2.775768053072774, 2.932927845064212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.03790283203125})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.8988254070281982})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.0494256019592285})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.2338781356811523})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.6560442447662354})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.8205513954162598})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.576249599456787})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5881, 'crossentropy': 3.5212859375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3579680919647217})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.523221731185913})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3322663307189941})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3841276168823242})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3308794498443604})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3648737668991089})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49419], ['id', 46585], ['id', 49101], ['id', 19531], ['id', 1749]], 'labels': [-1, -1, -1, 5, 3], 'scores': [1.1762777136546614, 2.015920225021062, 2.5860347353862565, 2.934251048856856, 3.0846967419891875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.9994826316833496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.5843639373779297})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6510729789733887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.009007453918457})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.054276466369629})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.4569039344787598})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.14047908782959})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.853396415710449})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6124, 'crossentropy': 3.365983984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3915754556655884})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4000582695007324})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3994712829589844})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.307023048400879})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.383164644241333})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4156320095062256})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3614094257354736})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 32452], ['id', 46903], ['id', 40262], ['id', 20328], ['id', 17760]], 'labels': [-1, -1, -1, 0, 5], 'scores': [1.1605212623800603, 2.1638723161976734, 2.7955579294252133, 3.0901837249888677, 3.2219220319769883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.8064796924591064})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 2.4180212020874023})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.8887739181518555})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.091172218322754})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.106250286102295})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.191213846206665})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.382807970046997})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.9352006912231445})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.214984893798828})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4929795265197754})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.5951, 'crossentropy': 3.85843515625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.4328380823135376})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4534707069396973})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4058080911636353})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.4430820941925049})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.402535319328308})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 55316], ['id', 58507], ['id', 36866], ['id', 17926], ['id', 22649]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0425872089954562, 1.9215794691060761, 2.54042905049754, 2.8334885882600265, 2.9654922891017312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.696922779083252})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.3932464122772217})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.739278793334961})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.8668718338012695})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.372072219848633})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1088171005249023})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6015, 'crossentropy': 2.70061484375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2959041595458984})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3577220439910889})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2970001697540283})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3540465831756592})
store['active_learning_steps'][19]['eval_training']['best_epoch']=1
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 7408], ['id', 6000], ['id', 8388], ['id', 24422], ['id', 15382]], 'labels': [-1, 8, -1, -1, 2], 'scores': [0.9825094751078778, 1.8664073770318095, 2.3860335146895335, 2.6885258387897046, 2.8242621634392133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.5898059606552124})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.1692256927490234})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.4871644973754883})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.138749599456787})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0387115478515625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9641380310058594})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9606480598449707})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.5040581226348877})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6118, 'crossentropy': 3.107884765625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.408887505531311})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3907195329666138})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4099304676055908})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3841252326965332})
store['active_learning_steps'][20]['eval_training']['best_epoch']=1
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 26187], ['id', 37678], ['id', 2148], ['id', 27181], ['id', 15119]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9254579618249461, 1.7342284395965857, 2.309723837498691, 2.585788860997595, 2.7000758118500325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.7674823999404907})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.1862223148345947})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.694979190826416})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.9129247665405273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8249588012695312})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9514474868774414})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.222193717956543})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.466799736022949})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6086, 'crossentropy': 3.158253515625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.325120449066162})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3303682804107666})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3110754489898682})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2561341524124146})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2486873865127563})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3765568733215332})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2801291942596436})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 22620], ['id', 6860], ['id', 6424], ['id', 39171], ['id', 38613]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1084211676246039, 1.9144328741873649, 2.4853977371401, 2.7942321378481667, 2.9547480185144073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.7386411428451538})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.1467738151550293})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.4860939979553223})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.05049991607666})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.926689624786377})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.020371437072754})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2081499099731445})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.3950939178466797})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.215750217437744})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.2728517055511475})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.142246246337891})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.580838680267334})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.708712577819824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5764334201812744})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3938839435577393})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.759117603302002})
store['active_learning_steps'][22]['training']['best_epoch']=13
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.5985, 'crossentropy': 4.055880859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.360741376876831})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3718323707580566})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.561625361442566})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.5528725385665894})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.5161995887756348})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 25732], ['id', 55818], ['id', 48967], ['id', 13883], ['id', 3418]], 'labels': [-1, -1, -1, 1, 9], 'scores': [1.1072709948327129, 2.0184892143731683, 2.6802319426361065, 2.9755745707596084, 3.0968560515952444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.7309880256652832})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.895518183708191})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.5572428703308105})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.037734031677246})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.985015392303467})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.614, 'crossentropy': 2.2207791015625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1968097686767578})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1651434898376465})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1217567920684814})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1436479091644287})
store['active_learning_steps'][23]['eval_training']['best_epoch']=1
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 3603], ['id', 42309], ['id', 24023], ['id', 52242], ['id', 26568]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9701392139632823, 1.7989382801167593, 2.32123980497128, 2.6025713381478077, 2.7191318485840865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4976757764816284})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.884356141090393})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.2793612480163574})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.665668249130249})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.717505931854248})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6305527687072754})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6261, 'crossentropy': 2.36150703125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.177997350692749})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.170445203781128})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1763997077941895})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1612377166748047})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1659700870513916})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 26230], ['id', 46593], ['id', 55523], ['id', 380], ['id', 21146]], 'labels': [-1, -1, -1, 6, 1], 'scores': [0.9682350348975621, 1.7578814119366433, 2.2572622518701646, 2.5246326946424116, 2.663410013485265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3307476043701172})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5557913780212402})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.093127727508545})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.130211353302002})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3144259452819824})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6512, 'crossentropy': 1.8162482421875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0925211906433105})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0333800315856934})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0142147541046143})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.004507303237915})
store['active_learning_steps'][25]['eval_training']['best_epoch']=2
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 58885], ['id', 13120], ['id', 7887], ['id', 54461], ['id', 49933]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8352708310346333, 1.5531177833623084, 2.074405465806115, 2.3895283810711803, 2.5810166990993864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4903934001922607})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9685554504394531})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.199237823486328})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.463221311569214})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5311169624328613})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.5558769702911377})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.73953914642334})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.688520669937134})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6526, 'crossentropy': 2.6124755859375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1255910396575928})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1065857410430908})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0877245664596558})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1208348274230957})
store['active_learning_steps'][26]['eval_training']['best_epoch']=1
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 12585], ['id', 37671], ['id', 32445], ['id', 1624], ['id', 24978]], 'labels': [-1, -1, -1, 8, 6], 'scores': [1.0307484006177703, 1.926126613470493, 2.4387352803823354, 2.665407379922577, 2.740483400102012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.440035343170166})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8519026041030884})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.222675323486328})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.358391761779785})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5229241847991943})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.967209815979004})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8982887268066406})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.992490291595459})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.360750913619995})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.002309799194336})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1012399196624756})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1335203647613525})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.356766939163208})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1101112365722656})
store['active_learning_steps'][27]['training']['best_epoch']=11
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6371, 'crossentropy': 3.372433984375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1698508262634277})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.177391529083252})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2381641864776611})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2284232378005981})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2201528549194336})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 45872], ['id', 7254], ['id', 29769], ['id', 1933], ['id', 21713]], 'labels': [-1, -1, -1, 2, 6], 'scores': [1.1794618318226344, 2.141628280242599, 2.754967150219165, 3.0861614269288182, 3.2023316033819977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.4813625812530518})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.9871480464935303})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.0827856063842773})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.4221107959747314})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.490001678466797})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6198, 'crossentropy': 2.0491953125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.173086404800415})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1590392589569092})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1278685331344604})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1181731224060059})
store['active_learning_steps'][28]['eval_training']['best_epoch']=1
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 12585], ['id', 39283], ['id', 30220], ['id', 49593], ['id', 28709]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.930335326947618, 1.688978883679951, 2.2106774028951754, 2.5189651139832536, 2.672323431520393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4431607723236084})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.924825668334961})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.132432460784912})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.47947359085083})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.373255968093872})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.549422264099121})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.8957157135009766})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7999587059020996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9075851440429688})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 2.907896875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2133762836456299})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3199090957641602})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2341904640197754})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2629616260528564})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2042710781097412})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.276628017425537})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.242967128753662})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2966636419296265})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 21304], ['id', 27], ['id', 46069], ['id', 49066], ['id', 55563]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.155117801317418, 1.9828026958106346, 2.533848346256222, 2.8398118027322945, 2.988304161239025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.5199856758117676})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.8572642803192139})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1313915252685547})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.217878818511963})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.405546188354492})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.7618207931518555})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6332, 'crossentropy': 2.3507142578125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1907093524932861})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.160050868988037})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1951826810836792})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.173722743988037})
store['active_learning_steps'][30]['eval_training']['best_epoch']=1
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 48063], ['id', 49880], ['id', 39625], ['id', 27413], ['id', 900]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.021489956615735, 1.90832246413511, 2.462214451749354, 2.7328990581663852, 2.852623181492276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4999299049377441})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.8553168773651123})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9618735313415527})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.241583824157715})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4174914360046387})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7654542922973633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.777958869934082})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.1727142333984375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.891495704650879})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6546, 'crossentropy': 2.7869818359375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2548707723617554})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.194506287574768})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2352737188339233})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1961400508880615})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.220284104347229})
store['active_learning_steps'][31]['eval_training']['best_epoch']=2
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 36339], ['id', 32192], ['id', 12271], ['id', 56561], ['id', 44121]], 'labels': [-1, -1, -1, 2, 2], 'scores': [1.0289038048411734, 1.9033467159110602, 2.4851674458822894, 2.7614540132016696, 2.9020007221422546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.4588960409164429})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.9805400371551514})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.107853412628174})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3543806076049805})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.63002872467041})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.538602352142334})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5281481742858887})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6337, 'crossentropy': 2.576587890625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2540595531463623})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.170455813407898})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1867990493774414})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.173940658569336})
store['active_learning_steps'][32]['eval_training']['best_epoch']=1
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 24602], ['id', 45607], ['id', 57606], ['id', 52728], ['id', 19025]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1569790000654718, 2.023069751726049, 2.6180858120136588, 2.904346490512297, 3.028610776257131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4544825553894043})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.8476834297180176})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.01635479927063})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.2769010066986084})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4698104858398438})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8536040782928467})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9637558460235596})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.96242618560791})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8759546279907227})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6361, 'crossentropy': 3.02557890625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3128609657287598})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2719061374664307})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3392239809036255})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3488235473632812})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3823094367980957})
store['active_learning_steps'][33]['eval_training']['best_epoch']=2
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 43513], ['id', 9699], ['id', 35344], ['id', 55753], ['id', 18166]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.033791726127475, 1.9224861072963524, 2.447205064965468, 2.675633347209766, 2.741016043155658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.242324709892273})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.805474042892456})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.879941463470459})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.3183093070983887})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6644, 'crossentropy': 1.2933681640625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0766886472702026})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.02576744556427})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9967867136001587})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 33161], ['id', 1048], ['id', 45832], ['id', 391], ['id', 554]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8167119691119482, 1.3955817072151002, 1.8582211854138198, 2.2062143393565163, 2.463038952330571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.361892580986023})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8074607849121094})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0201797485351562})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1631274223327637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.453676700592041})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.500450611114502})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.5835671424865723})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.657, 'crossentropy': 2.340268359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.140716791152954})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0899779796600342})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0628399848937988})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0817232131958008})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0950181484222412})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0993077754974365})
store['active_learning_steps'][35]['eval_training']['best_epoch']=3
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 28275], ['id', 34062], ['id', 49824], ['id', 9567], ['id', 31847]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.0049091405634543, 1.7879266503187927, 2.3243054481732095, 2.588370548326589, 2.733967110062024]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3570220470428467})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5933183431625366})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.9833979606628418})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.208425521850586})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.2706775665283203})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.445629596710205})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.5970451831817627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.689690113067627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.7773241996765137})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.9793503284454346})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 3.013944625854492})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.9828929901123047})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6704, 'crossentropy': 2.87720234375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2368848323822021})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1491628885269165})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.100814938545227})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0773040056228638})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1160860061645508})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0657916069030762})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.129943609237671})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.137704610824585})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0952167510986328})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 21809], ['id', 23026], ['id', 19719], ['id', 37080], ['id', 13781]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1505977958463647, 2.0649263293513385, 2.6686905776789773, 2.9455210764055435, 3.0853896009003154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2841993570327759})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.746111273765564})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8082928657531738})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.228537082672119})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.526038646697998})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.4389519691467285})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6609, 'crossentropy': 2.0580736328125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1243044137954712})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1140179634094238})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0680830478668213})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1299879550933838})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1138947010040283})
store['active_learning_steps'][37]['eval_training']['best_epoch']=2
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 17926], ['id', 23497], ['id', 17967], ['id', 58670], ['id', 12241]], 'labels': [-1, -1, -1, 8, 5], 'scores': [0.8262086031332391, 1.5322881146315876, 2.0611187862406375, 2.362786407370862, 2.5574052487808077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4177111387252808})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6124799251556396})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8406859636306763})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1766793727874756})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.146130084991455})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.4196248054504395})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.71610689163208})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7675275802612305})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5012450218200684})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6396, 'crossentropy': 2.7600205078125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2605247497558594})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2498852014541626})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2432589530944824})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3060243129730225})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3413548469543457})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2024643421173096})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2556209564208984})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3278772830963135})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 56298], ['id', 49160], ['id', 3694], ['id', 45230], ['id', 33703]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.0885234194649713, 1.9691544037070021, 2.5618658868556685, 2.8409941984572216, 2.9379830767789095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3610587120056152})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6976776123046875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.0685129165649414})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.236166000366211})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.3191919326782227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.498960256576538})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.5966954231262207})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4925146102905273})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.1442904472351074})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.754269599914551})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6654, 'crossentropy': 2.770830078125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2639952898025513})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2027298212051392})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1379592418670654})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.242048740386963})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2529826164245605})
store['active_learning_steps'][39]['eval_training']['best_epoch']=2
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 15775], ['id', 27289], ['id', 35607], ['id', 49824], ['id', 14924]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.0751658415765668, 1.9361154442408415, 2.4923039968738996, 2.7827521863822877, 2.9062440975945876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2043957710266113})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.498468041419983})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8059335947036743})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.081968307495117})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.2139978408813477})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.427560806274414})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.4653995037078857})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6557, 'crossentropy': 2.26153671875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0850772857666016})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.093841791152954})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0864949226379395})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1174777746200562})
store['active_learning_steps'][40]['eval_training']['best_epoch']=1
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 26340], ['id', 16574], ['id', 22793], ['id', 28076], ['id', 48102]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0446110505160422, 1.8399314437977425, 2.3734892595090527, 2.6480691195660144, 2.786838701238679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4013375043869019})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.657990574836731})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.9440898895263672})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.161895275115967})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.234238386154175})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.2788033485412598})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.607717990875244})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5786831378936768})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6001930236816406})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6479954719543457})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.0389857292175293})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.348529577255249})
store['active_learning_steps'][41]['training']['best_epoch']=9
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6492, 'crossentropy': 2.9944892578125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2184841632843018})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.214590072631836})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2687442302703857})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2721110582351685})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3549954891204834})
store['active_learning_steps'][41]['eval_training']['best_epoch']=2
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 13994], ['id', 108], ['id', 51385], ['id', 39304], ['id', 45276]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1153388059960587, 1.9889302995429694, 2.6234185553285223, 2.9008925578203684, 3.025020300399313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2542526721954346})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.610170841217041})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.9899711608886719})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.08313250541687})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.1289873123168945})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2122650146484375})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.3535985946655273})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4590580463409424})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6664, 'crossentropy': 2.3404484375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1535837650299072})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0965274572372437})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1700021028518677})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1217621564865112})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0817277431488037})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0723841190338135})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1336612701416016})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 9052], ['id', 46493], ['id', 52560], ['id', 35604], ['id', 40744]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.1525088413175273, 2.028115416333993, 2.6402868307142446, 2.9018502615373327, 3.0105790398172587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3074392080307007})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7451484203338623})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.0137243270874023})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.2257449626922607})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.461270332336426})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.4039688110351562})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.352639675140381})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.800434112548828})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6452, 'crossentropy': 2.7414537109375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1745357513427734})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2046796083450317})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1640169620513916})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1723058223724365})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1793814897537231})
store['active_learning_steps'][43]['eval_training']['best_epoch']=2
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 56213], ['id', 2292], ['id', 5951], ['id', 52942], ['id', 51904]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.045241592132695, 1.9012324501102613, 2.5075775106638014, 2.815262816212333, 2.9297246486811446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.168217658996582})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.490671157836914})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7506952285766602})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.1658122539520264})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6621, 'crossentropy': 1.2487798828125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0836677551269531})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0176280736923218})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.978781521320343})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 44712], ['id', 54511], ['id', 26624], ['id', 55496], ['id', 36159]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7133671565640345, 1.2368175185383774, 1.6697255163092732, 1.9675379956303107, 2.1965465094819336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2795846462249756})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.571073055267334})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.851330041885376})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.975175142288208})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.1689419746398926})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.199522018432617})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3864479064941406})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6727, 'crossentropy': 2.2503890625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0842838287353516})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0230114459991455})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.066164255142212})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.04062819480896})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0182437896728516})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0824264287948608})
store['active_learning_steps'][45]['eval_training']['best_epoch']=3
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 37827], ['id', 50117], ['id', 10768], ['id', 52158], ['id', 51828]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0433260472618469, 1.8081467287396893, 2.3705311440236976, 2.691370121510834, 2.8626132714971835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3535592555999756})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.6920406818389893})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0154776573181152})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.2130720615386963})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4031968116760254})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 1.8059578125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1629064083099365})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1191201210021973})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.180438756942749})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1294708251953125})
store['active_learning_steps'][46]['eval_training']['best_epoch']=1
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 35887], ['id', 51809], ['id', 18803], ['id', 17714], ['id', 3800]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9727220136706876, 1.7138060844427274, 2.199548780147084, 2.506304955611835, 2.6778155048832755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.213367223739624})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.561112403869629})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8643131256103516})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.299740791320801})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5838613510131836})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6384, 'crossentropy': 1.6847294921875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1585769653320312})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0397154092788696})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.074009656906128})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0135529041290283})
store['active_learning_steps'][47]['eval_training']['best_epoch']=2
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 19737], ['id', 36337], ['id', 20897], ['id', 55588], ['id', 32575]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8667540598745664, 1.5147895360334847, 1.992578962093333, 2.317441836230902, 2.517423344968707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1855412721633911})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4980734586715698})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.8848965167999268})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0582380294799805})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6429, 'crossentropy': 1.26571376953125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1186766624450684})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0354682207107544})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0418570041656494})
store['active_learning_steps'][48]['eval_training']['best_epoch']=2
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 2962], ['id', 11273], ['id', 36109], ['id', 28357], ['id', 7843]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7929397878549851, 1.3219222082314857, 1.7363404161610054, 2.040832315559893, 2.2726199915578205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1653780937194824})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.501059889793396})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.8436024188995361})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.9576137065887451})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.164842367172241})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.341817855834961})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.265681266784668})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.455137252807617})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.5258407592773438})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.3937575817108154})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.435769557952881})
store['active_learning_steps'][49]['training']['best_epoch']=8
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6701, 'crossentropy': 2.6764619140625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1652833223342896})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1499614715576172})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2449791431427002})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1690657138824463})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.090556025505066})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0837204456329346})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0792243480682373})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1649072170257568})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1454002857208252})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1238181591033936})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 57323], ['id', 6391], ['id', 6626], ['id', 37542], ['id', 2404]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1280164007144071, 2.0073719806758774, 2.6140247829637997, 2.917548351479117, 3.0638713938057442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.360841989517212})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4693900346755981})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.8533927202224731})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.1051225662231445})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.163330554962158})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0926833152770996})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.3850178718566895})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.1620218753814697})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.6156115531921387})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.6961231231689453})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6541, 'crossentropy': 2.6524744140625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1410566568374634})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1515705585479736})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1889792680740356})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2966210842132568})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2217613458633423})
store['active_learning_steps'][50]['eval_training']['best_epoch']=2
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 39726], ['id', 42432], ['id', 24108], ['id', 50106], ['id', 4833]], 'labels': [-1, -1, 8, -1, 3], 'scores': [1.1744580470928858, 2.0648814040032684, 2.6282006790001367, 2.919752561699508, 3.048923670560784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.263471007347107})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.538423776626587})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.745819091796875})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.257133960723877})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.3826911449432373})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6662, 'crossentropy': 1.75833828125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1460089683532715})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0420160293579102})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0501980781555176})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0378873348236084})
store['active_learning_steps'][51]['eval_training']['best_epoch']=2
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 41516], ['id', 56479], ['id', 44235], ['id', 20894], ['id', 1361]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.873901563980819, 1.5942643318834522, 2.129360571824602, 2.4461239117335536, 2.6148995590427697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2875558137893677})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4839942455291748})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7132532596588135})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9121476411819458})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.170604705810547})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.1281728744506836})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3591339588165283})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3785641193389893})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6662, 'crossentropy': 2.22993984375}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2076398134231567})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1154224872589111})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1327190399169922})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0995908975601196})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1659796237945557})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0472279787063599})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.094466209411621})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 57919], ['id', 7925], ['id', 14835], ['id', 55196], ['id', 12254]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.9638457209584108, 1.7691363235661832, 2.342682717352363, 2.6419287422157103, 2.807488349404802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.405468225479126})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6887999773025513})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.9778995513916016})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.1463074684143066})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.179500102996826})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6053667068481445})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7986536026000977})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.6162047386169434})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6528, 'crossentropy': 2.523004296875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1645255088806152})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2163069248199463})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.185820460319519})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1956357955932617})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2293744087219238})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1975681781768799})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2589846849441528})
store['active_learning_steps'][53]['eval_training']['best_epoch']=4
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 12644], ['id', 41887], ['id', 58360], ['id', 5790], ['id', 55042]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0171387418639002, 1.9111554088514593, 2.5184061535845945, 2.8678400519660645, 3.060387305181199]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2583818435668945})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4251084327697754})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.8087544441223145})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.999821424484253})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.245129108428955})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3559799194335938})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.491915702819824})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5485973358154297})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6414, 'crossentropy': 2.529451171875}
