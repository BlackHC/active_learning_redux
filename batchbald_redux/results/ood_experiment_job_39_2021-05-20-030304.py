store = {}
store['timestamp']=1621476184
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=39']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=39
store['worker_id']=39
store['num_workers']=80
store['config']={'seed': 1275, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.3251402378082275})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.781033515930176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.3349599838256836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3077425956726074})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.466301918029785})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.389097213745117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.4688825607299805})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4547536373138428})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.301854133605957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3099570274353027})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.9542675018310547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.421673536300659})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6221, 'crossentropy': 3.5584859375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3462066650390625})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.308990240097046})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4298510551452637})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.323133945465088})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2988368272781372})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3472014665603638})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.410360336303711})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4322752952575684})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4064075946807861})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3464899063110352})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.384800672531128})
store['active_learning_steps'][0]['eval_training']['best_epoch']=11
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 42059], ['id', 8826], ['id', 27874], ['id', 12635], ['id', 6079]], 'labels': [-1, -1, -1, 2, 4], 'scores': [1.2646770350893748, 2.166227010294991, 2.774053596352134, 3.13134194919341, 3.3032285048113543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.8858370780944824})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3582184314727783})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.560960054397583})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.654871940612793})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6524, 'crossentropy': 1.9413572265625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2123361825942993})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1570038795471191})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.120513916015625})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 6889], ['id', 3362], ['id', 56585], ['id', 49229], ['id', 51418]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.9867525698710264, 1.735556418664086, 2.2472187724907284, 2.558987370743081, 2.753867149385149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.10379958152771})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.785682201385498})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7974817752838135})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.148930549621582})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6143851280212402})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.386228561401367})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.631, 'crossentropy': 2.9290921875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2422120571136475})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2866990566253662})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2993388175964355})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3123705387115479})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 4799], ['id', 39510], ['id', 9386], ['id', 18598], ['id', 12744]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0290431947531702, 1.908684149114746, 2.441213961740941, 2.737559134329974, 2.908563853646803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0960686206817627})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.031310796737671})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0402402877807617})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.176090955734253})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.799802541732788})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.271113395690918})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.486706256866455})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.811587333679199})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.3356924057006836})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.790444850921631})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.808960199356079})
store['active_learning_steps'][3]['training']['best_epoch']=8
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.637, 'crossentropy': 3.526461328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3226019144058228})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4304885864257812})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4477914571762085})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4017077684402466})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4295363426208496})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4526540040969849})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4569008350372314})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 54081], ['id', 23654], ['id', 22897], ['id', 14046], ['id', 40082]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.1992894499666775, 2.0841299813300074, 2.701119696768121, 3.020810536415662, 3.1422748560151543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1190621852874756})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5860037803649902})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0931286811828613})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1974868774414062})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.232119560241699})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.5923502445220947})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.004608392715454})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.7137656211853027})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6539, 'crossentropy': 3.21771953125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.308899164199829})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2740068435668945})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3647472858428955})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3096880912780762})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.308894157409668})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 52372], ['id', 49149], ['id', 10326], ['id', 52198], ['id', 22034]], 'labels': [-1, -1, 5, 3, 4], 'scores': [1.1817162027100012, 2.077654680410492, 2.5849845495206294, 2.85380179937527, 2.964380046038279]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7569506168365479})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.370222806930542})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.724527597427368})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5999574661254883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.882380485534668})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.0382754802703857})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.7152509689331055})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.679, 'crossentropy': 2.6814044921875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1998133659362793})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.209336519241333})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2952380180358887})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2619633674621582})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 4827], ['id', 28218], ['id', 51167], ['id', 36884], ['id', 27328]], 'labels': [-1, 2, 0, -1, -1], 'scores': [1.087661439826246, 1.871768044765418, 2.418536099036114, 2.7153562247112357, 2.8801291169521246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8161485195159912})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.3770089149475098})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.719881534576416})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9358277320861816})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.44101619720459})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.194035768508911})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6643, 'crossentropy': 2.6046998046875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2529141902923584})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.312218189239502})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.234494924545288})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2428085803985596})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3052188158035278})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 27431], ['id', 34906], ['id', 35230], ['id', 25349], ['id', 24896]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.161375466123805, 2.002143354433508, 2.5300909532771176, 2.847460643988671, 3.0085222487408823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.9694321155548096})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.6943745613098145})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8056693077087402})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.0895800590515137})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 4.060564994812012})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.054612159729004})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.3643064498901367})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6518, 'crossentropy': 3.018166796875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.250079870223999})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.461334466934204})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.396435260772705})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.485259771347046})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3677433729171753})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3376479148864746})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 43930], ['id', 10681], ['id', 32757], ['id', 8700], ['id', 18858]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0674409142721824, 1.849070546988378, 2.3868771665404287, 2.662879664466362, 2.776742987308787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8858168125152588})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.2615175247192383})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.6444969177246094})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.964332342147827})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2886269092559814})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.978646755218506})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6594, 'crossentropy': 2.650469921875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1681419610977173})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3483099937438965})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3074357509613037})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3515210151672363})
store['active_learning_steps'][8]['eval_training']['best_epoch']=1
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 4138], ['id', 52190], ['id', 20013], ['id', 32997], ['id', 41071]], 'labels': [-1, -1, -1, 4, 2], 'scores': [1.1253317076851053, 1.9045577309926491, 2.4469858232356207, 2.7014431492444952, 2.8316757179993095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8252931833267212})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5394744873046875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.244344711303711})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2308127880096436})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.2095534801483154})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2127041816711426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.32810115814209})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.629800796508789})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6413, 'crossentropy': 3.0714986328125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2916570901870728})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4195533990859985})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3989026546478271})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.321087121963501})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10225], ['id', 11232], ['id', 7516], ['id', 55713], ['id', 3066]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.0738980925389416, 1.8843951030270523, 2.504417564294844, 2.847306758720678, 2.984096864998061]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7472187280654907})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.2891409397125244})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.756807327270508})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.157325506210327})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.401371955871582})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.3762662410736084})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.3954076766967773})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6598, 'crossentropy': 2.8870603515625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.309962272644043})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.361587643623352})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3185369968414307})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3765230178833008})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4311683177947998})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3841018676757812})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 52012], ['id', 6143], ['id', 54167], ['id', 59366], ['id', 46064]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.0789636439491277, 1.8835449944816292, 2.4466230286108352, 2.84114119070217, 3.0737149480236665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.0381228923797607})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.4457297325134277})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.797138214111328})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8995633125305176})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3119726181030273})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.2013373374938965})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.806002616882324})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.1044321060180664})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.6048216819763184})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 4.262700080871582})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.7011356353759766})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6518, 'crossentropy': 3.0190998046875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.378025770187378})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.236525297164917})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4512717723846436})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.358795404434204})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4232141971588135})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3440768718719482})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3332209587097168})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3917455673217773})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3384326696395874})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3862577676773071})
store['active_learning_steps'][11]['eval_training']['best_epoch']=8
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 12561], ['id', 4475], ['id', 36852], ['id', 20656], ['id', 27381]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.1888135526938859, 2.0256557682248695, 2.582837855011372, 2.930720180910003, 3.0925703029788956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.8629748821258545})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4318180084228516})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.475094795227051})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3869524002075195})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.4391493797302246})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6463, 'crossentropy': 2.369056640625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3473742008209229})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.39290452003479})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3942606449127197})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4233615398406982})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 37050], ['id', 36280], ['id', 36751], ['id', 20982], ['id', 10181]], 'labels': [-1, -1, -1, 5, 0], 'scores': [0.928606006170456, 1.6855731367872866, 2.220451334863684, 2.584204690650379, 2.7777822268540353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.706571102142334})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.7579259872436523})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6552648544311523})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9851717948913574})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.19549298286438})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2126851081848145})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.954461097717285})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.7308223247528076})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 4.172055244445801})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6378, 'crossentropy': 3.358277734375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4513826370239258})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3479217290878296})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.489022970199585})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3200527429580688})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3596054315567017})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.432288408279419})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4694547653198242})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 14819], ['id', 3433], ['id', 23741], ['id', 54147], ['id', 51054]], 'labels': [-1, -1, 9, -1, 8], 'scores': [1.089604780406464, 1.9477786936998003, 2.5230403433692556, 2.809412617260403, 2.9072552097213906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.8551669120788574})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7137227058410645})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.819148063659668})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.309129238128662})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.610875129699707})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.508273124694824})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.724242925643921})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.542858839035034})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 4.294795036315918})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.716261863708496})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.778263092041016})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.65, 'crossentropy': 3.56460234375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2871787548065186})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4970769882202148})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4754116535186768})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5099703073501587})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 46565], ['id', 8104], ['id', 55314], ['id', 46375], ['id', 41663]], 'labels': [-1, -1, -1, 1, 9], 'scores': [1.0777654405606396, 1.9898375599923241, 2.619512595808897, 2.984901060853934, 3.133386270128313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9080485105514526})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.798433303833008})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.3387677669525146})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.3672714233398438})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.724334955215454})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.6327061653137207})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 4.165567874908447})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 4.355156898498535})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.6563589572906494})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6333, 'crossentropy': 3.750395703125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4244589805603027})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4320446252822876})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4126794338226318})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5022821426391602})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3950755596160889})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5483996868133545})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.442129135131836})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5061309337615967})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 27993], ['id', 54527], ['id', 32582], ['id', 33852], ['id', 41570]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.104545894850568, 1.9381382404626626, 2.4795639374453176, 2.797715309544105, 2.9772723412320783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.6349420547485352})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.7684125900268555})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.4826531410217285})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0801379680633545})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.7061238288879395})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.7563724517822266})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.037026405334473})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6319, 'crossentropy': 3.2288390625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3500308990478516})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2932302951812744})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2667484283447266})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.400710105895996})
store['active_learning_steps'][16]['eval_training']['best_epoch']=1
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 44985], ['id', 21383], ['id', 5355], ['id', 10710], ['id', 11514]], 'labels': [-1, -1, 4, -1, -1], 'scores': [1.019371308980454, 1.6976204681121785, 2.152771169195784, 2.388011737176801, 2.528612811080011]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.7419664859771729})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.4095990657806396})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.565392017364502})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8374180793762207})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0139894485473633})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.043506622314453})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6309, 'crossentropy': 2.5231802734375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3271279335021973})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3485562801361084})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.424668550491333})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3166260719299316})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3675713539123535})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 53673], ['id', 11041], ['id', 37647], ['id', 51388], ['id', 38567]], 'labels': [-1, -1, -1, 7, -1], 'scores': [1.006727525603735, 1.7613575918888515, 2.286151060513748, 2.669005474234371, 2.8407661530879187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.7311931848526})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.6130480766296387})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.826702833175659})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8321352005004883})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.332113265991211})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.2277536392211914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.962015151977539})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.367219924926758})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 3.169545703125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4339125156402588})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3753716945648193})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.296630620956421})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3742189407348633})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3655847311019897})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3505163192749023})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4352335929870605})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 49907], ['id', 37340], ['id', 15622], ['id', 16406], ['id', 933]], 'labels': [-1, -1, 0, 3, 4], 'scores': [1.15353521506385, 1.9669118046574612, 2.4732008247023174, 2.7575029595301483, 2.9177908381478463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7171868085861206})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.4880166053771973})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9200260639190674})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.072089672088623})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.26827335357666})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.430844306945801})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.300835609436035})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.594217300415039})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6416, 'crossentropy': 3.1299623046875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4067902565002441})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4131625890731812})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3929593563079834})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.457594871520996})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.474806547164917})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3862663507461548})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4446001052856445})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 23393], ['id', 4850], ['id', 51013], ['id', 37827], ['id', 11975]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.972802095673222, 1.7512044101786852, 2.2672993539853614, 2.567679550635229, 2.723840755806613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.763627290725708})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.5023622512817383})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.863062858581543})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.02683162689209})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.1080546379089355})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1411244869232178})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.5144448280334473})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.4849014282226562})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.743072032928467})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6478, 'crossentropy': 3.486241796875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4489550590515137})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3937807083129883})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.487673044204712})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3731164932250977})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4161183834075928})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4517242908477783})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3938641548156738})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.403007984161377})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 14084], ['id', 39952], ['id', 22583], ['id', 11374], ['id', 18057]], 'labels': [-1, -1, -1, 2, 1], 'scores': [1.0253269455451894, 1.7605815846571553, 2.2618424886209167, 2.525270440023288, 2.6806028065375047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5284204483032227})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1364710330963135})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4766082763671875})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.9460277557373047})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.718113422393799})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.2469592094421387})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.0934650897979736})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.0421056747436523})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6736, 'crossentropy': 2.7728568359375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2538954019546509})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2688570022583008})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.331416130065918})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2739803791046143})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2844204902648926})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3389639854431152})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.295647144317627})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52863], ['id', 31994], ['id', 15119], ['id', 57872], ['id', 47074]], 'labels': [-1, -1, 0, 8, 6], 'scores': [1.0038078364233225, 1.7877058719329773, 2.33405859680747, 2.638202560701237, 2.802528039894484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4640415906906128})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8999078273773193})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1908106803894043})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3014354705810547})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.7070841789245605})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6803479194641113})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.1302709579467773})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6742, 'crossentropy': 2.342749609375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.213620901107788})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.237858533859253})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1704165935516357})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2168147563934326})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.217826008796692})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2190101146697998})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 28347], ['id', 15624], ['id', 55419], ['id', 18135], ['id', 38233]], 'labels': [-1, -1, 5, -1, 7], 'scores': [0.9703678262866888, 1.742617301983521, 2.3212309935961084, 2.732143854014013, 2.92800601034678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.4481830596923828})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.009958267211914})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.6285226345062256})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.423494338989258})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.0835981369018555})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.162993907928467})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.173081398010254})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6716, 'crossentropy': 2.4421330078125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1773600578308105})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.206379771232605})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.234130620956421})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1681208610534668})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.22701096534729})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1797902584075928})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 50473], ['id', 2805], ['id', 50527], ['id', 13322], ['id', 15268]], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.9790447665186224, 1.740427356080179, 2.2264578797418175, 2.54786195337725, 2.7121002585506613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5386269092559814})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.8285973072052002})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2273569107055664})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4595375061035156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8940019607543945})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6902737617492676})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6673, 'crossentropy': 2.2625404296875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2960559129714966})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2618273496627808})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.256571888923645})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.293027400970459})
store['active_learning_steps'][24]['eval_training']['best_epoch']=1
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 21668], ['id', 48608], ['id', 53753], ['id', 31557], ['id', 23997]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.1150327415872479, 2.04354598440895, 2.679064417758385, 3.025365358166548, 3.1771501183535307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4129114151000977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.945837140083313})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.487210273742676})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.692878246307373})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.514291524887085})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6568, 'crossentropy': 1.9341818359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1740739345550537})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1116435527801514})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1051983833312988})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1059582233428955})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 217], ['id', 24081], ['id', 52413], ['id', 45734], ['id', 18164]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.043795124430459, 1.8207261975545959, 2.314708119994582, 2.58190649468154, 2.705649014959735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5111688375473022})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1297590732574463})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.162137031555176})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.357689380645752})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.6363043785095215})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.9924397468566895})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6835, 'crossentropy': 2.1347931640625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2271113395690918})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2356586456298828})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2251086235046387})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1803603172302246})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1527185440063477})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 18324], ['id', 53902], ['id', 5830], ['id', 27509], ['id', 45510]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.8804562785531094, 1.6279806874626495, 2.1379586022905324, 2.456568203575184, 2.6482066465805953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5559744834899902})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.9425147771835327})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.2083351612091064})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.401854991912842})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.5411555767059326})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6818, 'crossentropy': 1.9233255859375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2578332424163818})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1554235219955444})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1381208896636963})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1862876415252686})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 20640], ['id', 50127], ['id', 7406], ['id', 44388], ['id', 14591]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.0353079429590706, 1.8234207193799432, 2.349379034616974, 2.6626897576510418, 2.823949790294485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4853719472885132})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.9972045421600342})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.4774010181427})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.66804838180542})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9178354740142822})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.079765796661377})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.67, 'crossentropy': 2.4141748046875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1351728439331055})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2566039562225342})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2834864854812622})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3029730319976807})
store['active_learning_steps'][28]['eval_training']['best_epoch']=1
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 25868], ['id', 4798], ['id', 13384], ['id', 49895], ['id', 20348]], 'labels': [-1, -1, 0, -1, 0], 'scores': [1.034287452021456, 1.8614165479137745, 2.3824709918589946, 2.641932586532012, 2.7277213835469185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4479196071624756})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9084265232086182})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.601452350616455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.875197410583496})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.665234088897705})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.6848831176757812})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.43172025680542})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.621779441833496})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.4523983001708984})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6707, 'crossentropy': 2.70919453125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3123058080673218})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.308083176612854})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.377445936203003})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2966866493225098})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3530616760253906})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3671331405639648})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.273586630821228})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2925984859466553})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 48691], ['id', 46430], ['id', 770], ['id', 59754], ['id', 12992]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.2366611571777075, 2.1739384125848806, 2.790961387546208, 3.0821074990965407, 3.2166431125277626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4814032316207886})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.878586769104004})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.1928601264953613})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.227309226989746})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.408751964569092})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.8386409282684326})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.908384323120117})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6936, 'crossentropy': 2.1796681640625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2148433923721313})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2931329011917114})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2425847053527832})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2153420448303223})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1618390083312988})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1872735023498535})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 55545], ['id', 35230], ['id', 39245], ['id', 45674], ['id', 12747]], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.9298261491942206, 1.6635094530729841, 2.1799950732429876, 2.4909064015319764, 2.6664756370143197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4263969659805298})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.694350242614746})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.063052177429199})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.350979804992676})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.41752028465271})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.4084386825561523})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6603164672851562})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 3.1764087677001953})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.0654821395874023})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 3.04722261428833})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 3.035093307495117})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6896, 'crossentropy': 2.97821796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2745134830474854})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2708985805511475})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2777667045593262})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2754775285720825})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2817984819412231})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3062893152236938})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3068456649780273})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2660497426986694})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.31584632396698})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3196160793304443})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 14084], ['id', 33550], ['id', 52881], ['id', 29339], ['id', 49067]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2260049650259344, 2.082131292404544, 2.596864162865028, 2.8717219733168857, 3.005378148551152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.372867465019226})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7254447937011719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.0709023475646973})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6013383865356445})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.386065721511841})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.6346917152404785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.9960498809814453})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.8364319801330566})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6814, 'crossentropy': 2.3486306640625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1942355632781982})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1993451118469238})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2424089908599854})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2288010120391846})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.235152006149292})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.228339672088623})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2120977640151978})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 24131], ['id', 42535], ['id', 40034], ['id', 14055], ['id', 52407]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.1375489374875358, 1.9654241467358733, 2.568452064618037, 2.9245381879070553, 3.101163275582333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2961974143981934})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.715877652168274})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.233872890472412})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.072099447250366})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.528988838195801})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.674933910369873})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.522332191467285})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6995, 'crossentropy': 2.101306640625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1848833560943604})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2129610776901245})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.180086374282837})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1833375692367554})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1892331838607788})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.157700538635254})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 47017], ['id', 40749], ['id', 52145], ['id', 36879], ['id', 38440]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0019114743155808, 1.8575381863623504, 2.3579109635604727, 2.6587868009641733, 2.8202940207157186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3268851041793823})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.701865553855896})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7753872871398926})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.1333656311035156})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.263998031616211})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3894968032836914})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.774573802947998})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.6768603324890137})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7078, 'crossentropy': 2.237469921875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1686954498291016})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1620055437088013})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1974494457244873})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1610455513000488})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1543807983398438})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1461036205291748})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1371046304702759})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 41468], ['id', 8338], ['id', 44230], ['id', 4962], ['id', 39486]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1636906015798054, 1.997137404621852, 2.54600506636977, 2.768376743459636, 2.8547766266759176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.420375108718872})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.8207261562347412})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.0706329345703125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.2184014320373535})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.3991260528564453})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.557222843170166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.6911678314208984})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.842411518096924})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.7006168365478516})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7034, 'crossentropy': 2.53648515625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1389269828796387})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1588339805603027})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.206237554550171})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2141484022140503})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2353684902191162})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2477011680603027})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2126864194869995})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3016855716705322})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 45293], ['id', 42624], ['id', 399], ['id', 55947], ['id', 39591]], 'labels': [-1, -1, -1, 2, 5], 'scores': [0.9698700682404663, 1.7613241261471373, 2.3596852116032108, 2.6760313051012394, 2.8236776557164687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3442537784576416})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6537702083587646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.0569591522216797})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.47282075881958})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.472118854522705})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.804363250732422})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.785768508911133})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 3.0044074058532715})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6935, 'crossentropy': 2.368450390625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1219916343688965})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2370233535766602})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2381813526153564})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2244482040405273})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2919690608978271})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1513445377349854})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1774094104766846})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 13496], ['id', 25452], ['id', 6047], ['id', 4039], ['id', 47745]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0306708936970594, 1.8918687308005655, 2.508151028911755, 2.8168255593191853, 2.9536707306578656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2815771102905273})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6975172758102417})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.134202003479004})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.445542812347412})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.4934582710266113})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 3.0487024784088135})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.855001926422119})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.5204625129699707})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.9221978187561035})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.2531023025512695})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.697, 'crossentropy': 2.8303029296875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.200995683670044})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.244661808013916})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3529350757598877})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.283573865890503})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2531156539916992})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4095516204833984})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4955081939697266})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 8484], ['id', 2773], ['id', 59597], ['id', 27231], ['id', 42267]], 'labels': [-1, -1, 8, -1, 5], 'scores': [1.1010498792288357, 2.0027789255695803, 2.6008694279816345, 2.902758573511691, 3.0502887286229567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.414867639541626})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6131848096847534})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.792846918106079})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.145331859588623})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5080037117004395})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.5162434577941895})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7046, 'crossentropy': 1.756547265625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1584504842758179})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1348984241485596})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.13935387134552})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.041391134262085})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0935380458831787})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 7464], ['id', 8411], ['id', 334], ['id', 5541], ['id', 20588]], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.9098095502426555, 1.6384988538091885, 2.1392759402600903, 2.4796567211797114, 2.679904788848244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.360002040863037})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6319572925567627})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9519248008728027})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.1616854667663574})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.2722394466400146})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.753235340118408})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7033, 'crossentropy': 1.9009044921875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.221010446548462})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.152857780456543})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1500808000564575})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1410021781921387})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1878503561019897})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 46036], ['id', 9386], ['id', 32070], ['id', 28566], ['id', 45101]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9138545280690842, 1.6008203125376212, 2.1024496600694915, 2.416550908288218, 2.614982976019549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3923096656799316})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6691107749938965})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9307515621185303})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.1609158515930176})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.408392906188965})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.301539421081543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 3.0344295501708984})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.8327317237854004})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7034, 'crossentropy': 2.3991443359375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.229219675064087})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2945290803909302})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2644693851470947})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.157122015953064})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2768259048461914})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1999917030334473})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2205917835235596})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 51764], ['id', 8566], ['id', 24422], ['id', 50317], ['id', 37477]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0866217655017159, 1.9354627244874063, 2.481653125196855, 2.713060316757778, 2.816788494388291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.426633596420288})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7794429063796997})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0021538734436035})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.234609603881836})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.4200594425201416})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.618542194366455})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.3513805866241455})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.353084087371826})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.5124857425689697})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.8976778984069824})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.9205331802368164})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7118, 'crossentropy': 2.3739501953125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2069820165634155})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.118795394897461})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1437971591949463})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2546217441558838})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2025504112243652})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2634738683700562})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2237575054168701})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 54535], ['id', 49067], ['id', 42866], ['id', 35005], ['id', 44525]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0242211309214881, 1.8373739317285853, 2.406994824806328, 2.6661640349498024, 2.7421305313406545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.348433494567871})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.5515260696411133})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.864691972732544})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0689139366149902})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.510242462158203})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.6051998138427734})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.7227816581726074})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6938, 'crossentropy': 2.010481640625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.181412696838379})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1872010231018066})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1660969257354736})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1468322277069092})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1075782775878906})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1579358577728271})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 19060], ['id', 54443], ['id', 4232], ['id', 5545], ['id', 56309]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0559987206118298, 1.8996031763290748, 2.4114073888014866, 2.749503371756391, 2.8924311560849345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4216296672821045})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6750187873840332})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0733115673065186})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.401431083679199})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3535523414611816})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.7079997062683105})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.741295576095581})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.8638808727264404})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.9327573776245117})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.9418840408325195})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.9194250106811523})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 3.399592876434326})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 3.410679817199707})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 3.308267593383789})
store['active_learning_steps'][43]['training']['best_epoch']=11
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7029, 'crossentropy': 2.8600802734375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.266822338104248})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2458420991897583})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.237050175666809})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2317934036254883})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.292301893234253})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2239906787872314})
store['active_learning_steps'][43]['eval_training']['best_epoch']=3
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 3667], ['id', 17063], ['id', 14020], ['id', 9703], ['id', 19114]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.1426428244583178, 2.067190024366133, 2.553815540302929, 2.8057718795348476, 2.9307257447551276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2829492092132568})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.720050573348999})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.057863712310791})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.351902961730957})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.641493082046509})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6937, 'crossentropy': 1.716025}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1425801515579224})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1713790893554688})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1239062547683716})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1132919788360596})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 11041], ['id', 45102], ['id', 10100], ['id', 50016], ['id', 14205]], 'labels': [-1, -1, 5, -1, 7], 'scores': [0.9169296023533531, 1.5798957829482432, 2.015383649530759, 2.310850255229024, 2.510889530026689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2718589305877686})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7096436023712158})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9871320724487305})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.1148879528045654})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.4691977500915527})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.6822662353515625})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.7300920486450195})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.759777545928955})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.7207813262939453})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.792372703552246})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.8982160091400146})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 3.0191879272460938})
store['active_learning_steps'][45]['training']['best_epoch']=9
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.7038, 'crossentropy': 2.6806505859375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2238072156906128})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.239030122756958})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2770075798034668})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2369695901870728})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.261546015739441})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3433382511138916})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.339897871017456})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3357725143432617})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2933613061904907})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3102885484695435})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3550896644592285})
store['active_learning_steps'][45]['eval_training']['best_epoch']=9
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 54709], ['id', 7023], ['id', 43294], ['id', 27958], ['id', 49502]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.102533769997506, 1.9315776891596756, 2.6018254678678567, 2.8825874522351587, 3.042180921551208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.292338490486145})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7375178337097168})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0670018196105957})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9655957221984863})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.279480457305908})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.2070889472961426})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.3519628047943115})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.577085494995117})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4006171226501465})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.7071, 'crossentropy': 2.2431216796875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2290441989898682})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2596864700317383})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2498407363891602})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2753009796142578})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2179160118103027})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2276917695999146})
store['active_learning_steps'][46]['eval_training']['best_epoch']=3
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 56817], ['id', 48752], ['id', 28572], ['id', 46730], ['id', 10249]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0180088338533242, 1.8191344755700225, 2.36425316937762, 2.654582612938434, 2.776017923054485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2862467765808105})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.526810646057129})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9638744592666626})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.0859336853027344})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.3672330379486084})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.4052605628967285})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.5817980766296387})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.849146842956543})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.7601325511932373})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.793848991394043})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.7182583808898926})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.7522435188293457})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.7084, 'crossentropy': 2.78893359375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2217916250228882})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2281626462936401})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3444464206695557})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3466925621032715})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2911372184753418})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.268454670906067})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3410720825195312})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3548825979232788})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2809429168701172})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2896277904510498})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2984100580215454})
store['active_learning_steps'][47]['eval_training']['best_epoch']=9
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 59415], ['id', 13520], ['id', 56754], ['id', 48562], ['id', 24457]], 'labels': [-1, -1, 8, 4, -1], 'scores': [1.1199535312632256, 1.9759507551548412, 2.546047199281765, 2.8723214805170514, 3.003840353275234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2694846391677856})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4644277095794678})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.8533843755722046})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.020629405975342})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.0659852027893066})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.206820487976074})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.7041, 'crossentropy': 1.8667232421875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1571333408355713})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.133394718170166})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.073216438293457})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1019071340560913})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.094405174255371})
store['active_learning_steps'][48]['eval_training']['best_epoch']=2
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 36866], ['id', 12388], ['id', 59218], ['id', 24422], ['id', 47918]], 'labels': [-1, 3, -1, -1, 4], 'scores': [0.8198795703039474, 1.5430435249944585, 2.110197487490307, 2.4056090037393387, 2.5520171751369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3970859050750732})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.473775863647461})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.732560157775879})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.117154121398926})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.1887269020080566})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.1478428840637207})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.563946485519409})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.646519184112549})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.62640118598938})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.7027, 'crossentropy': 2.2537291015625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1296181678771973})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2040743827819824})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.199845552444458})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1211600303649902})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1893361806869507})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2295318841934204})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2092278003692627})
store['active_learning_steps'][49]['eval_training']['best_epoch']=4
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 31804], ['id', 29359], ['id', 10303], ['id', 26270], ['id', 41556]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0509541751563896, 1.9119286495318804, 2.498945279032357, 2.8240634380328578, 2.946932999816859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2404439449310303})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3963125944137573})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8119736909866333})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.1555421352386475})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.205986976623535})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.42606782913208})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.270535945892334})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.4654135704040527})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.7098, 'crossentropy': 2.128884765625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2322877645492554})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1644293069839478})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1504828929901123})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1749022006988525})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1730268001556396})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2141706943511963})
store['active_learning_steps'][50]['eval_training']['best_epoch']=3
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 42714], ['id', 50117], ['id', 13326], ['id', 13251], ['id', 55503]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.9261846576435244, 1.6916561752747015, 2.221734249572313, 2.527460913970361, 2.7105120382215278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.35308837890625})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4201605319976807})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7960675954818726})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2273056507110596})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.213838815689087})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.251053810119629})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.3367838859558105})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.551457405090332})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.7028372287750244})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.8075029850006104})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.962191581726074})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.7118, 'crossentropy': 2.51254296875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.109417200088501})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1304148435592651})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2358088493347168})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1576416492462158})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1461716890335083})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1163160800933838})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.121532917022705})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1401259899139404})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0949835777282715})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1053216457366943})
store['active_learning_steps'][51]['eval_training']['best_epoch']=9
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 3712], ['id', 48752], ['id', 42475], ['id', 8581], ['id', 54960]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.0620668973927034, 1.9425788261899326, 2.5728519394072586, 2.8863975949763523, 3.0508528765394294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.241082787513733})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4467648267745972})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7152023315429688})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8527661561965942})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.9805819988250732})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.122894287109375})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.492612600326538})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.7047, 'crossentropy': 1.95018203125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1420097351074219})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1665241718292236})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1655855178833008})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0676130056381226})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.074630618095398})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1093147993087769})
store['active_learning_steps'][52]['eval_training']['best_epoch']=5
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 56136], ['id', 5683], ['id', 17576], ['id', 15031], ['id', 44378]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9828656321696931, 1.7630489933950177, 2.3106400403021734, 2.5949131301862485, 2.7285923120266204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2759277820587158})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4532032012939453})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7242920398712158})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8009228706359863})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.0687882900238037})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.34698486328125})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.2386436462402344})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.484375})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.7086, 'crossentropy': 2.2243755859375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.246948003768921})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1702628135681152})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.143532633781433})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2036948204040527})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.177492380142212})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1758081912994385})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1546940803527832})
store['active_learning_steps'][53]['eval_training']['best_epoch']=5
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 32619], ['id', 40292], ['id', 31833], ['id', 42514], ['id', 39418]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0806572526119664, 1.9121373594724753, 2.4983727783427536, 2.7941239387360444, 2.89703713485239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2577884197235107})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4346611499786377})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.958906888961792})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8237700462341309})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.9118053913116455})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.391535997390747})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.342611312866211})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.343018054962158})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.247603416442871})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2997283935546875})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.587040901184082})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.922330856323242})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.812964916229248})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.97869610786438})
store['active_learning_steps'][54]['training']['best_epoch']=11
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.7058, 'crossentropy': 2.7488546875}
