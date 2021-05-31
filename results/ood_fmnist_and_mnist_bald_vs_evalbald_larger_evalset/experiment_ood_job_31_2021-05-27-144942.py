store = {}
store['timestamp']=1622123382
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=31']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=31
store['worker_id']=31
store['num_workers']=80
store['config']={'seed': 1266, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.6730666160583496})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8378591537475586})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.3676321506500244})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.5308666229248047})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.735665798187256})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5937, 'crossentropy': 3.120914453125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 32832], ['ood', 14335], ['id', 24014], ['ood', 8474], ['ood', 29180]], 'labels': [-1, -1, 6, -1, -1], 'scores': [1.4514035867233872, 2.534800080403725, 3.3366752468755596, 3.897064510327228, 4.224703269963122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.4327096939086914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.704064130783081})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9041314125061035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.27384614944458})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.069884777069092})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.7367405891418457})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 3.1465849609375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 36675], ['ood', 7649], ['ood', 56936], ['ood', 17077], ['ood', 3362]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5313306816835635, 2.706947852249729, 3.500524570927083, 4.028042874331852, 4.304046728850724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.217573881149292})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.8356804847717285})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2635316848754883})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.4436771869659424})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3935763835906982})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5965, 'crossentropy': 2.8519412109375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 22141], ['ood', 38394], ['ood', 22100], ['ood', 31063], ['ood', 19495]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4146449449441505, 2.53444007017959, 3.4047221296681345, 3.958688703673861, 4.2667579310058255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.7011735439300537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.2541279792785645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.754443645477295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.7617223262786865})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.7812390327453613})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.628862142562866})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.0894293785095215})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5882, 'crossentropy': 3.879694921875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 19599], ['ood', 50294], ['ood', 16228], ['ood', 12585], ['id', 1254]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.5695319442961781, 2.744305669524543, 3.61489889063974, 4.12124719017875, 4.370301250371705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.240311622619629})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.676102876663208})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.86586856842041})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7110390663146973})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9586453437805176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.338435173034668})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2151875495910645})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6276, 'crossentropy': 2.8223130859375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 35705], ['ood', 34366], ['ood', 10337], ['ood', 23020], ['ood', 27247]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.440742327373414, 2.651257711309431, 3.4815551742951047, 4.024378042739231, 4.313938131452119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.6490297317504883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0493485927581787})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.1678647994995117})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.6677632331848145})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.669887065887451})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6003, 'crossentropy': 3.101873046875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 8553], ['id', 59771], ['ood', 54196], ['ood', 14111], ['ood', 43105]], 'labels': [-1, 4, -1, -1, -1], 'scores': [1.5306015341734203, 2.808571808990017, 3.682249412749096, 4.1505539391580895, 4.378438326461872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.15299654006958})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6149635314941406})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.803011894226074})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.213292121887207})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8564460277557373})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8179283142089844})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1260552406311035})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.625478744506836})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.4601683616638184})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2045748233795166})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2537975311279297})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.658158779144287})
store['active_learning_steps'][6]['training']['best_epoch']=9
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6052, 'crossentropy': 3.67874453125}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 23648], ['ood', 18245], ['ood', 56866], ['ood', 48431], ['ood', 52494]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6211326296587893, 2.8452830304748846, 3.726182867646779, 4.212902988087961, 4.429169898742705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1203956604003906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.699368953704834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.067330837249756})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2552475929260254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3501038551330566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8677892684936523})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.401966094970703})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6026, 'crossentropy': 3.502859765625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 25180], ['ood', 3370], ['ood', 40091], ['ood', 11566], ['ood', 25994]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6828894456097148, 2.8755254660557497, 3.7304478069729665, 4.200899759552819, 4.42676892678892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.9544339179992676})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4062530994415283})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.1975574493408203})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.9831690788269043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9844908714294434})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9640917778015137})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0300369262695312})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.333458185195923})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.1241703125}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 10918], ['ood', 25294], ['ood', 48970], ['ood', 47214], ['ood', 46344]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5195582809394885, 2.775732856633211, 3.615838523959747, 4.106192963800207, 4.361244900253608]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.428673267364502})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.1519219875335693})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3398165702819824})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.7591500282287598})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.412095069885254})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.7083683013916016})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.5341973304748535})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.3531265258789062})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.705246925354004})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.6023778915405273})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.7634527683258057})
store['active_learning_steps'][9]['training']['best_epoch']=8
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5957, 'crossentropy': 3.52302890625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 986], ['ood', 34267], ['ood', 46232], ['ood', 2450], ['ood', 19276]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.659702290251859, 2.858915277668235, 3.6905792194581553, 4.1774815944296435, 4.4161427572163365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.100583791732788})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.924203872680664})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.2014575004577637})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.2235569953918457})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9944279193878174})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1305556297302246})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.4703879356384277})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.728199005126953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5479419231414795})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6175, 'crossentropy': 3.1999443359375}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 10243], ['ood', 50622], ['ood', 19202], ['ood', 20157], ['id', 33188]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.4991668476214521, 2.7351060273208097, 3.5586832400816437, 4.069327322745044, 4.328912678723174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.8179714679718018})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.4736390113830566})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.600330352783203})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7178752422332764})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.785305976867676})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.937562942504883})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.2844581604003906})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.510108470916748})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.455970048904419})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.126138210296631})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.490952734375}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 37720], ['ood', 47487], ['ood', 36281], ['ood', 59158], ['ood', 48814]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.7118536170141745, 2.916134972038986, 3.7687317158225007, 4.2406881770010125, 4.450494849333032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.827499270439148})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.0117549896240234})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4949636459350586})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6641814708709717})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5603084564208984})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0428450107574463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.904921293258667})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.2591519355773926})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6445, 'crossentropy': 2.7908103515625}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 27530], ['ood', 45793], ['ood', 16995], ['ood', 4694], ['ood', 25907]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5158753017439404, 2.7021929210181965, 3.541282430173572, 4.060399724864303, 4.3389895775075065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8666757345199585})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.3173985481262207})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6103882789611816})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7484939098358154})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.997170925140381})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 2.500791015625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 52346], ['ood', 38796], ['ood', 24294], ['ood', 33522], ['ood', 22807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4172482494786531, 2.6317747697320715, 3.4624041720941205, 3.989274277324932, 4.27042976496886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.113300323486328})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.620253086090088})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7339773178100586})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.11984920501709})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0987250804901123})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.384756088256836})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5431149005889893})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1641149520874023})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.748561143875122})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 3.527144140625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 51634], ['ood', 5728], ['ood', 7937], ['id', 7327], ['ood', 55970]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.516950521875847, 2.686335904271754, 3.516627350766356, 4.0294536211889795, 4.327636288320239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.056370973587036})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4490277767181396})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.760134220123291})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.988825798034668})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.3314061164855957})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3592586517333984})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.916771411895752})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.422025203704834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.860759973526001})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.597506284713745})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 3.22030703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 24142], ['ood', 28243], ['ood', 36281], ['ood', 23096], ['ood', 56866]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4820635128060764, 2.767467317613805, 3.617902135235724, 4.143076090158622, 4.392441013363777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8023467063903809})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4728312492370605})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.406921863555908})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.717132091522217})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.671128511428833})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 2.5038775390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 23041], ['ood', 35346], ['ood', 22807], ['ood', 4799], ['ood', 19089]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4268557082516486, 2.515328153936486, 3.3086418576437406, 3.8612292554993672, 4.1862294598108125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8814480304718018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.319000720977783})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.576347827911377})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5968425273895264})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.764054775238037})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.497899055480957})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9321584701538086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.042755603790283})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.088818073272705})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1404080390930176})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6261, 'crossentropy': 3.067033203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 28662], ['ood', 18502], ['ood', 23041], ['ood', 19488], ['ood', 20942]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5483733624010365, 2.7347967072007826, 3.6134511681288, 4.1133246393649205, 4.363549666590448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.037360668182373})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.3829448223114014})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8170247077941895})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.346494197845459})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9837188720703125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.0340757369995117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.3734147548675537})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.3702220916748047})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.447484016418457})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.626, 'crossentropy': 3.406237109375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 12223], ['ood', 39561], ['ood', 39184], ['ood', 37799], ['ood', 59409]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4979872954106603, 2.8064159527542643, 3.6013505642229466, 4.093430589379394, 4.367931143862225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8622245788574219})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3782238960266113})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.908745050430298})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8085718154907227})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6371, 'crossentropy': 1.9023330078125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 59424], ['ood', 36805], ['ood', 49850], ['ood', 45048], ['ood', 13306]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1979289084076232, 2.1378126209149797, 2.918920334109009, 3.468110010444816, 3.8472617375530325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.0345664024353027})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.648249626159668})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8329763412475586})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0776801109313965})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.6335666179656982})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.3007450103759766})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9830310344696045})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.7425103187561035})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.229994297027588})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.619, 'crossentropy': 3.496613671875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 1983], ['ood', 8621], ['ood', 9116], ['ood', 45209], ['ood', 43823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5686707522669057, 2.8668589957727155, 3.6514491381628424, 4.12320161494637, 4.369361037302662]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.022078275680542})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.5316848754882812})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7246580123901367})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.790996551513672})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2193899154663086})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 2.5856080078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 6965], ['ood', 53551], ['ood', 39461], ['ood', 47613], ['ood', 5928]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3540449819766562, 2.4958513654877494, 3.3077318344520616, 3.825531739850568, 4.14434470040846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1072607040405273})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5334811210632324})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9686176776885986})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.8860700130462646})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.084789276123047})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2351393699645996})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2059478759765625})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.383592128753662})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.277595043182373})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.94287109375})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.424635887145996})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.362576961517334})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.632, 'crossentropy': 3.68641484375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 9870], ['ood', 53674], ['ood', 40907], ['ood', 26358], ['ood', 6081]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5879639699135626, 2.848603445218663, 3.7001108415153894, 4.166311969840049, 4.409377257205106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.7998212575912476})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.279599905014038})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6391115188598633})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4723129272460938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6563167572021484})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6812033653259277})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8565964698791504})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6286, 'crossentropy': 2.6968734375}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 30199], ['ood', 59405], ['ood', 22412], ['ood', 34822], ['ood', 33186]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.449920928724139, 2.656251676259961, 3.483515874250342, 4.021097770211792, 4.298825479751175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0864109992980957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.540801525115967})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.725165367126465})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.181028366088867})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.893904685974121})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9915177822113037})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6434, 'crossentropy': 2.8308306640625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 17253], ['ood', 25107], ['ood', 23372], ['ood', 8462], ['ood', 45329]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4657225947522168, 2.7206664086603087, 3.5776908981985613, 4.089209291286673, 4.359202545204563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.028247356414795})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.727013111114502})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5739858150482178})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7831971645355225})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0078792572021484})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.297565221786499})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6157, 'crossentropy': 2.6607630859375}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 56769], ['ood', 10910], ['ood', 45705], ['ood', 53048], ['ood', 58285]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.485617831839579, 2.641773226718899, 3.4448409016543495, 3.961652857936949, 4.263770754297409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7809009552001953})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.136935234069824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.789841413497925})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.650421142578125})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5051498413085938})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.8739805221557617})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.201307535171509})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.23966121673584})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.895979166030884})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.999955415725708})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.2007546424865723})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1096177101135254})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6398, 'crossentropy': 3.088307421875}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 54757], ['ood', 32006], ['ood', 53956], ['ood', 21479], ['ood', 17941]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4955896768105883, 2.728674737316572, 3.6258178018429454, 4.169668303424952, 4.415360538913879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.139112949371338})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.6720991134643555})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8965768814086914})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0578718185424805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1849558353424072})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.441279649734497})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1159610748291016})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.6106045246124268})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.617, 'crossentropy': 3.625316796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 31574], ['ood', 4899], ['ood', 29427], ['ood', 9659], ['ood', 15462]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4441352822340636, 2.638793883598482, 3.5159715368515716, 4.059400705083432, 4.316938132214373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2928414344787598})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7586326599121094})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.658583641052246})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.916203498840332})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.7695231437683105})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1248879432678223})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.120267391204834})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2506089210510254})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.928236484527588})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6254, 'crossentropy': 3.3049671875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 45462], ['ood', 47923], ['ood', 34908], ['ood', 23692], ['ood', 17602]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5092445160622403, 2.755370809541005, 3.6496819125447866, 4.159302612911597, 4.3971855899173615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.269598960876465})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.5529799461364746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.923990488052368})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1124801635742188})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1667518615722656})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.5275063514709473})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.411992073059082})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.194993734359741})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 3.3284046875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 54419], ['ood', 26863], ['ood', 5407], ['ood', 19215], ['ood', 40798]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4119591690993727, 2.6060671043111476, 3.395070843004847, 3.9413013716105425, 4.246415164201401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.877169132232666})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.756948232650757})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7243893146514893})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8384761810302734})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6269, 'crossentropy': 1.9322505859375}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 33867], ['ood', 16736], ['id', 54217], ['ood', 6047], ['id', 11446]], 'labels': [-1, -1, 8, -1, 5], 'scores': [1.256419888872513, 2.2209124821621327, 2.9053189263886363, 3.4559802826066903, 3.8222745469144375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9323904514312744})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.499415874481201})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3380320072174072})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5574731826782227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.743868827819824})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9322128295898438})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6361, 'crossentropy': 2.4938177734375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 28856], ['ood', 34847], ['ood', 47303], ['ood', 34897], ['ood', 44952]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.604974406171622, 2.8099868791173126, 3.630127433605421, 4.096088966787919, 4.36668010960378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.7219409942626953})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.091212511062622})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6204380989074707})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8110861778259277})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4798359870910645})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.818760871887207})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.826815605163574})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.1140832901000977})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.114100933074951})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.042975902557373})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.3898673057556152})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2152836322784424})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6352, 'crossentropy': 3.21346328125}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 48435], ['ood', 43689], ['ood', 57255], ['ood', 21824], ['ood', 43224]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5530977591337507, 2.819731075111794, 3.665547833793723, 4.148278707461908, 4.4051458473786145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.6476783752441406})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.057568073272705})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6820249557495117})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5828278064727783})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.996325969696045})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.798041820526123})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 2.77396015625}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 19931], ['ood', 24637], ['ood', 19982], ['ood', 13214], ['ood', 18551]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4808145443838265, 2.765638202388769, 3.6755536746186923, 4.152678119626312, 4.386476726440517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.8542920351028442})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.304779529571533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.2239208221435547})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5594301223754883})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.695614814758301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.889357566833496})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.1118006706237793})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6481, 'crossentropy': 2.6835650390625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 52322], ['ood', 15845], ['ood', 54688], ['ood', 45616], ['ood', 56866]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5513078592808203, 2.6928461698500707, 3.5568886552618775, 4.059729754150504, 4.333364922285548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.7700622081756592})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.204463481903076})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6191277503967285})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.22860050201416})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.7296605110168457})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0437307357788086})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0992817878723145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.2922139167785645})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.527867317199707})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.8326621055603027})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2344021797180176})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.611287109375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 45161], ['ood', 34847], ['ood', 47717], ['ood', 22679], ['ood', 1158]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5640762462457705, 2.776544547500736, 3.641690765548276, 4.146108801048096, 4.402962013368075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7207050323486328})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.9722518920898438})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.5367591381073})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6620030403137207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.5903820991516113})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.7686328887939453})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.885709285736084})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9907660484313965})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6385, 'crossentropy': 2.7599376953125}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 36643], ['ood', 29844], ['ood', 9699], ['ood', 43630], ['ood', 48435]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5328442092875196, 2.684430520863893, 3.558360217275677, 4.072226504543913, 4.35356694509167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9416509866714478})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.623204231262207})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.799056053161621})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.68276047706604})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.071168899536133})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.0728988647460938})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6303, 'crossentropy': 2.85525625}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 42583], ['ood', 47636], ['ood', 56741], ['ood', 31958], ['ood', 24856]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5043241966085237, 2.713612781520622, 3.609507913965526, 4.092463060177973, 4.353251151283764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7289413213729858})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.1943254470825195})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1858925819396973})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.574495315551758})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.561713695526123})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.752365827560425})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0186400413513184})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.846562147140503})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.9614148139953613})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6389, 'crossentropy': 2.9916564453125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 20982], ['ood', 14065], ['ood', 19525], ['ood', 6857], ['ood', 5684]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.485261971571346, 2.6825461876287133, 3.5196307031599545, 4.0352586346867305, 4.324158956372351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.9182544946670532})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.265718698501587})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.230695962905884})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3743176460266113})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5511422157287598})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.6006197929382324})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.554504871368408})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7193071842193604})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5081071853637695})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6523, 'crossentropy': 2.631099609375}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 9864], ['ood', 9699], ['ood', 57570], ['ood', 10237], ['ood', 42957]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4923664013857216, 2.7594751367150243, 3.681006912369056, 4.1968953114808105, 4.423020006260108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5797208547592163})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1278860569000244})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.5804855823516846})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8532204627990723})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6354, 'crossentropy': 1.71704921875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 32046], ['ood', 35801], ['ood', 18412], ['ood', 55084], ['ood', 16909]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.258991072709962, 2.23770076313113, 3.079776601292898, 3.64520490867573, 4.001954890702624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.827868938446045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.6647493839263916})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7496891021728516})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.6478140354156494})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.7474160194396973})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0792272090911865})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6268, 'crossentropy': 2.84298359375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 36643], ['ood', 18324], ['ood', 13306], ['ood', 10855], ['ood', 36550]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4834765995886077, 2.6186039663653364, 3.478184105908939, 4.011624607677451, 4.3218049876663125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.808392882347107})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.583199977874756})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.055694580078125})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8330559730529785})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9265589714050293})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.976189613342285})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6562180519104004})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9203386306762695})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1405820846557617})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.215301990509033})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4524264335632324})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5534892082214355})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.824244976043701})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6288, 'crossentropy': 3.279840234375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 3970], ['ood', 59669], ['ood', 8586], ['ood', 14819], ['ood', 21846]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5773622657379915, 2.8443053939528147, 3.7820540175752635, 4.25522175234546, 4.455156175561661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7481060028076172})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1008687019348145})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.3275532722473145})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.652714967727661})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8729381561279297})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.635, 'crossentropy': 2.1910734375}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 53556], ['ood', 29218], ['ood', 12263], ['ood', 9699], ['ood', 4663]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3656099130496067, 2.452995265399533, 3.2863772929904567, 3.8622365284428035, 4.192867735318818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6869996786117554})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.137899398803711})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.4960885047912598})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.6224162578582764})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.0933022499084473})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.006866931915283})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7674367427825928})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.628, 'crossentropy': 3.0217234375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 12941], ['ood', 29472], ['ood', 18598], ['ood', 14048], ['ood', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.540358862179723, 2.7229686707789518, 3.6063130282926057, 4.104605413224359, 4.358021257333383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8412806987762451})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4700090885162354})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.35323166847229})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.448373317718506})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.912508964538574})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.110936403274536})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.64, 'crossentropy': 2.5321384765625}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 45329], ['ood', 4243], ['ood', 40313], ['ood', 10297], ['ood', 17073]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.55679523981008, 2.690833737391033, 3.4850719747916274, 4.002389324380528, 4.300362017959888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8383445739746094})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.294743537902832})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6262617111206055})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.947619915008545})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1819775104522705})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6294, 'crossentropy': 2.557214453125}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 10038], ['ood', 46591], ['id', 5124], ['ood', 56866], ['ood', 53528]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.2879972529083583, 2.413769841296279, 3.2434686313651593, 3.816060614958059, 4.151108351770384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7341711521148682})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.1308035850524902})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1988372802734375})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.6460185050964355})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5941050052642822})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.71964693069458})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6369, 'crossentropy': 2.3406673828125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 12223], ['ood', 24472], ['ood', 56455], ['ood', 56721], ['ood', 33792]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4399486642420545, 2.65091465590088, 3.4834217360593103, 4.034143989701948, 4.3069647277530505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9282028675079346})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.20809006690979})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6956939697265625})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.650796890258789})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.901409387588501})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6267, 'crossentropy': 2.2593751953125}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 43152], ['ood', 31046], ['ood', 56231], ['ood', 53380], ['ood', 25018]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3485761179708442, 2.4743390866809096, 3.32250272043232, 3.8660779827761758, 4.193387813000895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7241401672363281})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.3646421432495117})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.431084156036377})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.96962571144104})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.064136028289795})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8339951038360596})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9383416175842285})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.090867042541504})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.422330856323242})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.4222636222839355})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5193843841552734})
store['active_learning_steps'][49]['training']['best_epoch']=8
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6231, 'crossentropy': 3.2263150390625}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 50391], ['ood', 6081], ['ood', 8140], ['id', 4689], ['ood', 27431]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.469049297965558, 2.6089844620075295, 3.48305444661119, 4.042072664042804, 4.334527726768886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6890263557434082})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2398838996887207})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4161081314086914})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5455846786499023})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8248772621154785})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.935157299041748})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 2.672255078125}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 41843], ['ood', 29004], ['ood', 13902], ['ood', 46406], ['ood', 23902]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4489240161912773, 2.6340009367183432, 3.5354530982291514, 4.07335078743907, 4.340472173915748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.816032886505127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.589958667755127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.589305877685547})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8262155055999756})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.1872506141662598})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.175318717956543})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6107, 'crossentropy': 2.6541771484375}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 10160], ['ood', 35662], ['ood', 47156], ['ood', 48968], ['ood', 23469]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3143835781023763, 2.503444784772534, 3.3584614041727043, 3.9242969815207482, 4.243145986311189]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.8691623210906982})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.327176809310913})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5585479736328125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7520463466644287})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.882308006286621})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.9302713871002197})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.292999505996704})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7724547386169434})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.971362590789795})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 3.1304482421875}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 19869], ['ood', 21519], ['ood', 1954], ['ood', 10503], ['ood', 22791]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.497008240547561, 2.7200704898942, 3.5792504391683444, 4.100730873515907, 4.36041929270384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.95583975315094})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.2513487339019775})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.719606876373291})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8491907119750977})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0519659519195557})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.895205497741699})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6263, 'crossentropy': 2.7590375}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 49890], ['ood', 5013], ['ood', 22144], ['ood', 13902], ['ood', 39619]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4340230186459424, 2.675438511995022, 3.4998880531037067, 4.022969022270871, 4.323289283551414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8210585117340088})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1363940238952637})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.909705638885498})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.687130928039551})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7246174812316895})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6266, 'crossentropy': 2.3715541015625}
