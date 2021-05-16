store = {}
store['timestamp']=1620992130
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=10']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=20
store['config']={'seed': 1249, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1137166023254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2941315174102783})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.829442024230957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3553199768066406})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6785, 'crossentropy': 1.9317615234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1459364891052246})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.18696928024292})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1400997638702393})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [22673, 56775, 27343, 12377, 25191, 41108, 38848, 50013, 51761, 3759], 'labels': [2, 0, 0, 3, -1, 0, 5, 8, 9, -1], 'scores': [0.3970640003681183, 0.9831562638282776, 0.8450400829315186, 0.9083294868469238, 0.5225843191146851, 0.5127368569374084, 0.40022796392440796, 0.66255784034729, 0.7788476943969727, 0.515116810798645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.220566987991333})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.69543719291687})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.669931650161743})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.727275848388672})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.01819296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.240752935409546})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.213132619857788})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2003698348999023})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [12579, 8420, 38059, 30870, 17453, 10984, 9339, 11327, 32012, 6346], 'labels': [-1, 6, 5, 8, 5, 3, 5, 6, 8, 5], 'scores': [0.5461395978927612, 0.7483068704605103, 0.5711703896522522, 0.9875325560569763, 0.6361669301986694, 0.8432955741882324, 0.5969749689102173, 0.5709503293037415, 0.634698748588562, 0.6436364650726318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.1116943359375})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1985058784484863})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.7135419845581055})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.7857985496520996})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6968, 'crossentropy': 1.853581640625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0980370044708252})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0742031335830688})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0772650241851807})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [46565, 21449, 51595, 32235, 19793, 43583, 50937, 34432, 56933, 43193], 'labels': [7, 9, 9, 9, 3, 1, 4, 2, 9, 9], 'scores': [0.4402451515197754, 0.6355593204498291, 0.8071940541267395, 0.6690641641616821, 0.7316413521766663, 0.5647357702255249, 0.7258957624435425, 0.6705523133277893, 0.6248173117637634, 0.5907796621322632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7007235288619995})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.3444411754608154})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.068685531616211})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.3047666549682617})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7263, 'crossentropy': 1.704360546875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1821188926696777})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0947184562683105})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0642024278640747})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [40595, 48887, 57041, 18353, 16358, 3310, 40323, 36478, 49525, 40609], 'labels': [8, 2, 0, 8, 5, -1, 7, 8, 8, 6], 'scores': [0.4760587215423584, 0.6230073571205139, 0.5065313577651978, 0.4570372700691223, 0.619918167591095, 0.35418522357940674, 0.3321859836578369, 0.42804449796676636, 0.7291964888572693, 0.6524086594581604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0812351703643799})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3180509805679321})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.491034984588623})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3840750455856323})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7776, 'crossentropy': 1.1224384765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.8913093209266663})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.790600597858429})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.7576279044151306})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [7214, 8344, 546, 10190, 21475, 14299, 37082, 49999, 51695, 36984], 'labels': [3, 4, -1, 6, 8, 7, 3, 8, 3, 5], 'scores': [0.5431514978408813, 0.33625316619873047, 0.20985102653503418, 0.4213780164718628, 0.49412089586257935, 0.5635135173797607, 0.3983309268951416, 0.439716100692749, 0.3377811312675476, 0.48470431566238403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9865219593048096})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0412061214447021})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3043506145477295})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1111105680465698})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8201, 'crossentropy': 1.00775283203125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8180985450744629})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7284307479858398})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7096540927886963})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [48475, 41431, 17334, 51088, 31939, 15424, 12778, 11734, 14833, 42437], 'labels': [8, 8, 0, 7, 9, 8, 8, 8, 7, 9], 'scores': [0.6661762595176697, 0.3812848925590515, 0.44030535221099854, 0.4642552137374878, 0.5415806770324707, 0.5444484949111938, 0.5205329656600952, 0.45671188831329346, 0.47639960050582886, 0.5419168472290039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0187854766845703})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0015301704406738})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.018550157546997})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2568159103393555})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0633885860443115})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8325, 'crossentropy': 0.99337744140625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8064562082290649})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.6984257698059082})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6241798400878906})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.626664400100708})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [51738, 58877, 54191, 4205, 28954, 51102, 28720, 57135, 53022, 16952], 'labels': [2, -1, 3, 4, 2, 7, 5, 4, 9, 2], 'scores': [0.5485824346542358, 0.35165733098983765, 0.5589351058006287, 0.4377749562263489, 0.5732200145721436, 0.5034176707267761, 0.47243767976760864, 0.35738974809646606, 0.28427642583847046, 0.6126710772514343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.875106692314148})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8897457122802734})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9844381809234619})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1598281860351562})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8444, 'crossentropy': 0.818855810546875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8781648874282837})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7658592462539673})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7355060577392578})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [49448, 46246, 16748, 9180, 44882, 54134, 58464, 39963, 39266, 57336], 'labels': [6, 3, 3, 3, 9, 2, 8, 4, 8, 3], 'scores': [0.5083777904510498, 0.2793358564376831, 0.37793171405792236, 0.34955376386642456, 0.46209418773651123, 0.44467079639434814, 0.517979621887207, 0.443359375, 0.45679134130477905, 0.3441448211669922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8038038015365601})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9038901329040527})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9405614733695984})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0019659996032715})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.8204544921875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8744425773620605})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7337875366210938})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7245113849639893})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [55591, 1276, 32555, 14623, 20812, 42935, 12950, 46368, 48779, 26196], 'labels': [5, 5, 9, 5, 8, 5, 2, 8, 4, 5], 'scores': [0.45485079288482666, 0.5960460901260376, 0.46735310554504395, 0.6763551235198975, 0.3877429962158203, 0.3124687671661377, 0.4405369758605957, 0.573639452457428, 0.37033677101135254, 0.418735146522522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.923477292060852})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7929655313491821})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7026862502098083})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8445318937301636})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9023656845092773})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8261898756027222})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.62742607421875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6737647652626038})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5458710193634033})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4980461001396179})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.468073308467865})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.46806442737579346})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [3273, 36781, 32208, 27283, 14619, 47387, 12650, 20508, 51889, 2288], 'labels': [8, 2, 7, 0, 3, 8, 5, 9, -1, 2], 'scores': [0.6231243014335632, 0.5374102592468262, 0.5177075564861298, 0.6125265061855316, 0.531699001789093, 0.6410613656044006, 0.657558798789978, 0.5395716428756714, 0.5084540843963623, 0.7248174548149109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9230727553367615})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6964230537414551})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6908594965934753})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7087994813919067})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6855898499488831})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7212212681770325})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8140414953231812})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8281521201133728})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.626161279296875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6637457609176636})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5736100673675537})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47997310757637024})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4468845725059509})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4431183636188507})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4363568425178528})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.45981520414352417})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [48006, 2526, 20388, 9601, 51988, 59641, 51295, 40805, 51524, 10210], 'labels': [6, -1, 0, 8, 7, 2, -1, 3, 5, 3], 'scores': [0.5259741842746735, 0.5676649808883667, 0.4215092062950134, 0.5317618250846863, 0.5884787440299988, 0.5094790160655975, 0.5955055952072144, 0.4371417760848999, 0.4997764229774475, 0.7433881163597107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8506532907485962})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.597789466381073})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6474639773368835})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6198427081108093})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7527276873588562})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9093, 'crossentropy': 0.61049375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7453030347824097})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5616741180419922})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5183517932891846})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.537460446357727})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [1405, 37861, 41339, 58470, 18637, 56533, 40653, 47166, 28701, 893], 'labels': [1, -1, 7, 9, 4, 0, 2, 0, 2, 2], 'scores': [0.33030879497528076, 0.4257282018661499, 0.4286097288131714, 0.48816436529159546, 0.2316630780696869, 0.442641019821167, 0.4364997148513794, 0.3544917404651642, 0.35575175285339355, 0.338447630405426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7803282737731934})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6251614093780518})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5550233125686646})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.638592004776001})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6740515828132629})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6849849224090576})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.546578759765625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7609902620315552})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5139598846435547})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5130097270011902})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47796136140823364})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4292498528957367})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [35858, 47378, 39821, 49202, 20977, 5024, 30422, 32348, 26801, 14544], 'labels': [5, -1, 7, 5, 7, 9, 4, 5, 7, 5], 'scores': [0.49356698989868164, 0.26412129402160645, 0.4405781626701355, 0.6000929474830627, 0.37303367257118225, 0.5772930383682251, 0.5328322649002075, 0.5754579901695251, 0.5260611772537231, 0.4894619584083557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7552925944328308})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5496380925178528})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.571658730506897})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5204223394393921})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.565829873085022})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6493262052536011})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6043637990951538})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9315, 'crossentropy': 0.48113740234375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6675793528556824})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4577863812446594})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4383692741394043})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43065041303634644})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41738784313201904})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4023362398147583})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [58469, 12321, 33697, 5740, 7793, 44902, 38510, 509, 39351, 32747], 'labels': [-1, 0, 2, 9, 8, -1, 8, 3, 9, -1], 'scores': [0.2962275743484497, 0.5223733186721802, 0.48503050208091736, 0.6885517239570618, 0.43618953227996826, 0.38726234436035156, 0.40502792596817017, 0.5394112467765808, 0.29793375730514526, 0.30240046977996826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.809136152267456})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6336371302604675})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5691379308700562})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5320839285850525})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5608184933662415})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.546980619430542})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5963003635406494})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9289, 'crossentropy': 0.47996328125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7135897278785706})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5025764107704163})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.46759456396102905})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41844838857650757})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.429989755153656})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.40729039907455444})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [28847, 34303, 38932, 56455, 29132, 49891, 49316, 24342, 41572, 2765], 'labels': [-1, -1, 5, 6, 8, 7, 5, 6, 6, 0], 'scores': [0.1491328477859497, 0.4465104341506958, 0.43085432052612305, 0.4164881408214569, 0.5903413891792297, 0.4369938373565674, 0.6206473112106323, 0.4904631972312927, 0.486319363117218, 0.5258720517158508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8576246500015259})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5092633366584778})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4743654131889343})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5217020511627197})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5027098655700684})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5739456415176392})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.936, 'crossentropy': 0.45406826171875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6757442951202393})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5195876359939575})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4999183416366577})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.425504207611084})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4167442321777344})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [4822, 16019, 26444, 4795, 21023, 11696, 27183, 57728, 19199, 45801], 'labels': [4, 3, 1, 3, 2, 5, 3, 9, 7, 3], 'scores': [0.47056037187576294, 0.33125460147857666, 0.7016147375106812, 0.4036524295806885, 0.4275960326194763, 0.36743736267089844, 0.5097220540046692, 0.5651217699050903, 0.2847748398780823, 0.5695233941078186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8396795988082886})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5628725290298462})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5097932815551758})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5260151028633118})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5796374678611755})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5964605808258057})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.4493728515625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.724989652633667})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4876560568809509})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48145779967308044})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43516772985458374})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45239314436912537})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [39363, 14766, 43288, 47548, 15613, 4613, 29955, 24703, 41230, 17603], 'labels': [-1, -1, -1, 8, 4, -1, -1, 4, -1, 0], 'scores': [0.35415875911712646, 0.3290099501609802, 0.39074182510375977, 0.48478496074676514, 0.3135932981967926, 0.33582037687301636, 0.3877881169319153, 0.4022197127342224, 0.3394327163696289, 0.4041370153427124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8529919981956482})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5644222497940063})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5527387857437134})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6051474809646606})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6146998405456543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.577496349811554})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.486839501953125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8172832727432251})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5434608459472656})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47577130794525146})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4526379108428955})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4903711676597595})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [15832, 55891, 28539, 13816, 5013, 14940, 45888, 29083, 49892, 108], 'labels': [9, -1, 8, 0, 2, 6, 9, -1, 5, 0], 'scores': [0.5241795778274536, 0.2658146619796753, 0.3335506319999695, 0.4635165333747864, 0.40087395906448364, 0.32988864183425903, 0.4421840310096741, 0.3126249313354492, 0.46379798650741577, 0.35002774000167847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8315238952636719})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47768938541412354})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5404602289199829})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5226584672927856})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5004153847694397})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.48977197265625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7387281656265259})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6274986267089844})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4920245409011841})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5514391660690308})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [49014, 1239, 35326, 43278, 16959, 27317, 33035, 35784, 3094, 31090], 'labels': [0, 8, 5, 4, 5, 5, 6, 5, 8, 4], 'scores': [0.3061150312423706, 0.31832677125930786, 0.33468711376190186, 0.36201685667037964, 0.30625951290130615, 0.3640209436416626, 0.29665958881378174, 0.3629208207130432, 0.4458392858505249, 0.42973804473876953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8914873600006104})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5865124464035034})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5268654823303223})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5066865682601929})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47866249084472656})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5416757464408875})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5127668380737305})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5729533433914185})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.942, 'crossentropy': 0.43445244140625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7642321586608887})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44457197189331055})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4500717520713806})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3689095079898834})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4240359663963318})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.367889404296875})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3745708167552948})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [38829, 50963, 54388, 4873, 14767, 21011, 11822, 57683, 487, 47583], 'labels': [9, 7, 1, 8, 1, -1, 7, 9, -1, 1], 'scores': [0.29550519585609436, 0.3692222237586975, 0.48276424407958984, 0.5650734007358551, 0.5385698080062866, 0.30913007259368896, 0.3548637628555298, 0.34749746322631836, 0.4073524475097656, 0.40811431407928467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8582675457000732})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.508902907371521})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49155014753341675})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48697763681411743})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4728638529777527})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4742501974105835})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5020276308059692})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.52725750207901})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.422308544921875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8058305978775024})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5191022753715515})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4492666721343994})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41209572553634644})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4126296043395996})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36377304792404175})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3463941216468811})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [1388, 45056, 41129, 40132, 54682, 146, 18574, 47440, 19855, 30718], 'labels': [-1, 8, -1, 1, -1, -1, -1, -1, -1, -1], 'scores': [0.46313297748565674, 0.5582860708236694, 0.49306464195251465, 0.23528584837913513, 0.5993421077728271, 0.5129472017288208, 0.34425604343414307, 0.48426055908203125, 0.44028162956237793, 0.46111661195755005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.000646710395813})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5814727544784546})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49156227707862854})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45106256008148193})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4710259735584259})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.498863160610199})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5045461654663086})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.434382470703125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7236142754554749})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4776676893234253})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3935317099094391})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3779888451099396})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3943157196044922})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3588535189628601})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [6345, 37916, 33634, 23263, 32855, 9568, 7336, 46313, 10647, 37648], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4873453974723816, 0.4655120372772217, 0.328096866607666, 0.4310173988342285, 0.4575120210647583, 0.44234657287597656, 0.3910897970199585, 0.4871218204498291, 0.4365307092666626, 0.46017885208129883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0524861812591553})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5740119218826294})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5248641967773438})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5208154916763306})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4931040406227112})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4852597713470459})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5279269814491272})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5479758977890015})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5613593459129333})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.44424560546875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7590932846069336})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5098894834518433})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38962551951408386})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.36918509006500244})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34016773104667664})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3385448455810547})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.347898006439209})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35413289070129395})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [48329, 52462, 935, 39418, 56208, 17213, 32052, 29667, 34126, 40720], 'labels': [-1, 9, 8, -1, 1, 1, -1, 2, -1, 3], 'scores': [0.3618276119232178, 0.4997329115867615, 0.4941402077674866, 0.4309275150299072, 0.364950954914093, 0.5423619747161865, 0.36348485946655273, 0.6501280069351196, 0.3184483051300049, 0.40376418828964233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8922038078308105})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5087826251983643})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47610536217689514})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4553927779197693})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4592597484588623})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5202493667602539})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5229370594024658})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.42904345703125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7461330890655518})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4916955828666687})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42519354820251465})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3764086365699768})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3986368179321289})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3776228129863739})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [9633, 22874, 10939, 59485, 14263, 8768, 35842, 5774, 29508, 47288], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, 7, -1], 'scores': [0.5741708874702454, 0.4675474166870117, 0.487255334854126, 0.33082032203674316, 0.5277743339538574, 0.35915470123291016, 0.5051389932632446, 0.32503485679626465, 0.47627896070480347, 0.4199068546295166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8949662446975708})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5164917707443237})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4915955662727356})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4559905230998993})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.499397873878479})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5229201316833496})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5478283166885376})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.44226123046875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7463191747665405})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49254193902015686})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42932435870170593})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3999617099761963})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4056466817855835})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39941078424453735})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [3449, 16369, 31029, 21692, 29936, 34058, 51831, 3430, 11244, 43955], 'labels': [-1, -1, -1, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.3195512294769287, 0.2613433599472046, 0.3459811210632324, 0.46142667531967163, 0.47890883684158325, 0.3493567705154419, 0.3125600814819336, 0.23219037055969238, 0.2832540273666382, 0.40953874588012695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9147157669067383})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6329412460327148})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48679643869400024})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48135191202163696})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.511013388633728})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6059889793395996})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6002053022384644})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.449575439453125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7448910474777222})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5506209135055542})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45279714465141296})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35690346360206604})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3670724034309387})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3850553631782532})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [45576, 52246, 22734, 50910, 43609, 18987, 38544, 17055, 30092, 42761], 'labels': [8, 4, 5, -1, 8, -1, 8, 8, 8, -1], 'scores': [0.38981080055236816, 0.27203959226608276, 0.266141414642334, 0.3525233268737793, 0.5441113710403442, 0.42757976055145264, 0.5220995545387268, 0.7616524696350098, 0.2853706181049347, 0.2276366949081421]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9724298119544983})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5832622647285461})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4881296157836914})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44033098220825195})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4306713342666626})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44540485739707947})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4190024137496948})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47841891646385193})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5237603783607483})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5175783634185791})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.414764501953125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7549771070480347})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4557206630706787})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3765564560890198})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3473654091358185})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32757607102394104})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3389054536819458})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29970893263816833})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.30313435196876526})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31607043743133545})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [13374, 37074, 42828, 55268, 11495, 25996, 21723, 26460, 33900, 11492], 'labels': [2, 4, 7, 8, -1, -1, 8, 5, -1, -1], 'scores': [0.34180617332458496, 0.4066633880138397, 0.6053866147994995, 0.5157461166381836, 0.5359179973602295, 0.47329413890838623, 0.44764137268066406, 0.5566371083259583, 0.3525298833847046, 0.4286147356033325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9322648048400879})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5791407823562622})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5019768476486206})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5103324055671692})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5490813255310059})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6174216270446777})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.47743271484375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.760802686214447})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5171669125556946})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.45813342928886414})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4618450403213501})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3966280519962311})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [40723, 41724, 56616, 43781, 7350, 47321, 47100, 28536, 42781, 11029], 'labels': [4, -1, 3, 4, 4, 2, 8, 3, 4, 0], 'scores': [0.38342955708503723, 0.3489084243774414, 0.2909160256385803, 0.37478041648864746, 0.3841531276702881, 0.3960334062576294, 0.29667508602142334, 0.5787657499313354, 0.4613235592842102, 0.5111030340194702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9840867519378662})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5256540179252625})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46146610379219055})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.459667444229126})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43226176500320435})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4906160533428192})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49783486127853394})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4813516438007355})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.41127392578125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8089859485626221})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5020614266395569})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42847269773483276})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39241984486579895})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3611566424369812})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33289608359336853})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34314030408859253})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [47795, 33162, 32342, 41054, 18049, 33464, 27576, 35065, 34650, 32047], 'labels': [-1, 8, 9, 7, 3, -1, 5, -1, 2, 9], 'scores': [0.38355839252471924, 0.33767393231391907, 0.3157328963279724, 0.5371568202972412, 0.3779560923576355, 0.3771017789840698, 0.5597724318504333, 0.21355009078979492, 0.330730140209198, 0.45235055685043335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9968596696853638})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5801514387130737})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5135657787322998})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4581350088119507})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4306972324848175})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4645586609840393})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4669194221496582})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4995135962963104})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.946, 'crossentropy': 0.434410595703125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7821896076202393})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5007348656654358})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4242536425590515})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36818981170654297})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3832940459251404})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3636566400527954})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3532133102416992})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [15404, 36141, 4360, 18227, 37118, 50073, 49107, 55011, 2406, 40841], 'labels': [6, 1, 6, 3, 3, -1, 5, 2, 4, -1], 'scores': [0.5746659636497498, 0.5253075957298279, 0.597644567489624, 0.47262269258499146, 0.6981276869773865, 0.2905235290527344, 0.5167648792266846, 0.40610551834106445, 0.4248451590538025, 0.22596359252929688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9894770383834839})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5422514081001282})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4470900595188141})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42749857902526855})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43871641159057617})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4585336148738861})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44266611337661743})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.3995594482421875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8508049249649048})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5388532876968384})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40828052163124084})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4448212683200836})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38745489716529846})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40620869398117065})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [35041, 38135, 23486, 50425, 607, 5246, 16190, 49488, 22199, 46367], 'labels': [-1, -1, 4, -1, -1, -1, 3, 1, -1, 4], 'scores': [0.38974273204803467, 0.38746416568756104, 0.482441782951355, 0.4412294030189514, 0.3274928331375122, 0.3818145990371704, 0.42539918422698975, 0.40216124057769775, 0.43862414360046387, 0.5161937475204468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9086487889289856})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4844364523887634})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4561645984649658})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4285929501056671})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3999207615852356})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43634921312332153})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4938390851020813})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4492584466934204})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9532, 'crossentropy': 0.3752923095703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7612060308456421})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5050101280212402})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3937864303588867})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3842391073703766})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3582412600517273})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35232019424438477})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.300771564245224})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [884, 14649, 24221, 32282, 11976, 20799, 48723, 46769, 2118, 35482], 'labels': [7, 0, -1, 7, -1, -1, -1, -1, 7, 4], 'scores': [0.5251275300979614, 0.5414754152297974, 0.22037827968597412, 0.41721707582473755, 0.45770859718322754, 0.31502389907836914, 0.22470080852508545, 0.21187031269073486, 0.45727473497390747, 0.44616538286209106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0386502742767334})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5714942216873169})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5008236765861511})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4292590022087097})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45410239696502686})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.500298261642456})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49105018377304077})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9476, 'crossentropy': 0.387483447265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7827395796775818})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.523666262626648})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42563551664352417})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38953715562820435})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35871732234954834})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3690360188484192})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [3440, 8865, 11056, 23776, 19614, 40076, 59681, 59487, 9036, 10800], 'labels': [1, 3, -1, 2, -1, 2, 0, -1, 2, 8], 'scores': [0.29179829359054565, 0.502326488494873, 0.35252606868743896, 0.3058711588382721, 0.35755014419555664, 0.5033301115036011, 0.6710752844810486, 0.3022325038909912, 0.5420563817024231, 0.4894145727157593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0104026794433594})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49704450368881226})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.427848219871521})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4006979465484619})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.433920681476593})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3817821741104126})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4315092861652374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4435580372810364})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4062134623527527})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9544, 'crossentropy': 0.361439697265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7984921336174011})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.491691529750824})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4233064651489258})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37055855989456177})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.363578736782074})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3264440894126892})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3148709535598755})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3329242467880249})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [21056, 33868, 48912, 16868, 36816, 48783, 46187, 15771, 39336, 528], 'labels': [-1, -1, 2, 0, -1, -1, 3, 5, 6, 8], 'scores': [0.49810463190078735, 0.39239758253097534, 0.49318522214889526, 0.5266140103340149, 0.28272515535354614, 0.40386033058166504, 0.3631015419960022, 0.5111916661262512, 0.426032155752182, 0.5028704404830933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.050844669342041})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5116032361984253})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3973187208175659})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3974129557609558})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43325716257095337})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.442139208316803})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9518, 'crossentropy': 0.3958814697265625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8289617300033569})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5579726099967957})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4254923462867737})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4285045564174652})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42269760370254517})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [32702, 13652, 16756, 40070, 23321, 22597, 54902, 14524, 13259, 22200], 'labels': [5, -1, 7, -1, 6, 9, 5, -1, 1, 2], 'scores': [0.55030357837677, 0.3261446952819824, 0.4914698004722595, 0.3187018036842346, 0.27730369567871094, 0.5468490123748779, 0.4703776240348816, 0.37386202812194824, 0.5543533563613892, 0.4198577404022217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.924216091632843})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5039398670196533})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.444378525018692})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4212247133255005})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3900730311870575})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3957545757293701})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39937299489974976})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4202619194984436})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9544, 'crossentropy': 0.3511713623046875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8667895793914795})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5202645063400269})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41391316056251526})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3477939963340759})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3426039516925812})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3390635550022125})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3258780241012573})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [6846, 1024, 956, 7768, 23816, 56298, 14458, 8768, 26434, 59072], 'labels': [2, 5, -1, 8, -1, -1, 2, -1, -1, -1], 'scores': [0.6331967413425446, 0.5641648173332214, 0.35183465480804443, 0.4785526394844055, 0.37158527970314026, 0.48817121982574463, 0.6812354922294617, 0.39476895332336426, 0.36415213346481323, 0.4998551607131958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.089170217514038})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5399868488311768})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4078676402568817})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3586711883544922})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36848151683807373})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4248775839805603})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.425971120595932})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.320843359375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7936568856239319})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5175828337669373})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3991406559944153})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34232664108276367})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36868786811828613})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.352647602558136})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [17526, 54711, 53054, 49828, 54287, 26568, 19948, 37422, 59072, 1282], 'labels': [-1, 0, -1, -1, -1, -1, 8, -1, -1, 9], 'scores': [0.4207509756088257, 0.30060863494873047, 0.5169642567634583, 0.5177730321884155, 0.4233229160308838, 0.5857818126678467, 0.32213807106018066, 0.19881725311279297, 0.5398989915847778, 0.3932204246520996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9362253546714783})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5374250411987305})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43185538053512573})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39425748586654663})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40113896131515503})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41481417417526245})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.40849387645721436})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.3263637451171875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8776533007621765})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4722391664981842})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3981824517250061})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3617435097694397})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35426393151283264})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3455503284931183})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [37945, 32199, 4934, 36254, 4191, 52086, 32436, 19939, 40260, 8409], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.3996775150299072, 0.4115194082260132, 0.3442267179489136, 0.41156959533691406, 0.2995328903198242, 0.46100878715515137, 0.3555114269256592, 0.40782463550567627, 0.2979269027709961, 0.40885472297668457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.93455970287323})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5702434778213501})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40730762481689453})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37482893466949463})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3976811170578003})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.391363263130188})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36262765526771545})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41330984234809875})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4569016396999359})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46383917331695557})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9574, 'crossentropy': 0.33020927734375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9347732067108154})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5607291460037231})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4529111981391907})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37298309803009033})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3585183918476105})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3249143958091736})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3261765241622925})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30594438314437866})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31643903255462646})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [30774, 55172, 44441, 59466, 33404, 44353, 33503, 23208, 778, 59507], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 5, -1], 'scores': [0.40557563304901123, 0.3858954906463623, 0.44611167907714844, 0.40218114852905273, 0.4526335597038269, 0.2817409038543701, 0.37121105194091797, 0.45761656761169434, 0.4787318706512451, 0.4217503070831299]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1300623416900635})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5034370422363281})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43096429109573364})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3734627962112427})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4026658535003662})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3787086009979248})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3984763026237488})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9549, 'crossentropy': 0.352289892578125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9142360091209412})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.501739501953125})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4076976776123047})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3776405453681946})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3594370484352112})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35470956563949585})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [46126, 10462, 6894, 49524, 25993, 24061, 19866, 54077, 58625, 54195], 'labels': [3, 4, 3, 6, 3, -1, 3, 3, 8, 8], 'scores': [0.527938723564148, 0.4958827495574951, 0.4772909879684448, 0.3704227805137634, 0.4948790669441223, 0.3636646270751953, 0.3196120858192444, 0.49233824014663696, 0.22690290212631226, 0.5267776250839233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9889110326766968})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.50362229347229})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3809707462787628})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3296666145324707})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3350532054901123})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29931706190109253})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33011990785598755})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33637887239456177})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38076335191726685})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.295599853515625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7265204191207886})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45597338676452637})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3460358679294586})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36395782232284546})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3015316128730774})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2885271906852722})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25939738750457764})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2874361276626587})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [5615, 56898, 6467, 35480, 8643, 29274, 22593, 25159, 51858, 50773], 'labels': [-1, -1, -1, 9, -1, -1, 7, 0, -1, -1], 'scores': [0.39960920810699463, 0.2877190113067627, 0.33576810359954834, 0.42534488439559937, 0.39845311641693115, 0.45450079441070557, 0.34738433361053467, 0.5155798196792603, 0.4637260437011719, 0.4663960933685303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9648057818412781})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5194857716560364})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41583359241485596})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35931336879730225})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3741872310638428})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4052782654762268})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3741135001182556})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.330552001953125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9266287088394165})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.494531512260437})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4390823245048523})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4310305714607239})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3331017792224884})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.337990939617157})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [37630, 10268, 33438, 36704, 3798, 46746, 55350, 8093, 53864, 47768], 'labels': [-1, 1, -1, 2, 7, 0, 6, 0, 8, 5], 'scores': [0.3787508010864258, 0.47889256477355957, 0.2555183172225952, 0.5157046318054199, 0.5372848510742188, 0.3130265474319458, 0.29080286622047424, 0.602934718132019, 0.4213829040527344, 0.22078821063041687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9699374437332153})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5141249895095825})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40312403440475464})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34810540080070496})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34477168321609497})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38335925340652466})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3576123118400574})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3392757177352905})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35650715231895447})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32396480441093445})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34896332025527954})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3778797686100006})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3519086241722107})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.3110399169921875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.775853157043457})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44067054986953735})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3693392276763916})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3119279146194458})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3294604420661926})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2800171971321106})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2695510983467102})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3003312945365906})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2622663974761963})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27566492557525635})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2570950388908386})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26344218850135803})
store['active_learning_steps'][42]['eval_training']['best_epoch']=11
store['active_learning_steps'][42]['acquisition']={'indices': [43136, 58508, 46905, 53108, 55902, 14035, 56751, 23950, 43617, 34387], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.43240952491760254, 0.44833528995513916, 0.4690965414047241, 0.3221994638442993, 0.3953598737716675, 0.37933921813964844, 0.5132964849472046, 0.4217935800552368, 0.525321364402771, 0.46766364574432373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.006247878074646})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5229437351226807})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41157424449920654})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32021263241767883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32295870780944824})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3245079517364502})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3597135841846466})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9572, 'crossentropy': 0.3234227294921875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7655346393585205})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4415155053138733})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39201122522354126})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3046143651008606})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3354601263999939})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31275102496147156})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [51130, 16011, 32360, 43160, 7795, 21256, 14590, 46021, 11206, 14266], 'labels': [-1, 5, 9, -1, -1, -1, -1, 9, -1, 3], 'scores': [0.4257645606994629, 0.3842887878417969, 0.34324127435684204, 0.38919496536254883, 0.4171653985977173, 0.38592636585235596, 0.3838552236557007, 0.3657553791999817, 0.3737180233001709, 0.4357936382293701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9277175664901733})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47216343879699707})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3871306777000427})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36151134967803955})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3410152792930603})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3225986361503601})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35475075244903564})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4176240563392639})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34287840127944946})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3155671630859375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8661143779754639})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44439417123794556})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3628946542739868})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3805277347564697})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3425946831703186})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3132656216621399})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3143477141857147})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2903990149497986})
store['active_learning_steps'][44]['eval_training']['best_epoch']=8
store['active_learning_steps'][44]['acquisition']={'indices': [24212, 24630, 34688, 11271, 31184, 9120, 13521, 27880, 9760, 20050], 'labels': [-1, 5, 9, -1, 9, -1, -1, 2, -1, 9], 'scores': [0.25434690713882446, 0.5635002851486206, 0.6338739991188049, 0.5914043188095093, 0.7158098816871643, 0.4014924168586731, 0.3784204125404358, 0.6200289726257324, 0.41622698307037354, 0.5530845522880554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.113502860069275})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.556380033493042})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3787679076194763})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34890827536582947})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3759515881538391})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3547763228416443})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35183292627334595})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.3251076904296875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.864655613899231})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4889436662197113})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4048156142234802})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3661489486694336})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33225250244140625})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3541885018348694})
store['active_learning_steps'][45]['eval_training']['best_epoch']=5
store['active_learning_steps'][45]['acquisition']={'indices': [47424, 51850, 35504, 49416, 25892, 5904, 16690, 31252, 22169, 12271], 'labels': [-1, -1, -1, 2, -1, 5, -1, 5, 2, 6], 'scores': [0.2771623134613037, 0.30775678157806396, 0.2001807689666748, 0.34246689081192017, 0.3800729513168335, 0.4453997015953064, 0.5027812719345093, 0.5038647651672363, 0.4617527723312378, 0.40936803817749023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9551863670349121})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4718025326728821})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3985973596572876})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3493574261665344})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3287895619869232})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3229474127292633})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.303069144487381})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3349735736846924})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3609086871147156})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29662901163101196})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3509500026702881})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.314716100692749})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3208533525466919})
store['active_learning_steps'][46]['training']['best_epoch']=10
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.2943005859375}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9008784294128418})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46130067110061646})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33035731315612793})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29178062081336975})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29200512170791626})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2532411217689514})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2516961097717285})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2682979702949524})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25507688522338867})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23551906645298004})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23326906561851501})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23214004933834076})
store['active_learning_steps'][46]['eval_training']['best_epoch']=12
store['active_learning_steps'][46]['acquisition']={'indices': [32250, 20170, 49985, 45385, 30884, 9433, 8731, 3588, 32906, 4381], 'labels': [2, 9, 3, -1, 2, 7, 5, -1, 7, -1], 'scores': [0.36575257778167725, 0.5868710279464722, 0.5722454190254211, 0.3034834861755371, 0.5256695449352264, 0.7537919878959656, 0.4277605712413788, 0.3117091655731201, 0.4068825840950012, 0.44801080226898193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9938220381736755})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5320361256599426})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.396668940782547})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34315675497055054})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34110039472579956})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34994739294052124})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3084874749183655})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3487849831581116})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3904830515384674})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3435579538345337})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.3123909423828125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8418834805488586})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5248329639434814})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39629220962524414})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36047664284706116})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3163332939147949})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2979198098182678})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2785796523094177})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2752149701118469})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27014026045799255})
store['active_learning_steps'][47]['eval_training']['best_epoch']=9
store['active_learning_steps'][47]['acquisition']={'indices': [38194, 47587, 15070, 58832, 27479, 15631, 29834, 19545, 46614, 51984], 'labels': [5, 3, -1, 3, -1, -1, -1, -1, -1, -1], 'scores': [0.6216999888420105, 0.43694812059402466, 0.3090623617172241, 0.4267815947532654, 0.3953661322593689, 0.4329029321670532, 0.2876175045967102, 0.4186922311782837, 0.3853346109390259, 0.43688637018203735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9768668413162231})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47601205110549927})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36866649985313416})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32338330149650574})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3017062544822693})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30227410793304443})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3119922876358032})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3075907528400421})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.2943292724609375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8601978421211243})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5569886565208435})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4532901644706726})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3955608904361725})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3218156695365906})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.322059690952301})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29719278216362})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [25091, 54482, 1269, 55260, 44839, 45784, 59739, 54771, 39151, 11600], 'labels': [-1, -1, -1, -1, -1, 9, -1, -1, -1, -1], 'scores': [0.37594807147979736, 0.4532340168952942, 0.643791913986206, 0.4070965051651001, 0.3598442077636719, 0.375365674495697, 0.3886634111404419, 0.505247950553894, 0.221099853515625, 0.5484957695007324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0789086818695068})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.554065465927124})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40258413553237915})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3503914177417755})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33505427837371826})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34873074293136597})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30500808358192444})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33652663230895996})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3515428304672241})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35709136724472046})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.3132322265625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7958365678787231})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4640960693359375})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3869488835334778})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3278975486755371})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3098016679286957})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3256644606590271})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29642727971076965})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3002218008041382})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27680763602256775})
store['active_learning_steps'][49]['eval_training']['best_epoch']=9
store['active_learning_steps'][49]['acquisition']={'indices': [33110, 22370, 47022, 21706, 31738, 11292, 31366, 13741, 42920, 17011], 'labels': [1, 1, 1, 7, 8, 1, 1, -1, -1, 6], 'scores': [0.5080322027206421, 0.3265780210494995, 0.44944262504577637, 0.34683364629745483, 0.42974603176116943, 0.4740927219390869, 0.45941340923309326, 0.21210527420043945, 0.40567755699157715, 0.2837073504924774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.159777283668518})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49196645617485046})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3934760093688965})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33241933584213257})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3377609848976135})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3123925030231476})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3277896046638489})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3081676959991455})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.325105220079422})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32966527342796326})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32758772373199463})
store['active_learning_steps'][50]['training']['best_epoch']=8
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.3052084716796875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8411827087402344})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.545554518699646})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37915414571762085})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3564784526824951})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2944878935813904})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2846025228500366})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30058762431144714})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2772022485733032})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2825818657875061})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2571093738079071})
store['active_learning_steps'][50]['eval_training']['best_epoch']=10
store['active_learning_steps'][50]['acquisition']={'indices': [43496, 11482, 8861, 50308, 40549, 13774, 56774, 47659, 47478, 37413], 'labels': [-1, 8, 7, 3, -1, 2, 9, -1, 8, 5], 'scores': [0.3691070079803467, 0.5005747079849243, 0.3891029953956604, 0.6703892350196838, 0.5634545087814331, 0.4811743497848511, 0.38116276264190674, 0.41823697090148926, 0.37682145833969116, 0.2552748918533325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.094914436340332})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.547542929649353})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35574495792388916})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32907235622406006})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3449590802192688})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31330329179763794})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3236545920372009})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2993360459804535})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29935184121131897})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30626440048217773})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28597551584243774})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3160969018936157})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32954806089401245})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33245909214019775})
store['active_learning_steps'][51]['training']['best_epoch']=11
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.28758662109375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9340073466300964})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.504561185836792})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3699607849121094})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31854498386383057})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3182560205459595})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27257239818573})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2667807638645172})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2602653205394745})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2599527835845947})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2317284643650055})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23965540528297424})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2671945095062256})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25009047985076904})
store['active_learning_steps'][51]['eval_training']['best_epoch']=10
store['active_learning_steps'][51]['acquisition']={'indices': [13328, 32880, 54449, 26938, 43430, 41933, 58798, 24592, 27940, 30016], 'labels': [-1, 0, 9, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.391310453414917, 0.5737696886062622, 0.4584845304489136, 0.47932714223861694, 0.3481297492980957, 0.5324440002441406, 0.3707599639892578, 0.4321955442428589, 0.5833600759506226, 0.5156651735305786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1028646230697632})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4969058632850647})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3805462121963501})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34413427114486694})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32488223910331726})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3123599886894226})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3565009832382202})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30079197883605957})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3061635494232178})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3098030686378479})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3462265133857727})
store['active_learning_steps'][52]['training']['best_epoch']=8
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.2812651611328125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9903669357299805})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5369789600372314})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3478991985321045})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3368174433708191})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2901071310043335})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.301694393157959})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.272674560546875})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27027061581611633})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2708635926246643})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27173662185668945})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [18487, 51604, 59308, 24479, 41933, 45207, 14654, 29713, 48754, 29018], 'labels': [4, -1, -1, 8, 5, -1, -1, 0, -1, -1], 'scores': [0.44361060857772827, 0.21946370601654053, 0.3957703113555908, 0.5421339869499207, 0.6148910522460938, 0.44436806440353394, 0.4619631767272949, 0.37616652250289917, 0.4031355381011963, 0.5036203861236572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1028985977172852})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5186043977737427})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.350220263004303})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3292011022567749})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3291703462600708})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2865588068962097})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3138624131679535})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31836509704589844})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.355182945728302})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.2878121826171875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8895771503448486})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4864106774330139})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39329981803894043})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3198358416557312})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3109814524650574})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3019688129425049})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32333433628082275})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2833433449268341})
store['active_learning_steps'][53]['eval_training']['best_epoch']=8
store['active_learning_steps'][53]['acquisition']={'indices': [31161, 23774, 38584, 58041, 52139, 15482, 49657, 54838, 2381, 10823], 'labels': [-1, -1, -1, -1, 9, -1, -1, -1, 7, -1], 'scores': [0.4018763303756714, 0.33299708366394043, 0.3000530004501343, 0.2319357991218567, 0.455788254737854, 0.4172464609146118, 0.37542974948883057, 0.4258427023887634, 0.47868943214416504, 0.5504294633865356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0304871797561646})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5331826210021973})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3937993049621582})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33601894974708557})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31611084938049316})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3295000493526459})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3390880525112152})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3419899344444275})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.29292734375}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8620349168777466})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46483463048934937})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40508806705474854})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38535112142562866})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33464139699935913})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31999677419662476})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2723689079284668})
store['active_learning_steps'][54]['eval_training']['best_epoch']=7
store['active_learning_steps'][54]['acquisition']={'indices': [36744, 37776, 21990, 892, 10920, 134, 577, 37502, 46658, 8670], 'labels': [1, 8, 1, 6, -1, 1, -1, 6, 8, 2], 'scores': [0.4057677984237671, 0.32249724864959717, 0.32438212633132935, 0.3530089855194092, 0.26963090896606445, 0.47703224420547485, 0.3445083498954773, 0.2932247519493103, 0.39632683992385864, 0.32730478048324585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.161996603012085})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5475071668624878})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.403148889541626})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36704152822494507})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3365147113800049})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.303667813539505})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3451306223869324})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3237481117248535})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30521807074546814})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.3068290283203125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.882717490196228})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5357103943824768})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3913966417312622})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3642255663871765})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3177170753479004})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3377683460712433})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2853028178215027})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2992382049560547})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [54969, 36507, 11894, 24740, 33635, 52413, 32206, 35689, 25062, 13588], 'labels': [6, -1, -1, -1, -1, -1, 8, -1, -1, 8], 'scores': [0.3318445086479187, 0.5282900333404541, 0.40635091066360474, 0.4587188959121704, 0.3505355715751648, 0.3656737804412842, 0.32450348138809204, 0.37217819690704346, 0.387961745262146, 0.40934330224990845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.247718095779419})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5537958741188049})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3399069607257843})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33770304918289185})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32882630825042725})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2973843812942505})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2933216691017151})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3003847897052765})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3363155424594879})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30711156129837036})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2707835693359375}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7238229513168335})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4522024393081665})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30074530839920044})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3114786744117737})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2672068476676941})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28175199031829834})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2501375377178192})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2742351293563843})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2542797327041626})
store['active_learning_steps'][56]['eval_training']['best_epoch']=7
store['active_learning_steps'][56]['acquisition']={'indices': [59718, 23451, 49890, 20402, 9173, 31429, 18813, 17799, 48524, 52232], 'labels': [8, -1, 5, -1, -1, -1, 9, 9, 9, 9], 'scores': [0.351750910282135, 0.5348808765411377, 0.4147007465362549, 0.2614476680755615, 0.4334261417388916, 0.5707712769508362, 0.36965760588645935, 0.34093397855758667, 0.40773385763168335, 0.5259773135185242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2365398406982422})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6013522148132324})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4405630826950073})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3364429473876953})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3248310685157776})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28018733859062195})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30381932854652405})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3089025020599365})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30010172724723816})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.2887685302734375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7299544811248779})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4783306121826172})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38264715671539307})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30066919326782227})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28692328929901123})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27551689743995667})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2728416919708252})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2957054674625397})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [14920, 2762, 38756, 41376, 45778, 51992, 17125, 26568, 27900, 31197], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.40051519870758057, 0.4022563695907593, 0.32600438594818115, 0.42085790634155273, 0.5213223695755005, 0.37531399726867676, 0.4404449462890625, 0.5450782179832458, 0.44825732707977295, 0.27836883068084717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.074180006980896})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5779144167900085})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3592393398284912})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3557698130607605})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29918986558914185})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2891958951950073})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2772553563117981})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.312747061252594})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29440680146217346})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29488813877105713})
store['active_learning_steps'][58]['training']['best_epoch']=7
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.26790810546875}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9218918085098267})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4888169765472412})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36631256341934204})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32636457681655884})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30373018980026245})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27199578285217285})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25489890575408936})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2670927047729492})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24747179448604584})
store['active_learning_steps'][58]['eval_training']['best_epoch']=9
store['active_learning_steps'][58]['acquisition']={'indices': [44855, 53990, 23451, 49192, 22948, 33086, 43950, 52170, 10382, 19539], 'labels': [-1, -1, -1, 2, -1, -1, 9, -1, -1, -1], 'scores': [0.5676624774932861, 0.6787365078926086, 0.6248523592948914, 0.5348113179206848, 0.3845503330230713, 0.6759222745895386, 0.36042797565460205, 0.5807770490646362, 0.3716970682144165, 0.5584496855735779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.23639714717865})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6127132177352905})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44294026494026184})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31628352403640747})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.329836905002594})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2861703932285309})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3373480439186096})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2791130542755127})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28598350286483765})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3323633670806885})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3614453077316284})
store['active_learning_steps'][59]['training']['best_epoch']=8
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9651, 'crossentropy': 0.295605908203125}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8535289764404297})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5541454553604126})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32255199551582336})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32061004638671875})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2782668173313141})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27722108364105225})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24281325936317444})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26525890827178955})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24583081901073456})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24909985065460205})
store['active_learning_steps'][59]['eval_training']['best_epoch']=7
store['active_learning_steps'][59]['acquisition']={'indices': [10539, 55282, 3941, 20233, 14514, 843, 26471, 23028, 50177, 21956], 'labels': [-1, 4, 3, -1, 3, -1, 8, 2, -1, 5], 'scores': [0.4516497254371643, 0.5598706901073456, 0.8243270516395569, 0.4617144465446472, 0.4033215641975403, 0.33683592081069946, 0.44216668605804443, 0.5323339700698853, 0.44135236740112305, 0.45997387170791626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2687900066375732})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6156113743782043})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3960350751876831})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34159940481185913})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3141602575778961})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32159286737442017})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30010223388671875})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2905064523220062})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3054320514202118})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.311845600605011})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2839595675468445})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3108185827732086})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30030763149261475})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34705281257629395})
store['active_learning_steps'][60]['training']['best_epoch']=11
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.2936915771484375}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8387277722358704})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.449209988117218})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3429790735244751})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2909865379333496})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28850609064102173})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2860786020755768})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2333209216594696})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28292611241340637})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23621416091918945})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24202296137809753})
store['active_learning_steps'][60]['eval_training']['best_epoch']=7
store['active_learning_steps'][60]['acquisition']={'indices': [41959, 54671, 40512, 3981, 5659, 15699, 48880, 58706, 5967, 35689], 'labels': [-1, 5, -1, -1, -1, 2, 4, -1, -1, -1], 'scores': [0.4671432375907898, 0.46819642186164856, 0.429579496383667, 0.5814149379730225, 0.34825241565704346, 0.3914710283279419, 0.3953796625137329, 0.6729525923728943, 0.2648228406906128, 0.2933751344680786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1723144054412842})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.555210292339325})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3775838613510132})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3029995858669281})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2975160777568817})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27249062061309814})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2846625745296478})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32713356614112854})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2977808713912964})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2803441650390625}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8996536731719971})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4568560719490051})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4232945144176483})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30614954233169556})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29993921518325806})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29356932640075684})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2794332504272461})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2514246702194214})
store['active_learning_steps'][61]['eval_training']['best_epoch']=8
store['active_learning_steps'][61]['acquisition']={'indices': [25801, 40939, 20678, 42529, 24404, 5158, 1341, 30653, 14124, 35620], 'labels': [-1, -1, -1, -1, 8, 5, 3, -1, -1, -1], 'scores': [0.39036470651626587, 0.3419886827468872, 0.3737192153930664, 0.30043840408325195, 0.21475642919540405, 0.4743303060531616, 0.42430055141448975, 0.33194583654403687, 0.35333526134490967, 0.34366095066070557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0746303796768188})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5393766164779663})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3976113200187683})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3480834364891052})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3097221851348877})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3242923319339752})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29723629355430603})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32806074619293213})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3109503388404846})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3410685658454895})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.2846178466796875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8970925807952881})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4865143895149231})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38265544176101685})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32063770294189453})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3080251216888428})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2878153920173645})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28297317028045654})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26721590757369995})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24513199925422668})
store['active_learning_steps'][62]['eval_training']['best_epoch']=9
store['active_learning_steps'][62]['acquisition']={'indices': [5112, 25224, 48130, 49599, 23619, 51320, 53873, 41982, 8608, 41060], 'labels': [-1, -1, -1, 9, -1, 2, 4, -1, -1, 6], 'scores': [0.5830116868019104, 0.3953399658203125, 0.43978023529052734, 0.479633629322052, 0.46691977977752686, 0.42143720388412476, 0.47894376516342163, 0.4710226058959961, 0.3670830726623535, 0.43679529428482056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1612317562103271})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5504573583602905})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4109363555908203})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2951134443283081})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30061405897140503})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2634406089782715})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.280329167842865})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30002301931381226})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.314361572265625})
store['active_learning_steps'][63]['training']['best_epoch']=6
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.2693481201171875}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9466738700866699})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5490981340408325})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4097336232662201})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3522772789001465})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31351566314697266})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31209278106689453})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27375394105911255})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29016077518463135})
store['active_learning_steps'][63]['eval_training']['best_epoch']=7
store['active_learning_steps'][63]['acquisition']={'indices': [52033, 46915, 44172, 25624, 49395, 45185, 51066, 45422, 50120, 4110], 'labels': [-1, -1, 8, -1, 1, 7, -1, 0, 1, -1], 'scores': [0.4335392713546753, 0.36018872261047363, 0.5435117483139038, 0.49680042266845703, 0.45794814825057983, 0.5039094686508179, 0.23920190334320068, 0.47739893198013306, 0.5321115851402283, 0.35076165199279785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0586100816726685})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.502642810344696})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3718910813331604})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34402352571487427})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3187907338142395})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26982471346855164})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29908210039138794})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25582802295684814})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2777596414089203})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30882686376571655})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26765862107276917})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.2793711181640625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8950135707855225})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5587676763534546})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3645249009132385})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33617860078811646})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30896416306495667})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27158060669898987})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2824394404888153})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2862165868282318})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2693859934806824})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24475692212581635})
store['active_learning_steps'][64]['eval_training']['best_epoch']=10
store['active_learning_steps'][64]['acquisition']={'indices': [4827, 32892, 7286, 10174, 50912, 23951, 42136, 46106, 11899, 56826], 'labels': [-1, -1, -1, -1, 6, -1, -1, -1, -1, -1], 'scores': [0.36871254444122314, 0.35360944271087646, 0.4388742446899414, 0.40776193141937256, 0.4926779568195343, 0.4045918583869934, 0.2853015065193176, 0.32994067668914795, 0.47316956520080566, 0.4187766909599304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3010139465332031})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6177883744239807})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42761456966400146})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36396172642707825})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3741600811481476})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32407793402671814})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32305335998535156})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31865525245666504})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3169657588005066})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3222388029098511})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3006320595741272})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35338109731674194})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31905385851860046})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32985419034957886})
store['active_learning_steps'][65]['training']['best_epoch']=11
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.2913223388671875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9217014312744141})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5494939684867859})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37249863147735596})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3217040002346039})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3104206621646881})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2917376756668091})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28611552715301514})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2838086485862732})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2728133201599121})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2669333219528198})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2638717293739319})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24135570228099823})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2653709650039673})
store['active_learning_steps'][65]['eval_training']['best_epoch']=12
store['active_learning_steps'][65]['acquisition']={'indices': [4675, 47723, 51155, 34783, 4058, 11271, 1891, 27595, 14658, 11033], 'labels': [-1, 8, 4, -1, 8, -1, -1, 6, -1, -1], 'scores': [0.514283299446106, 0.5464842915534973, 0.5732417106628418, 0.3926529288291931, 0.6904754042625427, 0.629564642906189, 0.5246304273605347, 0.6161433756351471, 0.38920748233795166, 0.4485096335411072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1127156019210815})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4833148717880249})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35862499475479126})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30507469177246094})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2917397618293762})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27565816044807434})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29142147302627563})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2880593538284302})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27481353282928467})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2754814624786377})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30661290884017944})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30911242961883545})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.28288642578125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9744885563850403})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5130507946014404})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4099016785621643})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31045395135879517})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29502755403518677})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2618611454963684})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23824556171894073})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2591850459575653})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.227679044008255})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25094324350357056})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2343136966228485})
store['active_learning_steps'][66]['eval_training']['best_epoch']=9
store['active_learning_steps'][66]['acquisition']={'indices': [23816, 44095, 2606, 46758, 32358, 48149, 23523, 56662, 41982, 30851], 'labels': [-1, 2, -1, -1, -1, -1, -1, 0, -1, -1], 'scores': [0.5682187080383301, 0.4574354887008667, 0.3853387236595154, 0.5231065154075623, 0.446661114692688, 0.48816990852355957, 0.35305583477020264, 0.44324684143066406, 0.5839701890945435, 0.3296605944633484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9586061239242554})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.46738922595977783})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3486090302467346})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31518083810806274})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30064162611961365})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29706478118896484})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26686471700668335})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26881980895996094})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2879587709903717})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29025131464004517})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.255182373046875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8759846687316895})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5158765316009521})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40196046233177185})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33706390857696533})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28272944688796997})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25848808884620667})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25446295738220215})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25467628240585327})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25288793444633484})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [17469, 4824, 5224, 57612, 15774, 5938, 24129, 40938, 55028, 38604], 'labels': [-1, -1, -1, -1, 3, -1, -1, 9, 3, 5], 'scores': [0.4004960060119629, 0.2715451717376709, 0.42861342430114746, 0.2687181234359741, 0.3332393765449524, 0.34450483322143555, 0.4393618702888489, 0.441659152507782, 0.4988069534301758, 0.5761860609054565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1174085140228271})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5469659566879272})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3820040225982666})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34608718752861023})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3060099482536316})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31076452136039734})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2525860667228699})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30824071168899536})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29033488035202026})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29941055178642273})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.264352685546875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8850364089012146})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.487059086561203})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35715025663375854})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33290666341781616})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27921217679977417})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26189497113227844})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26675426959991455})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2653690278530121})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2768442928791046})
store['active_learning_steps'][68]['eval_training']['best_epoch']=6
store['active_learning_steps'][68]['acquisition']={'indices': [21117, 18193, 35205, 5679, 37183, 46248, 15510, 8598, 38307, 49828], 'labels': [-1, -1, 6, 3, -1, 7, 2, -1, -1, -1], 'scores': [0.3569899797439575, 0.4042612314224243, 0.4776722192764282, 0.5111435651779175, 0.36768901348114014, 0.38897794485092163, 0.3990435004234314, 0.22624826431274414, 0.26738953590393066, 0.4787919521331787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0127408504486084})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.523574709892273})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3617439270019531})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30323585867881775})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28134238719940186})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2617915868759155})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26647141575813293})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25609952211380005})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2605663239955902})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2795426845550537})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2647976577281952})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2588698974609375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8446836471557617})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47990334033966064})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37878721952438354})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35311371088027954})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30696767568588257})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2768043577671051})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25156497955322266})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2380322366952896})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26980558037757874})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2139584720134735})
store['active_learning_steps'][69]['eval_training']['best_epoch']=10
store['active_learning_steps'][69]['acquisition']={'indices': [58275, 34539, 50695, 10053, 9383, 46253, 15926, 45626, 4877, 2807], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.38806045055389404, 0.4369078278541565, 0.3094896078109741, 0.4748228192329407, 0.311470627784729, 0.3142009973526001, 0.4268985986709595, 0.38327038288116455, 0.3235299289226532, 0.37312376499176025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0432246923446655})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5202583074569702})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33933025598526})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29204508662223816})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29810023307800293})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27693378925323486})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27837854623794556})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2313079684972763})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27132588624954224})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26559796929359436})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29622215032577515})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2558263427734375}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8790624737739563})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5090669393539429})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.36222320795059204})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3198111653327942})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.300418883562088})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2540304958820343})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24990016222000122})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24195614457130432})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23441380262374878})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2348472774028778})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [31114, 8301, 32744, 21262, 33505, 52761, 15656, 38275, 5065, 31413], 'labels': [4, -1, -1, 4, 2, 9, -1, 2, 2, 5], 'scores': [0.5633285045623779, 0.29937875270843506, 0.3253568410873413, 0.44660669565200806, 0.636168360710144, 0.4367837905883789, 0.4550600051879883, 0.6383165717124939, 0.691867470741272, 0.5088967084884644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.353771448135376})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5598546266555786})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3759492337703705})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3254157304763794})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29826098680496216})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28959521651268005})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2580402195453644})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2853860557079315})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27108854055404663})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30472418665885925})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2494625244140625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9162947535514832})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.489703893661499})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3653603494167328})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31035733222961426})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3016413450241089})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3221041262149811})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2839839458465576})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27324554324150085})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27955344319343567})
store['active_learning_steps'][71]['eval_training']['best_epoch']=8
store['active_learning_steps'][71]['acquisition']={'indices': [33181, 43838, 16690, 29715, 17135, 39545, 57573, 1942, 39442, 26768], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.2541912794113159, 0.41619873046875, 0.5647879838943481, 0.4299207925796509, 0.3325093984603882, 0.5717760324478149, 0.43799853324890137, 0.32646942138671875, 0.2863762378692627, 0.31609606742858887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1628475189208984})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5506746172904968})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3765592575073242})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32793450355529785})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3271438479423523})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2898106276988983})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28379765152931213})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26063841581344604})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.248896986246109})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29593056440353394})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2722243070602417})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29184120893478394})
store['active_learning_steps'][72]['training']['best_epoch']=9
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.24737021484375}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8793008327484131})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4907988905906677})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36687248945236206})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3146018087863922})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.298652708530426})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26555997133255005})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25401225686073303})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2563909888267517})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25175726413726807})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22904255986213684})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23208825290203094})
store['active_learning_steps'][72]['eval_training']['best_epoch']=10
store['active_learning_steps'][72]['acquisition']={'indices': [58459, 30306, 52942, 47140, 32747, 41691, 48752, 17521, 57186, 15068], 'labels': [-1, -1, -1, 3, 8, -1, -1, 3, -1, -1], 'scores': [0.3476431965827942, 0.36225342750549316, 0.6741976141929626, 0.3341027498245239, 0.5468196272850037, 0.451279878616333, 0.4518578052520752, 0.4864172339439392, 0.3482780456542969, 0.3546229600906372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.1317777633666992})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6038267016410828})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3653915524482727})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3029749095439911})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3473675847053528})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28290021419525146})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29503142833709717})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28869789838790894})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26376813650131226})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2684093117713928})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24462714791297913})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2595673203468323})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2544472813606262})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2735700011253357})
store['active_learning_steps'][73]['training']['best_epoch']=11
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.253371337890625}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.870478630065918})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47370368242263794})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31444916129112244})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31790921092033386})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28475525975227356})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24962714314460754})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24226877093315125})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2330605685710907})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25185132026672363})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2358531951904297})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23262521624565125})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21714982390403748})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.19817107915878296})
store['active_learning_steps'][73]['eval_training']['best_epoch']=13
store['active_learning_steps'][73]['acquisition']={'indices': [48360, 40372, 42416, 11366, 30120, 17868, 53990, 30587, 45003, 3115], 'labels': [3, -1, -1, -1, -1, -1, -1, -1, 5, -1], 'scores': [0.34045207500457764, 0.4477981925010681, 0.3639211654663086, 0.2649703025817871, 0.24680733680725098, 0.2630910873413086, 0.6264410614967346, 0.526611328125, 0.3738749623298645, 0.35273098945617676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9845359325408936})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5229747891426086})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38647565245628357})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3161761462688446})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.308089017868042})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2625970244407654})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26743802428245544})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2616167962551117})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28040969371795654})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2750071883201599})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3046078383922577})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.25973505859375}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8737295866012573})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.47184479236602783})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3755720555782318})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3254304528236389})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2575787901878357})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26802700757980347})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27115219831466675})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.261654794216156})
store['active_learning_steps'][74]['eval_training']['best_epoch']=5
store['active_learning_steps'][74]['acquisition']={'indices': [43235, 37974, 9436, 139, 44167, 47476, 1111, 13156, 14722, 31301], 'labels': [-1, 2, 4, -1, 4, -1, -1, 2, 0, 5], 'scores': [0.5068567395210266, 0.5627528429031372, 0.46953654289245605, 0.18015944957733154, 0.3641323447227478, 0.43374842405319214, 0.3737049698829651, 0.5195868611335754, 0.6335688829421997, 0.569672703742981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.030218482017517})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4781971871852875})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3803151845932007})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3096048831939697})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2670774459838867})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2629062533378601})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24246525764465332})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2741970419883728})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2524570822715759})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2843908667564392})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2498362548828125}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0426874160766602})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5377278923988342})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41895708441734314})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3757677376270294})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3045523464679718})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2978760004043579})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2659391760826111})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2605533003807068})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2617174983024597})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [7168, 23578, 32982, 24278, 32776, 39616, 41630, 33061, 28639, 41832], 'labels': [8, 2, -1, 3, 4, 7, -1, -1, -1, 2], 'scores': [0.4652886390686035, 0.42134690284729004, 0.36801624298095703, 0.47772789001464844, 0.5115333795547485, 0.5480997562408447, 0.48731911182403564, 0.49062252044677734, 0.4065493941307068, 0.44305551052093506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1757845878601074})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5259581208229065})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3963501751422882})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3426024913787842})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2719951868057251})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.253278911113739})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2774531841278076})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28118300437927246})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24774715304374695})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2872990369796753})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2833484411239624})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2533941864967346})
store['active_learning_steps'][76]['training']['best_epoch']=9
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9743, 'crossentropy': 0.2288876708984375}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9524993896484375})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5040695667266846})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3772444725036621})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31123086810112})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27852311730384827})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2994786500930786})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2559949457645416})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2518589198589325})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2476624846458435})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27222898602485657})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2424187809228897})
store['active_learning_steps'][76]['eval_training']['best_epoch']=11
store['active_learning_steps'][76]['acquisition']={'indices': [40036, 47172, 18894, 50994, 9098, 6839, 24052, 52661, 32173, 13404], 'labels': [-1, -1, -1, 7, 2, 2, 4, 3, 7, -1], 'scores': [0.4981541633605957, 0.4052011966705322, 0.3516879081726074, 0.5396860241889954, 0.5042487978935242, 0.4274963140487671, 0.34459930658340454, 0.5878201723098755, 0.6342217922210693, 0.3828974962234497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.101888656616211})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5620715618133545})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4228595495223999})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30300819873809814})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2720268964767456})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2781226336956024})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.21802636981010437})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26305830478668213})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24080374836921692})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2636678218841553})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2493052978515625}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9182172417640686})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48880913853645325})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3867765963077545})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3067673444747925})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30006861686706543})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24771800637245178})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2958880066871643})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26458466053009033})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2543627917766571})
store['active_learning_steps'][77]['eval_training']['best_epoch']=6
store['active_learning_steps'][77]['acquisition']={'indices': [5430, 11729, 11531, 26568, 32573, 51146, 36515, 11570, 216, 23751], 'labels': [8, -1, -1, -1, 8, -1, 3, 3, 0, -1], 'scores': [0.3489333391189575, 0.34391629695892334, 0.19531136751174927, 0.506611168384552, 0.5382730960845947, 0.33628618717193604, 0.4951320290565491, 0.4684341549873352, 0.3900185823440552, 0.5013424158096313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.146822214126587})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5231069922447205})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.41284510493278503})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2911885976791382})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2916720509529114})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2746417820453644})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24093881249427795})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2479260265827179})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26584476232528687})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24357467889785767})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.2440880615234375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9662247896194458})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5020865797996521})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36714500188827515})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32289400696754456})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3296642303466797})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2907933294773102})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26675087213516235})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27457112073898315})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2680817246437073})
store['active_learning_steps'][78]['eval_training']['best_epoch']=7
store['active_learning_steps'][78]['acquisition']={'indices': [12999, 31557, 120, 24753, 706, 36626, 41852, 52610, 54599, 32130], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4385889768600464, 0.47331392765045166, 0.3559681177139282, 0.4948955774307251, 0.42579150199890137, 0.3109797239303589, 0.4179035425186157, 0.2915767431259155, 0.3634147644042969, 0.41171586513519287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.3123623132705688})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6771165132522583})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4472062885761261})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37687206268310547})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2917231321334839})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2619410753250122})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24787461757659912})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26862242817878723})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23088648915290833})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24931085109710693})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22835367918014526})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2306242287158966})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2475546896457672})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25643226504325867})
store['active_learning_steps'][79]['training']['best_epoch']=11
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.2591315185546875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9380419254302979})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5062121748924255})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3525170683860779})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3046525716781616})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30165624618530273})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2505463659763336})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22724001109600067})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23467950522899628})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23667000234127045})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22219109535217285})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22609473764896393})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22089973092079163})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22179263830184937})
store['active_learning_steps'][79]['eval_training']['best_epoch']=12
store['active_learning_steps'][79]['acquisition']={'indices': [31537, 26571, 5905, 55434, 42366, 14729, 47647, 36392, 55683, 48288], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.42841148376464844, 0.40256357192993164, 0.4283810257911682, 0.3567514419555664, 0.36412906646728516, 0.4248450994491577, 0.4709489345550537, 0.6119664311408997, 0.4559410810470581, 0.39680373668670654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.1308443546295166})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5826038122177124})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42720499634742737})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3164820671081543})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3261078894138336})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2798718214035034})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2668553590774536})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2614235579967499})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.264523983001709})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28627699613571167})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27149152755737305})
store['active_learning_steps'][80]['training']['best_epoch']=8
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.255659130859375}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9892035126686096})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5359690189361572})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3974568247795105})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3231492340564728})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2895423173904419})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2627084255218506})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2849853038787842})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23396077752113342})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25223761796951294})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2157650887966156})
store['active_learning_steps'][80]['eval_training']['best_epoch']=10
store['active_learning_steps'][80]['acquisition']={'indices': [1468, 13814, 46393, 48347, 47274, 22196, 54896, 58172, 37347, 19537], 'labels': [-1, -1, -1, -1, 8, -1, 8, -1, 2, -1], 'scores': [0.4018362760543823, 0.4461236596107483, 0.393521249294281, 0.4729103446006775, 0.5697270631790161, 0.3408575654029846, 0.5496946573257446, 0.5516974329948425, 0.5384842157363892, 0.4902385473251343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.361283779144287})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6044117212295532})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4346293807029724})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40480837225914})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3086719512939453})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33024898171424866})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2995429039001465})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3198758065700531})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.264801561832428})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25526827573776245})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2780686318874359})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2791213393211365})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2805463373661041})
store['active_learning_steps'][81]['training']['best_epoch']=10
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.251853955078125}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9884904623031616})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.587263286113739})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4231795072555542})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31621336936950684})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2832667827606201})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2858923077583313})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2968163788318634})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24879969656467438})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2292531579732895})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24393713474273682})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25684189796447754})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2284139096736908})
store['active_learning_steps'][81]['eval_training']['best_epoch']=12
store['active_learning_steps'][81]['acquisition']={'indices': [35747, 3209, 1518, 54167, 5038, 48968, 59722, 10520, 32793, 10393], 'labels': [5, -1, 9, -1, -1, 9, -1, -1, -1, -1], 'scores': [0.6647237539291382, 0.4851440191268921, 0.42325693368911743, 0.6606738567352295, 0.18561744689941406, 0.4293838143348694, 0.45183032751083374, 0.6206448674201965, 0.5175915956497192, 0.46299052238464355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2333524227142334})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5866870880126953})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3880820870399475})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35541000962257385})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2804414629936218})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.274742990732193})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26094815135002136})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2719324827194214})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2719946801662445})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.21909931302070618})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2627175748348236})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23936596512794495})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24949777126312256})
store['active_learning_steps'][82]['training']['best_epoch']=10
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.21728603515625}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0278410911560059})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5306339859962463})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34013259410858154})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3037678599357605})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.294208288192749})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2786644995212555})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2651319205760956})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23624569177627563})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26411888003349304})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.22835074365139008})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.22827088832855225})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2279607057571411})
store['active_learning_steps'][82]['eval_training']['best_epoch']=12
store['active_learning_steps'][82]['acquisition']={'indices': [57416, 12944, 21840, 50980, 16348, 10979, 58649, 10744, 26266, 45320], 'labels': [-1, -1, 9, -1, -1, -1, 0, 7, 7, -1], 'scores': [0.4234932065010071, 0.39385926723480225, 0.5327230095863342, 0.5798976421356201, 0.4752931594848633, 0.390078067779541, 0.41113632917404175, 0.5532782673835754, 0.6166426539421082, 0.24421656131744385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2334015369415283})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5954412221908569})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3658970594406128})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3311309814453125})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2714874744415283})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.239630326628685})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25614163279533386})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27342504262924194})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2736448347568512})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.240008349609375}
