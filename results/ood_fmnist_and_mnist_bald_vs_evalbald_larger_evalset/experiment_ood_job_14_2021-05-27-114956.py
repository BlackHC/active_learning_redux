store = {}
store['timestamp']=1622112596
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=14']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=80
store['config']={'seed': 1248, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6456799507141113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6113224029541016})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.609628677368164})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.810276985168457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.19087553024292})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9848976135253906})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6759, 'crossentropy': 2.4325560546875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 33126], ['id', 1985], ['id', 22845], ['id', 16751], ['id', 10308]], 'labels': [9, 6, 5, 9, 2], 'scores': [1.2108496241505846, 2.2589463029876944, 3.0981435721852826, 3.6651720023819294, 4.029422538325905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4005308151245117})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.721266746520996})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7194337844848633})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6547045707702637})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.7584266662597656})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.932232141494751})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3552279472351074})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2635035514831543})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6866, 'crossentropy': 2.37564140625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 5173], ['id', 2748], ['id', 19298], ['id', 29591], ['id', 38589]], 'labels': [3, 2, 6, 9, 8], 'scores': [1.228571006085318, 2.274271120531563, 3.108771498022275, 3.7057998343086638, 4.085236145823677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.05129075050354})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.3332366943359375})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4514105319976807})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.439026355743408})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.8035013675689697})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.500471830368042})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.7214174270629883})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.5596518516540527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.8560805320739746})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.800139904022217})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.036050319671631})
store['active_learning_steps'][2]['training']['best_epoch']=8
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7308, 'crossentropy': 2.257450390625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1311], ['id', 20481], ['id', 14817], ['id', 55545], ['id', 52574]], 'labels': [5, 0, 0, 2, 2], 'scores': [1.358979019592829, 2.5909693402774447, 3.4785841724850792, 4.017040371259574, 4.310076627043209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.132493019104004})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.751408338546753})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9285430908203125})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.9915075302124023})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6633, 'crossentropy': 2.0418498046875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 41426], ['id', 4549], ['id', 20079], ['id', 38615], ['id', 13073]], 'labels': [4, 4, 8, 7, 4], 'scores': [1.0370998837921048, 1.9421072334680387, 2.7235985799097753, 3.2784378370955505, 3.683963938105668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.5507440567016602})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7061662673950195})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9683599472045898})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.0074124336242676})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6973812580108643})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.147362232208252})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.39054536819458})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 2.0059614181518555})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.1855766773223877})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.2916297912597656})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.3249659538269043})
store['active_learning_steps'][4]['training']['best_epoch']=8
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.801, 'crossentropy': 1.697883203125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34800], ['id', 41613], ['id', 31046], ['id', 51544], ['id', 11643]], 'labels': [5, 9, 6, 1, 5], 'scores': [1.2345606307846475, 2.3434854669002494, 3.254736152611189, 3.862477450606537, 4.211975032435701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3548243045806885})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.5218372344970703})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.6996617317199707})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7935577630996704})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.8251502513885498})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 2.0106990337371826})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 2.101893186569214})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.113823652267456})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 2.1411914825439453})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7943, 'crossentropy': 1.79747421875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 46996], ['id', 59726], ['id', 12688], ['id', 29453], ['id', 14825]], 'labels': [5, 5, 5, 2, 3], 'scores': [1.2593088809462967, 2.374984704172457, 3.306701773021789, 3.8690876875476627, 4.212490539603316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.242915391921997})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4490458965301514})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.7104549407958984})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.4536433219909668})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.7345659732818604})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8022570610046387})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9246282577514648})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8124, 'crossentropy': 1.35533134765625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 57474], ['id', 7033], ['id', 59314], ['id', 16916], ['id', 37034]], 'labels': [3, 7, 9, 2, 7], 'scores': [1.1137699370005978, 2.108652913339815, 2.951818056483905, 3.5891767795511393, 4.021868745025679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4176584482192993})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.4164369106292725})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.8275288343429565})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8135178089141846})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.8800084590911865})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.9402095079421997})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7224029302597046})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.0353899002075195})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.8631477355957031})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 2.0913209915161133})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.337888240814209})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 2.204880714416504})
store['active_learning_steps'][7]['training']['best_epoch']=9
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8073, 'crossentropy': 1.8294662109375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 22943], ['id', 57736], ['id', 26570], ['id', 14623], ['id', 17079]], 'labels': [3, 8, 5, 5, 6], 'scores': [1.3323161780348542, 2.5120222340771576, 3.438732708225084, 4.024970570220637, 4.3355860077531725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.357530117034912})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.5205717086791992})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.7321321964263916})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.5621098279953003})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.5699771642684937})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.8754005432128906})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.771127462387085})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9869143962860107})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8183, 'crossentropy': 1.32114951171875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 16209], ['id', 20820], ['id', 4784], ['id', 57232], ['id', 30646]], 'labels': [2, 9, 7, 5, 9], 'scores': [1.2021976297877044, 2.2834312045971403, 3.1399266170386966, 3.7464056654854225, 4.138055929869509]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2778666019439697})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.3449070453643799})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.4568730592727661})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.568669080734253})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.754500389099121})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.0049824714660645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.7620078325271606})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7913, 'crossentropy': 1.44103623046875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 12345], ['id', 49658], ['id', 40457], ['id', 18398], ['id', 9472]], 'labels': [3, 5, 0, 4, 2], 'scores': [1.1249585460891984, 2.1456811440739183, 2.968933625899438, 3.59260199357439, 3.9897612601659533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.279067039489746})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.3729788064956665})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.5792709589004517})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.7810006141662598})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6289491653442383})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.765988826751709})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.077364683151245})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6523520946502686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.8582606315612793})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8289380073547363})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.8260700702667236})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8419184684753418})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.279735565185547})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.030257225036621})
store['active_learning_steps'][10]['training']['best_epoch']=11
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7952, 'crossentropy': 1.7227228515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 50802], ['id', 1772], ['id', 15579], ['id', 14852], ['id', 28657]], 'labels': [2, 7, 5, 2, 5], 'scores': [1.3118775733998977, 2.4347868511326, 3.355899615181313, 3.9564618029939265, 4.280345760656845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.1587464809417725})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.3678739070892334})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3265371322631836})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.4456565380096436})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.5750141143798828})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6784230470657349})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.7468035221099854})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.563482642173767})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.6741461753845215})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7076696157455444})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5919976234436035})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.9387519359588623})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.8419945240020752})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7959716320037842})
store['active_learning_steps'][11]['training']['best_epoch']=11
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8037, 'crossentropy': 1.44753974609375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 50090], ['id', 7168], ['id', 21880], ['id', 46348], ['id', 23104]], 'labels': [4, 8, 2, 8, 0], 'scores': [1.1902880624763452, 2.2662131004671604, 3.105290390454817, 3.717626840860393, 4.112424378558083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2766411304473877})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4619208574295044})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3890354633331299})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5602846145629883})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.832798957824707})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.0881552696228027})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7861, 'crossentropy': 1.346242578125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 6375], ['id', 25309], ['id', 25644], ['id', 43833], ['id', 18003]], 'labels': [7, 2, 4, 3, 2], 'scores': [1.0161175208788573, 1.953695829774455, 2.77909964626466, 3.396491955363472, 3.8522022427262144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0559518337249756})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0619179010391235})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0611305236816406})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3857619762420654})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.396990418434143})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3147014379501343})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8248, 'crossentropy': 1.05841328125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 12748], ['id', 43648], ['id', 49537], ['id', 966], ['id', 46329]], 'labels': [0, 5, 2, 3, 3], 'scores': [1.113417986536579, 2.0468748178013483, 2.8347323173138506, 3.4418793534366454, 3.8645226302912583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.2461556196212769})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2429754734039307})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3377888202667236})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.4903301000595093})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.5153453350067139})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5373460054397583})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3621362447738647})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5524320602416992})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.4549155235290527})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5106768608093262})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.910919427871704})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.2409324645996094})
store['active_learning_steps'][14]['training']['best_epoch']=9
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8165, 'crossentropy': 1.37425048828125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 34328], ['id', 5474], ['id', 30322], ['id', 34739], ['id', 33162]], 'labels': [8, 8, 8, 9, 8], 'scores': [1.2214345167828382, 2.2786640194545535, 3.1469687027067534, 3.750213786407585, 4.1220342794111025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1587334871292114})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0129259824752808})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1558626890182495})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2582241296768188})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3064286708831787})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8193, 'crossentropy': 0.9778361328125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 52697], ['id', 39304], ['id', 57972], ['id', 40466], ['id', 17491]], 'labels': [3, 4, 4, 8, 3], 'scores': [0.9145780894487965, 1.7547080792665475, 2.4801930661383196, 3.081472117171826, 3.5526911141011546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0835727453231812})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9912781715393066})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1122705936431885})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0587952136993408})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.232062816619873})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2056056261062622})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.100356101989746})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1382157802581787})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2343233823776245})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4263050556182861})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2951395511627197})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8471, 'crossentropy': 1.10456328125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46776], ['id', 25910], ['id', 20169], ['id', 39266], ['id', 20989]], 'labels': [8, 1, 4, 8, 3], 'scores': [1.1178253574249033, 2.0998215524171058, 2.957046971376734, 3.5810153264896645, 3.997332629266303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1329810619354248})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1984859704971313})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0964500904083252})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2095398902893066})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.37041437625885})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2202818393707275})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3982956409454346})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4019775390625})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3035097122192383})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8339, 'crossentropy': 1.12855595703125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 17756], ['id', 42787], ['id', 43961], ['id', 26208], ['id', 12089]], 'labels': [8, 4, 0, 3, 3], 'scores': [1.1476671988396667, 2.153776031822711, 2.988015416582458, 3.620014374106538, 4.023067696755372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1153576374053955})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9656836986541748})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8913542032241821})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.028099775314331})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1557776927947998})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.159541368484497})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2773655652999878})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.20625638961792})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.857, 'crossentropy': 0.97736064453125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 5707], ['id', 57728], ['id', 49525], ['id', 29303], ['id', 43532]], 'labels': [2, 9, 8, 8, 8], 'scores': [1.1566396623209547, 2.1854796484855736, 3.0201350451086526, 3.666015269081173, 4.0562069349002225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0987553596496582})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8807641267776489})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9751347303390503})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.042665719985962})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1501898765563965})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2046139240264893})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8338, 'crossentropy': 0.92907373046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14760], ['id', 37574], ['id', 30188], ['id', 20119], ['id', 13714]], 'labels': [2, 5, 7, 6, 4], 'scores': [0.9766493453386085, 1.9039492592446394, 2.6642964729620484, 3.3000376169939916, 3.73511326051159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2483317852020264})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9694067239761353})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0173189640045166})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0021674633026123})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1234972476959229})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0017708539962769})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1246720552444458})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0783309936523438})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1193547248840332})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8606, 'crossentropy': 0.96428505859375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 52462], ['id', 50317], ['id', 32047], ['id', 4822], ['id', 39561]], 'labels': [9, 3, 9, 4, 2], 'scores': [1.1465715734435205, 2.2061945057568306, 3.0950708813818295, 3.7309804877333734, 4.124903010478926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.1345629692077637})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7898825407028198})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8253023624420166})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8098046779632568})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7829777002334595})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.954115629196167})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8813636302947998})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.873, 'crossentropy': 0.79277080078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 39656], ['id', 44806], ['id', 40654], ['id', 34765], ['id', 36337]], 'labels': [0, 8, 5, 6, 3], 'scores': [1.1443470235419355, 2.1055308459257436, 2.890212699040541, 3.497307464754959, 3.9115123090915755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.173377275466919})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7845070362091064})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.754449188709259})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7948676943778992})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7656193971633911})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9193887114524841})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8698511123657227})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9752044677734375})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.7211447265625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 49505], ['id', 52089], ['id', 54004], ['id', 50878], ['id', 39872]], 'labels': [6, 7, 0, 7, 8], 'scores': [1.0644698586678472, 1.9989427782187028, 2.8241195611394607, 3.468481416561783, 3.9172566234884005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.234512448310852})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8316152095794678})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7664230465888977})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7270382642745972})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8363028168678284})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8252813816070557})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.844772458076477})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.884, 'crossentropy': 0.744362646484375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 12305], ['id', 14722], ['id', 506], ['id', 13983], ['id', 53998]], 'labels': [9, 0, 6, 3, 9], 'scores': [1.076387114397152, 2.046221842021452, 2.8197581758182224, 3.440670306006627, 3.876318713324367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1196703910827637})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7797359228134155})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7943234443664551})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7763440608978271})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7914329171180725})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8154513835906982})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9538617134094238})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8780240416526794})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8576619625091553})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9306176900863647})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9735374450683594})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9405223727226257})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8943, 'crossentropy': 0.82514736328125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 2761], ['id', 7833], ['id', 37696], ['id', 16658], ['id', 45602]], 'labels': [8, 5, 2, 8, 5], 'scores': [1.1407835105584685, 2.1589378890914466, 3.010400544784435, 3.6620912986071765, 4.061506839358264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1026716232299805})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7646996974945068})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6940162181854248})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6878207325935364})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7719700932502747})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7300782203674316})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8247444033622742})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8922, 'crossentropy': 0.690310400390625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 36008], ['id', 13969], ['id', 5168], ['id', 27641], ['id', 26358]], 'labels': [8, 3, 1, 2, 3], 'scores': [1.0046930299221755, 1.9049416895149314, 2.6973726640310707, 3.3208843936570815, 3.773809209759456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.270466685295105})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6814879775047302})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6223270297050476})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6411375999450684})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6202059984207153})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6483144164085388})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7416592836380005})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7310899496078491})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.59774423828125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 20172], ['ood', 52889], ['id', 31184], ['id', 11572], ['id', 55612]], 'labels': [4, -1, 9, 5, 9], 'scores': [1.0414689171968976, 1.9812950037345134, 2.8166090746219226, 3.4447006336714683, 3.8814180842159978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1569421291351318})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6518796682357788})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6207337379455566})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5956025123596191})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6455250978469849})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6757388710975647})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6784887313842773})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.549506591796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 5684], ['id', 24424], ['id', 28152], ['id', 18150], ['id', 47322]], 'labels': [6, 1, 6, 8, 8], 'scores': [1.0838107493810356, 2.0277160869511475, 2.8427021014521223, 3.466139655894094, 3.902101771223432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0957441329956055})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7429847121238708})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5586525797843933})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5554797053337097})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6069635152816772})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.621382474899292})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6026515960693359})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.524652392578125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 34524], ['id', 53872], ['id', 44998], ['id', 31512], ['id', 48681]], 'labels': [8, 8, 4, 2, 2], 'scores': [0.9958120082136406, 1.9291685177151825, 2.7179218148876165, 3.362996618130989, 3.810107085230828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3190927505493164})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7101647853851318})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5675865411758423})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5919129848480225})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6595383882522583})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.667177677154541})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.698742151260376})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6438045501708984})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.59312841796875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 31404], ['id', 5175], ['id', 5679], ['id', 34520], ['id', 52169]], 'labels': [3, 4, 3, 6, 2], 'scores': [1.0697725187973095, 2.0200591253680105, 2.8209825802274917, 3.439779987676811, 3.8840383694488434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2483223676681519})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6106483936309814})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5952386856079102})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5685520172119141})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5332621932029724})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5590649843215942})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5913125872612})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5830861926078796})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6164580583572388})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5600579380989075})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6021072864532471})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.524584912109375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 2706], ['id', 19590], ['ood', 50736], ['id', 31349], ['id', 43212]], 'labels': [7, 5, -1, 3, 5], 'scores': [1.1519014683605326, 2.1762023447752425, 3.0860964956278343, 3.715518306195433, 4.106521635610676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1919320821762085})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6571828126907349})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5835360288619995})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5790516138076782})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5478581786155701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.534520149230957})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6711291074752808})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6587013602256775})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6949144005775452})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.555100146484375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 46412], ['id', 21636], ['id', 37469], ['id', 18598], ['id', 57311]], 'labels': [0, 2, 2, 9, 5], 'scores': [1.1336489796096227, 2.112471350265757, 2.9259431774224938, 3.5462189291426327, 3.9764503742396275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.280897617340088})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.659132719039917})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5365901589393616})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6450193524360657})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6248660087585449})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7162876725196838})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.5412328125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 16692], ['id', 59731], ['id', 5842], ['id', 40046], ['id', 17365]], 'labels': [5, 5, 1, 7, 0], 'scores': [0.8611196535421137, 1.647644949383463, 2.342461103927752, 2.9287626362429675, 3.4076895190887946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3015930652618408})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7497463226318359})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5731868743896484})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.615027666091919})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.609808087348938})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5997673273086548})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5945875644683838})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6300002336502075})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6776872873306274})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.57125810546875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 39405], ['id', 57714], ['id', 59286], ['id', 54858], ['id', 11534]], 'labels': [5, 1, 8, 3, 7], 'scores': [1.0808516268196806, 2.073182305587257, 2.911424338893582, 3.5635786058837082, 3.980151742900567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2063021659851074})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7161177396774292})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6071140766143799})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5481917858123779})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6154208183288574})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6243962049484253})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6405780911445618})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.534699658203125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49395], ['id', 19244], ['id', 57742], ['id', 34396], ['id', 7851]], 'labels': [1, 9, 6, 3, 8], 'scores': [0.9797653629375906, 1.8932875295527771, 2.694915727195572, 3.3088205602039222, 3.7496571549850195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2245252132415771})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.624435305595398})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5352253913879395})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5944047570228577})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5576965808868408})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5520517826080322})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5415842533111572})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5552103519439697})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5989292860031128})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6201922297477722})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9324, 'crossentropy': 0.5068908203125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 38920], ['id', 55244], ['id', 53280], ['id', 30173], ['id', 4820]], 'labels': [7, 7, 9, 8, 5], 'scores': [1.0421247881872988, 1.943853237210675, 2.7356479978764927, 3.3703552947611692, 3.810689931706099]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2308883666992188})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7098616361618042})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5253254175186157})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5340242981910706})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48576128482818604})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49540138244628906})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5451452732086182})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6146632432937622})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.48116259765625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 5790], ['ood', 52889], ['id', 39208], ['id', 3644], ['id', 46368]], 'labels': [2, -1, 5, 1, 8], 'scores': [1.0474962814862003, 1.9713100680065963, 2.771728384609352, 3.3901577426605876, 3.8213352282109323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.271888256072998})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6468712091445923})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5510730743408203})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5106574296951294})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4781917631626129})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4924547076225281})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5675692558288574})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5708734393119812})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5873783230781555})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.489649365234375}
