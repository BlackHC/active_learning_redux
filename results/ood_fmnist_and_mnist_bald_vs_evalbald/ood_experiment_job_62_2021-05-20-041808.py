store = {}
store['timestamp']=1621480688
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=62']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=62
store['worker_id']=62
store['num_workers']=80
store['config']={'seed': 1299, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.370114326477051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4344100952148438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.697539806365967})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.979166030883789})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.9680657386779785})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9716858863830566})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.057248592376709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8897109031677246})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6828, 'crossentropy': 2.70736171875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 57593], ['id', 29454], ['id', 53029], ['id', 46620], ['id', 24107]], 'labels': [5, 6, 2, 2, 5], 'scores': [1.3595974591196267, 2.4800978354302186, 3.2797978372217793, 3.864734829676565, 4.197170159838044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.280712127685547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.392354965209961})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7357189655303955})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.742201805114746})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.822874069213867})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6824, 'crossentropy': 2.1597251953125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 5173], ['id', 9799], ['id', 57296], ['id', 57334], ['id', 47912]], 'labels': [3, 8, 0, 7, 2], 'scores': [1.1355974427662832, 2.12235893871427, 2.952988211929923, 3.5669626141681814, 3.9698675585659977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.2665371894836426})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.3893256187438965})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8426623344421387})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.14530086517334})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.6089510917663574})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1327128410339355})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6691, 'crossentropy': 2.5682759765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 27873], ['id', 51081], ['id', 30865], ['id', 36529], ['id', 57991]], 'labels': [9, 4, 2, 8, 7], 'scores': [1.2587726410509654, 2.2992298367017665, 3.146967602082479, 3.729012701829183, 4.078224299811625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.0353338718414307})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.2806332111358643})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.1517186164855957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.56213641166687})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4524917602539062})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.4948692321777344})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.904904842376709})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.54586124420166})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.766378879547119})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7177, 'crossentropy': 2.604738671875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 3531], ['id', 8656], ['id', 58344], ['id', 52729], ['id', 59101]], 'labels': [7, 5, 9, 4, 8], 'scores': [1.267330188831109, 2.3759764908804404, 3.2788257970344308, 3.8810464794536195, 4.212220429776063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7946209907531738})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.0797982215881348})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.4323246479034424})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.636077880859375})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.6453890800476074})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.8095903396606445})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.672283172607422})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.525418281555176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.653001308441162})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 3.2481417655944824})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7223, 'crossentropy': 2.4102416015625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 41951], ['id', 5045], ['id', 27070], ['id', 23059], ['id', 11877]], 'labels': [5, 9, 0, 1, 7], 'scores': [1.2970014669541903, 2.4147714391587503, 3.278002889890945, 3.8489412299950505, 4.195260918741003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2813308238983154})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4908745288848877})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.6964401006698608})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8410189151763916})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.8278825283050537})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.0232203006744385})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.9669889211654663})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7772, 'crossentropy': 1.77909921875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 33472], ['id', 36894], ['id', 53309], ['id', 3026], ['id', 44968]], 'labels': [9, 0, 5, 8, 8], 'scores': [1.2325344197644985, 2.301461358609452, 3.153420194453746, 3.767067720095998, 4.138353301656524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4233531951904297})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5307811498641968})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.7674155235290527})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.936712622642517})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.154635190963745})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.2347006797790527})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7735, 'crossentropy': 1.6577310546875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 34594], ['id', 20171], ['id', 17756], ['id', 52011], ['id', 51464]], 'labels': [8, 5, 8, 2, 0], 'scores': [1.287538141068124, 2.4223421401051164, 3.274782245200015, 3.8403222435718325, 4.172882730420902]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.250744104385376})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3680906295776367})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.6755754947662354})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.5701725482940674})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.584859848022461})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5329293012619019})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7837932109832764})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.9588449001312256})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.9553415775299072})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.7754976749420166})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8165, 'crossentropy': 1.4683318359375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 51653], ['id', 33856], ['id', 53170], ['id', 44143], ['id', 41911]], 'labels': [2, 1, 8, 2, 2], 'scores': [1.1858333084926407, 2.2540266382600374, 3.111822558730317, 3.753846778781609, 4.131712495570593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.320105791091919})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.4103949069976807})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.662583827972412})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.8951220512390137})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.8418538570404053})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7823, 'crossentropy': 1.3414775390625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 57985], ['id', 12117], ['id', 11202], ['id', 12957], ['id', 14256]], 'labels': [4, 3, 9, 5, 6], 'scores': [1.0867504749376735, 2.1010695982385563, 2.902970542593895, 3.511187316171993, 3.9079229764525056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.276199221611023})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.4730093479156494})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5577994585037231})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.5207505226135254})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6906085014343262})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.7484006881713867})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.8892321586608887})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8158, 'crossentropy': 1.4168796875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 37974], ['id', 49156], ['id', 50403], ['id', 14844], ['id', 53325]], 'labels': [2, 3, -1, 9, 3], 'scores': [1.2039988257012277, 2.2777180312018794, 3.0985874129294704, 3.7188126613849386, 4.103865663726859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0816645622253418})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1210997104644775})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.173621416091919})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2212135791778564})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.248676061630249})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.4270615577697754})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.5569500923156738})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.455904245376587})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8433, 'crossentropy': 1.1341076171875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 2072], ['id', 37339], ['id', 13030], ['id', 20840], ['id', 5618]], 'labels': [4, 4, 0, 0, 2], 'scores': [1.2355602509997818, 2.3315301854639223, 3.2027065592517996, 3.796524403697094, 4.170458527119668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9651921987533569})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9179537296295166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.015878438949585})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0889267921447754})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1406543254852295})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2596590518951416})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.92342255859375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 52544], ['id', 8443], ['id', 31650], ['id', 18610], ['id', 19298]], 'labels': [6, 2, 5, 9, 6], 'scores': [1.1574755068051, 2.1793488944344057, 2.9917740379249365, 3.580888164892956, 3.9762134758888976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.046090841293335})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0056188106536865})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.074199914932251})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1098241806030273})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0978410243988037})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2097046375274658})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.20192551612854})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2961370944976807})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.9889529296875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 31664], ['id', 59380], ['id', 2000], ['id', 28455], ['id', 20641]], 'labels': [3, 8, 5, 5, 9], 'scores': [1.1680868991567168, 2.1954559973363885, 3.057909151426932, 3.6828489512084595, 4.074198768306457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0451648235321045})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9751951694488525})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0505313873291016})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1517045497894287})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1891767978668213})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8302, 'crossentropy': 0.9609505859375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 42763], ['id', 14394], ['id', 19892], ['id', 36998], ['id', 40334]], 'labels': [7, 3, 5, 2, 4], 'scores': [1.0156804746173407, 1.9164090561369473, 2.6302834765250864, 3.218089898293419, 3.673480695424912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9681229591369629})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.957284152507782})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9668522477149963})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0353221893310547})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0584063529968262})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8576, 'crossentropy': 0.80359130859375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 36508], ['id', 19942], ['id', 16692], ['id', 35401], ['id', 32511]], 'labels': [5, 5, 5, 3, 5], 'scores': [1.0546621766555362, 2.0033815701444064, 2.813804865991326, 3.421039930512232, 3.8459048782164196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9759951829910278})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8337090015411377})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9013373851776123})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.917164146900177})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8440937995910645})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.111499547958374})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.206066370010376})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.005576491355896})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.88, 'crossentropy': 0.80617001953125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 33593], ['id', 8196], ['id', 42787], ['id', 57342], ['id', 12196]], 'labels': [2, 7, 4, 2, 2], 'scores': [1.2103336046884516, 2.2451429550497823, 3.06106552974681, 3.642881661344056, 4.033825633474466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0107285976409912})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8027806282043457})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9479106664657593})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.053931713104248})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0004867315292358})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.971872091293335})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0170814990997314})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1049957275390625})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0044327974319458})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1836928129196167})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0890494585037231})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2572178840637207})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0602625608444214})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0800799131393433})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.207780361175537})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2491447925567627})
store['active_learning_steps'][16]['training']['best_epoch']=13
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8782, 'crossentropy': 0.9313796875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 5086], ['id', 28412], ['id', 16969], ['id', 14405], ['id', 48587]], 'labels': [3, 0, 4, 6, 3], 'scores': [1.2269501435935501, 2.353452798572502, 3.303858666888255, 3.928265483496805, 4.262233255857447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8823555707931519})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7558192014694214})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8688746690750122})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7812528610229492})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8878401517868042})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8769450783729553})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8629881739616394})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9330765008926392})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8639844655990601})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9167627096176147})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.75952509765625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 23140], ['id', 22483], ['id', 39305], ['id', 51432], ['id', 17494]], 'labels': [7, 8, 7, 1, 5], 'scores': [1.3723161020726926, 2.4531601263240503, 3.293064783420128, 3.890735470332589, 4.220849923241297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8708855509757996})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7580549716949463})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8360813856124878})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0056450366973877})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8680834770202637})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8762, 'crossentropy': 0.68989599609375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 49509], ['id', 6684], ['id', 3719], ['id', 36744], ['id', 9118]], 'labels': [8, 0, 2, 1, 9], 'scores': [0.9613670049602618, 1.8067941885373422, 2.5392310030590153, 3.130299755956359, 3.578530175463368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9738613367080688})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8056904673576355})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8635135889053345})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7649248838424683})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8988082408905029})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8510856628417969})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8495903015136719})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.712815771484375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 57507], ['id', 24479], ['id', 29335], ['id', 51764], ['id', 1075]], 'labels': [0, 8, 8, 5, 7], 'scores': [1.1500162590136072, 2.096770581948254, 2.921200481301458, 3.5180592647302467, 3.931850924910817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9811772108078003})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7550482153892517})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7291462421417236})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8178197145462036})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8384042978286743})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8847440481185913})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8474053144454956})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.863027811050415})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9671847820281982})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9006, 'crossentropy': 0.6933833984375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 31090], ['id', 34328], ['id', 19824], ['id', 39429], ['id', 39480]], 'labels': [4, 8, 9, 2, 9], 'scores': [1.143947417852262, 2.171704639001215, 3.032900799802257, 3.6671778679555516, 4.080734609554499]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0805578231811523})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7803040742874146})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6849759817123413})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7442921996116638})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8160659670829773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.920634388923645})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8463352918624878})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9585391283035278})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9222805500030518})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.963984489440918})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8939, 'crossentropy': 0.76448466796875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 424], ['id', 17382], ['id', 33505], ['id', 15948], ['id', 12297]], 'labels': [9, 6, 2, 2, 9], 'scores': [1.1506216249279642, 2.220296878185969, 3.096061901995526, 3.7043896878444604, 4.095449733379734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0414445400238037})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7445979118347168})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.759825587272644})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9024105072021484})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9293234944343567})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9402397871017456})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8535629510879517})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9333792924880981})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.075688362121582})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9976530075073242})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8874, 'crossentropy': 0.78614912109375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5842], ['id', 39405], ['id', 35232], ['id', 21023], ['id', 34520]], 'labels': [1, 5, 8, 2, 6], 'scores': [1.1228137818062107, 2.190565910479723, 3.0915536903400147, 3.7251713640677195, 4.130193549285211]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.972113847732544})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6917380094528198})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6824357509613037})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.679044783115387})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.753408670425415})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.832429051399231})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7312946319580078})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.63711845703125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 14367], ['id', 12986], ['id', 9428], ['id', 39818], ['id', 16051]], 'labels': [3, 5, 9, 1, 4], 'scores': [1.0140600097511485, 1.9847997491181504, 2.779849049628279, 3.397856988373091, 3.8495342842464115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.96422278881073})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7789478302001953})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7145538330078125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.833409309387207})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9040817022323608})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8900908827781677})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9490096569061279})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.750063134765625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31301], ['id', 19855], ['id', 9472], ['id', 54652], ['id', 46493]], 'labels': [5, 3, 2, -1, 7], 'scores': [1.0576553947779388, 2.0421005696959833, 2.8385634029793554, 3.4806989920521234, 3.9193085716482443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0855069160461426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.801644504070282})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.79632568359375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7803233861923218})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8039388060569763})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9188411235809326})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0160808563232422})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.68782353515625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 57872], ['id', 29764], ['id', 49091], ['id', 42703], ['id', 18150]], 'labels': [3, 4, 3, 0, 8], 'scores': [1.0039028286526195, 1.908748155816589, 2.699855277230938, 3.3318146641692534, 3.802154555133452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1092898845672607})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7153217792510986})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7069196701049805})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7533673048019409})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6855415105819702})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.745712161064148})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8354924917221069})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7876555919647217})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7520064115524292})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7613583207130432})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9058120250701904})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.911413848400116})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9136, 'crossentropy': 0.64378642578125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 47626], ['id', 36072], ['id', 46832], ['id', 576], ['id', 5129]], 'labels': [-1, 2, 7, 4, 2], 'scores': [1.0894303144768562, 2.1171853968104233, 3.014991140131132, 3.6387069618903585, 4.048509597260658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9871881604194641})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6235960721969604})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6392035484313965})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6265034079551697})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7001075744628906})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.61393408203125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 6604], ['id', 45443], ['id', 48507], ['id', 42020], ['id', 46899]], 'labels': [8, 5, 6, 9, 3], 'scores': [0.8373173086497634, 1.6081498944342574, 2.292123375306315, 2.8870975617059544, 3.3365370851990477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0207768678665161})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7260127067565918})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7151657342910767})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6589043140411377})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7755520939826965})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8953, 'crossentropy': 0.637655810546875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42707], ['id', 56440], ['id', 25004], ['id', 17079], ['id', 34597]], 'labels': [3, 4, 2, 6, 3], 'scores': [0.8494937734895707, 1.5929761366555888, 2.2819550840579765, 2.8523846005035427, 3.3077054879668806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0224838256835938})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7007145285606384})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5793766975402832})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6197736263275146})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6565698385238647})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6439728736877441})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6449239253997803})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6450164318084717})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6912562847137451})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.5510044921875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 57305], ['id', 21442], ['id', 43176], ['id', 30359], ['id', 18003]], 'labels': [1, 4, 2, 7, 2], 'scores': [1.0233767044614912, 1.9929721654564538, 2.8256617477967314, 3.4865887786291676, 3.9534425183511726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0759837627410889})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.669196605682373})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5787866115570068})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6368968486785889})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5899046063423157})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7194081544876099})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9205, 'crossentropy': 0.503496337890625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 14765], ['id', 25839], ['id', 4822], ['id', 5684], ['id', 1634]], 'labels': [3, 0, 4, 6, 3], 'scores': [0.9299284720997825, 1.7570386946996948, 2.509497199710885, 3.1110150161678014, 3.5689960087304655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9609599113464355})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6247770190238953})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5659948587417603})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6578260660171509})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5683412551879883})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6465315222740173})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.658356785774231})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6088727712631226})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6039072871208191})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6925167441368103})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7591778039932251})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.5004697265625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 1512], ['id', 38511], ['id', 27024], ['id', 10746], ['id', 27429]], 'labels': [0, 6, 8, 9, 0], 'scores': [1.0930071708133715, 2.1086634583181794, 2.9855433522242976, 3.620429813933799, 4.036449451555567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1382781267166138})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6459409594535828})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5023922920227051})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6007282733917236})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.581977367401123})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5994437336921692})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5758501291275024})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5796765089035034})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6644723415374756})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6256492137908936})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.54388134765625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 36417], ['id', 44350], ['id', 55128], ['id', 34946], ['id', 32519]], 'labels': [6, 3, 8, 8, 5], 'scores': [1.1149121087467577, 2.1208877294117077, 2.985181108679442, 3.6151433266945414, 4.046333683636853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2610783576965332})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6943259239196777})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5557732582092285})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5500527620315552})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5943652391433716})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5609914064407349})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5807755589485168})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5818461179733276})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5524216294288635})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5829876065254211})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6073226928710938})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6375992894172668})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.50536806640625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 28587], ['id', 26577], ['id', 22272], ['id', 7984], ['id', 18598]], 'labels': [8, 2, 5, 4, 9], 'scores': [1.0995880239089337, 2.143399400079181, 3.0213320390845873, 3.6677878799388317, 4.090934301900427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9650196433067322})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6015783548355103})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5114142894744873})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5006784200668335})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5503244400024414})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5304868221282959})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9397, 'crossentropy': 0.459089697265625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 18487], ['id', 29132], ['id', 14373], ['id', 36818], ['id', 35128]], 'labels': [4, 8, 2, 7, 2], 'scores': [0.8461878911582519, 1.6133873045048377, 2.315963165087843, 2.9060586589085737, 3.377315050957276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.189568042755127})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6176987886428833})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5513435006141663})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5801440477371216})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5553466081619263})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5443608164787292})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6092804670333862})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6312949061393738})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.677261233329773})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.462119580078125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 22286], ['id', 43702], ['id', 48681], ['id', 43796], ['id', 1674]], 'labels': [8, 3, 2, 7, 9], 'scores': [1.068274242749851, 2.0237642781672154, 2.8726072182718934, 3.4835252961378806, 3.910839021234178]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0621618032455444})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6308969259262085})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49682486057281494})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4924375116825104})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5690488815307617})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5581395626068115})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5880277156829834})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5781439542770386})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5646455883979797})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5049880743026733})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5636889934539795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6331990361213684})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5408312082290649})
store['active_learning_steps'][36]['training']['best_epoch']=10
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9392, 'crossentropy': 0.503509765625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 44661], ['id', 40654], ['id', 17941], ['id', 59286], ['id', 37469]], 'labels': [1, 5, 0, 8, 2], 'scores': [1.1143637177286094, 2.1520691595034185, 3.037945531430685, 3.6637839183256817, 4.075925667602787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1710374355316162})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5267230868339539})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5662658214569092})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5131114721298218})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47752106189727783})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45820605754852295})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5114790201187134})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46865180134773254})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49162405729293823})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5300824642181396})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5049728155136108})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.439600048828125}
