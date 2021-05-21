store = {}
store['timestamp']=1621477739
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=46']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=46
store['worker_id']=46
store['num_workers']=80
store['config']={'seed': 1282, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.239051342010498})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.780768632888794})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.5997610092163086})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.87355899810791})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6968, 'crossentropy': 2.1076455078125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 37795], ['id', 47322], ['id', 30359], ['id', 57523], ['id', 22380]], 'labels': [3, 8, 7, 3, 5], 'scores': [1.3141000533819422, 2.382842563257018, 3.1781412175835637, 3.756237370412241, 4.075653068471514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.9565517902374268})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.2351579666137695})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.423508644104004})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4616706371307373})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5319933891296387})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.324540615081787})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.6727848052978516})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.7976512908935547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.748953342437744})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7162, 'crossentropy': 2.1656197265625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 17124], ['id', 19569], ['id', 46463], ['id', 37521], ['id', 54106]], 'labels': [0, 2, 2, 5, 7], 'scores': [1.2654834920346212, 2.3646004189231062, 3.1874438940148977, 3.7418696385528936, 4.112070106781047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0794906616210938})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.0549123287200928})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.2309117317199707})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.371553421020508})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6226754188537598})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7442989349365234})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.6408133506774902})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7097, 'crossentropy': 2.2283806640625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 50294], ['id', 52462], ['id', 9437], ['id', 40422], ['id', 45845]], 'labels': [6, 9, 9, 5, 2], 'scores': [1.2450497782395258, 2.3427138548439084, 3.198225627073649, 3.7879661884603504, 4.143614998483946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.036074638366699})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.9677681922912598})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.2763168811798096})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.6198134422302246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.786837577819824})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7017, 'crossentropy': 1.8849388671875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 25315], ['id', 45800], ['id', 24758], ['id', 47992], ['id', 36642]], 'labels': [5, 9, 4, 3, 5], 'scores': [1.2259835709935105, 2.233632870947187, 3.0426942918279973, 3.6444837446003486, 4.041357708685533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7273736000061035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.28993821144104})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.415083408355713})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.290855646133423})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.301445245742798})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.2533066272735596})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.3283214569091797})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.4039089679718018})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.49617338180542})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7434, 'crossentropy': 2.1072609375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 7833], ['id', 40702], ['id', 25920], ['id', 27783], ['id', 30800]], 'labels': [5, 4, 2, 3, 0], 'scores': [1.3404119826223835, 2.512455479149562, 3.3841831040808925, 3.929204665249742, 4.244173318391072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.510427474975586})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.5228793621063232})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.9336705207824707})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7956171035766602})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.06160306930542})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7944, 'crossentropy': 1.30284267578125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 27121], ['id', 38404], ['id', 14125], ['id', 24716], ['id', 2648]], 'labels': [8, 0, 2, 5, 2], 'scores': [1.0985379296097628, 2.07498508097101, 2.8843978405177833, 3.465146193672201, 3.8697656986414755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4173598289489746})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.450906753540039})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.0787529945373535})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.7665684223175049})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.86964750289917})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7866, 'crossentropy': 1.30987939453125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 49824], ['id', 47925], ['id', 42707], ['id', 14295], ['id', 26613]], 'labels': [8, 3, 3, 2, 2], 'scores': [1.1125265612582431, 2.0573349283246194, 2.858018252624853, 3.4696364856235684, 3.892860310494145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3757593631744385})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8423430919647217})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.1413354873657227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.1527135372161865})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.0493531227111816})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 2.1231284141540527})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.3542566299438477})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.4284932613372803})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.2786617279052734})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7829, 'crossentropy': 1.8864962890625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 37048], ['id', 40595], ['id', 29132], ['id', 12361], ['id', 22747]], 'labels': [9, 8, 8, 2, 4], 'scores': [1.3720043814580354, 2.5157963473423983, 3.414332346852067, 3.959169833174789, 4.2529549050720945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4145262241363525})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.6284162998199463})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.705732822418213})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.8302431106567383})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.9212592840194702})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9597378969192505})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.1189515590667725})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.1884636878967285})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 2.240748167037964})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 2.2858364582061768})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 2.031810760498047})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 2.0497803688049316})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 2.1244163513183594})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.9169496297836304})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.34537935256958})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.324524164199829})
store['active_learning_steps'][8]['training']['best_epoch']=13
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8031, 'crossentropy': 1.8796501953125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 34122], ['id', 18420], ['id', 46163], ['id', 14705], ['id', 49656]], 'labels': [5, 4, 2, 0, 9], 'scores': [1.2259731072606894, 2.3517635739455605, 3.2438680737490575, 3.842321041999706, 4.211715522372344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1982395648956299})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3414088487625122})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.5977704524993896})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.741528034210205})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7863, 'crossentropy': 1.09158564453125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 33162], ['id', 9749], ['id', 51544], ['id', 37089], ['id', 33812]], 'labels': [8, 8, 1, 5, 6], 'scores': [0.8516537184271116, 1.5917112323510132, 2.2115910003275054, 2.7450053864714636, 3.1941191849305373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.3127930164337158})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.5304510593414307})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6684985160827637})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.0020904541015625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.865720272064209})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.8817138671875})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8004, 'crossentropy': 1.41375302734375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 54573], ['id', 31883], ['id', 21896], ['id', 14896], ['id', 7596]], 'labels': [2, 4, 8, 8, 4], 'scores': [1.0783980041751968, 2.0154557350748274, 2.792667575802623, 3.4095823019543525, 3.8549262637213175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.299142599105835})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.6703541278839111})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.0200517177581787})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.027421236038208})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.946568250656128})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.9757511615753174})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.2001500129699707})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.368152141571045})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7871, 'crossentropy': 1.731025390625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 38861], ['id', 14902], ['id', 59314], ['id', 33505], ['id', 30157]], 'labels': [6, 8, 9, 2, 6], 'scores': [1.1742893832668206, 2.2201711008529976, 3.119505083588276, 3.754282685231834, 4.13373959435811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.124635100364685})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.093616008758545})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1682108640670776})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1958060264587402})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3666398525238037})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3828716278076172})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.5938029289245605})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.570508360862732})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3779799938201904})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2721179723739624})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3606441020965576})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.651906132698059})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.7246556282043457})
store['active_learning_steps'][12]['training']['best_epoch']=10
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 1.10299599609375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 14580], ['id', 24424], ['id', 59286], ['id', 25520], ['id', 3795]], 'labels': [9, 1, 8, 6, 7], 'scores': [1.2163568858623472, 2.3195343928618923, 3.220016783934451, 3.831067421812417, 4.204093886215223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.060854196548462})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0116138458251953})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0569055080413818})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1570184230804443})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2051165103912354})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2832956314086914})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8576, 'crossentropy': 1.03854326171875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 47077], ['id', 14878], ['id', 2381], ['id', 49525], ['id', 28536]], 'labels': [5, 3, 7, 8, 3], 'scores': [1.2705684115311087, 2.32673327815404, 3.171653005832786, 3.7598662777941776, 4.115235085904008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8872095942497253})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8370969295501709})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.87077796459198})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9187273383140564})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9174417853355408})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.009511113166809})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0428740978240967})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.051805019378662})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8823, 'crossentropy': 0.817973193359375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 43648], ['id', 53694], ['id', 36238], ['id', 59297], ['id', 15779]], 'labels': [5, 7, 7, 1, 0], 'scores': [1.132918585877556, 2.159697093834945, 2.9759460385926824, 3.5961234002036644, 3.996644859534161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9750829935073853})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9553005695343018})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0065020322799683})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0134663581848145})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0024099349975586})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.997449517250061})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0770927667617798})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.020545244216919})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.184680461883545})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0411584377288818})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1898083686828613})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8695, 'crossentropy': 0.971732421875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 11074], ['id', 52169], ['id', 50562], ['id', 45917], ['id', 57392]], 'labels': [9, 2, 9, 9, 8], 'scores': [1.2688607009692467, 2.373458988536763, 3.2669138791811667, 3.8743434796828087, 4.210376413052481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9478597044944763})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7896233797073364})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.797691822052002})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9294765591621399})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0092525482177734})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8623, 'crossentropy': 0.773127880859375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 5740], ['id', 24636], ['id', 6994], ['id', 59698], ['id', 37696]], 'labels': [9, 0, 8, 2, 2], 'scores': [0.9651911731415583, 1.8043176689678582, 2.5227210044741506, 3.1075276513286854, 3.549228465753049]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0152738094329834})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8948757648468018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.921206533908844})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8898223638534546})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9305136203765869})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9506309032440186})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.111797571182251})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.802917529296875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 9948], ['id', 18962], ['id', 46412], ['id', 59747], ['id', 17011]], 'labels': [8, 7, 0, 5, 6], 'scores': [1.155766967021227, 2.1693616034842504, 3.0148697787651217, 3.640162372841119, 4.034082265865239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0085809230804443})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9354996681213379})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9405186176300049})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9614449739456177})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.905902624130249})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0427470207214355})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1781835556030273})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.072801113128662})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8792, 'crossentropy': 0.810662353515625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 15899], ['id', 20820], ['id', 1674], ['id', 42687], ['id', 47068]], 'labels': [9, 9, 9, 5, 4], 'scores': [1.0999898572168008, 2.1212205213400352, 2.9410355453146764, 3.5928417780707154, 4.001509465345084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0306224822998047})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8132231831550598})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8836037516593933})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8989953398704529})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9086203575134277})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.002286672592163})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0069785118103027})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8831, 'crossentropy': 0.7821248046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 18227], ['id', 17870], ['id', 35246], ['id', 22083], ['id', 35864]], 'labels': [3, 4, 8, 2, 5], 'scores': [1.0663531955610455, 2.057778116715481, 2.895637263060066, 3.5437569086925516, 3.9612906456182735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1782464981079102})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.853142499923706})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8634786605834961})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8635082244873047})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9694988131523132})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9109128713607788})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8846653699874878})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0481959581375122})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0648643970489502})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.7972734375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 7984], ['id', 826], ['id', 41540], ['id', 20869], ['id', 31157]], 'labels': [4, 9, 2, 3, 3], 'scores': [1.1608672129098978, 2.2673650389296753, 3.1056769300486664, 3.735338901684342, 4.116620597882147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0306715965270996})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7782150506973267})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9288769364356995})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7612910866737366})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9152628779411316})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8502881526947021})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0506435632705688})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.695659716796875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 12663], ['id', 17494], ['id', 30464], ['id', 42384], ['id', 36633]], 'labels': [8, 5, 4, 8, 1], 'scores': [0.9445010674991559, 1.8319089984916683, 2.609756643011556, 3.2424022311073113, 3.7069292970775685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0799931287765503})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8112524747848511})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6569496989250183})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7825648784637451})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8110898733139038})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8314304351806641})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8291611075401306})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.665810009765625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 52358], ['id', 28512], ['id', 14935], ['id', 53156], ['id', 6152]], 'labels': [2, 5, 3, 3, 8], 'scores': [1.1688464412151855, 2.2633239654253843, 3.0790143511978965, 3.679973806364927, 4.076062877161435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0288493633270264})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6804166436195374})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6799699068069458})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6950433850288391})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6834398508071899})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.760922908782959})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7889070510864258})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7722994685173035})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.589720458984375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 41572], ['id', 24740], ['id', 45658], ['id', 42746], ['id', 46088]], 'labels': [6, 8, 3, 2, 6], 'scores': [1.0677336820235288, 2.036872480295394, 2.860517902567773, 3.4893409138878297, 3.913250187566792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1506178379058838})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.781899631023407})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6757765412330627})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7336206436157227})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7217580080032349})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7520755529403687})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7376538515090942})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.784153401851654})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.67632734375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 32323], ['id', 32276], ['id', 5626], ['id', 39480], ['id', 5013]], 'labels': [5, 3, 7, 9, 2], 'scores': [1.1463349674192123, 2.1887885490599572, 3.0519566030947383, 3.6881418512171695, 4.07427329403656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1833359003067017})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7427918910980225})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7409366369247437})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7458533644676208})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7763316631317139})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7393836975097656})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8568069934844971})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7436275482177734})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8444751501083374})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.904, 'crossentropy': 0.6722865234375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 18324], ['id', 14335], ['id', 4083], ['id', 11292], ['id', 56773]], 'labels': [0, 4, 8, 1, 9], 'scores': [1.1490219761782006, 2.163378849437617, 2.9853002128979664, 3.581550924415703, 3.985696058373362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9872480630874634})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7089767456054688})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6835957765579224})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6514688730239868})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6213986873626709})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6332747340202332})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6599560379981995})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7008757591247559})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.5464552734375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 24265], ['id', 5474], ['id', 22531], ['id', 18098], ['id', 27540]], 'labels': [0, 8, 4, 4, -1], 'scores': [1.023135035275438, 1.9654055028490203, 2.758175670363098, 3.3989344413681426, 3.860024094398458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1000089645385742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6498194932937622})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6347569227218628})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6641804575920105})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6390134692192078})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6787986755371094})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6625354290008545})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6607016324996948})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.599341650390625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 42703], ['id', 8771], ['id', 36072], ['id', 47297], ['id', 40654]], 'labels': [0, 3, 2, 8, 5], 'scores': [1.0776127883558333, 2.0258993563656285, 2.856740399287311, 3.4721487388839414, 3.895047862544388]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1675009727478027})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.681185245513916})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5702176690101624})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6239604949951172})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6329001188278198})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5142396092414856})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6225768327713013})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5778381824493408})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6970810890197754})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.50723154296875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 20057], ['id', 274], ['id', 26358], ['id', 31184], ['id', 50743]], 'labels': [6, 6, 3, 9, 7], 'scores': [1.043272954073398, 1.9971674250934695, 2.8281662615643155, 3.4718308449535105, 3.917152503952785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1226844787597656})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6541683673858643})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5950891971588135})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.606257438659668})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6506293416023254})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5853525400161743})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6861002445220947})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6176788806915283})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.768552839756012})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.53017998046875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 52138], ['id', 45048], ['id', 31293], ['id', 1019], ['id', 18598]], 'labels': [9, 4, 8, 7, 9], 'scores': [1.064776828489509, 2.0686143781634203, 2.8725572421528387, 3.4962111226841692, 3.933780154388918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2154850959777832})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6563286185264587})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5382359623908997})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5311235189437866})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5592864751815796})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5716844201087952})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5706667900085449})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6163235902786255})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.632665753364563})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6245628595352173})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.55105830078125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 7322], ['id', 39309], ['id', 28795], ['id', 54885], ['id', 22193]], 'labels': [3, 0, 2, 6, 5], 'scores': [1.0609892191756014, 2.0597131283137893, 2.8783787464345814, 3.506453188760866, 3.959039458779819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1590070724487305})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6083662509918213})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5930749773979187})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5336786508560181})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5184189677238464})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5300720930099487})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5946129560470581})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5453099012374878})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5521384477615356})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5724393129348755})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5816981792449951})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5188028216362})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6491481065750122})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6157887578010559})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.651587724685669})
store['active_learning_steps'][31]['training']['best_epoch']=12
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9395, 'crossentropy': 0.54063173828125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 40589], ['id', 26184], ['id', 23927], ['id', 5679], ['id', 29508]], 'labels': [2, 0, 5, 3, 7], 'scores': [1.1920353747093375, 2.3073763020950864, 3.232925328618901, 3.834387662846696, 4.209546484525164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2879149913787842})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6346005201339722})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5284526944160461})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5024832487106323})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.625281810760498})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.588415801525116})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.51021533203125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 8228], ['id', 34520], ['id', 32668], ['id', 21355], ['id', 50317]], 'labels': [3, 6, 9, 0, 3], 'scores': [0.9222134081225162, 1.769857544285704, 2.485419310238626, 3.068626859943569, 3.5199895974261537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0590128898620605})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6222063302993774})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5447481870651245})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5513037443161011})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4998784065246582})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5634357929229736})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5818654894828796})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5644887089729309})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9341, 'crossentropy': 0.465848291015625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42317], ['id', 57311], ['id', 1512], ['id', 43052], ['id', 12650]], 'labels': [5, 5, 0, 7, 5], 'scores': [0.963428637641143, 1.8743340587709216, 2.648409068353134, 3.2634008752470276, 3.7357696048363014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2080429792404175})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6016391515731812})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5409797430038452})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4945492744445801})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5266790390014648})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5543992519378662})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5367792844772339})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.48339541015625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52086], ['id', 30214], ['id', 4646], ['id', 36818], ['id', 24587]], 'labels': [5, 1, 2, 7, 8], 'scores': [1.0266530810965353, 2.011889907593482, 2.834808363601679, 3.4743549963438394, 3.899227400288317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0731532573699951})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5599764585494995})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48729318380355835})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5216310620307922})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4602225720882416})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4521472752094269})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5694021582603455})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5155799388885498})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5535393357276917})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.48002099609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 17365], ['id', 22272], ['id', 22497], ['id', 37843], ['id', 35401]], 'labels': [0, 5, 7, 1, 3], 'scores': [1.1117466925817274, 2.101866979299996, 2.9297662094686396, 3.532860640359212, 3.949186413152579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4123103618621826})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7235586047172546})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.539952278137207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5287010669708252})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4717637300491333})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47217386960983276})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4717009663581848})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5223550796508789})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.512245237827301})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.567131519317627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49874287843704224})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5387144088745117})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5117347836494446})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5568551421165466})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5829439759254456})
store['active_learning_steps'][36]['training']['best_epoch']=12
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.50026904296875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 44487], ['id', 10746], ['id', 46368], ['id', 18739], ['id', 17079]], 'labels': [-1, 9, 8, 3, 6], 'scores': [1.2152492117154579, 2.25454970761888, 3.1221254707970285, 3.760272720299332, 4.150399964279208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.293053388595581})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5837415456771851})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5593125820159912})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5070715546607971})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5026782751083374})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45330631732940674})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4768259525299072})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4871041774749756})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5284239649772644})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.44682158203125}
