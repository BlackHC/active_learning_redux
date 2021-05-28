store = {}
store['timestamp']=1622122244
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=29']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=29
store['worker_id']=29
store['num_workers']=80
store['config']={'seed': 1264, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6338698863983154})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.453017234802246})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.331414222717285})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 4.04849910736084})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.8944966793060303})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.011069297790527})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.21176815032959})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.207342624664307})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5943, 'crossentropy': 4.01021953125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 38600], ['ood', 4480], ['ood', 45800], ['ood', 56228], ['ood', 36287]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.6197263469776186, 2.8732225921042858, 3.6843695959719938, 4.159353999077878, 4.393835210104067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.8666061162948608})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.3668599128723145})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.6359500885009766})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.569423198699951})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.8898110389709473})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.981344223022461})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.886698007583618})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.71478271484375})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.2643895149230957})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.2784790992736816})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.958158493041992})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6049, 'crossentropy': 3.0013828125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 13754], ['id', 14178], ['id', 20946], ['id', 53167], ['id', 14213]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1716428602051603, 2.1000400219941806, 2.8293234968198258, 3.3814734283272116, 3.777490593692666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6193286180496216})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.25363826751709})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.474388837814331})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.4786338806152344})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6021, 'crossentropy': 1.646373828125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 20150], ['id', 4407], ['id', 36323], ['id', 26636], ['id', 3194]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7092857233536802, 1.3009428379460033, 1.8289002314403708, 2.292311188928945, 2.7086582778825203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.6773518323898315})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.9526487588882446})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.411597728729248})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.665506362915039})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.973616123199463})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1114392280578613})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.054527521133423})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6048, 'crossentropy': 2.78874140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 1799], ['ood', 16796], ['ood', 7008], ['id', 38307], ['id', 2434]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9677811172857789, 1.861485111624642, 2.5697450522530936, 3.1593908155355352, 3.6114787887459476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5192577838897705})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.9090639352798462})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.164346218109131})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4088988304138184})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.3904292583465576})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.7069852352142334})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.5731468200683594})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.583220958709717})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.619, 'crossentropy': 2.76310234375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 25420], ['id', 45018], ['id', 59772], ['id', 47989], ['id', 40187]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0556943360357964, 1.9111589532992417, 2.657159841667334, 3.2629068425698673, 3.721891196900982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4093976020812988})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.070380449295044})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.371565341949463})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1059279441833496})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.499661445617676})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.420900821685791})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.615713119506836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.6581006050109863})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.287071704864502})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.4490959644317627})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6265, 'crossentropy': 2.6814626953125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 42648], ['id', 57213], ['id', 11274], ['id', 19443], ['id', 4770]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0218055894148055, 1.9623121610201961, 2.7159416948215407, 3.3186983738603297, 3.756915427321884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3342034816741943})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7251410484313965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.8844199180603027})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.0533504486083984})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.41087007522583})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.237797975540161})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3978424072265625})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.1576547622680664})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4928507804870605})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6448, 'crossentropy': 2.4803958984375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 51231], ['id', 2731], ['id', 7646], ['id', 53825], ['id', 39750]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0702538008120235, 2.036864175964735, 2.847329286609459, 3.4719645597628848, 3.9210286442709847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4967892169952393})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5814359188079834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.9471945762634277})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.088223457336426})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3863606452941895})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 1.59692958984375}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 59387], ['id', 58130], ['id', 38613], ['ood', 5485], ['id', 4492]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8060060777946605, 1.57059772754421, 2.2212474352187623, 2.7696180868696274, 3.1936216670391344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3272231817245483})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3953852653503418})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4765198230743408})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.832869052886963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.007138729095459})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.1283106803894043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.2417054176330566})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3170762062072754})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6334, 'crossentropy': 2.03267578125}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 30678], ['ood', 56244], ['id', 39560], ['id', 51918], ['id', 57392]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.05447842128719, 1.9605647510523339, 2.7196075979709873, 3.325081218735498, 3.766562550091624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.362260341644287})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.580672025680542})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.5418261289596558})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.879357099533081})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.011120319366455})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2983078956604004})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.0917530059814453})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2457191944122314})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.1167569160461426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0086708068847656})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.359363079071045})
store['active_learning_steps'][9]['training']['best_epoch']=8
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6565, 'crossentropy': 2.455873828125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 56380], ['id', 37709], ['id', 39333], ['id', 18003], ['id', 48685]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9879348235381906, 1.8446443257344871, 2.6059314918744754, 3.1936419947048353, 3.649627388212812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3425800800323486})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4339863061904907})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7463222742080688})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0545711517333984})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.1011972427368164})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.995613932609558})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.415524959564209})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.386235237121582})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.568542957305908})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6538, 'crossentropy': 2.1354658203125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 53781], ['id', 23295], ['id', 30220], ['id', 53015], ['id', 4034]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9893717938880133, 1.8533246727850017, 2.5514942331607333, 3.131725486791458, 3.5817503057035527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3851540088653564})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3608145713806152})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.554701328277588})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7658483982086182})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.9479191303253174})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.9389898777008057})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.278987407684326})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.1741981506347656})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.094268798828125})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6499, 'crossentropy': 2.050098828125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59771], ['id', 15032], ['id', 24815], ['id', 29755], ['id', 58242]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8438012348714494, 1.631352788140234, 2.341765394356063, 2.952067394640668, 3.4486660573216987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3162171840667725})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3759621381759644})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6169275045394897})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.070629119873047})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1217055320739746})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.2189855575561523})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6332, 'crossentropy': 1.6626587890625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 12078], ['id', 32176], ['id', 27800], ['id', 4689], ['id', 4915]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8351864389890764, 1.5978211629858499, 2.2353533734744975, 2.77357825619273, 3.2147154656642103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3766340017318726})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3709254264831543})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.555122971534729})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.8359217643737793})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.0994889736175537})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1290719509124756})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.332538366317749})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.300448417663574})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.212161064147949})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.46932315826416})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6537, 'crossentropy': 2.2948419921875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 56769], ['id', 15841], ['id', 19138], ['id', 19038], ['id', 30553]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0357793034553717, 1.9951525011997013, 2.7309669799232417, 3.3208015563267175, 3.7774496996259375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.345900297164917})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3123993873596191})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.7652252912521362})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.8940331935882568})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.265964984893799})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6449, 'crossentropy': 1.384874609375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 41355], ['id', 10567], ['id', 2723], ['ood', 10259], ['id', 26217]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6981932222079028, 1.3249618557668672, 1.849736542191616, 2.329694219050853, 2.7480146143476816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.4911212921142578})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.4136109352111816})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5613439083099365})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.789629340171814})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.0201525688171387})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.042922019958496})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.815422534942627})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.089893341064453})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.0929694175720215})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.2780587673187256})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.1542201042175293})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.1265807151794434})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.240166664123535})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5354514122009277})
store['active_learning_steps'][15]['training']['best_epoch']=11
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6397, 'crossentropy': 2.2743482421875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 33801], ['id', 50272], ['id', 51163], ['id', 48019], ['ood', 22183]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9900302741571485, 1.8653047442619206, 2.6610697350122567, 3.289868030413107, 3.7739947291312586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.4811811447143555})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.4411346912384033})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4257525205612183})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6397716999053955})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6795881986618042})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.042041540145874})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0056331157684326})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6228, 'crossentropy': 1.8062939453125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 37489], ['id', 55098], ['id', 59815], ['id', 29799], ['id', 37150]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7365636562115268, 1.4156134616958198, 2.0470155540095325, 2.6088299624846423, 3.082533300117028]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3177473545074463})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2848228216171265})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5086703300476074})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.7107632160186768})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.806759238243103})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.0347490310668945})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.1328506469726562})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.1365365982055664})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.50327467918396})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.2903685569763184})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.235572099685669})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1442267894744873})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.299201250076294})
store['active_learning_steps'][17]['training']['best_epoch']=10
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6324, 'crossentropy': 2.4398142578125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 7475], ['id', 18414], ['id', 54198], ['id', 55459], ['id', 13195]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9873499713835976, 1.8713519292327199, 2.6468343387683415, 3.2543154227930593, 3.7169890846543296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.37711763381958})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.210018277168274})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.522562026977539})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.552126407623291})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.684744119644165})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.619307518005371})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.814673900604248})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9670242071151733})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1852517127990723})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6324, 'crossentropy': 1.748515234375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 48939], ['id', 52619], ['id', 12326], ['id', 56978], ['id', 44447]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.803639714768082, 1.5522130467489026, 2.2423722661717393, 2.8377366624555282, 3.3215035551460232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.438335657119751})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3298277854919434})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3978281021118164})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.6319682598114014})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6519200801849365})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9991068840026855})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6502, 'crossentropy': 1.4172255859375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 32578], ['id', 70], ['id', 31014], ['id', 3694], ['id', 18584]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6945211356732108, 1.3486226561747263, 1.9572813755420615, 2.481951003876266, 2.934961155559618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.4214701652526855})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2604026794433594})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.359809398651123})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6800930500030518})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.624204397201538})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.7441861629486084})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.880812168121338})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.060675621032715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.1335840225219727})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.225693941116333})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3317456245422363})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.654, 'crossentropy': 2.146541015625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 33674], ['id', 53549], ['id', 22521], ['id', 49078], ['id', 18913]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8634936346526754, 1.6821226872824036, 2.415134503310858, 3.0508349940128525, 3.5362253742360252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.4745047092437744})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2956628799438477})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.308427333831787})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4819601774215698})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5680127143859863})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.8199257850646973})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6247, 'crossentropy': 1.418355859375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 43543], ['ood', 57979], ['id', 36293], ['id', 52223], ['id', 33141]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.61777433386653, 1.2065557595027494, 1.7272598024202424, 2.2037496834353085, 2.6238375546482544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.4217581748962402})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2525203227996826})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3600202798843384})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.5410115718841553})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4404165744781494})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6352226734161377})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8712929487228394})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7598435878753662})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6625, 'crossentropy': 1.59456455078125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 19576], ['id', 54078], ['id', 57751], ['id', 13642], ['id', 4148]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6995543939373949, 1.3352291575531385, 1.9273050140927381, 2.4648231314001787, 2.9375136502711916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.501953125, 'crossentropy': 1.5130863189697266})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.178182601928711})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2341477870941162})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2050846815109253})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5719575881958008})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5780342817306519})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5790609121322632})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.5766932964324951})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6220808029174805})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6270513534545898})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7587387561798096})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.8135606050491333})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6997277736663818})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.076429843902588})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8420212268829346})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8891226053237915})
store['active_learning_steps'][23]['training']['best_epoch']=13
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6776, 'crossentropy': 1.8809015625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 42192], ['id', 48480], ['id', 3931], ['id', 22718], ['id', 35913]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.028957345887751, 1.911630152447561, 2.7302165543331443, 3.345772710789136, 3.7940657387050365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.445740818977356})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.178843379020691})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4050452709197998})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6523585319519043})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4553680419921875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.494523286819458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7004215717315674})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.853766918182373})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.2056612968444824})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6668, 'crossentropy': 1.63738212890625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 43428], ['id', 6578], ['id', 4008], ['id', 7593], ['ood', 45952]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7748573680395456, 1.4717174191054534, 2.1124282906103087, 2.681112422593623, 3.1501845246916043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5009765625, 'crossentropy': 1.5888762474060059})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2368712425231934})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2660475969314575})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3455612659454346})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.344963550567627})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6430310010910034})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5949718952178955})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.630568265914917})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6371619701385498})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.9893712997436523})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.7686688899993896})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0268561840057373})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6862, 'crossentropy': 1.61451533203125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 58777], ['id', 35309], ['id', 2067], ['id', 7460], ['id', 18533]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8820772797755825, 1.693881378674809, 2.4194053314148505, 3.01879568600443, 3.478933721196827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.5065326690673828})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.181618571281433})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2009721994400024})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2710931301116943})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3365423679351807})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4353628158569336})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6057689189910889})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.515484094619751})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.6203161478042603})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.817347764968872})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.7404119968414307})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.691, 'crossentropy': 1.5470185546875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 52509], ['id', 20643], ['id', 20390], ['id', 53671], ['id', 20624]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8340026305283172, 1.6338662465351135, 2.342208072771353, 2.9136713088520985, 3.380489625800223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.4837632179260254})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1687133312225342})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2319810390472412})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4063864946365356})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4704866409301758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.555657148361206})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.673323631286621})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7453060150146484})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6717, 'crossentropy': 1.45637080078125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 33673], ['id', 43863], ['id', 11374], ['id', 10100], ['id', 1473]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6933722943954386, 1.3586888124494392, 1.970837544329135, 2.498222115895354, 2.960593283713175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.5480847358703613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2164080142974854})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2499933242797852})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4536060094833374})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5960593223571777})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4738601446151733})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6701726913452148})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.5936336517333984})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8341903686523438})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.7754452228546143})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9976894855499268})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1017043590545654})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9215621948242188})
store['active_learning_steps'][28]['training']['best_epoch']=10
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6876, 'crossentropy': 1.83211953125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 44492], ['id', 19954], ['id', 56435], ['id', 46212], ['id', 10052]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8952504681212439, 1.7203041541107567, 2.429237822145504, 3.031901065455286, 3.5015929903382963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.5959527492523193})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2156471014022827})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1735336780548096})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2825241088867188})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4719288349151611})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3893933296203613})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.5478310585021973})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5111756324768066})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6689026355743408})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.828158974647522})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8968509435653687})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6924, 'crossentropy': 1.521786328125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 2855], ['id', 9855], ['id', 40549], ['id', 50431], ['id', 20348]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9199974368372104, 1.7072643035114239, 2.4146785256189602, 3.007022504586553, 3.452585877505081]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.4990234375, 'crossentropy': 1.560288667678833})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.248733401298523})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2649598121643066})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2913769483566284})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.477311134338379})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.5969245433807373})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5931181907653809})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.656458854675293})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6965694427490234})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9314939975738525})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0967330932617188})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.7431480884552002})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1866211891174316})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.2836804389953613})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9719884395599365})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1322872638702393})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.1271824836730957})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.254572868347168})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.1986770629882812})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3711462020874023})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.31429386138916})
store['active_learning_steps'][30]['training']['best_epoch']=18
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6996, 'crossentropy': 2.06611015625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 36], ['id', 55778], ['id', 57885], ['id', 16023], ['id', 12388]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9734043483066697, 1.9175699139482623, 2.741946376060498, 3.3972327435834053, 3.853849668391459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.458984375, 'crossentropy': 1.6201013326644897})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.3982670307159424})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2284159660339355})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3294050693511963})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3430969715118408})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.5213701725006104})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5305984020233154})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.6159720420837402})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5168490409851074})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6437950134277344})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.7757840156555176})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.983101725578308})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8169556856155396})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6973, 'crossentropy': 1.6783146484375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 37457], ['id', 48772], ['id', 43215], ['id', 23954], ['id', 52331]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8696953734995678, 1.6868790426114293, 2.4201313382640315, 3.039599304742919, 3.4927770652034784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.5551278591156006})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.160959005355835})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.170340895652771})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.286751627922058})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.362898349761963})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3805508613586426})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.519383192062378})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.37857985496521})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4057631492614746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.685514211654663})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8105660676956177})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7135, 'crossentropy': 1.4024736328125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 53882], ['id', 3410], ['id', 54813], ['id', 29501], ['id', 18236]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8359418115435795, 1.6079036442728665, 2.2622003610895822, 2.8283677543513495, 3.2832771762875055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.6678977012634277})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2102715969085693})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0942988395690918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2624773979187012})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.35703706741333})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4455856084823608})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6161153316497803})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6017687320709229})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.7656900882720947})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6867, 'crossentropy': 1.46952529296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 43054], ['id', 46975], ['id', 30701], ['id', 10784], ['id', 40968]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7848648815563204, 1.4478199520978388, 2.0584909572001546, 2.585359213656064, 3.030471606641637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.5198431015014648})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1364893913269043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1875581741333008})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.337615728378296})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3283419609069824})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4287117719650269})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.5319557189941406})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5183327198028564})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7168259620666504})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7320222854614258})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6944, 'crossentropy': 1.481348828125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 20027], ['id', 19225], ['id', 43504], ['id', 23259], ['id', 6000]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7872972337041695, 1.4788161210602961, 2.124725591315075, 2.6983074841448706, 3.1666311832586675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.5549523830413818})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.176579475402832})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1461000442504883})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1323161125183105})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.3165103197097778})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.267275094985962})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.481325387954712})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.435186743736267})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4836125373840332})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.5282793045043945})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.526384949684143})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4933618307113647})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7183451652526855})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7182, 'crossentropy': 1.4971693359375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 42121], ['id', 19088], ['ood', 50930], ['id', 31230], ['id', 59741]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8191292227062417, 1.6064801211942243, 2.2983292014269194, 2.892754976862138, 3.375565933876026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.487185001373291})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2998247146606445})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1728415489196777})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2369887828826904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2865383625030518})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.408958911895752})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5437679290771484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4644229412078857})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7803287506103516})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6881, 'crossentropy': 1.3637482421875}
