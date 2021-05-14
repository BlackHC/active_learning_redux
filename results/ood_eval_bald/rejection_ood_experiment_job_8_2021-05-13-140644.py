store = {}
store['timestamp']=1620911204
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=8']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=20
store['config']={'seed': 1246, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.2311999797821045})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5560708045959473})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9476380348205566})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.904122829437256})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 2.0965587890625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2180712223052979})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2589911222457886})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.182807445526123})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [58285, 29132, 5653, 13099, 20551, 7842, 47995, 34842, 58684, 50025], 'labels': [0, 8, 5, 3, 0, 5, 5, 8, -1, 3], 'scores': [0.9981153607368469, 0.8727053999900818, 0.8743629455566406, 0.8966121077537537, 0.9035952687263489, 0.5524323582649231, 0.8530645966529846, 0.7763258814811707, 0.5803731679916382, 0.8528953790664673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.938022494316101})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.2852346897125244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.424373149871826})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.7125539779663086})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7005, 'crossentropy': 1.8833763671875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1473954916000366})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1044964790344238})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0925087928771973})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [11627, 40904, 2000, 50202, 59446, 11668, 50528, 35582, 44716, 1108], 'labels': [4, 3, 5, 5, 5, 9, 9, 3, -1, 3], 'scores': [0.6096547245979309, 0.6539188623428345, 0.515112042427063, 0.7519267201423645, 0.7945004105567932, 0.743386447429657, 0.6702796816825867, 0.5558741688728333, 0.34309959411621094, 0.7010573744773865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9532058238983154})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.233086585998535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2755746841430664})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.53253173828125})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7121, 'crossentropy': 1.692840625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.123550534248352})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1277662515640259})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1233258247375488})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [39395, 46074, 16213, 23578, 38567, 58857, 47322, 42020, 769, 37189], 'labels': [8, 6, 5, 2, 4, 2, 8, 9, -1, 0], 'scores': [0.6475107669830322, 0.6170821785926819, 0.5438907146453857, 0.7138010263442993, 0.5182819962501526, 0.6154923439025879, 0.8813169598579407, 0.5548760294914246, 0.4586446285247803, 0.5963577628135681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6345224380493164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8264744281768799})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.7805962562561035})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.071122646331787})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7396, 'crossentropy': 1.42237646484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.12868070602417})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.0292060375213623})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.0037055015563965})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [2449, 41189, 38805, 57657, 47342, 12308, 8453, 42064, 37071, 8116], 'labels': [4, 2, 8, 9, 2, 8, 2, 7, 6, 0], 'scores': [0.4544244408607483, 0.5771857500076294, 0.42364227771759033, 0.42887020111083984, 0.6298499703407288, 0.519400954246521, 0.7847528457641602, 0.4805273413658142, 0.5077740550041199, 0.6341890096664429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5941791534423828})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.0246894359588623})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.872648000717163})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.8613686561584473})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7599, 'crossentropy': 1.324727734375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0742416381835938})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9947400093078613})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9784998893737793})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [8790, 32065, 23038, 22965, 17362, 26622, 13410, 6279, 28726, 27359], 'labels': [3, 2, 2, 8, 8, 6, 7, 0, 8, 8], 'scores': [0.46430468559265137, 0.604046106338501, 0.5226277709007263, 0.4574245810508728, 0.5542787313461304, 0.5354662537574768, 0.6004841923713684, 0.5748265981674194, 0.3776693344116211, 0.6057446002960205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4124929904937744})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.4119129180908203})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8408528566360474})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.70941162109375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.0785396099090576})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8136, 'crossentropy': 1.1971623046875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.950509786605835})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9042940139770508})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8305515050888062})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8300049304962158})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [15751, 17744, 48177, 39994, 2110, 22449, 35539, 53621, 37803, 3451], 'labels': [2, 4, 1, 8, 1, 6, 7, 6, 6, 6], 'scores': [0.601731538772583, 0.5540129542350769, 0.40302807092666626, 0.5325449705123901, 0.495652437210083, 0.5999689102172852, 0.4581335186958313, 0.6078663468360901, 0.5845186710357666, 0.6083325147628784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9865974187850952})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0920177698135376})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1134146451950073})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3374561071395874})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 0.92949619140625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8924390077590942})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8115026950836182})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.789652407169342})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [11256, 22670, 46051, 8220, 20933, 26686, 37840, 31402, 54194, 43637], 'labels': [4, 4, 3, 9, 5, 0, 4, 5, 7, 3], 'scores': [0.3360196352005005, 0.3552144765853882, 0.4399900436401367, 0.3673774003982544, 0.4139202833175659, 0.3756934404373169, 0.4470876455307007, 0.4103328585624695, 0.18194657564163208, 0.3435525894165039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.84092777967453})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.813764214515686})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8132938146591187})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9711127281188965})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.891698956489563})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9127205610275269})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8872, 'crossentropy': 0.760937109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6968486309051514})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5585027933120728})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5597096681594849})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5149732828140259})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5228519439697266})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [48374, 40555, 32026, 20334, 34919, 45490, 23792, 48638, 55721, 52294], 'labels': [5, -1, 5, -1, 0, 5, 5, 0, 0, 0], 'scores': [0.3242923617362976, 0.4415912628173828, 0.49566519260406494, 0.33422350883483887, 0.5769610404968262, 0.5152186155319214, 0.498624324798584, 0.728756844997406, 0.6000697016716003, 0.7357255816459656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7890794277191162})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6974871754646301})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7523999214172363})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8615385293960571})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8190834522247314})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.631159765625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6989554166793823})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5428135395050049})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5165461301803589})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.4900655150413513})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [32509, 40259, 44624, 31456, 602, 34678, 22755, 48042, 7704, 10446], 'labels': [8, 8, 8, 9, 8, 8, 8, -1, 8, 8], 'scores': [0.593258798122406, 0.550413966178894, 0.5106408596038818, 0.6743242740631104, 0.48541682958602905, 0.608039140701294, 0.39635205268859863, 0.1950516700744629, 0.3652723431587219, 0.5762982964515686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8847787380218506})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6824535131454468})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7018181085586548})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6957375407218933})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.776633620262146})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8913, 'crossentropy': 0.652486083984375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7662266492843628})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5723931789398193})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5820207595825195})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5581855773925781})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [25309, 17535, 16921, 13709, 35791, 57632, 40670, 18130, 46524, 50381], 'labels': [2, 0, -1, 6, 6, 2, -1, 8, 6, 2], 'scores': [0.6411572694778442, 0.6036791205406189, 0.4178592562675476, 0.4763253927230835, 0.5293543338775635, 0.6757267713546753, 0.47095584869384766, 0.5998104810714722, 0.566767692565918, 0.5727123618125916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9438345432281494})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6974035501480103})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6666043996810913})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7019448280334473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8744363188743591})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8129187822341919})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.590922021484375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7396610975265503})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5687215328216553})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4976683557033539})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4687473773956299})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4859568476676941})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [33653, 24716, 46804, 59303, 59286, 13904, 23027, 45163, 42124, 57882], 'labels': [9, 5, -1, 8, 8, 9, -1, -1, 9, 0], 'scores': [0.6462129354476929, 0.6401372849941254, 0.3971271514892578, 0.5910534858703613, 0.6155080199241638, 0.4566332697868347, 0.6048283576965332, 0.5367365479469299, 0.4469667077064514, 0.6228571534156799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8376075625419617})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6440474987030029})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6355148553848267})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7355402112007141})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9189029335975647})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6847604513168335})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.594923388671875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7426380515098572})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5764064788818359})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.4881334900856018})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.46710699796676636})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4626380205154419})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [59646, 1957, 16987, 24201, 42028, 20087, 8228, 47351, 37729, 43619], 'labels': [-1, 6, -1, -1, 1, 6, 3, -1, 3, -1], 'scores': [0.2430235743522644, 0.5719517767429352, 0.17955434322357178, 0.31153297424316406, 0.36041414737701416, 0.3810073733329773, 0.41526496410369873, 0.34212732315063477, 0.35293668508529663, 0.2557762861251831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.945834219455719})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6841995120048523})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6705383658409119})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7476586103439331})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7086802124977112})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7020027041435242})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.623322900390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7888472080230713})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5855522155761719})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.47930580377578735})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.49304258823394775})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.4862671494483948})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [56006, 31883, 10350, 38309, 14381, 52185, 4787, 45521, 22053, 43868], 'labels': [3, 4, 4, -1, 2, -1, 4, 7, 5, 3], 'scores': [0.3294641375541687, 0.36848384141921997, 0.6129383444786072, 0.2392873764038086, 0.5157200694084167, 0.3420858383178711, 0.4845498204231262, 0.38868623971939087, 0.5496301054954529, 0.3887292146682739]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9076957106590271})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6174367666244507})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6139024496078491})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5753319263458252})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5748375654220581})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5766849517822266})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.669934868812561})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6695111989974976})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.5526419921875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7743850350379944})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.489680677652359})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47121670842170715})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42300891876220703})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3926122188568115})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3808109760284424})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3923940658569336})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [40855, 52957, 23960, 33364, 8678, 46871, 3106, 3671, 17777, 36048], 'labels': [9, -1, -1, 2, 1, -1, -1, -1, -1, -1], 'scores': [0.43905794620513916, 0.265791654586792, 0.4425405263900757, 0.630355179309845, 0.7481660842895508, 0.47611522674560547, 0.5553475618362427, 0.4991372227668762, 0.5066540241241455, 0.5662380456924438]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8875559568405151})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5483916997909546})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6526206731796265})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7599263787269592})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7037671804428101})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.534733203125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7601422667503357})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5301178097724915})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4985681474208832})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4824683368206024})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [47225, 635, 26472, 55438, 37811, 44961, 12748, 1863, 1610, 29034], 'labels': [3, 5, 6, 8, -1, 8, 0, 3, 9, 0], 'scores': [0.28890442848205566, 0.4695768356323242, 0.24734365940093994, 0.47878074645996094, 0.21908676624298096, 0.46906763315200806, 0.4823535680770874, 0.44030559062957764, 0.4833695888519287, 0.3911917805671692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.909061074256897})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5092955827713013})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6287106275558472})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5881701707839966})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.582088828086853})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.52216630859375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7026631832122803})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5294225215911865})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.49971285462379456})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4968562722206116})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [20328, 40189, 19954, 47613, 29255, 59335, 16161, 22052, 40475, 53508], 'labels': [8, -1, -1, 7, -1, -1, 6, 7, 6, -1], 'scores': [0.44486498832702637, 0.20568203926086426, 0.31413042545318604, 0.41038137674331665, 0.44507551193237305, 0.3415626287460327, 0.31746482849121094, 0.3466905355453491, 0.3362152576446533, 0.2723597288131714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.844467043876648})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6197845935821533})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.535742998123169})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5298282504081726})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5527742505073547})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6114680767059326})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6704634428024292})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.49304716796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7232331037521362})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5409072637557983})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4586073160171509})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.41056886315345764})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4260103106498718})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.39730405807495117})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [5620, 31782, 28362, 25018, 39556, 9344, 49094, 29254, 38019, 45446], 'labels': [5, 5, 7, 8, 5, 5, 5, 8, 5, 7], 'scores': [0.3815079629421234, 0.4791984558105469, 0.3049933910369873, 0.4666222333908081, 0.4538304805755615, 0.3666090965270996, 0.6765490174293518, 0.37178710103034973, 0.4604405015707016, 0.3840659260749817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8933000564575195})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5433048605918884})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5338701009750366})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5717084407806396})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5372319221496582})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5491203665733337})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.502362451171875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7121349573135376})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5449936389923096})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4353581666946411})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46040451526641846})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4145015478134155})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [16236, 39336, 41850, 28262, 25964, 3544, 59115, 21842, 31339, 56643], 'labels': [-1, 6, 3, 9, -1, 9, -1, 9, 6, 2], 'scores': [0.3347158432006836, 0.5112180709838867, 0.37472355365753174, 0.4714164733886719, 0.47943711280822754, 0.44257426261901855, 0.4178045392036438, 0.40174418687820435, 0.27097344398498535, 0.6732698678970337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8430964946746826})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6263999938964844})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5703054070472717})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5484133958816528})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5374374389648438})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6421574354171753})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5724285840988159})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6051852703094482})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.49969775390625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7618522047996521})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5232491493225098})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44753938913345337})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4403127431869507})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4101453423500061})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.42568284273147583})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3772004246711731})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [14769, 15120, 40465, 59477, 37829, 35632, 12589, 57392, 43796, 53832], 'labels': [4, -1, 7, -1, 6, 0, 4, 8, 7, 7], 'scores': [0.459023654460907, 0.42483776807785034, 0.5231994986534119, 0.38138413429260254, 0.4489439129829407, 0.41594642400741577, 0.29832926392555237, 0.3422120213508606, 0.5125427842140198, 0.4216747283935547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8334805369377136})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5148270130157471})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4954574406147003})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5046462416648865})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48342734575271606})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5067967176437378})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49939388036727905})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.588835597038269})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.45153388671875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7050840854644775})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45290514826774597})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3808539807796478})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36189281940460205})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3822159469127655})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3525403141975403})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3666236996650696})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [9921, 59546, 30192, 27514, 15450, 24426, 3691, 866, 21042, 10210], 'labels': [-1, 5, 6, 4, 6, 5, 0, 2, 2, 3], 'scores': [0.3236337900161743, 0.4567241668701172, 0.40986818075180054, 0.3788875341415405, 0.48573899269104004, 0.5368965864181519, 0.5525959134101868, 0.43886610865592957, 0.4610733389854431, 0.6717031598091125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9448740482330322})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5871507525444031})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5082370638847351})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5106096267700195})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6257833242416382})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5258455872535706})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.466500341796875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8216396570205688})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5588879585266113})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5151577591896057})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4379924535751343})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46275216341018677})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [47501, 35491, 43539, 56246, 47628, 15247, 29306, 14894, 39411, 10304], 'labels': [1, -1, 1, -1, 3, -1, -1, 5, 2, 6], 'scores': [0.41437220573425293, 0.386250376701355, 0.4125085473060608, 0.33022576570510864, 0.2595053017139435, 0.37323808670043945, 0.4154719114303589, 0.36063122749328613, 0.4665724039077759, 0.4391346573829651]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8499678373336792})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5011847019195557})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5290505290031433})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4490842819213867})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48679161071777344})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5296844244003296})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5250552892684937})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.432053271484375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7163695693016052})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49112945795059204})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4361792206764221})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4326338768005371})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41480398178100586})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4041372537612915})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [50494, 50576, 28328, 50, 36031, 2213, 7538, 31444, 15592, 35384], 'labels': [-1, 2, -1, -1, -1, 7, -1, 8, 9, -1], 'scores': [0.317325234413147, 0.5018708109855652, 0.3717852830886841, 0.47611570358276367, 0.3327662944793701, 0.5377480983734131, 0.32592833042144775, 0.2876049280166626, 0.45110058784484863, 0.4157591462135315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8191689848899841})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5049092173576355})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4585602283477783})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41897374391555786})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4679052233695984})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.459533154964447})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45688652992248535})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.3955459228515625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.667008638381958})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4518866240978241})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40414342284202576})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3619228005409241})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3526046872138977})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34440451860427856})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [44570, 13608, 37280, 1376, 207, 52560, 54340, 33222, 4820, 35702], 'labels': [7, 8, -1, 7, 3, -1, -1, 5, 5, 5], 'scores': [0.5056986808776855, 0.20388951897621155, 0.3438645601272583, 0.6135550141334534, 0.4889606833457947, 0.27774280309677124, 0.21856164932250977, 0.6391302347183228, 0.5170910358428955, 0.590366929769516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8513662815093994})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5602247714996338})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46032029390335083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4605209231376648})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46119439601898193})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4825412631034851})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.42669326171875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8084310293197632})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5517990589141846})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45831578969955444})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4353570342063904})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39014220237731934})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [2302, 54032, 49199, 57575, 56082, 12891, 37745, 25310, 19748, 8847], 'labels': [8, 6, 0, 0, 8, 5, -1, 1, 9, 9], 'scores': [0.4401804208755493, 0.4867938756942749, 0.6329249143600464, 0.44327789545059204, 0.40110957622528076, 0.47678494453430176, 0.3384437561035156, 0.3976665735244751, 0.5010025501251221, 0.4204444885253906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8498370051383972})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5491485595703125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4278092384338379})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.447865754365921})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42288729548454285})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4512081742286682})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42269232869148254})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5290614366531372})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47345268726348877})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4881467819213867})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9486, 'crossentropy': 0.413948681640625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6847389340400696})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4347958266735077})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3886587619781494})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3361232280731201})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3189287781715393})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32656344771385193})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34224504232406616})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3091716766357422})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31916141510009766})
store['active_learning_steps'][24]['eval_training']['best_epoch']=8
store['active_learning_steps'][24]['acquisition']={'indices': [47661, 30080, 16456, 2414, 2198, 44123, 23094, 59373, 12168, 12452], 'labels': [-1, -1, 2, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.38617682456970215, 0.4517233967781067, 0.5697266757488251, 0.2761174440383911, 0.450297474861145, 0.5943928956985474, 0.5395750403404236, 0.2125089168548584, 0.40335357189178467, 0.3541386127471924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.941089391708374})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.501373827457428})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46461838483810425})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4530085325241089})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43745195865631104})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48301178216934204})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.482280969619751})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5024198293685913})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9405, 'crossentropy': 0.4439611328125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8493701815605164})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4977469742298126})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4088572859764099})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39582228660583496})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.366767555475235})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3374890089035034})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3624947667121887})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [12389, 55116, 15929, 33848, 12655, 58437, 10070, 12718, 49350, 23100], 'labels': [9, 3, -1, -1, 9, 9, 9, -1, 3, 9], 'scores': [0.4376407265663147, 0.2806514501571655, 0.4028511643409729, 0.21416783332824707, 0.4834943115711212, 0.5455718636512756, 0.6489774584770203, 0.3457579016685486, 0.3519582152366638, 0.5607386827468872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9305089712142944})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48819637298583984})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4798644781112671})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4170460104942322})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44809991121292114})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4173716902732849})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.401318222284317})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47881168127059937})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4409016966819763})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43105220794677734})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9456, 'crossentropy': 0.392536328125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7718918323516846})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5044572353363037})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41710031032562256})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.346713125705719})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3460838198661804})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3372299075126648})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30935317277908325})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3260694146156311})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.32846584916114807})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [4043, 27952, 59072, 44757, 32926, 56043, 37704, 45740, 17006, 21544], 'labels': [-1, 5, -1, -1, 8, -1, 8, -1, -1, -1], 'scores': [0.5353205800056458, 0.43576669692993164, 0.3187781572341919, 0.4190545678138733, 0.5549447536468506, 0.5013364553451538, 0.46835172176361084, 0.3741801381111145, 0.42689329385757446, 0.4615703225135803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9392359256744385})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5470002889633179})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4621410369873047})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4231276214122772})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4290602207183838})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45140165090560913})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44378724694252014})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9436, 'crossentropy': 0.4061575439453125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8810375928878784})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45566946268081665})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42675676941871643})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3865870237350464})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36006462574005127})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39056193828582764})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [15220, 49202, 14806, 44172, 11074, 57496, 16587, 30561, 57718, 32747], 'labels': [6, 5, 5, 8, 9, 2, -1, 2, 7, 8], 'scores': [0.2703898549079895, 0.40823596715927124, 0.2916548252105713, 0.4590259790420532, 0.5838020443916321, 0.3998444676399231, 0.39380061626434326, 0.37402307987213135, 0.2515592575073242, 0.534916877746582]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8353338241577148})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5256639122962952})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43664830923080444})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4558500051498413})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49864256381988525})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4466286301612854})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9454, 'crossentropy': 0.4050677734375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7490406036376953})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4791489839553833})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42657244205474854})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4241463840007782})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41579103469848633})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [32359, 7224, 13652, 3070, 29444, 9119, 23386, 5013, 45056, 31301], 'labels': [-1, -1, 9, 1, 4, 9, 7, 2, 8, 5], 'scores': [0.21889054775238037, 0.27524256706237793, 0.4081566333770752, 0.4278358221054077, 0.3712775707244873, 0.22426843643188477, 0.34852445125579834, 0.5296353101730347, 0.3185916543006897, 0.5130934715270996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.000140905380249})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5549154281616211})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4127386212348938})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41171956062316895})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.472898006439209})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4760092496871948})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5091725587844849})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.3769270751953125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7323183417320251})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4604448974132538})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41121891140937805})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35124433040618896})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3430166244506836})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3549594283103943})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [42321, 11621, 424, 14171, 44142, 6967, 6980, 49261, 17585, 47737], 'labels': [5, 2, 9, -1, 3, -1, 5, -1, 0, 5], 'scores': [0.5080921053886414, 0.5752741098403931, 0.5491442084312439, 0.38365185260772705, 0.5562851428985596, 0.32577741146087646, 0.56080561876297, 0.5267016887664795, 0.6392150521278381, 0.4776086211204529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9373301863670349})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5081408023834229})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48136186599731445})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4766096770763397})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4257223606109619})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4584818482398987})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4560486078262329})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41251862049102783})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4345077872276306})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5129668712615967})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5109274387359619})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9474, 'crossentropy': 0.389650439453125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.814550518989563})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5107229948043823})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4114428758621216})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3711133599281311})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35680657625198364})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3277894854545593})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.30604010820388794})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.30541709065437317})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.31465843319892883})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2840079069137573})
store['active_learning_steps'][30]['eval_training']['best_epoch']=10
store['active_learning_steps'][30]['acquisition']={'indices': [11599, 32782, 28357, 21136, 45225, 17110, 26902, 4046, 17781, 20223], 'labels': [-1, 6, 0, 2, -1, -1, -1, 7, -1, 7], 'scores': [0.3621230125427246, 0.5614483952522278, 0.5530354380607605, 0.5662184953689575, 0.3828197717666626, 0.31908994913101196, 0.3566616177558899, 0.532573401927948, 0.31584596633911133, 0.39213332533836365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.038445234298706})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.525181770324707})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3891059160232544})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4040956497192383})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3594978451728821})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3808576762676239})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3641180992126465})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3796469569206238})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.3266330322265625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8331685066223145})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4950304329395294})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4006724953651428})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3490062952041626})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3512724041938782})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.31069299578666687})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.33333534002304077})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [48270, 36562, 6466, 49192, 19939, 31605, 15430, 35843, 42952, 49859], 'labels': [2, 0, 2, 2, -1, -1, -1, -1, 4, 3], 'scores': [0.4958159923553467, 0.3024665415287018, 0.5335466265678406, 0.4861792325973511, 0.48240476846694946, 0.3194844722747803, 0.43253135681152344, 0.3130086660385132, 0.2546060085296631, 0.4748784899711609]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9906554222106934})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49666279554367065})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4296995997428894})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3593237102031708})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3819432556629181})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3874269723892212})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.377113938331604})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9462, 'crossentropy': 0.3680428466796875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7832635045051575})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4963979423046112})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44788533449172974})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.40351736545562744})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38165533542633057})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.36810576915740967})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [18164, 25910, 14355, 39653, 17145, 31576, 29662, 20050, 51738, 45024], 'labels': [-1, 1, 2, -1, -1, 7, 2, 9, 2, 5], 'scores': [0.3341677188873291, 0.517514169216156, 0.5062007904052734, 0.22960329055786133, 0.3625481128692627, 0.45986002683639526, 0.2783745527267456, 0.5798664689064026, 0.4928087294101715, 0.34579402208328247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0305330753326416})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5711089372634888})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3940044641494751})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36631810665130615})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39666813611984253})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37097710371017456})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35155606269836426})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39015209674835205})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4468911588191986})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.404377818107605})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3365473388671875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7928833365440369})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4857075810432434})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3581174612045288})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34697967767715454})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3501207232475281})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32545459270477295})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3076120615005493})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3229091465473175})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.2883753180503845})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [57748, 1282, 3795, 55727, 27351, 56323, 27299, 28181, 32638, 29713], 'labels': [7, 9, -1, 0, -1, 9, 8, -1, -1, 0], 'scores': [0.46580106019973755, 0.4117307662963867, 0.48867934942245483, 0.6289344429969788, 0.30651676654815674, 0.3896912932395935, 0.7046384215354919, 0.38789796829223633, 0.427512526512146, 0.5142590999603271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0429141521453857})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5019651651382446})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4330376386642456})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42181307077407837})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3889228403568268})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4088195860385895})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4011875092983246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44476357102394104})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9506, 'crossentropy': 0.349818212890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8855443000793457})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4897662401199341})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43957003951072693})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3789527118206024})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35565513372421265})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34945154190063477})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3284342885017395})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [41734, 35722, 49792, 1248, 5669, 17540, 31989, 37964, 56773, 10260], 'labels': [-1, -1, 2, -1, -1, 1, -1, -1, 9, -1], 'scores': [0.41292911767959595, 0.2560915946960449, 0.36303335428237915, 0.3133370876312256, 0.25292301177978516, 0.498934805393219, 0.4401801824569702, 0.3972361087799072, 0.3787522315979004, 0.5328617095947266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0635966062545776})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5005502104759216})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3921178877353668})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.411297082901001})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34977710247039795})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3993428945541382})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36804020404815674})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39506232738494873})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.324329541015625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7770529985427856})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4919580817222595})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3643491566181183})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32830172777175903})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34596386551856995})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2962110936641693})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29186326265335083})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [18473, 7559, 13195, 52889, 30952, 37124, 3895, 14700, 54814, 41108], 'labels': [4, -1, -1, -1, 7, 3, -1, -1, 4, 0], 'scores': [0.48900097608566284, 0.2305830717086792, 0.5609713792800903, 0.5389853119850159, 0.4942898154258728, 0.47001898288726807, 0.5193623900413513, 0.46006253361701965, 0.3971976637840271, 0.4936901330947876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0733258724212646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6024205088615417})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.403350293636322})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41266000270843506})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4094296991825104})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37800198793411255})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3977096378803253})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45558902621269226})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4292641878128052})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9533, 'crossentropy': 0.356026904296875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8008580207824707})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45424479246139526})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36966341733932495})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3287416696548462})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3159691095352173})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2867370843887329})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2923494279384613})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2672892212867737})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [3432, 22545, 44690, 7458, 10141, 12869, 37184, 12236, 49656, 33012], 'labels': [8, 1, 6, 0, 3, -1, -1, 1, 9, -1], 'scores': [0.4011697769165039, 0.5052136182785034, 0.42098119854927063, 0.3853539824485779, 0.4570993483066559, 0.4751335382461548, 0.4153326749801636, 0.6538071632385254, 0.3873598575592041, 0.2564893066883087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8913407921791077})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4975213408470154})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4032694697380066})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3519083559513092})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3584195375442505})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3457333445549011})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40475910902023315})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.353310227394104})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37119436264038086})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.32876220703125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.803604006767273})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4688502550125122})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39510053396224976})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3395543098449707})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3308451771736145})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33140280842781067})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3164750635623932})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2773343324661255})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [23154, 11708, 20764, 30925, 56224, 8998, 52790, 36239, 50860, 22210], 'labels': [0, 3, -1, -1, 5, -1, -1, 1, 8, 6], 'scores': [0.5602114200592041, 0.399593710899353, 0.3540714979171753, 0.31927692890167236, 0.52567058801651, 0.44098150730133057, 0.3998758792877197, 0.45520323514938354, 0.3013826012611389, 0.21697455644607544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.106100082397461})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49815571308135986})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4391446113586426})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3648337721824646})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.381713330745697})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34361329674720764})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34197673201560974})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36925119161605835})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39370107650756836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42581984400749207})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.954, 'crossentropy': 0.3296253662109375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8381839990615845})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5009039640426636})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4353022277355194})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3452806770801544})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.325181245803833})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32578325271606445})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2927236557006836})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3200489282608032})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.284553587436676})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
