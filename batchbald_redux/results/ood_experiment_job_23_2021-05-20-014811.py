store = {}
store['timestamp']=1621471691
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=23']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=23
store['worker_id']=23
store['num_workers']=80
store['config']={'seed': 1258, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.2973294258117676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.0331573486328125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.4356398582458496})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.5713491439819336})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5896, 'crossentropy': 2.4716611328125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3819935321807861})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.3668193817138672})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.33302903175354})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 12972], ['id', 42405], ['id', 12121], ['id', 40570], ['id', 29646]], 'labels': [-1, -1, -1, 8, 2], 'scores': [1.147316915594757, 1.9015792928355362, 2.427663094687455, 2.7028118277723, 2.865636574328569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.386775016784668})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.1829752922058105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.914909839630127})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.8184702396392822})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.872097969055176})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.9594578742980957})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6017, 'crossentropy': 3.955104296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.5531214475631714})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.5494592189788818})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.533548355102539})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.5512527227401733})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5961322784423828})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 49115], ['id', 34106], ['id', 7400], ['id', 6575], ['id', 53789]], 'labels': [-1, -1, 6, 3, 6], 'scores': [1.0870541590495872, 1.9413901880954563, 2.443515022163141, 2.733571847352331, 2.8639061384873212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0911426544189453})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9731674194335938})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.27943754196167})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.2632572650909424})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.7095799446105957})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.52907133102417})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6211, 'crossentropy': 3.3313984375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3432579040527344})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4776920080184937})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.387047529220581})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4713025093078613})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 18170], ['id', 57308], ['id', 49160], ['id', 52396], ['id', 10262]], 'labels': [-1, -1, -1, 6, 0], 'scores': [1.1974843841818745, 2.064519348619092, 2.595036177851089, 2.86483420829909, 2.944838020785027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.022308826446533})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.6129562854766846})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.065078020095825})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.913508176803589})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2111618518829346})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6061, 'crossentropy': 2.956287109375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3339197635650635})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4570021629333496})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.455146312713623})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3936052322387695})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 15914], ['id', 13242], ['id', 57475], ['id', 50946], ['id', 3446]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1174113892242166, 1.9855411093552497, 2.6006243749637, 2.9105580171483734, 3.0440792663592777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.184231758117676})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.7788469791412354})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.049891948699951})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.3943536281585693})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.8909640312194824})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5976, 'crossentropy': 3.0877853515625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4119949340820312})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3670294284820557})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3567852973937988})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5055174827575684})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 56770], ['id', 49657], ['id', 18416], ['id', 19923], ['id', 42946]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.1115254839017494, 1.9021473275687923, 2.4154096318869005, 2.6550355912248635, 2.775853590058313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.029470682144165})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.6819305419921875})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.908977508544922})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.305093288421631})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.2921950817108154})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.660451889038086})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6025, 'crossentropy': 3.2109384765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.369506597518921})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2665334939956665})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3914365768432617})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.463848352432251})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2623485326766968})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 14804], ['id', 39730], ['id', 25517], ['id', 22053], ['id', 6164]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1368093324914859, 1.9572405773275112, 2.5352966789155946, 2.8403575934324836, 2.960859186461831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.770503282546997})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.7255735397338867})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.8505711555480957})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.281078577041626})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6201, 'crossentropy': 1.9227921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1944751739501953})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1405487060546875})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1426301002502441})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 30529], ['id', 21246], ['id', 13447], ['id', 3406], ['id', 19463]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.0170935909736083, 1.7157322881352997, 2.2193217109601058, 2.558875397748399, 2.7395633069057883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9344815015792847})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4337806701660156})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.165705680847168})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.722921371459961})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2342302799224854})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.251962661743164})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.323410987854004})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6181, 'crossentropy': 3.0277017578125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.385216236114502})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.235365867614746})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2545952796936035})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3165972232818604})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3229594230651855})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2434251308441162})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 28104], ['id', 32538], ['id', 24598], ['id', 53298], ['id', 1869]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.0953852496826761, 1.9209316353753252, 2.5289012604658545, 2.8408749950395906, 3.031434724394429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.8627794981002808})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6298956871032715})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0090901851654053})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3945348262786865})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 1.9193576171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2482914924621582})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1800589561462402})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.154052734375})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 18428], ['id', 25291], ['id', 27874], ['id', 28145], ['id', 40959]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.0887461345261267, 1.8389704550192643, 2.349643872576028, 2.6576244449433135, 2.8342549108052086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.0082192420959473})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.8552894592285156})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.9646310806274414})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4678590297698975})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.314452648162842})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 4.117197513580322})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8031365871429443})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5777, 'crossentropy': 3.6206203125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.4143595695495605})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3848992586135864})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4004099369049072})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4393160343170166})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5230321884155273})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10383], ['id', 48420], ['id', 38122], ['id', 4174], ['id', 28561]], 'labels': [-1, -1, -1, 7, 2], 'scores': [1.150534769078389, 2.06028520318803, 2.627173028938766, 2.931486453800354, 3.068654716554107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.000375270843506})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.489102840423584})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9194297790527344})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.976506233215332})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4894580841064453})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.500793218612671})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5921, 'crossentropy': 2.967683984375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.387589454650879})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.323584794998169})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3994332551956177})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.412308692932129})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3332533836364746})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 9749], ['id', 32208], ['id', 19386], ['id', 31644], ['id', 39668]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.196772002727403, 2.0642522811646815, 2.6796813725667317, 3.0552627232441925, 3.1999152061789182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.0646162033081055})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.7972006797790527})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2855072021484375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.5776820182800293})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3292529582977295})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.4583568572998047})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0397839546203613})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.6864981651306152})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3450002670288086})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.221258163452148})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 5.028943061828613})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.672305107116699})
store['active_learning_steps'][11]['training']['best_epoch']=9
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6177, 'crossentropy': 3.874245703125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3122937679290771})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4902336597442627})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5199589729309082})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4900050163269043})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 17582], ['id', 43301], ['id', 49889], ['id', 11364], ['id', 41160]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.100347302784046, 2.0187229503157504, 2.655352751421745, 2.9357989893675835, 3.015972497756433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.0435593128204346})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.9790902137756348})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0941474437713623})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.412249803543091})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.7889280319213867})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.8442492485046387})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.811577796936035})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6179, 'crossentropy': 3.49137890625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3565407991409302})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3690375089645386})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4132270812988281})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3727445602416992})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4065194129943848})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 4164], ['id', 39750], ['id', 20631], ['id', 59720], ['id', 43275]], 'labels': [-1, 0, -1, -1, 0], 'scores': [1.2031617123436318, 2.103575458821997, 2.69650484271225, 3.0018041227519534, 3.1488250340155517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.026880979537964})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.5426979064941406})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.093207597732544})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.4226346015930176})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.941049575805664})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.9877736568450928})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.5913515090942383})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.608048439025879})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5968, 'crossentropy': 3.3872046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.398289680480957})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3337781429290771})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3548288345336914})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3708550930023193})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.370800256729126})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3762133121490479})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 13447], ['id', 55629], ['id', 50418], ['id', 20681], ['id', 39707]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.09520798158816, 2.040198159914518, 2.6798617107305542, 2.9960584900128637, 3.1020365528409215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.0222601890563965})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.58870005607605})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8375391960144043})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8300938606262207})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.0191309452056885})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0754055976867676})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.314708948135376})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.8564014434814453})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6224, 'crossentropy': 3.357132421875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4351387023925781})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3620285987854004})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4785147905349731})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3691766262054443})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.426784873008728})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3871889114379883})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.430647850036621})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20280], ['id', 6784], ['id', 32641], ['id', 46996], ['id', 14428]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2019224369218626, 2.131606378265606, 2.8019665219021768, 3.15220947470615, 3.271063737276716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.9685065746307373})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.991812229156494})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.083026885986328})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.5350818634033203})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5915, 'crossentropy': 2.0079763671875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2897851467132568})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2180333137512207})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2264995574951172})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 54725], ['id', 21147], ['id', 6063], ['id', 57812], ['id', 24145]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9062505300123753, 1.530075353751604, 1.9922229832277472, 2.302594287972095, 2.498922649362278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.8454945087432861})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.342454433441162})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7120699882507324})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.038886547088623})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.9511313438415527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2891688346862793})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6046, 'crossentropy': 3.2229986328125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4012600183486938})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2931820154190063})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4082729816436768})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4086592197418213})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.508493423461914})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 4599], ['id', 38182], ['id', 1876], ['id', 47923], ['id', 24410]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.135447034902723, 1.9785964435012886, 2.487697852848793, 2.7733119305103298, 2.9029625785438364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4874460697174072})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.206815004348755})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7575528621673584})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9083340167999268})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6151, 'crossentropy': 1.68729921875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1523674726486206})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1619231700897217})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0802943706512451})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 14192], ['id', 40350], ['id', 9306], ['id', 14825], ['id', 46817]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0593544113777356, 1.816175065582586, 2.3362390302499962, 2.669804692272919, 2.882922301915139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.6570806503295898})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.294522285461426})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.091909885406494})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.133805513381958})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.6624436378479004})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6216, 'crossentropy': 2.4721263671875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3063499927520752})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3019802570343018})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2734240293502808})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.295715093612671})
store['active_learning_steps'][18]['eval_training']['best_epoch']=1
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 53556], ['id', 54608], ['id', 17089], ['id', 29900], ['id', 36462]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9874783308143051, 1.7865626716923209, 2.3375221935595665, 2.6275611376786863, 2.745186609571995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.7345415353775024})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4050540924072266})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.6348323822021484})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.07515287399292})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7956690788269043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.350395679473877})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6033, 'crossentropy': 2.915590625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3198819160461426})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3273155689239502})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.370070219039917})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2913818359375})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2709641456604004})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 31889], ['id', 28930], ['id', 27143], ['id', 19961], ['id', 1948]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0422072577034065, 1.8769007728351577, 2.468402435286041, 2.806584291911138, 2.950314578047079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.7513325214385986})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.551072120666504})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.551126718521118})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.6120734214782715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1206371784210205})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2608046531677246})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6155, 'crossentropy': 2.861101171875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.452746868133545})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3937979936599731})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3393309116363525})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3061065673828125})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4003145694732666})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 35216], ['id', 28595], ['id', 12800], ['id', 45840], ['id', 49629]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1448064632622432, 2.0388937254803325, 2.629710599092003, 2.9604325959090936, 3.116259041150232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.876268982887268})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4181790351867676})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6322875022888184})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8571157455444336})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8419077396392822})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0713951587677})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.821244239807129})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1461195945739746})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6312, 'crossentropy': 3.1993615234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.444157600402832})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4248579740524292})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4220259189605713})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4821019172668457})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3622710704803467})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3745887279510498})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3415532112121582})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 42595], ['id', 31580], ['id', 6257], ['id', 55037], ['id', 7924]], 'labels': [-1, -1, -1, 5, 1], 'scores': [1.2244923379750727, 2.1009523032388655, 2.7388700171379856, 3.0070762523258967, 3.1515676388187934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.660212755203247})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.152759075164795})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7751195430755615})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.069793462753296})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7690722942352295})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.600886344909668})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.142819404602051})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.151397705078125})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 3.1675369140625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2821714878082275})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3374898433685303})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3892943859100342})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4367451667785645})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4307971000671387})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3848199844360352})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5474], ['id', 40203], ['id', 31002], ['id', 56937], ['id', 31086]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.0199422385773897, 1.8328823645650645, 2.4009249593946644, 2.746201716657584, 2.9047308239970038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.649285078048706})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.2021005153656006})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.444944381713867})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.600965976715088})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1512503623962402})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.4807701110839844})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.621, 'crossentropy': 2.6916287109375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3051986694335938})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2498828172683716})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2089920043945312})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2458163499832153})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2453888654708862})
store['active_learning_steps'][23]['eval_training']['best_epoch']=2
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 14842], ['id', 22679], ['id', 53835], ['id', 10438], ['id', 28620]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1455512386362257, 2.0815217635017014, 2.6907919359842456, 2.9877069946194084, 3.1202742125627143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.7464535236358643})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4667298793792725})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.1841235160827637})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.0269055366516113})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.649524211883545})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.200338840484619})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.912229061126709})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.606, 'crossentropy': 3.202713671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3540089130401611})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.5705804824829102})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3975365161895752})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3708827495574951})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3616801500320435})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3123300075531006})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 33162], ['id', 44397], ['id', 20348], ['id', 38023], ['id', 23351]], 'labels': [-1, -1, 0, -1, 5], 'scores': [1.004574667050278, 1.8265313697630483, 2.394341243929687, 2.769008472017706, 2.938103008569069]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.641582727432251})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.4999589920043945})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.664984941482544})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0425736904144287})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.7523417472839355})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2260937690734863})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.151231050491333})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3302063941955566})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6039, 'crossentropy': 3.303176953125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3174693584442139})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3640501499176025})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.4229586124420166})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.263152837753296})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.347041130065918})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3530685901641846})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3472189903259277})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 6106], ['id', 28930], ['id', 29339], ['id', 34701], ['id', 35268]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.074048357777937, 1.9408623777148564, 2.5117735277275033, 2.861704711903162, 3.0391216470224993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.800682544708252})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.2658002376556396})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5324344635009766})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6161482334136963})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.66705322265625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.042141914367676})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.61, 'crossentropy': 2.803858203125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.369882345199585})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3865251541137695})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3018763065338135})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2645561695098877})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2738181352615356})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 32504], ['id', 53617], ['id', 12934], ['id', 53022], ['id', 45853]], 'labels': [-1, 8, -1, -1, -1], 'scores': [1.1004845400708598, 1.9192896511395157, 2.554104634581158, 2.9244530305747816, 3.076853336867801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.617978572845459})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.225254535675049})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.429609775543213})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0242972373962402})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4366259574890137})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.047451972961426})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 2.84753359375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4187954664230347})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4212970733642578})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4580347537994385})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.355054497718811})
store['active_learning_steps'][27]['eval_training']['best_epoch']=1
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 31947], ['id', 15104], ['id', 26095], ['id', 15296], ['id', 8628]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.1379076236491417, 1.9752352907486252, 2.511216285316369, 2.749093107550191, 2.816591176522916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5004348754882812})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.9781460762023926})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1237411499023438})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6163620948791504})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.722200870513916})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6246, 'crossentropy': 2.1955693359375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2321765422821045})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2057461738586426})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1994571685791016})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2048158645629883})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 54757], ['id', 35692], ['id', 48284], ['id', 11554], ['id', 15251]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.0514665511711274, 1.7881572746736754, 2.3441996703866215, 2.66923946818532, 2.8501184170401075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.5640664100646973})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1785483360290527})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.4267826080322266})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5182690620422363})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.686802387237549})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.7596545219421387})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0272257328033447})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3839263916015625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3254473209381104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0731630325317383})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.3580145835876465})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.311838150024414})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6485, 'crossentropy': 2.5583734375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1729488372802734})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1976776123046875})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.136980652809143})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1484744548797607})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1313977241516113})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.065542221069336})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20476], ['id', 8082], ['id', 3652], ['id', 15966], ['id', 32818]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.1776824889768087, 2.1545105826235833, 2.811619903344257, 3.0879160668349694, 3.184971906403355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.6618194580078125})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.5206544399261475})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6231932640075684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.0364794731140137})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.028372049331665})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.322270154953003})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6154, 'crossentropy': 2.616066796875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3441370725631714})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3705575466156006})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.329297661781311})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.191680669784546})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2107714414596558})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 22280], ['id', 59355], ['id', 27514], ['id', 9740], ['id', 38991]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0040725192217925, 1.8269864013673933, 2.4022150650313012, 2.7212181557681507, 2.851200524386451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.448838710784912})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.179159641265869})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.469916343688965})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.5523550510406494})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.2046899795532227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.484530448913574})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.075070381164551})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.219836473464966})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6186, 'crossentropy': 3.37917734375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.5110243558883667})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4805047512054443})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4386494159698486})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3775570392608643})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4509321451187134})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4173933267593384})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5331616401672363})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 36946], ['id', 722], ['id', 35182], ['id', 7867], ['id', 8920]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.0318686517039497, 1.8075624125951326, 2.390221742118089, 2.792711045715718, 3.010684695701788]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.7539477348327637})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.3532824516296387})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.777529716491699})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9425880908966064})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3245601654052734})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.044823169708252})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6074, 'crossentropy': 2.9154197265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.453371286392212})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4480905532836914})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3493863344192505})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.369847297668457})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3795572519302368})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 28182], ['id', 48056], ['id', 1336], ['id', 35850], ['id', 32492]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.041373509153424, 1.806678039152127, 2.3881374238007975, 2.6730031490902535, 2.8202391890106107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.824354887008667})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0151946544647217})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.263662338256836})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.3957293033599854})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.8982038497924805})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9510910511016846})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6137, 'crossentropy': 2.49993203125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.333524227142334})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2591800689697266})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2582844495773315})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2181003093719482})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3642234802246094})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 25350], ['id', 7490], ['id', 51142], ['id', 30393], ['id', 17506]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.977810837643075, 1.7722305863872412, 2.342174033776494, 2.650343807966281, 2.837274758416587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.5340608358383179})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.020202875137329})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3767342567443848})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7341489791870117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.606342315673828})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7227821350097656})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7271111011505127})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.114180088043213})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.273237943649292})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8513994216918945})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6376, 'crossentropy': 2.9342169921875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3622511625289917})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.368159532546997})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2081918716430664})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3180241584777832})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3163082599639893})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.293842077255249})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.407639741897583})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3526637554168701})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2895638942718506})
store['active_learning_steps'][34]['eval_training']['best_epoch']=9
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 28838], ['id', 34848], ['id', 37626], ['id', 722], ['id', 45124]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.1928700716847782, 2.140083041568243, 2.766065364796807, 3.109897986869763, 3.3180521937407983]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.5186504125595093})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.3809704780578613})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7946739196777344})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1342034339904785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9530129432678223})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6044, 'crossentropy': 2.5048796875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4061386585235596})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3578832149505615})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3987007141113281})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4129769802093506})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 58811], ['id', 10198], ['id', 21784], ['id', 1363], ['id', 34986]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0320902623529102, 1.8112745838249493, 2.4005878432237324, 2.694190091987018, 2.8611135746631042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.681900978088379})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.873028039932251})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.676567792892456})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5001838207244873})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.890880584716797})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6159167289733887})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0998353958129883})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6181, 'crossentropy': 2.805439453125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3313727378845215})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3451237678527832})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3138132095336914})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2974697351455688})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2749966382980347})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2605985403060913})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 15510], ['id', 49574], ['id', 42965], ['id', 57814], ['id', 35178]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.076279592522857, 1.983326261891813, 2.553080165002501, 2.8468650688594384, 2.9924852737014414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5534002780914307})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.1197099685668945})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.3544814586639404})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6314048767089844})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.8368234634399414})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1223998069763184})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8491358757019043})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6174, 'crossentropy': 2.809966796875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.472175121307373})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.38508141040802})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4420711994171143})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3457553386688232})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3485634326934814})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2941131591796875})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 55864], ['id', 2494], ['id', 20204], ['id', 35225], ['id', 36445]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.0432901590510928, 1.9290862102287818, 2.4609204938400904, 2.7867612801350212, 2.959622358553017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4966963529586792})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.9120190143585205})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4392881393432617})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4724740982055664})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6462478637695312})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6386, 'crossentropy': 2.0121697265625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.345860242843628})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2321126461029053})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2494702339172363})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2326033115386963})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 8453], ['id', 17253], ['id', 39376], ['id', 24722], ['id', 6047]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9913097434405787, 1.6938563713716817, 2.195274102532858, 2.5273387577038786, 2.692777150236889]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5428063869476318})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8119585514068604})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.213277816772461})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.3362936973571777})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.3054561614990234})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6401, 'crossentropy': 1.8823703125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1503098011016846})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1210923194885254})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1002660989761353})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0997867584228516})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 49520], ['id', 34468], ['id', 24192], ['id', 4664], ['id', 31461]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9943035691736464, 1.790071085608039, 2.3789552678017403, 2.772098671532003, 2.9442852197495766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.5545730590820312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8970037698745728})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.207714796066284})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.376260280609131})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5639724731445312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7117114067077637})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.076693296432495})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 2.648212109375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3563627004623413})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.349519968032837})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3160440921783447})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2786811590194702})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2782747745513916})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2413254976272583})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 24024], ['id', 21150], ['id', 742], ['id', 51506], ['id', 36050]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.070226878998436, 1.9848830488123852, 2.595413463363379, 2.875704208351119, 3.0386130506788946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3698606491088867})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.72536301612854})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.228076457977295})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5011696815490723})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.4657113552093506})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6393, 'crossentropy': 1.8282521484375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.203588843345642})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1732666492462158})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1366767883300781})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0864466428756714})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 42682], ['id', 47828], ['id', 38539], ['id', 53038], ['id', 18275]], 'labels': [1, -1, -1, -1, 5], 'scores': [0.7865491949123165, 1.4800333586111232, 1.993889203018778, 2.348415231127377, 2.5954273808530646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4172554016113281})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.9024670124053955})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.059178352355957})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.081967830657959})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.472520351409912})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.653, 'crossentropy': 1.9065720703125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1766281127929688})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1334718465805054})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1165461540222168})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0905494689941406})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 4717], ['id', 32361], ['id', 14334], ['id', 45110], ['id', 50651]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0663920085016634, 1.820658172463748, 2.381613812344484, 2.7058528007293017, 2.8402280987014663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4762884378433228})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.8202167749404907})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.0614118576049805})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.281581401824951})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7798733711242676})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.676126003265381})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6552, 'crossentropy': 2.317072265625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2177422046661377})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.200028896331787})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2036809921264648})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2061583995819092})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1917321681976318})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 18028], ['id', 47256], ['id', 8497], ['id', 31779], ['id', 3558]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.096561172968621, 2.0016896690553523, 2.6129475315491346, 2.947370997033012, 3.107271230943769]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4047255516052246})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8134474754333496})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.2336924076080322})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4112629890441895})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6620941162109375})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6486, 'crossentropy': 1.948364453125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.294065237045288})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1705116033554077})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.101304054260254})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.116328239440918})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 27079], ['id', 52039], ['id', 6857], ['id', 45928], ['id', 33528]], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.9744028619856231, 1.7417701551580151, 2.316796470293115, 2.6934800041552673, 2.855693690951078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3107702732086182})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6615228652954102})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.963477373123169})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.21163010597229})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.491672992706299})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6545205116271973})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6542, 'crossentropy': 2.18335390625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3638099431991577})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1880075931549072})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.228256106376648})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2190420627593994})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2495853900909424})
store['active_learning_steps'][45]['eval_training']['best_epoch']=2
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 34476], ['id', 27315], ['id', 28342], ['id', 440], ['id', 56807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.97703821193919, 1.800881750391187, 2.377619557873757, 2.6924887405829807, 2.859453730274371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.410207748413086})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7958295345306396})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.1059160232543945})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3430609703063965})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.364476203918457})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.4835710525512695})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3825011253356934})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4575986862182617})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.664, 'crossentropy': 2.6013326171875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1852198839187622})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2665421962738037})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2837252616882324})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.252805471420288})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3072426319122314})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2378768920898438})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2845933437347412})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 41740], ['id', 42789], ['id', 20644], ['id', 31863], ['id', 13679]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1190504539546906, 1.9755678445577094, 2.565123688566408, 2.8825908983313084, 2.9891427191986706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4415082931518555})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.9841818809509277})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.171060085296631})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.423694610595703})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5134005546569824})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5837244987487793})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6108570098876953})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.9702227115631104})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3610336780548096})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0596389770507812})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.2964484691619873})
store['active_learning_steps'][47]['training']['best_epoch']=8
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6389, 'crossentropy': 3.0975134765625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4341161251068115})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3181405067443848})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3618206977844238})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3423925638198853})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4458593130111694})
store['active_learning_steps'][47]['eval_training']['best_epoch']=2
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 29744], ['id', 27992], ['id', 54525], ['id', 47083], ['id', 47443]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.204435529302513, 2.0579726647740983, 2.6762344869808743, 3.015296969646055, 3.1557020407470207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4462134838104248})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6770190000534058})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.938509225845337})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.2170472145080566})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.2946343421936035})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6414427757263184})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6544, 'crossentropy': 2.228056640625}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3199732303619385})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3116133213043213})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2648093700408936})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2871217727661133})
store['active_learning_steps'][48]['eval_training']['best_epoch']=1
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 9212], ['id', 47914], ['id', 18145], ['id', 30197], ['id', 54284]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0222170914189284, 1.783215912050578, 2.3701256657631062, 2.7114015830578175, 2.891783123383921]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.335228681564331})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8079760074615479})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.106955051422119})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3509702682495117})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.411606788635254})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.7737908363342285})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.581021308898926})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6564, 'crossentropy': 2.427405859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2380785942077637})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.210784673690796})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2479751110076904})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2486937046051025})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3312351703643799})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.191601037979126})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 6076], ['id', 14004], ['id', 19737], ['id', 44984], ['id', 18028]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.018156046592255, 1.7966293187957065, 2.278834693080756, 2.5865731572814727, 2.7178350389462604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.429624319076538})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.7812936305999756})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.0398924350738525})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.353595495223999})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.3151345252990723})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7788467407226562})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.6819028854370117})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.935055732727051})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.643, 'crossentropy': 2.5397087890625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2769160270690918})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2536653280258179})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3053600788116455})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2487777471542358})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2428884506225586})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2232458591461182})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1860910654067993})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 40534], ['id', 48435], ['id', 48809], ['id', 46582], ['id', 35340]], 'labels': [-1, -1, -1, 8, 2], 'scores': [1.0034760081832463, 1.7924208987200623, 2.297097391882099, 2.5955753717249443, 2.785274855579872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3507680892944336})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.7669761180877686})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9936556816101074})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.163482666015625})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.360156774520874})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6353096961975098})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6643, 'crossentropy': 2.070904296875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2147555351257324})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1641497611999512})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2097162008285522})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1566879749298096})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1279878616333008})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 42934], ['id', 18521], ['id', 32843], ['id', 18201], ['id', 26892]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0068820828521403, 1.8151049741623804, 2.3821284540278214, 2.7287771267081924, 2.8544098928123054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3605854511260986})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.744922399520874})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1734626293182373})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.5484085083007812})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.2761430740356445})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6303277015686035})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.967827796936035})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7745141983032227})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6566, 'crossentropy': 2.5264451171875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.325814962387085})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2656564712524414})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3406763076782227})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2628687620162964})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3922752141952515})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2201638221740723})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2759392261505127})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 9118], ['id', 3383], ['id', 53164], ['id', 16731], ['id', 36763]], 'labels': [-1, -1, -1, 5, 1], 'scores': [1.0007844233683376, 1.8366170880903772, 2.388312623050976, 2.6369862017247243, 2.79684008645071]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4766218662261963})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.8529353141784668})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1801910400390625})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.2451438903808594})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2919740676879883})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.2286791801452637})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6615, 'crossentropy': 2.3337490234375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3063565492630005})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2503360509872437})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.204850435256958})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.300886631011963})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3014904260635376})
store['active_learning_steps'][53]['eval_training']['best_epoch']=3
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 12911], ['id', 28930], ['id', 52796], ['id', 20681], ['id', 33216]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1378646286563254, 2.032045980326021, 2.5837144250609296, 2.9122304487616146, 3.0605155563409125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3881099224090576})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.7541706562042236})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.0865211486816406})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.20723295211792})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.484455108642578})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4814233779907227})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7614545822143555})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6648, 'crossentropy': 2.362776953125}
