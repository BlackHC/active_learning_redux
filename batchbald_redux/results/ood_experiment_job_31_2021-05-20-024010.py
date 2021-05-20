store = {}
store['timestamp']=1621474810
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=31']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
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
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.6730668544769287})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8378593921661377})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.3676321506500244})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.5308666229248047})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.735665798187256})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5937, 'crossentropy': 3.120914453125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 32832], ['id', 14335], ['id', 24014], ['id', 8474], ['id', 29180]], 'labels': [-1, -1, 6, -1, -1], 'scores': [1.451403588739987, 2.534800084085771, 3.3366752571082507, 3.897064533047674, 4.224703300689425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.4327096939086914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.704063892364502})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9041314125061035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.27384614944458})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.069884777069092})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.7367405891418457})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 3.14658515625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36675], ['id', 7649], ['id', 56936], ['id', 17077], ['id', 3362]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5313306825898523, 2.7069478548160064, 3.500524578322537, 4.028042886350988, 4.304046747522829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.217573881149292})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.8356802463531494})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2635316848754883})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.4436769485473633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3935763835906982})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5965, 'crossentropy': 2.8519412109375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 22141], ['id', 38394], ['id', 22100], ['id', 31063], ['id', 19495]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4146449449462102, 2.5344400671001086, 3.404722134886441, 3.9586887040626824, 4.266757934344126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.701173782348633})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.2541279792785645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.754443645477295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.7617220878601074})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.7812390327453613})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.628862142562866})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.08942985534668})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5882, 'crossentropy': 3.879694921875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 19599], ['id', 50294], ['id', 16228], ['id', 12585], ['id', 1254]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.5695319451167213, 2.744305674949132, 3.6148988997680664, 4.121247207554436, 4.37030127575456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.240311622619629})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.676102638244629})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.86586856842041})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7110390663146973})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9586453437805176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.338435173034668})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2151875495910645})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6276, 'crossentropy': 2.822312890625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 35705], ['id', 34366], ['id', 10337], ['id', 23020], ['id', 27247]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4407423288872514, 2.651257707029491, 3.481555172153276, 4.024378048760623, 4.313938153904879]}
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
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 8553], ['id', 59771], ['id', 54196], ['id', 14111], ['id', 43105]], 'labels': [-1, 4, -1, -1, -1], 'scores': [1.5306015327682438, 2.808571815670522, 3.682249430046859, 4.150553957655736, 4.378438348888741]}
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
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.625478982925415})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.4601683616638184})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2045750617980957})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2537975311279297})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.658158779144287})
store['active_learning_steps'][6]['training']['best_epoch']=9
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6052, 'crossentropy': 3.67874453125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 23648], ['id', 18245], ['id', 56866], ['id', 48431], ['id', 52494]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6211326309357645, 2.8452830365381327, 3.7261828772244936, 4.212903008140574, 4.429169931860647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1203956604003906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.699368953704834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.067330837249756})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2552475929260254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3501033782958984})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8677892684936523})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.401966094970703})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6026, 'crossentropy': 3.502859765625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 25180], ['id', 3370], ['id', 40091], ['id', 11566], ['id', 25994]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6828894470847597, 2.87552546692475, 3.7304478103450807, 4.200899761505378, 4.426768921490753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.9544336795806885})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4062530994415283})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.1975574493408203})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.9831693172454834})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9844908714294434})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9640915393829346})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0300371646881104})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.333458423614502})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.1241701171875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 10918], ['id', 25294], ['id', 48970], ['id', 47214], ['id', 46344]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5195582810805686, 2.775732857853418, 3.6158385268112676, 4.106192976442051, 4.361244924114018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.428673267364502})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.1519222259521484})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3398163318634033})
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
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 986], ['id', 34267], ['id', 46232], ['id', 2450], ['id', 19276]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6597022919144053, 2.8589152797985116, 3.6905792178424974, 4.1774815942437975, 4.416142758557034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.100583791732788})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.924203872680664})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.2014575004577637})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.2235569953918457})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9944276809692383})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1305556297302246})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.4703879356384277})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.728199005126953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5479419231414795})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6175, 'crossentropy': 3.1999443359375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 10243], ['id', 50622], ['id', 19202], ['id', 20157], ['id', 33188]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.4991668489045762, 2.73510603413021, 3.5586832547211333, 4.069327360486473, 4.328912716599919]}
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
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.455970287322998})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.1261379718780518})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.490952734375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37720], ['id', 47487], ['id', 36281], ['id', 59158], ['id', 48814]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.711853617689505, 2.916134978659376, 3.7687317361066555, 4.240688209206883, 4.450494889356177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.827499270439148})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.0117549896240234})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4949638843536377})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6641814708709717})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5603084564208984})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.042844772338867})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.904921293258667})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.2591519355773926})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6445, 'crossentropy': 2.790810546875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27530], ['id', 45793], ['id', 16995], ['id', 4694], ['id', 25907]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5158753047481524, 2.702192933748288, 3.541282451986575, 4.060399753889978, 4.338989623403382]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.866675615310669})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.3173985481262207})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6103882789611816})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7484939098358154})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.997170925140381})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 2.5007908203125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 52346], ['id', 38796], ['id', 24294], ['id', 33522], ['id', 22807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.417248250337845, 2.6317747669375793, 3.4624041659166984, 3.9892742850190626, 4.2704297774339866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.113300323486328})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.620253086090088})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.733977794647217})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.11984920501709})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0987250804901123})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.384756088256836})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5431149005889893})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1641154289245605})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.748561382293701})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 3.527144140625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 51634], ['id', 5728], ['id', 7937], ['id', 7327], ['id', 55970]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.5169505196416426, 2.6863359029575586, 3.5166273480641745, 4.029453627831596, 4.3276362979571426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.0563712120056152})
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
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 3.2203072265625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 24142], ['id', 28243], ['id', 36281], ['id', 23096], ['id', 56866]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4820635133683293, 2.7674673240379843, 3.6179021533464866, 4.143076107001834, 4.392441040369276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8023464679718018})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4728314876556396})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.406921863555908})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.717132091522217})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.671128273010254})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 2.5038775390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 23041], ['id', 35346], ['id', 22807], ['id', 4799], ['id', 19089]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.426855709888836, 2.515328162006805, 3.308641869716907, 3.8612292709235003, 4.186229459688137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8814480304718018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.319000720977783})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.576347827911377})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5968422889709473})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.764055013656616})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.497899055480957})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9321584701538086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.042755365371704})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.088818073272705})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1404080390930176})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6261, 'crossentropy': 3.067033203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 28662], ['id', 18502], ['id', 23041], ['id', 19488], ['id', 20942]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5483733623739027, 2.73479670927432, 3.6134511763311465, 4.113324652236674, 4.363549684510827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.037360668182373})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.3829450607299805})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8170249462127686})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.346494197845459})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9837188720703125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.0340757369995117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.3734147548675537})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.3702220916748047})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.447484016418457})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.626, 'crossentropy': 3.40623671875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 12223], ['id', 39561], ['id', 39184], ['id', 37799], ['id', 59409]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4979872996748438, 2.806415968564391, 3.6013505851674124, 4.0934306160658505, 4.367931177081489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8622244596481323})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3782238960266113})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9087448120117188})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8085715770721436})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6371, 'crossentropy': 1.9023330078125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 59424], ['id', 36805], ['id', 49850], ['id', 45048], ['id', 13306]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1979289079363098, 2.137812626936867, 2.9189203463031603, 3.468110035708751, 3.847261778104186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.0345661640167236})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.648249626159668})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8329763412475586})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0776801109313965})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.633566379547119})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.3007450103759766})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9830310344696045})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.7425103187561035})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.229994297027588})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.619, 'crossentropy': 3.496613671875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 1983], ['id', 8621], ['id', 9116], ['id', 45209], ['id', 43823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5686707519982515, 2.8668589411852805, 3.65144908601211, 4.123201572961313, 4.369360907388619]}
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
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 6965], ['id', 53551], ['id', 39461], ['id', 47613], ['id', 5928]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3540449820008988, 2.495851365689973, 3.307731838099377, 3.8255317443787487, 4.14434470474162]}
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
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 9870], ['id', 53674], ['id', 40907], ['id', 26358], ['id', 6081]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.587963970071047, 2.848603453503827, 3.7001108608535986, 4.166312004433809, 4.409377303734782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.799821376800537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.279599905014038})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.639111280441284})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4723129272460938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6563167572021484})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6812033653259277})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8565964698791504})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6286, 'crossentropy': 2.6968734375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 30199], ['id', 59405], ['id', 22412], ['id', 34822], ['id', 33186]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4499209301219036, 2.6562516843120147, 3.4835158849304495, 4.021097793676455, 4.29882550221778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0864109992980957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.540801525115967})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.725165367126465})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.181028366088867})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8939049243927})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9915177822113037})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6434, 'crossentropy': 2.83083046875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 17253], ['id', 25107], ['id', 23372], ['id', 8462], ['id', 45329]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4657225960922915, 2.7206664162367358, 3.577690903765692, 4.089209301087522, 4.359202568624684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.028247356414795})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.727013111114502})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.573986053466797})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7831971645355225})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0078792572021484})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.297565221786499})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6157, 'crossentropy': 2.6607630859375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 56769], ['id', 10910], ['id', 45705], ['id', 53048], ['id', 58285]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4856178314761896, 2.6417732288583435, 3.444840920573508, 3.9616528930525536, 4.263770810583703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7809008359909058})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.136935234069824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.789841413497925})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.650421142578125})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5051496028900146})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.8739805221557617})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.201307535171509})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.23966121673584})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.895979166030884})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.999955177307129})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.2007546424865723})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1096177101135254})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6398, 'crossentropy': 3.0883072265625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 54757], ['id', 32006], ['id', 53956], ['id', 21479], ['id', 17941]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4955896754091897, 2.728674731656546, 3.625817792152099, 4.169668305926619, 4.41536054963254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.139112710952759})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.6720991134643555})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8965768814086914})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0578718185424805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1849558353424072})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.441279888153076})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1159610748291016})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.610604763031006})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.617, 'crossentropy': 3.625316796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 31574], ['id', 4899], ['id', 29427], ['id', 9659], ['id', 15462]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4441352822759128, 2.6387938850713333, 3.5159715409873558, 4.059400716489516, 4.316938147375518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2928414344787598})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7586326599121094})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.658583641052246})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.916203498840332})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.7695231437683105})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.124887704849243})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.120267868041992})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2506089210510254})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.928236484527588})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6254, 'crossentropy': 3.3049671875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 45462], ['id', 47923], ['id', 34908], ['id', 23692], ['id', 17602]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5092445157089953, 2.7553708111094837, 3.6496819134416754, 4.1593026069359365, 4.397185588836772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.269598960876465})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.5529799461364746})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.923990488052368})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1124799251556396})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1667518615722656})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.5275063514709473})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.411992311477661})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.194993734359741})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 3.3284046875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 54419], ['id', 26863], ['id', 5407], ['id', 19215], ['id', 40798]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4119591704390049, 2.6060671121104244, 3.395070854362947, 3.941301384838912, 4.246415175134507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.877169132232666})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.756948232650757})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7243895530700684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8384761810302734})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6269, 'crossentropy': 1.9322505859375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 33867], ['id', 16736], ['id', 54217], ['id', 6047], ['id', 11446]], 'labels': [-1, -1, 8, -1, 5], 'scores': [1.256419888442406, 2.2209124887163014, 2.9053189420473853, 3.4559803086538547, 3.8222745694505997]}
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
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 28856], ['id', 34847], ['id', 47303], ['id', 34897], ['id', 44952]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6049744062707667, 2.8099868823548677, 3.6301274476816197, 4.096088991194007, 4.366680135961161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.7219409942626953})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.091212511062622})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6204380989074707})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8110861778259277})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4798357486724854})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.818760871887207})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.826815605163574})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.1140835285186768})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.114100933074951})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.042975902557373})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.3898673057556152})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2152836322784424})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6352, 'crossentropy': 3.21346328125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 48435], ['id', 43689], ['id', 57255], ['id', 21824], ['id', 43224]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5530977603494431, 2.8197310761409677, 3.665547835625153, 4.1482787140603135, 4.405145857069976]}
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
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 2.7739603515625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 19931], ['id', 24637], ['id', 19982], ['id', 13214], ['id', 18551]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.480814544034153, 2.765638209951498, 3.6755536850161867, 4.1526781253380385, 4.386476734302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.8542922735214233})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.304779529571533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.2239208221435547})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5594301223754883})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.695614814758301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.889357566833496})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.1118006706237793})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6481, 'crossentropy': 2.68356484375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52322], ['id', 15845], ['id', 54688], ['id', 45616], ['id', 56866]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5513078573442605, 2.6928461696626877, 3.5568886573755725, 4.059729766831318, 4.333364939444122]}
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
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 45161], ['id', 34847], ['id', 47717], ['id', 22679], ['id', 1158]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5640762474463497, 2.77654455444388, 3.641690774240301, 4.146108820787186, 4.402962041717944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7207051515579224})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.9722518920898438})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.536759376525879})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6620032787323})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.5903818607330322})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.7686328887939453})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.885709285736084})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9907658100128174})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6385, 'crossentropy': 2.7599376953125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 36643], ['id', 29844], ['id', 9699], ['id', 43630], ['id', 48435]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.532844210801124, 2.68443053618759, 3.558360236165732, 4.072226555820277, 4.353567010192545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9416509866714478})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.623204231262207})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.799056053161621})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.682760238647461})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.071168899536133})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.072899103164673})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6303, 'crossentropy': 2.85525625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 42583], ['id', 47636], ['id', 56741], ['id', 31958], ['id', 24856]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5043241975349901, 2.71361278373913, 3.609507910035779, 4.0924630531747885, 4.353251155494967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7289413213729858})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.1943254470825195})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.185892343521118})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.574495315551758})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.561713695526123})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.752365827560425})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0186398029327393})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.846562147140503})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.9614148139953613})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6389, 'crossentropy': 2.99165625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 20982], ['id', 14065], ['id', 19525], ['id', 6857], ['id', 5684]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4852619720913371, 2.6825461890259623, 3.519630682574312, 4.035258620235899, 4.324158941312044]}
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
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7193069458007812})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5081071853637695})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6523, 'crossentropy': 2.631099609375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 9864], ['id', 9699], ['id', 57570], ['id', 10237], ['id', 42957]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4923664008572395, 2.759475134387251, 3.6810069225232755, 4.196895329343656, 4.423019976813697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5797208547592163})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1278860569000244})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.5804853439331055})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8532204627990723})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6354, 'crossentropy': 1.71704921875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 32046], ['id', 35801], ['id', 18412], ['id', 55084], ['id', 16909]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2589910716543287, 2.237700762659591, 3.0797766113103844, 3.6452049253597885, 4.001954916134617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.827868938446045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.6647493839263916})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7496891021728516})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.6478137969970703})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.747415781021118})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0792274475097656})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6268, 'crossentropy': 2.84298359375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 36643], ['id', 18324], ['id', 13306], ['id', 10855], ['id', 36550]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4834766005751208, 2.6186039703992208, 3.4781841126505437, 4.011624616769973, 4.321805026047533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8083927631378174})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.583199977874756})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.055694341659546})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8330562114715576})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9265589714050293})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.976189613342285})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6562180519104004})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9203388690948486})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1405820846557617})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.215301990509033})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4524264335632324})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5534892082214355})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.824244976043701})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6288, 'crossentropy': 3.279840625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 3970], ['id', 59669], ['id', 8586], ['id', 14819], ['id', 21846]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5773622664675826, 2.8443053941746363, 3.7820540293157574, 4.255221782236687, 4.4551562198046994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7481060028076172})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1008687019348145})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.3275537490844727})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.652714967727661})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8729381561279297})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.635, 'crossentropy': 2.1910734375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 53556], ['id', 29218], ['id', 12263], ['id', 9699], ['id', 4663]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3656099129411712, 2.4529952685404353, 3.286377293738825, 3.862236527874554, 4.192867746679443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.686999797821045})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.137899398803711})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.4960882663726807})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.6224162578582764})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.0933022499084473})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.006866931915283})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7674365043640137})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.628, 'crossentropy': 3.0217234375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 12941], ['id', 29472], ['id', 18598], ['id', 14048], ['id', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5403588660634964, 2.7229686766005825, 3.6063130370495635, 4.104605427424618, 4.358021277928769]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8412806987762451})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4700090885162354})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.35323166847229})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.448373556137085})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.912508964538574})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.110936403274536})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.64, 'crossentropy': 2.5321384765625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 45329], ['id', 4243], ['id', 40313], ['id', 10297], ['id', 17073]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.55679524361364, 2.690833744199629, 3.4850719974653774, 4.0023893632819885, 4.300362070014101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8383445739746094})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.294743537902832})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6262617111206055})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.947620153427124})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1819775104522705})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6294, 'crossentropy': 2.5572146484375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 10038], ['id', 46591], ['id', 5124], ['id', 56866], ['id', 53528]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.2879972527563042, 2.413769839359002, 3.2434686398321464, 3.81606062734243, 4.1511083678023635]}
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
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 12223], ['id', 24472], ['id', 56455], ['id', 56721], ['id', 33792]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4399486653060771, 2.6509146655248665, 3.483421763509595, 4.034144035351858, 4.3069647835142035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9282028675079346})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.20809006690979})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6956939697265625})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.650796890258789})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.901409149169922})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6267, 'crossentropy': 2.259375390625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 43152], ['id', 31046], ['id', 56231], ['id', 53380], ['id', 25018]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3485761185310021, 2.474339087527257, 3.3225027232135096, 3.8660779991969925, 4.193387836044671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7241401672363281})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.3646419048309326})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.431084156036377})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.96962571144104})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.064136028289795})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8339951038360596})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9383416175842285})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.090867042541504})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.422330379486084})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.4222636222839355})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5193843841552734})
store['active_learning_steps'][49]['training']['best_epoch']=8
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6231, 'crossentropy': 3.2263150390625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 50391], ['id', 6081], ['id', 8140], ['id', 4689], ['id', 27431]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.4690492985072992, 2.6089844080336846, 3.483054390768414, 4.04207261402971, 4.334527675885496]}
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
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 2.6722548828125}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 41843], ['id', 29004], ['id', 13902], ['id', 46406], ['id', 23902]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4489240186935177, 2.634000944867421, 3.5354531099093904, 4.07335081322148, 4.340472219440434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.816032886505127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.589958667755127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.589305877685547})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8262157440185547})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.1872506141662598})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.175318717956543})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6107, 'crossentropy': 2.6541771484375}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 10160], ['id', 35662], ['id', 47156], ['id', 48968], ['id', 23469]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3143835795759506, 2.5034447871030956, 3.3584614106967665, 3.9242969845091373, 4.24314598906436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.8691623210906982})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.327176809310913})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5585479736328125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7520461082458496})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.882307767868042})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.9302713871002197})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.292999744415283})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7724549770355225})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.971362590789795})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 3.1304482421875}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 19869], ['id', 21519], ['id', 1954], ['id', 10503], ['id', 22791]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.49700824087349, 2.7200704937888056, 3.5792504457211685, 4.10073090210277, 4.360419321497115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9558396339416504})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.2513487339019775})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.719606876373291})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8491907119750977})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0519659519195557})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.895205497741699})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6263, 'crossentropy': 2.7590375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 49890], ['id', 5013], ['id', 22144], ['id', 13902], ['id', 39619]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4340230185604268, 2.6754385072315383, 3.4998880514545085, 4.022969020419893, 4.32328927788852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8210582733154297})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1363940238952637})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.909705638885498})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6871306896209717})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7246174812316895})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6266, 'crossentropy': 2.371554296875}
