store = {}
store['timestamp']=1621471697
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=6']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=80
store['config']={'seed': 1240, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.504276990890503})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3698782920837402})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.887885570526123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.925203800201416})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6962, 'crossentropy': 2.0238193359375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2429718971252441})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1515264511108398})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1698318719863892})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 35151], ['id', 36475], ['id', 44808], ['id', 21156], ['id', 27643]], 'labels': [5, 2, 6, 3, 2], 'scores': [1.0527127297467356, 1.84425996040566, 2.4188348851272696, 2.8179967355541127, 3.0505164343057647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.1020779609680176})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4792556762695312})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.5426650047302246})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9789485931396484})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.9957733154296875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.482276439666748})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6923, 'crossentropy': 2.3079330078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1902834177017212})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1036678552627563})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1772572994232178})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.173027753829956})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1633163690567017})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 31030], ['id', 48010], ['id', 16158], ['id', 41556], ['id', 109]], 'labels': [8, 7, 8, 0, -1], 'scores': [1.052709437335154, 1.9296273193147142, 2.556856448951951, 2.911446088017014, 3.105859191772346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.7688124179840088})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.399481773376465})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.302394390106201})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.6145505905151367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6727070808410645})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 2.1444240234375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1685576438903809})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1141111850738525})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0966248512268066})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1239943504333496})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 4703], ['id', 0], ['id', 46148], ['id', 19677], ['id', 16590]], 'labels': [4, 5, 9, 4, 6], 'scores': [1.111198042258655, 1.9298002728347337, 2.5757816812013115, 2.9666129395091776, 3.184198859798858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5957987308502197})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.8772814273834229})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.134049892425537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.9916620254516602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.465780258178711})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.278179168701172})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.2683424949645996})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.78, 'crossentropy': 1.681703125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.9606437683105469})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.932988166809082})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9125082492828369})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.8741286396980286})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 8496], ['id', 20171], ['id', 36999], ['id', 27324], ['id', 34833]], 'labels': [8, 5, 5, 8, 2], 'scores': [0.99063137144578, 1.722655673363069, 2.2613609477647856, 2.6274396660414885, 2.8587949834360558]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.518359899520874})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.9667763710021973})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9448530673980713})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.9511500597000122})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.9697624444961548})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.2823328971862793})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.3274261951446533})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7839, 'crossentropy': 1.6401607421875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9413938522338867})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.8534708023071289})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8541725873947144})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8487207889556885})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.868655800819397})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.7962498068809509})
store['active_learning_steps'][4]['eval_training']['best_epoch']=6
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 19423], ['id', 47781], ['id', 43716], ['id', 59400], ['id', 44105]], 'labels': [2, 3, 5, 5, 4], 'scores': [1.0305428410002069, 1.8574322614408088, 2.5265108862541723, 2.8764238214153037, 3.0517825461701094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4792068004608154})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.757165789604187})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.8280131816864014})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.8154940605163574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.0743327140808105})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9744704961776733})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.001647710800171})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7929, 'crossentropy': 1.5623326171875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9559789299964905})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.8884021043777466})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.8164373636245728})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8290168046951294})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.8258427381515503})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8269909024238586})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 33043], ['id', 20606], ['id', 48712], ['id', 5348], ['id', 21765]], 'labels': [0, 3, 7, 8, -1], 'scores': [0.9678178026173452, 1.761699344747115, 2.3837370652705054, 2.7977728284250265, 3.03057040204045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.3530733585357666})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.6349126100540161})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.8487728834152222})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.1165390014648438})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7829, 'crossentropy': 1.192380078125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0362119674682617})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8725994825363159})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8813404440879822})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 53029], ['id', 12934], ['id', 36801], ['id', 47365], ['id', 58428]], 'labels': [2, 8, 1, 4, 5], 'scores': [0.7524298196814718, 1.3648554568857105, 1.8180605724946943, 2.1858697713688535, 2.4559492526366533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.122842788696289})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.262103796005249})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3086633682250977})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4045051336288452})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.4671905040740967})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.4415106773376465})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.7091395854949951})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.849, 'crossentropy': 1.099801171875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8711873292922974})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7094507813453674})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.6991111040115356})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.6598271131515503})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6539425849914551})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 4456], ['id', 44345], ['id', 125], ['id', 44738], ['id', 26100]], 'labels': [9, 4, -1, -1, -1], 'scores': [0.8889746037855502, 1.6482188526210662, 2.247207921315118, 2.659834256394948, 2.852517170094149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0544772148132324})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.112544059753418})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2917718887329102})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1697237491607666})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4848188161849976})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8507, 'crossentropy': 0.9050828125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7043077945709229})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6430798172950745})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.6692525148391724})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6343675851821899})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 5968], ['id', 7639], ['id', 38791], ['id', 5905], ['id', 15743]], 'labels': [7, 5, 8, -1, 3], 'scores': [0.7697569443773131, 1.446047829660496, 1.9935729009264742, 2.407963843953162, 2.6734199744616145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.032738208770752})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.038204550743103})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1806678771972656})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2107923030853271})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.3635156154632568})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.134756088256836})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2077651023864746})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.4467753171920776})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.4073328971862793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.4454271793365479})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8596, 'crossentropy': 1.09601201171875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7993685603141785})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6345317363739014})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6359061598777771})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.5976250767707825})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.5805416107177734})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5680721998214722})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.5805088877677917})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5760382413864136})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.5686108469963074})
store['active_learning_steps'][9]['eval_training']['best_epoch']=8
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 4153], ['id', 49473], ['id', 182], ['id', 40857], ['id', 26100]], 'labels': [2, 1, 5, 9, -1], 'scores': [0.932862062223776, 1.7735590329673019, 2.4661388391312737, 2.9135691457435824, 3.1429848602070045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0026371479034424})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0411702394485474})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1153621673583984})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.390069842338562})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3544237613677979})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.345468521118164})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2904011011123657})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3973884582519531})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4506620168685913})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.5374107360839844})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8648, 'crossentropy': 1.07468134765625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8447014093399048})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6709795594215393})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.644237756729126})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6470026969909668})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6182795763015747})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 15261], ['id', 48355], ['id', 40547], ['id', 6576], ['id', 55864]], 'labels': [3, 3, 8, 3, 3], 'scores': [0.9264054844950611, 1.7051834172066846, 2.290073738696867, 2.6400564285856856, 2.8182189490983633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9551409482955933})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9368433952331543})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8861691951751709})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9468824863433838})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9709498882293701})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9791602492332458})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0890331268310547})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0712785720825195})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8913, 'crossentropy': 0.8320955078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7180028557777405})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5939451456069946})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5637813806533813})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5126311779022217})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5286121368408203})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5066015720367432})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5049513578414917})
store['active_learning_steps'][11]['eval_training']['best_epoch']=7
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 4502], ['id', 19369], ['id', 16953], ['id', 9410], ['id', 37315]], 'labels': [1, 0, 9, 4, 6], 'scores': [0.8051491801541688, 1.5281707232231696, 2.1269877487876996, 2.5556708054441826, 2.8288303520767375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9207741022109985})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9562229514122009})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0582702159881592})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.064868688583374})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0479047298431396})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8732, 'crossentropy': 0.83893017578125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7828611135482788})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6824309825897217})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6218348145484924})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.612561821937561})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 37750], ['id', 38600], ['id', 19276], ['id', 13348], ['id', 47997]], 'labels': [5, 9, 6, 5, 0], 'scores': [0.8403258663738462, 1.526072490862429, 2.0922194532756713, 2.455812290620437, 2.668474868319726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8233577013015747})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8927054405212402})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9911108016967773})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0286247730255127})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.79298076171875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8539204597473145})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7458548545837402})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7058360576629639})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37048], ['id', 10744], ['id', 48356], ['id', 28389], ['id', 1812]], 'labels': [9, 7, 2, 2, 4], 'scores': [0.6925885792994708, 1.2743013147964861, 1.7737688677245043, 2.149297380105179, 2.416969874276809]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9285242557525635})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8431828022003174})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8270734548568726})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9265791177749634})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9703501462936401})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8865706920623779})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0149827003479004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0637104511260986})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.069366455078125})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8963, 'crossentropy': 0.78394580078125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7122282981872559})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5586386919021606})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5196932554244995})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5125840902328491})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4991418123245239})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.47776806354522705})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.45308321714401245})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.461730033159256})
store['active_learning_steps'][14]['eval_training']['best_epoch']=8
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 189], ['id', 7466], ['id', 42265], ['id', 46017], ['id', 48423]], 'labels': [2, 0, 7, 0, 2], 'scores': [0.8924176038745117, 1.6891265073525275, 2.2931902319015, 2.7052653180115067, 2.9394496715291023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8254426717758179})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7734329700469971})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8077210187911987})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8205270767211914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8870913982391357})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9253937005996704})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9486122131347656})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.71372685546875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6133105754852295})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5394736528396606})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.47279030084609985})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4887431859970093})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48796388506889343})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.4721195101737976})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 12377], ['id', 13075], ['id', 45256], ['id', 59242], ['id', 8301]], 'labels': [3, 0, 5, 3, 9], 'scores': [0.9048561690583086, 1.6503002987702904, 2.2660058120344093, 2.65259663295397, 2.8507775484367794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8554793000221252})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7334923148155212})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7827774286270142})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7494024038314819})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7627333998680115})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8445205688476562})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7871249914169312})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.673653369140625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6613636612892151})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5298625826835632})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4914017617702484})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.49778199195861816})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4755617082118988})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.467563271522522})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 37778], ['id', 32427], ['id', 38165], ['id', 32909], ['id', 39429]], 'labels': [8, 0, 5, 9, 2], 'scores': [0.7438964699454411, 1.4128502150043682, 1.982112385190404, 2.3711636570340247, 2.601768865026016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.854706346988678})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6830949187278748})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7338716983795166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8658759593963623})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.89555823802948})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8932923078536987})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8873436450958252})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8663060665130615})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9069532155990601})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8977, 'crossentropy': 0.81551083984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7038093209266663})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5771729946136475})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5153782367706299})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.464356929063797})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5013579726219177})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.48496606945991516})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4694983959197998})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.4711412787437439})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 8695], ['id', 37129], ['id', 8093], ['id', 4393], ['id', 15795]], 'labels': [4, 8, 0, 7, -1], 'scores': [0.9033155027354223, 1.6679615577133928, 2.2512151664703888, 2.594185044785318, 2.7764290188367973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8878220319747925})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.70004802942276})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7490842342376709})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.811625599861145})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7151565551757812})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.65427197265625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6894927024841309})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5417362451553345})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5074447989463806})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.44881755113601685})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 9428], ['id', 49893], ['id', 49487], ['id', 50351], ['id', 12392]], 'labels': [9, 3, 8, 7, 3], 'scores': [0.7629710843143804, 1.3771555754445846, 1.8681379361344863, 2.2298682268822176, 2.4630016121625644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9582056403160095})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7270791530609131})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7226377725601196})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6493910551071167})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6660478115081787})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.712777316570282})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7676196098327637})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7535351514816284})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.638124609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.725623369216919})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5719656944274902})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.49530017375946045})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46222227811813354})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.45004788041114807})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.44231081008911133})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40822693705558777})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 5303], ['id', 16860], ['id', 17906], ['id', 9804], ['id', 935]], 'labels': [-1, 8, -1, 1, -1], 'scores': [0.8244296108395968, 1.5746447173995417, 2.1387606657252363, 2.5297593836554464, 2.7908612030938507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9446560740470886})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.540112316608429})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6603488922119141})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6212797164916992})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5903133153915405})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6676605939865112})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7072402238845825})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7078063488006592})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.605647900390625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6272670030593872})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.47720974683761597})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43092334270477295})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4336758852005005})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.38502442836761475})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40181416273117065})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3841348886489868})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 43648], ['id', 34328], ['id', 49890], ['id', 26100], ['id', 33397]], 'labels': [5, 8, 5, -1, 6], 'scores': [0.8051265917630888, 1.467718089510336, 2.003977364229832, 2.3555679693895613, 2.5610815192519016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8528198599815369})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6279341578483582})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6112298369407654})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6486501097679138})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6848127841949463})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7164338231086731})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.620132958984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6846019625663757})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5558801293373108})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.435105562210083})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44568413496017456})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4330606460571289})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 57090], ['id', 47110], ['id', 26516], ['id', 6980], ['id', 41218]], 'labels': [8, -1, 6, 5, 8], 'scores': [0.7751057807059274, 1.405103373278076, 1.929370182245151, 2.299424572287701, 2.524099916314504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8119499087333679})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6504095792770386})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6717947721481323})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6453413963317871})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7201249599456787})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6710532903671265})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7095171809196472})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7661342620849609})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7386953234672546})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.68768984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6477013826370239})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48132967948913574})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43708711862564087})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4461892247200012})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41838258504867554})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40410399436950684})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4141952395439148})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39620131254196167})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 7924], ['id', 8926], ['id', 41334], ['id', 25308], ['id', 59438]], 'labels': [8, 0, 9, 7, 8], 'scores': [0.8635379462542498, 1.6521894757586422, 2.2022783695123573, 2.5481508804154327, 2.7651545629478838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8596863746643066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6470825672149658})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5975203514099121})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.678226113319397})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6120941042900085})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6202195882797241})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.56044931640625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7121977806091309})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5022510290145874})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45220959186553955})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.46626394987106323})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4320249557495117})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 2000], ['id', 5170], ['id', 55739], ['id', 51800], ['id', 31426]], 'labels': [5, 8, 5, 5, 9], 'scores': [0.6700168358704082, 1.2633909677019188, 1.7396616224795887, 2.126085927980191, 2.3779722257909537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9550877809524536})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6243053674697876})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6251012086868286})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6564233899116516})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6446616053581238})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6240962743759155})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6587281227111816})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7183710336685181})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.805748701095581})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.594173974609375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7078197002410889})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48879244923591614})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.48774129152297974})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4441208839416504})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3904038369655609})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4073970317840576})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4226296842098236})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.37973886728286743})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 19814], ['id', 54957], ['id', 13003], ['id', 46406], ['id', 37281]], 'labels': [9, -1, -1, 3, -1], 'scores': [0.7823858933114871, 1.505545143929417, 2.1061193986315985, 2.5300931472068404, 2.7715011743907993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9746031165122986})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6653867363929749})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.592557966709137})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5869652032852173})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6068968772888184})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6108300685882568})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.671172022819519})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.6285302734375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7175878882408142})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5327448844909668})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47300291061401367})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.47882068157196045})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4723912179470062})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.41739898920059204})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 28189], ['id', 55906], ['id', 10756], ['id', 25176], ['id', 22203]], 'labels': [2, 2, 3, 4, 2], 'scores': [0.771286878110955, 1.4518767995154662, 1.9540014896931845, 2.286290650743596, 2.486553103842432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8619027137756348})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6593614816665649})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.61695396900177})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6397080421447754})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6697300672531128})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5730488300323486})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.701332688331604})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.582901171875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7341378927230835})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5648195147514343})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4731716215610504})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4347364008426666})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4544341564178467})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43090805411338806})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 7829], ['id', 45746], ['id', 12768], ['id', 17985], ['id', 38307]], 'labels': [-1, 8, 9, -1, -1], 'scores': [0.7530149216051611, 1.3845608526570934, 1.8935225260824584, 2.258506356852652, 2.49146480839263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.989105761051178})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6398677825927734})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6871218681335449})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6024171113967896})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.640390157699585})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6862118244171143})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7454612255096436})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.594910107421875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7179944515228271})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5263596773147583})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5132275819778442})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.46487659215927124})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4493260383605957})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.45266014337539673})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 42139], ['id', 44753], ['id', 47387], ['id', 47426], ['id', 8488]], 'labels': [4, 5, 8, 3, 6], 'scores': [0.755275848792174, 1.3881373369424699, 1.8948519258346774, 2.247163482100582, 2.452689860611855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9356970191001892})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6881149411201477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.633954644203186})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5849252343177795})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5713457465171814})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6967852115631104})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6404420137405396})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.594368896484375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7663540840148926})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5652605891227722})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45366066694259644})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4631713628768921})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.477203369140625})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43194007873535156})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 6604], ['id', 5422], ['id', 40066], ['id', 9770], ['id', 45555]], 'labels': [8, 7, 4, 5, 9], 'scores': [0.6663009718895037, 1.2809184971769048, 1.7839226627094202, 2.172085088236389, 2.4189504187864177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0140178203582764})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6451826095581055})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5639542937278748})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5133686065673828})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.536487340927124})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5538265705108643})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.599001407623291})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.49903837890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7214139699935913})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5208256244659424})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46147620677948})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42969030141830444})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.379403293132782})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3911929130554199})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 4328], ['id', 45094], ['id', 15252], ['id', 56004], ['id', 17121]], 'labels': [3, 2, 1, 8, 8], 'scores': [0.6968874162097107, 1.3404532239117763, 1.8497602741460604, 2.189608259638062, 2.3744617756202944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0960564613342285})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6244771480560303})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5733126401901245})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5416285991668701})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5837603211402893})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5703873634338379})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6235001087188721})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5785621404647827})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.624984860420227})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.619112491607666})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6319944858551025})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.610752294921875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7147045135498047})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4736936092376709})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43973785638809204})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39143818616867065})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4059194326400757})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37414050102233887})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3924120366573334})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 49571], ['id', 11100], ['id', 55043], ['id', 39825], ['id', 28539]], 'labels': [7, -1, -1, 6, -1], 'scores': [0.9627862579779785, 1.7494732846627454, 2.33085606346447, 2.7074641629383915, 2.930474571190473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.119512677192688})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6419756412506104})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5068376064300537})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5350234508514404})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.472604364156723})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5827988386154175})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5522373914718628})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.525012731552124})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.524124264717102})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6216260194778442})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6918785572052002})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6338216066360474})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9351, 'crossentropy': 0.538345458984375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7003133296966553})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49366438388824463})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41943883895874023})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40539050102233887})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.36464226245880127})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3807733952999115})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36163389682769775})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3466634750366211})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3540378212928772})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34628814458847046})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 34520], ['id', 16448], ['id', 32747], ['id', 20206], ['id', 51649]], 'labels': [6, 4, 8, 7, 0], 'scores': [0.8010783371217534, 1.5122014627290707, 2.0989307962603125, 2.4598857765335325, 2.6532134321139775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9628698825836182})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5535300970077515})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.545832633972168})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4857481122016907})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.576508641242981})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5413981676101685})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5584867596626282})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5736219882965088})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5759474635124207})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5638238787651062})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6068117618560791})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6176812052726746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5571812391281128})
store['active_learning_steps'][32]['training']['best_epoch']=10
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.55393974609375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.711796760559082})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5108996629714966})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4313424825668335})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37720805406570435})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34097251296043396})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36142247915267944})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35170623660087585})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3469342887401581})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.32812434434890747})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3302135467529297})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3421325981616974})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3155723214149475})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 42799], ['id', 3694], ['id', 39764], ['id', 48278], ['id', 10972]], 'labels': [2, -1, 8, 6, 2], 'scores': [0.8028454148991768, 1.5159498844705719, 2.0752689280727257, 2.433039759545526, 2.649520243527201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1561733484268188})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6355734467506409})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4871710538864136})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5996315479278564})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5321357846260071})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6435859799385071})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.53515927734375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7830724120140076})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5788799524307251})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5216078758239746})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4589575529098511})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4531511664390564})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 31456], ['id', 33338], ['id', 51264], ['id', 41165], ['id', 54923]], 'labels': [9, 8, 4, 3, 6], 'scores': [0.7393939687118838, 1.416857557913712, 1.9541296810167479, 2.3317091172158584, 2.5767068736066765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9644826650619507})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5453478097915649})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4870263338088989})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5007148385047913})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5186580419540405})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.48310035467147827})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5036253929138184})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5512987375259399})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4892570376396179})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9423, 'crossentropy': 0.454395556640625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6953141689300537})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45353397727012634})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3870052993297577})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36901137232780457})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3632705807685852})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34010958671569824})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3258413076400757})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.346996545791626})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52140], ['id', 38698], ['id', 24589], ['id', 3694], ['id', 24570]], 'labels': [4, 5, 8, -1, -1], 'scores': [0.7627224766417418, 1.4197233788666876, 1.9309868989576984, 2.2623255506502735, 2.4540708888650666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0932071208953857})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6301196217536926})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5560986995697021})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49878254532814026})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5598728656768799})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49807703495025635})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5831384658813477})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5586198568344116})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.558021605014801})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5874337553977966})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5752103328704834})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5995081067085266})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5418111085891724})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5618592500686646})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.631166934967041})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6449635028839111})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.6093168258666992})
store['active_learning_steps'][35]['training']['best_epoch']=14
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.533755078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7417798638343811})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46728992462158203})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3805217146873474})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.351487398147583})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34518688917160034})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33177077770233154})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33402538299560547})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 57728], ['id', 7168], ['id', 16823], ['id', 38890], ['id', 11877]], 'labels': [9, 8, 7, -1, 7], 'scores': [0.871558264343468, 1.5878471471532238, 2.149355361681238, 2.5153834264789863, 2.757016625105315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.933914840221405})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6024925112724304})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.536862313747406})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47511738538742065})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46432316303253174})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5034967660903931})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5164614915847778})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5464122295379639})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.473102197265625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6613360047340393})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45586705207824707})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4086844325065613})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40951406955718994})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37447574734687805})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35687023401260376})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36819982528686523})
store['active_learning_steps'][36]['eval_training']['best_epoch']=5
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 9158], ['id', 59919], ['id', 15781], ['id', 13176], ['id', 12000]], 'labels': [0, 1, 5, 8, 7], 'scores': [0.767016104081349, 1.393583861834268, 1.9050243937114102, 2.26588399419599, 2.5136480463691466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0417441129684448})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5810983180999756})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4598081707954407})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5316078662872314})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4794081449508667})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4800153970718384})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.525122344493866})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4938376545906067})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4855175316333771})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48435282707214355})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5372006297111511})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48858508467674255})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.4902689453125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6951736807823181})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47478383779525757})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4140547513961792})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3766454756259918})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3620869517326355})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3468635678291321})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3462408185005188})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31695881485939026})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.309481143951416})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35287153720855713})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32052475214004517})
store['active_learning_steps'][37]['eval_training']['best_epoch']=9
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 53872], ['id', 40766], ['id', 54598], ['id', 14722], ['id', 59634]], 'labels': [8, 4, 5, 0, 9], 'scores': [0.8744038618745082, 1.6541362665384334, 2.1946605987195715, 2.5458421218734095, 2.748997359926313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.091956377029419})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.557958722114563})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5025729537010193})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4442652463912964})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4734165072441101})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47859814763069153})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4467581510543823})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44445398449897766})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5127162933349609})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5310491323471069})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5445566177368164})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.48397236328125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7223060131072998})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5146967768669128})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37616220116615295})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3632631301879883})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32214784622192383})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32624515891075134})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29906922578811646})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30809396505355835})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29148808121681213})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29866868257522583})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 54032], ['id', 40530], ['id', 18682], ['id', 13927], ['id', 6826]], 'labels': [6, 2, 7, 6, 3], 'scores': [0.8018062652563189, 1.514728415776947, 2.0761432548916314, 2.460926941534444, 2.7054358485863927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9588102102279663})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5372375845909119})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46970200538635254})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47490307688713074})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4429280161857605})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43699759244918823})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4739726781845093})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4814521372318268})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46016913652420044})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.43893583984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7686651945114136})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4857683777809143})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41494452953338623})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3832511007785797})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3533756136894226})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.340387225151062})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3310946822166443})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3379855155944824})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 1518], ['id', 12497], ['id', 35944], ['id', 56286], ['id', 16202]], 'labels': [9, 0, 3, 8, -1], 'scores': [0.791966064559332, 1.4622852152835275, 1.9417924129445243, 2.281273459772697, 2.491412396576072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0612014532089233})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5620009899139404})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4075247645378113})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39638447761535645})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4209548234939575})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3693356513977051})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41380637884140015})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40671807527542114})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.43090635538101196})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.411121484375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7688069343566895})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45852553844451904})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38185426592826843})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34187835454940796})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3420024514198303})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3033716678619385})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3134711980819702})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31562793254852295})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 5315], ['id', 56914], ['id', 51415], ['id', 54586], ['id', 49074]], 'labels': [3, 0, 0, 9, -1], 'scores': [0.6734893019935477, 1.2655041021708824, 1.7334996435500019, 2.0773816908390277, 2.3231422980862355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1708896160125732})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.571625828742981})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4998498558998108})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48801764845848083})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47651544213294983})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49283093214035034})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.46287596225738525})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4936147928237915})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5216727256774902})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45325279235839844})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4739258885383606})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4977024793624878})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4777244031429291})
store['active_learning_steps'][41]['training']['best_epoch']=10
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9442, 'crossentropy': 0.477052880859375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7271202206611633})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4563334286212921})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.400623083114624})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3441620469093323})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3376552164554596})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.314411461353302})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2912365794181824})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2979243993759155})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2789403796195984})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3117954432964325})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30247676372528076})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2973899841308594})
store['active_learning_steps'][41]['eval_training']['best_epoch']=11
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 53873], ['id', 36939], ['id', 34650], ['id', 53054], ['id', 59836]], 'labels': [4, -1, 2, -1, 1], 'scores': [0.8927181328232465, 1.6465401525825616, 2.2146532352380683, 2.587294410349295, 2.7737906166971857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0883570909500122})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5265549421310425})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4447867274284363})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4288681149482727})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3699471354484558})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3687235116958618})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3886725902557373})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40470901131629944})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.376452392578125}
