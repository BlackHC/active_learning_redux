store = {}
store['timestamp']=1621481956
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=69']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=69
store['worker_id']=69
store['num_workers']=80
store['config']={'seed': 1307, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.4345860481262207})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.02122163772583})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.788717269897461})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8582043647766113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.599320411682129})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5972, 'crossentropy': 3.33372265625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3838263750076294})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.5179532766342163})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4201428890228271})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4747577905654907})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 46777], ['id', 44143], ['id', 27073], ['id', 6382], ['id', 6552]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1752036590698727, 1.9832709599585976, 2.539157266626278, 2.8325270736683112, 2.9899299215421005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.618882417678833})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.262338399887085})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.407805919647217})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.777812957763672})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.698962688446045})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.8941993713378906})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.9797370433807373})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6003, 'crossentropy': 2.7766029296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.304088830947876})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4069290161132812})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5253888368606567})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.4798171520233154})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3542804718017578})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 3249], ['id', 41273], ['id', 17613], ['id', 34822], ['id', 23115]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7973619085291999, 1.3984106449501605, 1.8944179065356135, 2.2196028983603453, 2.435551289717522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5979282855987549})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.126749038696289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.3447675704956055})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.492830276489258})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6294376850128174})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6615443229675293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.392704963684082})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6394, 'crossentropy': 2.5980337890625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1832270622253418})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2366849184036255})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2238788604736328})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2394691705703735})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2812104225158691})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2049609422683716})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 37794], ['id', 42858], ['id', 27719], ['id', 8361], ['id', 54763]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8430724343833671, 1.6032285933385952, 2.113270696258013, 2.4959164167919363, 2.7452683592502787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.7505706548690796})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.3627047538757324})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.540879726409912})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.636195182800293})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8218936920166016})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0708160400390625})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6335, 'crossentropy': 2.679576953125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2568707466125488})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1628599166870117})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2958999872207642})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2539088726043701})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2692803144454956})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 20195], ['id', 3081], ['id', 18472], ['id', 47773], ['id', 30956]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7687953353696013, 1.4403791830067938, 1.908290204703401, 2.28039197555602, 2.5338456700245215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3514177799224854})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6896388530731201})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.942825198173523})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.9936597347259521})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.184419631958008})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.2164812088012695})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.366455078125})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6738, 'crossentropy': 2.14297890625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.157841444015503})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1254626512527466})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1042983531951904})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1079792976379395})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.117276906967163})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.114479422569275})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 43510], ['id', 33574], ['id', 36338], ['id', 6503], ['id', 4194]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8756532916099973, 1.5896125479144434, 2.113940867820874, 2.4566525837457025, 2.6843076670591035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3681035041809082})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.59354829788208})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.8632135391235352})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0215744972229004})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5237226486206055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.385944366455078})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.3271286487579346})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6693, 'crossentropy': 2.2107921875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1866343021392822})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1811814308166504})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1254243850708008})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1412711143493652})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.140293836593628})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1582365036010742})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 43536], ['id', 35699], ['id', 14115], ['id', 25328], ['id', 18058]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7683546792619012, 1.371906437989661, 1.8657571065355496, 2.232291011976886, 2.4662602358428263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3161845207214355})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.614275336265564})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8878767490386963})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.0976967811584473})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.3053970336914062})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6818, 'crossentropy': 1.59348076171875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.116270661354065})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.063936471939087})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0786573886871338})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0603140592575073})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 37489], ['id', 22937], ['id', 16803], ['id', 43241], ['id', 46975]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5547119698935552, 1.055261360308878, 1.5030328949990057, 1.8509102882970918, 2.1228010556418306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.34382963180542})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.353651523590088})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.794441819190979})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8277122974395752})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.3164267539978027})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.0737643241882324})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.1174051761627197})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6957, 'crossentropy': 1.826980078125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0520875453948975})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0300021171569824})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0176143646240234})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0290265083312988})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.999780535697937})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0396881103515625})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 51209], ['id', 48482], ['id', 1729], ['id', 15975], ['id', 4440]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7303359295968577, 1.3378296523282827, 1.8546582059555918, 2.2870061637061925, 2.5496459521466974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2464191913604736})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4838331937789917})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.716747760772705})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.819838285446167})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.026150703430176})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.15925669670105})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.078198194503784})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6897, 'crossentropy': 1.789787109375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0964794158935547})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0698153972625732})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0012962818145752})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0979437828063965})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0839731693267822})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0813852548599243})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 9302], ['id', 54352], ['id', 22617], ['id', 29088], ['id', 35776]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6222992099175069, 1.1199335061644033, 1.53827293829411, 1.8733670195258734, 2.1279582541696955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3139533996582031})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4671237468719482})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4794745445251465})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7725958824157715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.9884686470031738})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.158963441848755})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9830973148345947})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6919, 'crossentropy': 1.79815859375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1267452239990234})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0797202587127686})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1984047889709473})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1141595840454102})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.167362928390503})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1321890354156494})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 6093], ['id', 21859], ['id', 43346], ['id', 47864], ['id', 11643]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6121385493395963, 1.1495372347008717, 1.615883270753093, 1.9523554120833477, 2.2083029300188217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2868328094482422})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4136877059936523})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6596450805664062})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.988349199295044})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.1817190647125244})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.364910125732422})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.263258457183838})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6807, 'crossentropy': 1.9088912109375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1508734226226807})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1219490766525269})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0999820232391357})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0724585056304932})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1174081563949585})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1225322484970093})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 20932], ['id', 55929], ['id', 32550], ['id', 39146], ['id', 6212]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6516024585779026, 1.2345910768441053, 1.7085486179545812, 2.087014821242004, 2.3351847097531886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2570323944091797})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3535375595092773})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6879749298095703})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8616403341293335})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0916287899017334})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.1065855026245117})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2792723178863525})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.494856834411621})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.37324595451355})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6977, 'crossentropy': 2.0515935546875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1478126049041748})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1254557371139526})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0833256244659424})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1881628036499023})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.156259536743164})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1432468891143799})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1051479578018188})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.118741512298584})
store['active_learning_steps'][11]['eval_training']['best_epoch']=7
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 35782], ['id', 51064], ['id', 42501], ['id', 770], ['id', 52799]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6821914990336093, 1.276661298185548, 1.7756146642713162, 2.149759259191174, 2.4279766041532724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2350547313690186})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4764811992645264})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.74257493019104})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.882656216621399})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.0858278274536133})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.2160332202911377})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3646085262298584})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.4771175384521484})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2620997428894043})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.578115940093994})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.4714150428771973})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.7026078701019287})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.7425944805145264})
store['active_learning_steps'][12]['training']['best_epoch']=10
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7057, 'crossentropy': 2.39837265625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.138569712638855})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1504453420639038})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.181227445602417})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1535992622375488})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1836135387420654})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1860737800598145})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 15534], ['id', 29799], ['id', 24712], ['id', 58560], ['id', 39833]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7065076389788616, 1.3129116325715824, 1.8445929138427903, 2.2493396508116255, 2.530358353707798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2810105085372925})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2601683139801025})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4932456016540527})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.6926040649414062})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8000664710998535})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.9517619609832764})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9242521524429321})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8924753665924072})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.360112428665161})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.452223777770996})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.243659496307373})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6934, 'crossentropy': 1.9574384765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1069371700286865})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0561672449111938})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0834473371505737})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0822014808654785})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0149427652359009})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1208487749099731})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0671050548553467})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0355582237243652})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 2369], ['id', 36765], ['id', 22509], ['id', 33043], ['id', 49995]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6391534910538392, 1.239308182392564, 1.747207529775464, 2.1699907813431456, 2.452256239882902]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2522231340408325})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2426682710647583})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.3627430200576782})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5574915409088135})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.737525224685669})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8783257007598877})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6913, 'crossentropy': 1.39420263671875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.150672197341919})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.042040467262268})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0053924322128296})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0125155448913574})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9912352561950684})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 41119], ['id', 48506], ['id', 59448], ['id', 22131], ['id', 6740]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5257767557844528, 0.9865530567907843, 1.334784785215839, 1.6251483380268743, 1.8520696521116928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.3333419561386108})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3873324394226074})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3737306594848633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.6547907590866089})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.8118581771850586})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.927772045135498})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.0405008792877197})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.341710090637207})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.999208688735962})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.300931453704834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.3173952102661133})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.5812296867370605})
store['active_learning_steps'][15]['training']['best_epoch']=9
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6951, 'crossentropy': 2.093911328125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0962514877319336})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0567243099212646})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.118574857711792})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.064591884613037})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1552393436431885})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0754061937332153})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0862064361572266})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0732104778289795})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 56047], ['id', 13933], ['id', 9125], ['id', 56186], ['id', 43504]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6601671380261451, 1.230174178164134, 1.7248875931795684, 2.111933017150914, 2.385128226361611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.3784568309783936})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2310606241226196})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3920996189117432})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4404122829437256})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7381746768951416})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8956499099731445})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9200689792633057})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7053, 'crossentropy': 1.47014638671875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0702009201049805})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0134427547454834})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9762960076332092})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9627254009246826})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9717749953269958})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.954743504524231})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 1456], ['id', 38628], ['id', 39750], ['id', 16154], ['id', 25868]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5507297799487023, 1.078144355761884, 1.5319239101614333, 1.8699581214390415, 2.09204481742218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.4149038791656494})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.254194736480713})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2013957500457764})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.6606431007385254})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.731136679649353})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.705739974975586})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.8017280101776123})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.30755615234375})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9782745838165283})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.939807415008545})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7023, 'crossentropy': 1.900158984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1194988489151})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.053619623184204})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0358588695526123})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0153406858444214})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.045974612236023})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0169645547866821})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0374481678009033})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0113763809204102})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0287303924560547})
store['active_learning_steps'][17]['eval_training']['best_epoch']=9
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 32012], ['id', 15538], ['id', 508], ['id', 29126], ['id', 12287]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6932898174431975, 1.263125953275507, 1.740418442578453, 2.1046650747347746, 2.3735933922984103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.4218404293060303})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.147068977355957})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1890062093734741})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3777425289154053})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5043272972106934})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6634490489959717})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6698123216629028})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.71, 'crossentropy': 1.41004580078125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0764234066009521})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.969947338104248})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9790292382240295})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9901306629180908})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.006127953529358})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9458775520324707})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 23586], ['id', 35085], ['id', 3929], ['id', 55098], ['id', 38304]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6514270497838646, 1.2133643747827771, 1.7129031726851007, 2.0975922705229104, 2.359513272905165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3005249500274658})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1263079643249512})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3346478939056396})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3631888628005981})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6429070234298706})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5268266201019287})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6486937999725342})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8035614490509033})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.845106601715088})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.049318552017212})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.378220558166504})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.1780600547790527})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.302635908126831})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4857747554779053})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.2571449279785156})
store['active_learning_steps'][19]['training']['best_epoch']=12
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7065, 'crossentropy': 2.0756712890625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.09073805809021})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9569634199142456})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9914535284042358})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0194971561431885})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0292880535125732})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 52786], ['id', 14040], ['id', 11651], ['id', 40639], ['id', 54304]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.801279032275181, 1.4872872657787544, 2.078909737683932, 2.516212936602501, 2.796309715338472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.3118278980255127})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2305155992507935})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2184034585952759})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3697619438171387})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5549445152282715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6574316024780273})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6372802257537842})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.760024905204773})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.00749135017395})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9650074243545532})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.8901124000549316})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7092, 'crossentropy': 1.7522271484375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1186046600341797})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.975265383720398})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9437315464019775})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9676429033279419})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9493286609649658})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9547096490859985})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 3694], ['id', 587], ['id', 57641], ['id', 38826], ['id', 14265]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.722571545368905, 1.3145232785162624, 1.8124292766358634, 2.2206098209964766, 2.495315266238795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.232762336730957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2045503854751587})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.256593942642212})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3228105306625366})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4871320724487305})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6070417165756226})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6999214887619019})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.942783236503601})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.896471619606018})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.715, 'crossentropy': 1.6293462890625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.144157886505127})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0285887718200684})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9925196170806885})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9666116833686829})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9544567465782166})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9616233706474304})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9426516890525818})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9801042079925537})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 18255], ['id', 26174], ['id', 28145], ['id', 37368], ['id', 59247]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6164957130927364, 1.1735538192070858, 1.6637192524530002, 2.0357606878647747, 2.3097287225714442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.3933767080307007})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1134939193725586})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1348838806152344})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2476723194122314})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6532195806503296})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6106367111206055})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.5449137687683105})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.7616665363311768})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9633142948150635})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.017652988433838})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7156, 'crossentropy': 1.67412734375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1139925718307495})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9732260704040527})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9734348058700562})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.001071572303772})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9601839780807495})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9319698214530945})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9814268946647644})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9664634466171265})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9900088310241699})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 50052], ['id', 23295], ['id', 23187], ['id', 5946], ['id', 5309]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6072755243909206, 1.1391883687128472, 1.5860953492484136, 1.9726210373158262, 2.2468753666986725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.4404296875, 'crossentropy': 1.4253723621368408})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1482259035110474})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2363581657409668})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.3187010288238525})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.5568368434906006})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5604491233825684})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6518162488937378})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7243362665176392})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7219746112823486})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7835813760757446})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.8205899000167847})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.84824800491333})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.9628925323486328})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.0682873725891113})
store['active_learning_steps'][23]['training']['best_epoch']=11
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7246, 'crossentropy': 1.6914697265625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0890963077545166})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9363462924957275})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9516118764877319})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9335740804672241})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9507124423980713})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9831150770187378})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0058845281600952})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 53509], ['id', 56635], ['id', 8891], ['id', 50795], ['id', 3800]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7428566134413308, 1.3461021097065462, 1.8622077190700672, 2.2558431269817563, 2.504999849040937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.4755859375, 'crossentropy': 1.4493364095687866})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.192095398902893})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1155426502227783})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.32187819480896})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4087293148040771})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.7091271877288818})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6876, 'crossentropy': 1.14763623046875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1087908744812012})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.0307486057281494})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9966156482696533})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0078189373016357})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9668101072311401})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 12579], ['id', 2910], ['id', 9771], ['id', 29255], ['id', 27147]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4469445162089656, 0.8334436972270911, 1.182313745253131, 1.4801433409003515, 1.7232594110405515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.4423828125, 'crossentropy': 1.4088165760040283})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1619713306427002})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2010064125061035})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2733279466629028})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5365110635757446})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6213788986206055})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.638297438621521})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.691, 'crossentropy': 1.34190380859375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1581089496612549})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0122218132019043})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.977014422416687})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9551224708557129})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9854525327682495})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9729514718055725})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 12388], ['id', 30405], ['id', 27863], ['id', 11818], ['id', 1797]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4783118625575309, 0.8984039719950689, 1.270046469616661, 1.5775078496664738, 1.8340353906506532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.407280683517456})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1128426790237427})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1825981140136719})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2155177593231201})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3951222896575928})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.51812744140625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.6508530378341675})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6852, 'crossentropy': 1.27931591796875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1129159927368164})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0193818807601929})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9575875997543335})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9548125863075256})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9441268444061279})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9630300998687744})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 40572], ['id', 1447], ['id', 35730], ['id', 734], ['id', 8608]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5407295822611122, 0.9873827060915334, 1.3784306463121476, 1.7104813651456023, 1.9851880244522757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.4765625, 'crossentropy': 1.4922559261322021})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.121222972869873})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0811643600463867})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.253037929534912})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3415859937667847})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5150549411773682})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.50840163230896})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5268959999084473})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.756242036819458})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.7912707328796387})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9675705432891846})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7212, 'crossentropy': 1.520261328125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0968294143676758})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9485745429992676})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9852514266967773})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.932520866394043})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9574211835861206})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9318966865539551})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9423794150352478})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9482584595680237})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9386230707168579})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9481372833251953})
store['active_learning_steps'][27]['eval_training']['best_epoch']=10
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 35624], ['id', 59771], ['id', 25373], ['id', 58333], ['id', 16235]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5598560371672012, 1.0793109044299527, 1.5381732349009978, 1.9235550020544885, 2.1895258063397867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.474609375, 'crossentropy': 1.4862103462219238})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1255226135253906})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2361054420471191})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.372006893157959})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4076064825057983})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.663442850112915})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4518977403640747})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6134382486343384})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7077038288116455})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.818340539932251})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.944093108177185})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7035, 'crossentropy': 1.6660033203125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1404738426208496})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0439562797546387})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9910647869110107})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.980383038520813})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0514817237854004})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9761985540390015})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0039803981781006})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9873456954956055})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9869883060455322})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9931566715240479})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 8640], ['id', 10549], ['id', 18913], ['id', 54633], ['id', 5111]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7111381617987389, 1.3603995735906889, 1.8883887977823726, 2.2390715924384272, 2.4478302455969754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3458044528961182})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1295173168182373})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.137320876121521})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.344109058380127})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4819258451461792})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.4597811698913574})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.732666254043579})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7285782098770142})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.9235912561416626})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7092, 'crossentropy': 1.439697265625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1071207523345947})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9978104829788208})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.933000385761261})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9666023254394531})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9252484440803528})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9168254137039185})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.890078604221344})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9252817630767822})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 42229], ['id', 47822], ['id', 10233], ['id', 41019], ['id', 10519]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5889111155088915, 1.1108515924863172, 1.5711544316847137, 1.9282947733253524, 2.1911745674694005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.45703125, 'crossentropy': 1.5978431701660156})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2370951175689697})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0988339185714722})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.102614402770996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.273498296737671})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.318434715270996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.5285906791687012})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.630855917930603})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6894519329071045})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7209, 'crossentropy': 1.3839298828125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1245760917663574})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9754773378372192})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9434733390808105})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9484497308731079})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9195225834846497})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9243000745773315})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.8949892520904541})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.8817853927612305})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 4887], ['id', 4026], ['id', 16676], ['id', 32100], ['id', 25216]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5356145275135116, 0.9978568742035647, 1.419116846754088, 1.7692746947704672, 2.0637579070026986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3906810283660889})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.093508005142212})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0758858919143677})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.1149189472198486})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.264502763748169})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4789845943450928})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.531840443611145})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.544009804725647})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.6578363180160522})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6759045124053955})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.7779533863067627})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.9069223403930664})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.578019142150879})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.7944468259811401})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7252, 'crossentropy': 1.74220546875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.161295771598816})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9645947217941284})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9783830642700195})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9588718414306641})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9426866769790649})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9808070659637451})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9434652924537659})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9222916960716248})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 12580], ['id', 5194], ['id', 31737], ['id', 9612], ['id', 51770]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6275440711807263, 1.206108766612755, 1.6941734595007514, 2.0953938288519263, 2.38956030206242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.4699753522872925})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1732056140899658})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1318495273590088})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0766944885253906})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2286059856414795})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3869092464447021})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4302105903625488})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4912497997283936})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5357122421264648})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.712, 'crossentropy': 1.38439892578125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0563305616378784})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9364532828330994})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.8851162195205688})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.8829988241195679})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8749892711639404})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8693811893463135})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.8683391809463501})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.8671771883964539})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 32065], ['id', 3540], ['id', 125], ['id', 9436], ['id', 40776]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5134025097290198, 0.9855498806498755, 1.4320513897638216, 1.8034715061156055, 2.1028682160764216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.5171021223068237})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1809649467468262})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1194566488265991})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2034928798675537})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2162606716156006})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1808524131774902})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2972157001495361})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5043636560440063})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3829240798950195})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.6538875102996826})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.581458330154419})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6596741676330566})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8242065906524658})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7910306453704834})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8412294387817383})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.9105384349822998})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7735285758972168})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.1237006187438965})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.9178392887115479})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.9584083557128906})
store['active_learning_steps'][33]['training']['best_epoch']=17
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7334, 'crossentropy': 1.8870712890625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0385602712631226})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9527338743209839})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9485701322555542})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9100332260131836})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9989068508148193})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9747073650360107})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9934597015380859})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.9602434039115906})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9581073522567749})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9725223779678345})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9630088806152344})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 28812], ['id', 50748], ['id', 12773], ['id', 30432], ['id', 40035]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6897134986519724, 1.283215668846457, 1.7933071571474928, 2.17815013248784, 2.4515846531431613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.3505187034606934})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0633684396743774})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0054419040679932})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1441277265548706})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.1687953472137451})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.3193731307983398})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7165, 'crossentropy': 1.04492998046875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.132156491279602})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9805641770362854})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9701151847839355})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.8951210379600525})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9213078022003174})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 51163], ['id', 36120], ['id', 3301], ['id', 43997], ['id', 3913]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36356537897904095, 0.6845646793823126, 0.9816517883787803, 1.2337760642518774, 1.4547140212790275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.4130425453186035})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1061115264892578})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.0411388874053955})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0735827684402466})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1708954572677612})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.1784863471984863})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.3575544357299805})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.4069246053695679})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.418839931488037})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.4110667705535889})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4645462036132812})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.5820139646530151})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.610929250717163})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.6349334716796875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.7320325374603271})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7662429809570312})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.753868579864502})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.0078301429748535})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.770824909210205})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.8034858703613281})
store['active_learning_steps'][35]['training']['best_epoch']=17
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7487, 'crossentropy': 1.7988865234375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1319725513458252})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9287990927696228})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.8821854591369629})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.8970202207565308})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.882454514503479})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9249211549758911})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.9081604480743408})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9019498229026794})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.9123662114143372})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8940728902816772})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.8991115093231201})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9206010103225708})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8936604857444763})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9192923307418823})
store['active_learning_steps'][35]['eval_training']['best_epoch']=11
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 24696], ['id', 16680], ['id', 54297], ['id', 52619], ['id', 198]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6149873541567543, 1.204899120841742, 1.7246851872054956, 2.1559864221975635, 2.455155838121973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.4021508693695068})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0996954441070557})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9789060950279236})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.039970874786377})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.0988860130310059})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.1831369400024414})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.2996035814285278})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2599608898162842})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.461108684539795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.4637763500213623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.54409658908844})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.615660548210144})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7391, 'crossentropy': 1.46307177734375}
