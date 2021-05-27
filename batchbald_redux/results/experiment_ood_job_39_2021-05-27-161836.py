store = {}
store['timestamp']=1622128716
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=39']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
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
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.3251404762268066})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.781033515930176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.3349599838256836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3077425956726074})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4663021564483643})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.389097213745117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.4688825607299805})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4547536373138428})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.301854133605957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3099570274353027})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.9542675018310547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.421673536300659})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6221, 'crossentropy': 3.558486328125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3442827463150024})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.313856601715088})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4378559589385986})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3217558860778809})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2974052429199219})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3372184038162231})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4146329164505005})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3878223896026611})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3561255931854248})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3611888885498047})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4080336093902588})
store['active_learning_steps'][0]['eval_training']['best_epoch']=9
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 42059], ['ood', 42365], ['ood', 7168], ['id', 54832], ['id', 6400]], 'labels': [-1, -1, -1, 2, 0], 'scores': [1.2560300445203798, 2.1783707225405866, 2.8489362492228008, 3.1921315550074745, 3.3550010019280423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9608612060546875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7865004539489746})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6753339767456055})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0810999870300293})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8970069885253906})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1310296058654785})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.302759885787964})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6267, 'crossentropy': 3.26111015625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4571785926818848})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4683818817138672})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4078800678253174})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4131077527999878})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4639918804168701})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5753288269042969})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 26778], ['id', 18213], ['ood', 51589], ['id', 51418], ['id', 52168]], 'labels': [-1, 8, -1, 2, 9], 'scores': [1.1293556830402607, 1.9789961820440052, 2.5119376726139064, 2.8248152410883653, 2.984720622435945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.47255277633667})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.22786808013916})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.1009364128112793})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.622159957885742})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.574284076690674})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.8531651496887207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.7037787437438965})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.5021309852600098})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 4.360004425048828})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6981687545776367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.047860145568848})
store['active_learning_steps'][2]['training']['best_epoch']=8
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6297, 'crossentropy': 3.69307421875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3802436590194702})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4716824293136597})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4272819757461548})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3607025146484375})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.5106184482574463})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4013086557388306})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.424963355064392})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 24254], ['ood', 16430], ['ood', 31198], ['id', 52567], ['id', 719]], 'labels': [-1, -1, -1, 0, 9], 'scores': [1.1440529113472644, 2.1463643107512236, 2.725454724135191, 2.9983316805763103, 3.1130205942160174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.5228464603424072})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.0305533409118652})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6992030143737793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.7260663509368896})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.01039981842041})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 4.266529083251953})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.662773609161377})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6055, 'crossentropy': 3.7101484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.517594337463379})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5773272514343262})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6043188571929932})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5893726348876953})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.6636595726013184})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7785212993621826})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 37322], ['ood', 22774], ['ood', 14963], ['id', 59771], ['ood', 44267]], 'labels': [-1, -1, -1, 4, -1], 'scores': [1.02665584534786, 1.90458047046203, 2.513710499160891, 2.870270651934045, 3.0193950902784525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.3597252368927})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.2590558528900146})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.6740951538085938})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5941672325134277})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 3.901547431945801})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 4.0191569328308105})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.082547664642334})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5826, 'crossentropy': 4.026702734375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.384159803390503})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.548852562904358})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4540214538574219})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.7258143424987793})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 17660], ['ood', 18727], ['ood', 5689], ['id', 49035], ['id', 8168]], 'labels': [-1, -1, -1, 8, 2], 'scores': [1.1325027410076371, 2.013355239492764, 2.5488414033027107, 2.8232340886015965, 2.922368520172803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.2598633766174316})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.963991165161133})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.194802761077881})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.591487407684326})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.5342235565185547})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.080406188964844})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.575531005859375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.793331146240234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.517973899841309})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5859, 'crossentropy': 4.065396484375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.5980374813079834})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.5733495950698853})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.7077441215515137})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.6022238731384277})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.6544057130813599})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.6315882205963135})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.6544015407562256})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.745978593826294})
store['active_learning_steps'][5]['eval_training']['best_epoch']=7
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 33832], ['ood', 18551], ['ood', 53578], ['ood', 47260], ['ood', 11737]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.129564650101525, 1.9703380423985366, 2.586622191953288, 2.943276480841262, 3.1102589487406105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 2.33066463470459})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.8793392181396484})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.4042868614196777})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.172468662261963})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6407759189605713})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.735187530517578})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.8386354446411133})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.742012023925781})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6143, 'crossentropy': 4.024236328125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.664005994796753})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.6043177843093872})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.7226240634918213})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.668886661529541})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.792424201965332})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.690706491470337})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8448383808135986})
store['active_learning_steps'][6]['eval_training']['best_epoch']=6
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 30188], ['ood', 24589], ['ood', 21356], ['id', 12632], ['id', 57865]], 'labels': [-1, -1, -1, 5, 4], 'scores': [1.2228362419586891, 2.1694651678463184, 2.706897341860085, 2.9695975732538953, 3.1027689984752405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.9088599681854248})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.838275194168091})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.960371971130371})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.3183324337005615})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6361, 'crossentropy': 1.931045703125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2673888206481934})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2376958131790161})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2208356857299805})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 39168], ['ood', 54650], ['ood', 11074], ['id', 20501], ['id', 23855]], 'labels': [-1, -1, -1, 8, 3], 'scores': [1.0060176132944227, 1.6449835521721683, 2.1506930505801876, 2.508429308650177, 2.724228406967786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.1592822074890137})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.693694591522217})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.476470470428467})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.848376750946045})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.868659496307373})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.8926570415496826})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.585427284240723})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.785707473754883})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6055, 'crossentropy': 3.887583203125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.5315041542053223})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5200939178466797})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.5788586139678955})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.5753233432769775})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.6380645036697388})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 47164], ['ood', 42379], ['ood', 34488], ['id', 21152], ['ood', 32459]], 'labels': [9, -1, -1, 8, -1], 'scores': [1.0193116910254694, 1.8669536183473037, 2.466799834094044, 2.802471491411699, 2.94245187710636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.0165319442749023})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.9868035316467285})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.3291964530944824})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.7215962409973145})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.7284326553344727})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.045205116271973})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5942, 'crossentropy': 3.43131015625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.4745001792907715})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4801383018493652})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.5212769508361816})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.5416176319122314})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5642695426940918})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 36189], ['ood', 40851], ['id', 38991], ['ood', 37507], ['id', 1621]], 'labels': [-1, -1, 0, -1, 7], 'scores': [0.9879871163227378, 1.77069971922058, 2.311603158738464, 2.5691172471412607, 2.7100774412884467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.7570202350616455})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.381338119506836})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9096295833587646})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2011964321136475})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.546964168548584})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6068, 'crossentropy': 2.537933203125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3928940296173096})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.375972032546997})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4050233364105225})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.423308253288269})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 15862], ['ood', 39668], ['id', 54465], ['id', 32771], ['id', 2324]], 'labels': [-1, -1, 8, 3, 9], 'scores': [0.8928719260733124, 1.550119864715609, 2.065979980822539, 2.4323779633388876, 2.62689479144037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.8635220527648926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.576425790786743})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.829246759414673})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.042532205581665})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.2651755809783936})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 2.464250390625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3018282651901245})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2923269271850586})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2636749744415283})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.271608829498291})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 18643], ['ood', 57641], ['ood', 30983], ['id', 26407], ['id', 55422]], 'labels': [-1, -1, -1, 5, 5], 'scores': [0.9111981193178442, 1.6181850147083559, 2.1076520352429675, 2.4105224944863295, 2.5774642301919464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.8792407512664795})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.4082016944885254})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.5503621101379395})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2732629776000977})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.163778305053711})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.099393844604492})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6104, 'crossentropy': 2.7733712890625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3293795585632324})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3215043544769287})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4029349088668823})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3039218187332153})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3664058446884155})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 19373], ['ood', 29529], ['ood', 19941], ['ood', 3752], ['id', 22613]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0493772135632269, 1.915421576937856, 2.4663687286977467, 2.738139672983552, 2.892594023098896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.7761156558990479})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.257934093475342})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.2455077171325684})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.073734998703003})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3011531829833984})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.776132106781006})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.5971333980560303})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6188, 'crossentropy': 3.35159296875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.475717306137085})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4532074928283691})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5330936908721924})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5723943710327148})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5471034049987793})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.526235818862915})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 52218], ['ood', 9168], ['ood', 28905], ['ood', 2771], ['id', 48303]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0512987265208893, 1.9303492790617787, 2.4934717112451077, 2.834261961171453, 2.996985887726005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.769101858139038})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.5580508708953857})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9006404876708984})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.933863639831543})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.6888725757598877})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.7570314407348633})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 4.102713584899902})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6122, 'crossentropy': 3.210773046875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3671694993972778})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3644404411315918})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4703869819641113})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5326871871948242})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4395928382873535})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4116814136505127})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 54527], ['ood', 41063], ['ood', 55123], ['id', 29088], ['id', 26616]], 'labels': [-1, -1, -1, 8, 4], 'scores': [0.983639280853194, 1.8169430994444644, 2.3478329752874725, 2.668412162128984, 2.831116465954757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6349292993545532})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.1435670852661133})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.468435764312744})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.3633952140808105})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8207736015319824})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.936561346054077})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2818117141723633})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6454, 'crossentropy': 2.7041337890625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3389225006103516})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3487200736999512})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2711379528045654})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.284733772277832})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3297960758209229})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3327817916870117})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 31135], ['ood', 25107], ['ood', 5041], ['ood', 14121], ['ood', 24595]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.06931849700101, 1.9012969866744673, 2.4833688710402777, 2.832884241544847, 2.9781669707139358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.762817621231079})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.389827251434326})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.709904670715332})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1002767086029053})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.3587327003479004})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6133, 'crossentropy': 2.500416015625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2800772190093994})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.230149269104004})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.196251392364502})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2700055837631226})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 30355], ['ood', 39103], ['ood', 26985], ['ood', 30698], ['id', 12168]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0785383842806249, 1.7489413189425367, 2.2002607064395945, 2.515943815895395, 2.7420705147466506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.5342843532562256})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.165039300918579})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.373408317565918})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8361520767211914})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8594303131103516})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1413896083831787})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.017596483230591})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8737635612487793})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.5403738021850586})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.157400608062744})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.5042781829833984})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6415, 'crossentropy': 3.1709814453125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4151453971862793})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.40800940990448})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3692035675048828})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3603928089141846})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3817204236984253})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3688435554504395})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3437669277191162})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 33141], ['ood', 9355], ['ood', 12184], ['ood', 41516], ['id', 22649]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0942910639929058, 1.894465703371906, 2.4474248614779617, 2.7442086021655783, 2.8878965051769256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.572596788406372})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.9598033428192139})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2553908824920654})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6988301277160645})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6423, 'crossentropy': 1.580254296875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.195659875869751})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1079628467559814})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1377894878387451})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 34610], ['ood', 47781], ['ood', 1541], ['ood', 49286], ['id', 39840]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.7483112936411878, 1.338844528339835, 1.8386839354990325, 2.1422467024770615, 2.3713086888702914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.7982780933380127})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.137784004211426})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2815771102905273})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.4921231269836426})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7729296684265137})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0504684448242188})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6429, 'crossentropy': 2.48703984375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1942497491836548})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1472234725952148})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2198736667633057})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1624207496643066})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1221094131469727})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 22203], ['ood', 2350], ['ood', 50801], ['ood', 52494], ['id', 26132]], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.9772416347180855, 1.7253827862491251, 2.242818471831888, 2.477009529568047, 2.575704121328882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4356070756912231})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.7867544889450073})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2855167388916016})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4921932220458984})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6466798782348633})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6306, 'crossentropy': 1.91021640625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1939011812210083})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1430339813232422})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1228488683700562})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.162184476852417})
store['active_learning_steps'][20]['eval_training']['best_epoch']=1
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 18573], ['ood', 45758], ['ood', 26444], ['id', 59671], ['ood', 4066]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.0297343448592922, 1.778418341979302, 2.315860582602941, 2.6590689042504616, 2.85668693394536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4424233436584473})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.9560678005218506})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1702041625976562})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.3597259521484375})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3121676445007324})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6435, 'crossentropy': 1.9873115234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2001371383666992})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.154273271560669})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0829012393951416})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0706751346588135})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 32504], ['ood', 21505], ['ood', 45536], ['id', 19771], ['ood', 46247]], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.9714573556333173, 1.733624987133533, 2.2379787627488046, 2.591924536788075, 2.8002058161516024]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.330212950706482})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6934428215026855})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.170164108276367})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2170565128326416})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2616515159606934})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6547, 'crossentropy': 1.8140896484375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.159328579902649})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1801066398620605})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.080437183380127})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1287262439727783})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 27185], ['ood', 25142], ['ood', 54397], ['ood', 21426], ['ood', 47834]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0828494843155019, 1.8169570636161696, 2.3106627355182514, 2.582618025225983, 2.7353669190940177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.492591142654419})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9645040035247803})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.3921031951904297})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.4137182235717773})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5424985885620117})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.833733558654785})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.8463478088378906})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.160153865814209})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.126993179321289})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.400686264038086})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.647, 'crossentropy': 2.8629734375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3299649953842163})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.448604702949524})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.378114938735962})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.438166618347168})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4028031826019287})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.345739722251892})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2722058296203613})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2778494358062744})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.330338716506958})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 1948], ['ood', 5129], ['ood', 43042], ['ood', 44487], ['id', 22127]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1443582162477546, 2.0682942118075625, 2.650305941186879, 2.9286527440465013, 3.070273342166278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5084155797958374})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.840799331665039})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.1753339767456055})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4841504096984863})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.79183292388916})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6548337936401367})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.78324556350708})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9913220405578613})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.3420071601867676})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6479, 'crossentropy': 2.95034296875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2769267559051514})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3088308572769165})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.24541437625885})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2590140104293823})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.244633674621582})
store['active_learning_steps'][24]['eval_training']['best_epoch']=2
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 14320], ['ood', 31806], ['ood', 18687], ['id', 587], ['id', 41153]], 'labels': [-1, -1, -1, 8, 0], 'scores': [1.0972597763823597, 1.8831745716882775, 2.408571988585816, 2.6816161164031618, 2.81344168897059]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3849210739135742})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.774993658065796})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.0492472648620605})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.387333631515503})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.497889518737793})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.912761926651001})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.7992899417877197})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.033801794052124})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6496, 'crossentropy': 2.764199609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2422813177108765})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3765439987182617})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.314414381980896})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.235867977142334})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4126811027526855})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3331702947616577})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4050202369689941})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 47385], ['ood', 19040], ['ood', 43818], ['ood', 46469], ['id', 54212]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.9949958757008746, 1.8796489463389063, 2.4607634338868785, 2.7466184420408295, 2.876273606998584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4369828701019287})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.103243589401245})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.324298858642578})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5925350189208984})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.8338937759399414})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.8887314796447754})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.992183208465576})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.7505240440368652})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.2751247882843018})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.3361754417419434})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6457, 'crossentropy': 3.0639078125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.34326171875})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3601915836334229})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3725343942642212})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3377705812454224})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.350986361503601})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3737772703170776})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3355326652526855})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 12513], ['ood', 15404], ['ood', 3767], ['ood', 36756], ['ood', 30159]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0338089886607316, 1.9269751417195584, 2.4922361373116964, 2.8257839149309856, 2.971400766231808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4644865989685059})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.0134215354919434})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.390740394592285})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4593992233276367})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.785583972930908})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.9426403045654297})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.917512893676758})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6506, 'crossentropy': 2.60665234375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2662887573242188})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.326000690460205})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2663886547088623})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2524034976959229})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3441667556762695})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.255478024482727})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 43159], ['ood', 43104], ['ood', 5614], ['id', 54813], ['ood', 47366]], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.9976159459092263, 1.7561547762014795, 2.342136340660122, 2.6730770358348965, 2.860657706914057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.481929063796997})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.8066532611846924})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.0992584228515625})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.382931709289551})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8287620544433594})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.0249102115631104})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.08445405960083})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6519, 'crossentropy': 2.51829765625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.254666805267334})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3538780212402344})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4102386236190796})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.358837604522705})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3929429054260254})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2934246063232422})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 22155], ['ood', 54896], ['ood', 20950], ['ood', 45106], ['id', 14509]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9284417223704122, 1.6986414265987038, 2.266259294150448, 2.6263727489213764, 2.830891866991987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4435455799102783})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.6507792472839355})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0947365760803223})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.2233266830444336})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.417018413543701})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3246397972106934})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.600644826889038})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.9582533836364746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.2249703407287598})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6583, 'crossentropy': 2.63347265625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2973809242248535})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2649338245391846})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2692313194274902})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.304525375366211})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2819958925247192})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.377771019935608})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2263624668121338})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 56463], ['ood', 42934], ['ood', 12797], ['ood', 8808], ['id', 51011]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0458294758477318, 1.864910472852519, 2.4029771712756807, 2.7362233954556183, 2.897624487580729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3122851848602295})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8922531604766846})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.0486373901367188})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.5061073303222656})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.7394633293151855})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.928478479385376})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6632, 'crossentropy': 2.1257546875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2519183158874512})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2008811235427856})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1285401582717896})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2038874626159668})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1556748151779175})
store['active_learning_steps'][30]['eval_training']['best_epoch']=2
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 58488], ['ood', 39855], ['ood', 8833], ['ood', 48102], ['id', 31587]], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.892205334348501, 1.6238149760921523, 2.1797294683792057, 2.5435117694724676, 2.7169688887287027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4025013446807861})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8909944295883179})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.1022794246673584})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.3159549236297607})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.451751232147217})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.7530035972595215})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6577, 'crossentropy': 2.1361248046875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2338321208953857})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1679694652557373})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1335159540176392})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1772934198379517})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1643869876861572})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 39143], ['ood', 24179], ['id', 7019], ['ood', 27447], ['ood', 6256]], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.9066823937570969, 1.6274272700885803, 2.1319894713383296, 2.4475037903301073, 2.6453742903179815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3424875736236572})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6235198974609375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.011523962020874})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.2160258293151855})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2274599075317383})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6658, 'crossentropy': 1.6814298828125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1108578443527222})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.106384515762329})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0989620685577393})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0982189178466797})
store['active_learning_steps'][32]['eval_training']['best_epoch']=1
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 27340], ['ood', 39855], ['ood', 3292], ['id', 41608], ['id', 26210]], 'labels': [-1, -1, -1, 5, 3], 'scores': [0.8344957380695093, 1.5146439525572695, 2.040998048961314, 2.452860620019093, 2.628687912010257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3464510440826416})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5869953632354736})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.9987751245498657})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1806132793426514})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5122666358947754})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.664, 'crossentropy': 1.5753341796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1256840229034424})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1073169708251953})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1091407537460327})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.022485613822937})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 11484], ['ood', 35373], ['ood', 27293], ['ood', 25882], ['ood', 59615]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9259568070622128, 1.6645649692505127, 2.1524016005877415, 2.441042926320371, 2.6005426739223765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.337275505065918})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6161271333694458})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0588035583496094})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4556236267089844})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5121564865112305})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.660351514816284})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.716231346130371})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.6961264610290527})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6555, 'crossentropy': 2.5895109375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1766666173934937})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1884922981262207})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3604531288146973})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.249258041381836})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1907212734222412})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3232636451721191})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.177422285079956})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 31133], ['ood', 53543], ['ood', 46157], ['ood', 53358], ['id', 57599]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.110351161833278, 1.9883452244464368, 2.533306762178249, 2.810498824749179, 2.9371888757954396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3964569568634033})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6901659965515137})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.208608627319336})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.49520206451416})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.1692283153533936})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.5216963291168213})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.1907076835632324})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.854083299636841})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.0273280143737793})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6616, 'crossentropy': 2.70231328125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3135948181152344})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2384707927703857})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3271615505218506})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3817965984344482})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.339877724647522})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4031076431274414})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3039617538452148})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.369093894958496})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 54408], ['ood', 4256], ['id', 35232], ['ood', 13760], ['ood', 24979]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.0226720587364815, 1.794242234800671, 2.3353240259051766, 2.6592824316402766, 2.828239389980711]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3483619689941406})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.5893685817718506})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9747734069824219})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.2778985500335693})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.276817798614502})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.38808536529541})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0840747356414795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6636204719543457})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6665, 'crossentropy': 2.4769359375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1701326370239258})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1447499990463257})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1922688484191895})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.128760576248169})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.149229645729065})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1296260356903076})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.200974941253662})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 56702], ['ood', 49], ['ood', 35808], ['ood', 55479], ['ood', 22123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0067232694906505, 1.8314751211980225, 2.4624154668887233, 2.8361227912320004, 3.0196824750771842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3439159393310547})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.63154137134552})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.9344314336776733})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.2904505729675293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.650449275970459})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.2891886234283447})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.664, 'crossentropy': 1.8759591796875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.132961392402649})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1050176620483398})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.135464072227478})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1312317848205566})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.117727518081665})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 57314], ['ood', 49670], ['ood', 37445], ['id', 31456], ['id', 23653]], 'labels': [-1, -1, -1, 7, 5], 'scores': [0.9432636364715681, 1.6869520688826447, 2.2344791727496043, 2.53569520128635, 2.7460060717164163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.282006025314331})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6786389350891113})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.097400426864624})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.1030759811401367})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.168943405151367})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.5940375328063965})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.551548480987549})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.6839070320129395})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4999613761901855})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.047004222869873})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 3.0440855026245117})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.812441825866699})
store['active_learning_steps'][38]['training']['best_epoch']=9
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6722, 'crossentropy': 2.680256640625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2508565187454224})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1474303007125854})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.168933391571045})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.193986415863037})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2067711353302002})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1708134412765503})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 8622], ['ood', 49602], ['ood', 45209], ['ood', 5313], ['ood', 11436]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0029003540126293, 1.8344538875003638, 2.4009857427308905, 2.751520408159334, 2.9403217090632987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2287452220916748})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6732568740844727})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.7879277467727661})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.02408766746521})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.0117416381835938})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.3312149047851562})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5706522464752197})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.677, 'crossentropy': 2.00365703125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1089075803756714})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1003402471542358})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0352659225463867})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0787451267242432})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0952630043029785})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.078934907913208})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 27026], ['ood', 2535], ['ood', 40969], ['ood', 29132], ['ood', 43043]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8682272720224148, 1.6030410648363254, 2.1819993042355295, 2.53758349392798, 2.7534975203131413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2690941095352173})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6170322895050049})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7665839195251465})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9427604675292969})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.2267534732818604})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.4089646339416504})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6831, 'crossentropy': 1.8634625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1462695598602295})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1273066997528076})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0555994510650635})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1103034019470215})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0619544982910156})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 22323], ['id', 1254], ['ood', 59590], ['ood', 6029], ['ood', 46716]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.9818053998808904, 1.7533660190984324, 2.239296458838103, 2.5284673581942156, 2.706858032591416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.285522222518921})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5198824405670166})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8834176063537598})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.345994710922241})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.33064603805542})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.314120292663574})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6887, 'crossentropy': 1.798063671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0934066772460938})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.049163818359375})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9852613210678101})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0103161334991455})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.015453577041626})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 20663], ['ood', 44998], ['ood', 55378], ['ood', 37501], ['ood', 32453]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9011277306097247, 1.616094132775804, 2.189614512746866, 2.565307949778483, 2.7443677982237684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2943410873413086})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4938534498214722})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8847155570983887})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.030932903289795})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3640432357788086})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6719, 'crossentropy': 1.53861650390625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1784863471984863})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0476131439208984})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0317586660385132})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0355390310287476})
store['active_learning_steps'][42]['eval_training']['best_epoch']=3
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 5365], ['ood', 2831], ['ood', 30214], ['id', 35913], ['ood', 49950]], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.8621253466718397, 1.544108930466733, 2.0895705923012606, 2.39982893475415, 2.5987603220389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2113587856292725})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5958311557769775})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9104782342910767})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0716497898101807})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1716275215148926})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.5159571170806885})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.332864284515381})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4343769550323486})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6833, 'crossentropy': 2.2332162109375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1972169876098633})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1209020614624023})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1243234872817993})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1427185535430908})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1392807960510254})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0880091190338135})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0838127136230469})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 46903], ['ood', 12784], ['ood', 54883], ['id', 32982], ['ood', 37538]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.0536636719875005, 1.828547613775633, 2.381615098412245, 2.6595005486427326, 2.8065500770344727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2469391822814941})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5892350673675537})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8005707263946533})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8649530410766602})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.4114973545074463})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.5379271507263184})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.661406993865967})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6783, 'crossentropy': 2.0829865234375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1453460454940796})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0786571502685547})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1047430038452148})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1011321544647217})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0761981010437012})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.095068097114563})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 3638], ['ood', 58438], ['ood', 45456], ['ood', 27431], ['id', 16297]], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.9481457749786593, 1.692790840481773, 2.291617185206505, 2.5989012504882245, 2.7418828416686267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.320582628250122})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8053293228149414})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8385021686553955})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.21014404296875})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.1795578002929688})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.7091548442840576})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.0602786540985107})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6548, 'crossentropy': 2.3561181640625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1337594985961914})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1024177074432373})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1477904319763184})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.224381685256958})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1932518482208252})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1570839881896973})
store['active_learning_steps'][45]['eval_training']['best_epoch']=5
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 30349], ['ood', 37442], ['ood', 24145], ['ood', 17241], ['ood', 12934]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9701881159502892, 1.732897584758338, 2.3326285840592007, 2.654591659388177, 2.813041521886136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2804651260375977})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.6457089185714722})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8218586444854736})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.285947322845459})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.6369051933288574})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.4955596923828125})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6678, 'crossentropy': 1.86838828125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1462924480438232})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0946557521820068})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1525263786315918})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1704649925231934})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1123552322387695})
store['active_learning_steps'][46]['eval_training']['best_epoch']=4
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 47761], ['ood', 47422], ['ood', 52708], ['ood', 54883], ['ood', 27799]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9214603161299599, 1.642348965789501, 2.1376050275053826, 2.428966017821921, 2.6073162714123743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.262089729309082})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.6419122219085693})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.7069802284240723})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.159170627593994})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.0975098609924316})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6752, 'crossentropy': 1.60812822265625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1197755336761475})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1313974857330322})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0323517322540283})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.056523084640503})
store['active_learning_steps'][47]['eval_training']['best_epoch']=4
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 1309], ['ood', 10192], ['ood', 16007], ['ood', 14749], ['ood', 38300]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8657146836528087, 1.544895167466919, 2.0795503250784755, 2.4514249220840965, 2.67603433167975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2913212776184082})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5882906913757324})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7986418008804321})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.024529457092285})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.217421054840088})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.50757098197937})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6714, 'crossentropy': 1.9280546875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0947368144989014})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0591728687286377})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0529152154922485})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.032594919204712})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0115606784820557})
store['active_learning_steps'][48]['eval_training']['best_epoch']=3
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 21134], ['ood', 20418], ['ood', 50689], ['ood', 18098], ['ood', 42133]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8707922299377224, 1.616315433954001, 2.087479409873561, 2.3597314648987187, 2.506673233572151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2565114498138428})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.766506552696228})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9458568096160889})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.1299004554748535})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.3648107051849365})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.576920509338379})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.5418901443481445})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6765, 'crossentropy': 2.211794921875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0839265584945679})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.137009859085083})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1030409336090088})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0752973556518555})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.053871512413025})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0675699710845947})
store['active_learning_steps'][49]['eval_training']['best_epoch']=5
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 54257], ['ood', 50619], ['ood', 26252], ['ood', 24940], ['ood', 57669]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0803234425220842, 1.9353357406412885, 2.505565285457108, 2.8803569376082168, 3.029885318846632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2847511768341064})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6270761489868164})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7607195377349854})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.152060031890869})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6076278686523438})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.230989456176758})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.626692295074463})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.860004186630249})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.776883363723755})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6822, 'crossentropy': 2.27812421875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.135551929473877})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0638132095336914})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0785908699035645})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0796000957489014})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.078381896018982})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0632312297821045})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0868780612945557})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.077641487121582})
store['active_learning_steps'][50]['eval_training']['best_epoch']=8
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 8669], ['ood', 49190], ['ood', 47143], ['ood', 40249], ['ood', 16690]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0249845487616274, 1.9187088464872408, 2.4676152453368987, 2.7646467099257936, 2.8997307419945706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1817612648010254})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5367300510406494})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.948488473892212})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.130662202835083})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6501, 'crossentropy': 1.22023984375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0930912494659424})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0640488862991333})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0274505615234375})
store['active_learning_steps'][51]['eval_training']['best_epoch']=2
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 37103], ['id', 27090], ['ood', 42681], ['ood', 2365], ['id', 13598]], 'labels': [-1, 8, -1, -1, 3], 'scores': [0.5742497948934338, 1.053822878124977, 1.4148695936968165, 1.7200239474114678, 1.9582170856380152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2825202941894531})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5094144344329834})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.790013074874878})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3724923133850098})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.230607271194458})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5011134147644043})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6715, 'crossentropy': 1.81903046875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1261513233184814})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0444653034210205})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0311379432678223})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0605123043060303})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0438607931137085})
store['active_learning_steps'][52]['eval_training']['best_epoch']=5
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 10787], ['ood', 20294], ['ood', 19320], ['ood', 12522], ['ood', 33169]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8349454488254098, 1.4811207641661106, 1.9695455914891626, 2.262812646185413, 2.417559906457128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.282218337059021})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3918678760528564})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.7778005599975586})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2587647438049316})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.192842960357666})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6596, 'crossentropy': 1.49035439453125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0855215787887573})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0660303831100464})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0100749731063843})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0382637977600098})
store['active_learning_steps'][53]['eval_training']['best_epoch']=3
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 56083], ['ood', 56551], ['ood', 58872], ['ood', 45082], ['ood', 1185]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7721066647372634, 1.3705031395447644, 1.8280775041215644, 2.1772337021460784, 2.398145446069903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3589763641357422})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5152897834777832})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.782871127128601})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.138038396835327})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.3432273864746094})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.719332695007324})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6673, 'crossentropy': 1.8757412109375}
