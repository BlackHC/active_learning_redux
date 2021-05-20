store = {}
store['timestamp']=1621471678
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=5']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=5
store['worker_id']=5
store['num_workers']=80
store['config']={'seed': 1239, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.5092897415161133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.3695240020751953})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.4138526916503906})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.605605363845825})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.133161544799805})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5986, 'crossentropy': 3.385106640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2698540687561035})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.30440354347229})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2914576530456543})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.279985785484314})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 40429], ['id', 29764], ['id', 47291], ['id', 20087], ['id', 19527]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1555598973842023, 2.1020790585842555, 2.648399658072556, 2.9802884447240343, 3.105894238661671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.7483173608779907})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.6307339668273926})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.612196922302246})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.567840099334717})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.7202799320220947})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.0173683166503906})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.2263429164886475})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 2.9429916015625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3886032104492188})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.393143892288208})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.383798360824585})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4033725261688232})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4956786632537842})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.5020856857299805})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 34961], ['id', 8361], ['id', 42051], ['id', 9302], ['id', 8126]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7387704423199981, 1.3676339449515464, 1.901698974531314, 2.2497531311031738, 2.494499750721486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.6183500289916992})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.219271659851074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.690213918685913})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.589198112487793})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 1.6672431640625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1730430126190186})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1650696992874146})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1933362483978271})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1707], ['id', 11473], ['id', 22344], ['id', 34822], ['id', 19687]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5122050217751011, 0.9705624887868054, 1.30588869810677, 1.5806674217213637, 1.7922948529391132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4418524503707886})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0117812156677246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.3750226497650146})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7676706314086914})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.7451577186584473})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8738515377044678})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6309, 'crossentropy': 2.46889375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2519959211349487})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.250462532043457})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2791954278945923})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.339478850364685})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.298192024230957})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 28218], ['id', 29376], ['id', 24891], ['id', 32671], ['id', 6714]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7810486130063742, 1.388898734597839, 1.846489454975237, 2.2203643570985836, 2.4944945770368108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3301143646240234})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6737148761749268})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.2122159004211426})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.271073818206787})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.2165021896362305})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.649, 'crossentropy': 1.7036408203125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1732933521270752})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1475390195846558})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1335947513580322})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1515774726867676})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 9232], ['id', 13195], ['id', 31385], ['id', 31778], ['id', 55165]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6241184877990773, 1.168411220459709, 1.5946920180386357, 1.9201433194956241, 2.17502837424664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4535069465637207})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.6428425312042236})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.0128865242004395})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.079277753829956})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.223890781402588})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.193047523498535})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9090147018432617})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6348, 'crossentropy': 2.2340373046875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1674611568450928})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2048943042755127})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2541091442108154})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1921069622039795})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1544468402862549})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1579110622406006})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 5997], ['id', 8105], ['id', 12669], ['id', 416], ['id', 37898]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7403991980675322, 1.3670808643915042, 1.90307304739507, 2.2519215895532945, 2.505398637489778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3671941757202148})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.857102632522583})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.074970245361328})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4014265537261963})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.976451873779297})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7588629722595215})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6323, 'crossentropy': 2.0871138671875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2372972965240479})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.219289779663086})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.300925612449646})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2102603912353516})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.230072021484375})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 42695], ['id', 15635], ['id', 24459], ['id', 51167], ['id', 20002]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6933264777192834, 1.195941814708743, 1.6042650453262182, 1.9106735391224294, 2.1391325096932308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2472825050354004})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5624470710754395})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.049222469329834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.4568681716918945})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6205, 'crossentropy': 1.2759375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2383636236190796})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1922664642333984})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1931087970733643})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 39750], ['id', 59771], ['id', 35654], ['id', 38100], ['id', 55765]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5399694578633516, 0.9357537078334097, 1.2730609503838002, 1.5598912089698151, 1.794821733025234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2784119844436646})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.466404676437378})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9587512016296387})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0380172729492188})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.318697929382324})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.4722707271575928})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6446, 'crossentropy': 2.02753515625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2361129522323608})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2599583864212036})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2642704248428345})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.220055341720581})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2150815725326538})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 55083], ['id', 5355], ['id', 5513], ['id', 34263], ['id', 57078]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6095144009499207, 1.1640384131976762, 1.6114761550265992, 1.9585807330272003, 2.239183234070767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.391526460647583})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.781162977218628})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.108452320098877})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.2280988693237305})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6129424571990967})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8956358432769775})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.918898820877075})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.177673816680908})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.894914150238037})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.1435792446136475})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6424, 'crossentropy': 2.80606875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2945796251296997})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.289302110671997})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3735688924789429})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4232592582702637})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4034008979797363})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4626424312591553})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4753928184509277})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4944360256195068})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5127640962600708})
store['active_learning_steps'][9]['eval_training']['best_epoch']=7
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 18126], ['id', 51101], ['id', 22547], ['id', 59741], ['id', 17971]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6461207369912814, 1.2019449603424612, 1.6602849667147046, 2.022611021592275, 2.282026866838466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.288692831993103})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.7242194414138794})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.166553497314453})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.2216286659240723})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.425701141357422})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.701765537261963})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.823474645614624})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.2101566791534424})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.1063265800476074})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.462049961090088})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.3051576614379883})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.37260103225708})
store['active_learning_steps'][10]['training']['best_epoch']=9
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6376, 'crossentropy': 3.369304296875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3481743335723877})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.429251790046692})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4315541982650757})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4292314052581787})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3687233924865723})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3379273414611816})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3901389837265015})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3697552680969238})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 42826], ['id', 20789], ['id', 37253], ['id', 20943], ['id', 7790]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7546425666290748, 1.3721249397991242, 1.9070938456626045, 2.303261768503871, 2.552161959274051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3797073364257812})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3848302364349365})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.609621286392212})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.0108494758605957})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8759088516235352})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6597, 'crossentropy': 1.4175455078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.227470874786377})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1615068912506104})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1739778518676758})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1312627792358398})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 2434], ['id', 34056], ['id', 13259], ['id', 2780], ['id', 24043]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.49732439499228365, 0.9745248245333342, 1.3610259329569114, 1.6876985466028582, 1.9376504305503754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.312788963317871})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3869116306304932})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5679652690887451})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7907496690750122})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.047600507736206})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.1640818119049072})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6652, 'crossentropy': 1.5719791015625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1509597301483154})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.118851661682129})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1677381992340088})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1031427383422852})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.099388599395752})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 45096], ['id', 54271], ['id', 26018], ['id', 20332], ['id', 11565]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5091482787092079, 0.9803473887292005, 1.3806725323231213, 1.7154817182172293, 1.9582399490997062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3136467933654785})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3323276042938232})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.6544883251190186})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.800239086151123})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.9504363536834717})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8373299837112427})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3634321689605713})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.683377981185913})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.435987949371338})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6704, 'crossentropy': 1.9959169921875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.176387071609497})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0925772190093994})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0761637687683105})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.112737774848938})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1087324619293213})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.135359287261963})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.092416763305664})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0940309762954712})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 48756], ['id', 57290], ['id', 38448], ['id', 9855], ['id', 18164]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5374935050256475, 1.0463449161866878, 1.5229479951569989, 1.9227625791426712, 2.2333088576429407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3957455158233643})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4284734725952148})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5051350593566895})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.7974058389663696})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.8478693962097168})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.5556998252868652})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.3635401725769043})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.393759250640869})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.4449024200439453})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.4511170387268066})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6596, 'crossentropy': 2.434524609375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2616939544677734})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2374238967895508})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2153024673461914})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2436912059783936})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2137447595596313})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 2572], ['id', 3895], ['id', 56472], ['id', 44428], ['id', 36120]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6422713653001502, 1.2428890702221551, 1.7686976711450937, 2.1701123658404358, 2.4413410233805903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2845699787139893})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2726726531982422})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4737622737884521})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7156851291656494})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.848555326461792})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8222819566726685})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.0156233310699463})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.163083076477051})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.37906551361084})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.4469704627990723})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2655279636383057})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6653, 'crossentropy': 2.328173046875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.21039879322052})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2103945016860962})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2493013143539429})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3429055213928223})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2700934410095215})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2444629669189453})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2334463596343994})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.216864824295044})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2262495756149292})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2377891540527344})
store['active_learning_steps'][15]['eval_training']['best_epoch']=7
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 19268], ['id', 25420], ['id', 19837], ['id', 8658], ['id', 57768]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6688318630549757, 1.2692973418038243, 1.7819735650668367, 2.161198299424134, 2.4343779756723674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3146190643310547})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3009283542633057})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5072803497314453})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.605987310409546})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.609755516052246})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8730602264404297})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9523429870605469})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6746, 'crossentropy': 1.6798455078125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2104134559631348})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0902495384216309})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0855576992034912})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0692476034164429})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0666412115097046})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0407812595367432})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46619], ['id', 34149], ['id', 19842], ['id', 17701], ['id', 9862]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5847905651280185, 1.0918875984657022, 1.5067151700797945, 1.8378791191918191, 2.0805453386987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.306502103805542})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.201946496963501})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.213876485824585})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.404315710067749})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.590601921081543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.6699942350387573})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.653867244720459})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1422770023345947})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.0178141593933105})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9279403686523438})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6896, 'crossentropy': 1.8293208984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1220417022705078})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1357448101043701})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1015777587890625})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0933436155319214})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1170110702514648})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0667500495910645})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.084667682647705})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0641666650772095})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 32832], ['id', 35308], ['id', 13530], ['id', 33456], ['id', 59250]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6567783297310348, 1.2141633867810997, 1.6978597928752146, 2.0716373918662923, 2.3447478349231714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2928955554962158})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2279932498931885})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3184852600097656})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.500020980834961})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.6813507080078125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8133128881454468})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.044956922531128})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6791, 'crossentropy': 1.5654265625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1491172313690186})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0873830318450928})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1000328063964844})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.095020055770874})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0648701190948486})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0553483963012695})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 40742], ['id', 23444], ['id', 4148], ['id', 27747], ['id', 59682]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5886569134452213, 1.1056452393934673, 1.5486044519536968, 1.9120186107481718, 2.192595013856253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.447408676147461})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3728888034820557})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3866777420043945})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4368633031845093})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.6801531314849854})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7992836236953735})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9762929677963257})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0560855865478516})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.056581497192383})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9426040649414062})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9041790962219238})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.368457317352295})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3585822582244873})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6863, 'crossentropy': 2.054155859375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2073051929473877})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1420432329177856})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0849583148956299})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1019566059112549})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0935728549957275})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0927555561065674})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0950305461883545})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0944385528564453})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.187436819076538})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 29901], ['id', 55037], ['id', 7360], ['id', 48784], ['id', 32232]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6883234273013219, 1.2852298149512147, 1.8005658358835044, 2.21457546055207, 2.4957924414694688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.4920284748077393})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1749296188354492})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.29664945602417})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3113138675689697})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4174314737319946})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6861231327056885})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8653264045715332})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.850361943244934})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.682, 'crossentropy': 1.503073046875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2103792428970337})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0849761962890625})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0723998546600342})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0358061790466309})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0805535316467285})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0434372425079346})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0391442775726318})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 38262], ['id', 47230], ['id', 26431], ['id', 55968], ['id', 17382]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5925051000579891, 1.1446622256704075, 1.6008497788898737, 1.9644837539004918, 2.236921508586372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3988251686096191})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2317224740982056})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.280034065246582})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.724454641342163})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6401965618133545})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8471450805664062})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7305793762207031})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9184175729751587})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.954331874847412})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.492250919342041})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.684, 'crossentropy': 1.902418359375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1775493621826172})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.118808627128601})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0950230360031128})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.086136817932129})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0800762176513672})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0932376384735107})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 596], ['id', 35340], ['id', 17550], ['id', 45010], ['id', 35971]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6942750469402079, 1.2804008555067496, 1.7648405033625751, 2.159799123816045, 2.446979055058634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.5078527927398682})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.236337661743164})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.325925350189209})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.499310851097107})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8372622728347778})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6502002477645874})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8132905960083008})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.004544734954834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0186870098114014})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6769, 'crossentropy': 1.758390234375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.20034921169281})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1396305561065674})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.164604902267456})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1300675868988037})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.104529619216919})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1265323162078857})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1330879926681519})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1312892436981201})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 31662], ['id', 56414], ['id', 38494], ['id', 45750], ['id', 56435]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5812102715446239, 1.0730569146131792, 1.51261556911364, 1.8776231418381535, 2.1625813393159117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3800380229949951})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3252512216567993})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.385528564453125})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4926016330718994})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5721607208251953})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.767171859741211})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7861615419387817})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8630379438400269})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6838, 'crossentropy': 1.6723625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.26560378074646})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1629122495651245})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1202201843261719})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1378216743469238})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1015937328338623})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0847914218902588})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0984387397766113})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 19138], ['id', 46332], ['id', 37709], ['id', 47058], ['id', 13941]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6501014952748236, 1.2569240551315595, 1.767226480145406, 2.185534231943959, 2.485943279832285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4356094598770142})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1576422452926636})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2042248249053955})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3010642528533936})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.481027364730835})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.5677675008773804})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6603057384490967})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.895501732826233})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6842, 'crossentropy': 1.5643041015625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.183046579360962})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.119877815246582})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1140440702438354})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.045074701309204})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.098744511604309})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1275986433029175})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0718140602111816})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 55855], ['id', 34821], ['id', 44125], ['id', 35268], ['id', 43148]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.547867848407849, 1.0303986127972724, 1.4608415261908005, 1.8130865564282654, 2.079503028323585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3005390167236328})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0870800018310547})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2499562501907349})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2214164733886719})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4234344959259033})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.408045768737793})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.614957332611084})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6753835678100586})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.8011071681976318})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.1155295372009277})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.973991870880127})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7015, 'crossentropy': 1.7205095703125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2343077659606934})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0225350856781006})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0191702842712402})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.001727819442749})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9765573143959045})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0090036392211914})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9943408966064453})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 27238], ['id', 52387], ['id', 6029], ['id', 53985], ['id', 32930]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7256875237127458, 1.3995467862026998, 1.9625313061454772, 2.369419651324935, 2.6324851951010917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3596018552780151})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0837517976760864})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1014591455459595})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2051957845687866})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4898887872695923})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6921913623809814})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6593852043151855})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7016, 'crossentropy': 1.26745546875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1904785633087158})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1048691272735596})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9833681583404541})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.004239797592163})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9782766699790955})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.975858211517334})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 27863], ['id', 18835], ['id', 39707], ['id', 13979], ['id', 25397]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6143101624052778, 1.08311074157666, 1.4943697385893366, 1.830642716394844, 2.1039790023885523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3624956607818604})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1202657222747803})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1315457820892334})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3222882747650146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3566062450408936})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5422978401184082})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7066, 'crossentropy': 1.1346015625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1583701372146606})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0412331819534302})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.993444561958313})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9637807607650757})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.957546591758728})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 35309], ['id', 26636], ['id', 26760], ['id', 6685], ['id', 24340]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36446255971493, 0.7164399345296539, 1.0333083368165212, 1.325701074375063, 1.5850899789275523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.5257210731506348})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1651229858398438})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1199818849563599})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.213775873184204})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4053716659545898})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.457411527633667})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.6462681293487549})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.5556368827819824})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7310662269592285})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.030282497406006})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.932283878326416})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7036, 'crossentropy': 1.738954296875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2274169921875})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1044337749481201})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0898463726043701})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0450372695922852})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.079071283340454})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.079229712486267})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 5413], ['id', 25728], ['id', 7949], ['id', 15939], ['id', 45740]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6859266160463988, 1.2906816640871583, 1.816392075032435, 2.2331602869267835, 2.498643706426111]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.4967620372772217})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.143693208694458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.10783052444458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.190369963645935})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.287830114364624})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5509684085845947})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8009679317474365})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7061, 'crossentropy': 1.18707177734375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1039128303527832})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.034617304801941})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0163650512695312})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9406963586807251})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.973662257194519})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9556325078010559})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 35305], ['id', 36], ['id', 39350], ['id', 17191], ['id', 25703]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4856870497015051, 0.907771506441772, 1.2770060899152638, 1.5856988452565872, 1.8447783102353679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.4340763092041016})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1959161758422852})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1055865287780762})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0715835094451904})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2992955446243286})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.385369062423706})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.515769600868225})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.4784519672393799})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6776573657989502})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7850334644317627})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.7781774997711182})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6983, 'crossentropy': 1.60868271484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1612486839294434})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1288340091705322})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0289688110351562})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9769189357757568})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9418824911117554})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9748951196670532})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.962936520576477})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0028786659240723})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9155447483062744})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9492648243904114})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 48763], ['id', 59111], ['id', 48654], ['id', 17340], ['id', 14280]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.607966161134931, 1.155566241005518, 1.5980927966004659, 1.9551217002182373, 2.2338586908673506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.4517590999603271})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1510508060455322})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1992847919464111})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1845929622650146})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3211162090301514})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.647326946258545})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.621335744857788})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.627181887626648})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.80898118019104})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.7926201820373535})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.9969532489776611})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.096578598022461})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.946988582611084})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.715, 'crossentropy': 1.8734720703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1640920639038086})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0505168437957764})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0477344989776611})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0044770240783691})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0721368789672852})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.016011357307434})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9910417199134827})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9708300232887268})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0094705820083618})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9941054582595825})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9824557304382324})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 34620], ['id', 30337], ['id', 42243], ['id', 33445], ['id', 50403]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6173612710287696, 1.172108490180678, 1.6609194252765827, 2.057304046863293, 2.3421900592819735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.3984100818634033})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1415214538574219})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1614770889282227})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2794864177703857})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3224737644195557})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3456616401672363})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6053211688995361})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.6672024726867676})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7029, 'crossentropy': 1.3499337890625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1648499965667725})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.075984001159668})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9681153297424316})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0102686882019043})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9526280760765076})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9584144353866577})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9553588628768921})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 22069], ['id', 6000], ['id', 21333], ['id', 57976], ['id', 15300]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.534608649730411, 1.0095394757950062, 1.392343087154412, 1.7203418600803193, 1.977593043777489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.380828857421875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0851564407348633})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1766983270645142})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1630699634552002})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2557342052459717})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.359938144683838})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4038245677947998})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.513580560684204})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7180070877075195})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7026, 'crossentropy': 1.44022236328125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1561219692230225})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0575605630874634})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.024897813796997})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9846245050430298})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0024259090423584})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9954520463943481})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9737957119941711})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.014735460281372})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 43510], ['id', 28414], ['id', 59953], ['id', 31933], ['id', 47656]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6100122252590192, 1.181311856840316, 1.6425520676981105, 2.0019767329629943, 2.263278329319773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.3606886863708496})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.136549472808838})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0362317562103271})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0578280687332153})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2591378688812256})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.207668423652649})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3016808032989502})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5116641521453857})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5623700618743896})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6277140378952026})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5717887878417969})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.8220329284667969})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.7984850406646729})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.7200207710266113})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.9461758136749268})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2220797538757324})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.884044885635376})
store['active_learning_steps'][34]['training']['best_epoch']=14
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7155, 'crossentropy': 1.8489888671875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1665019989013672})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1171313524246216})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0257112979888916})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0516669750213623})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0138955116271973})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0494327545166016})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0177359580993652})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0425995588302612})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0032252073287964})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.0154714584350586})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0426793098449707})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49603], ['id', 46039], ['id', 40225], ['id', 46610], ['id', 23771]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6898188871939193, 1.3335767528471854, 1.8852945874549856, 2.2984566529981016, 2.6083302330376483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.4027020931243896})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1485333442687988})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0447731018066406})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.156738042831421})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.1955199241638184})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3470840454101562})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.393244743347168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.5431443452835083})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7166, 'crossentropy': 1.22365703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0735423564910889})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0253784656524658})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9660587310791016})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.933887243270874})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9137628078460693})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8988066911697388})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8774144053459167})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 1882], ['id', 40160], ['id', 11562], ['id', 44192], ['id', 26279]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4983289496095382, 0.9363063044242965, 1.3257927457756429, 1.6385625420811616, 1.8844748771080049]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.3996634483337402})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0677886009216309})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0293660163879395})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.140650987625122})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.2447326183319092})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.2807557582855225})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4446239471435547})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.633546233177185})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.7988777160644531})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7137, 'crossentropy': 1.3635271484375}
