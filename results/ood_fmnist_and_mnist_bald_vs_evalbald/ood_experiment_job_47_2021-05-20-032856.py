store = {}
store['timestamp']=1621477736
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=47']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=47
store['worker_id']=47
store['num_workers']=80
store['config']={'seed': 1283, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.3716793060302734})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.897088050842285})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.39961838722229})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2913506031036377})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.373009204864502})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6079, 'crossentropy': 3.0739474609375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 37326], ['id', 44790], ['id', 31020], ['id', 20331], ['id', 49896]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5294369027543784, 2.6894897785236465, 3.5242542835357646, 4.060044783438052, 4.323358659403937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.4320900440216064})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.9037246704101562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.16855525970459})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1647772789001465})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.855003595352173})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.653506278991699})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.609435558319092})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.948227882385254})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.6261706352233887})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6004, 'crossentropy': 3.8810015625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 39723], ['id', 37171], ['id', 48926], ['id', 14335], ['id', 31892]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5422343083515888, 2.8218759927532355, 3.700416412163878, 4.190233756140963, 4.428471717139641]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.609023332595825})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 3.360595941543579})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.795793294906616})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.9586527347564697})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.9544882774353027})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.047112941741943})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5816, 'crossentropy': 3.711108984375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 54588], ['id', 9046], ['id', 2381], ['id', 27863], ['id', 39545]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.4900915068509373, 2.6563631096176166, 3.497796427489634, 3.9988302555985475, 4.279493772788198]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.674294948577881})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.4012269973754883})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.361936569213867})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.8609189987182617})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.6789135932922363})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5787, 'crossentropy': 3.690195703125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 57328], ['id', 48420], ['id', 32399], ['id', 1672], ['id', 22231]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4741779310533392, 2.6226630874247023, 3.5059531243880366, 4.056534255967692, 4.324400406599796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.7341628074645996})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.2601242065429688})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2578468322753906})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.425790786743164})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.6678338050842285})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4508109092712402})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.6398696899414062})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 4.107003211975098})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.289262771606445})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.745288133621216})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.536334276199341})
store['active_learning_steps'][4]['training']['best_epoch']=8
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6054, 'crossentropy': 4.25172421875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 22518], ['id', 28856], ['id', 49058], ['id', 27355], ['id', 51163]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.5891362827481652, 2.8452386605083477, 3.7542830508077865, 4.21771291716535, 4.437772487163368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.3349721431732178})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6372532844543457})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.787555694580078})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.041421413421631})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3719749450683594})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.514634132385254})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.425386905670166})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.530651092529297})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2875916957855225})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6087, 'crossentropy': 3.788455859375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 58174], ['id', 45324], ['id', 13677], ['id', 49593], ['id', 51986]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6703354216533364, 3.03002085044586, 3.861199095085019, 4.262960202801298, 4.458162124794209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.8652987480163574})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.573164463043213})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.098572254180908})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.596823215484619})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 4.513339996337891})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.578222751617432})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 5.08846378326416})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5833, 'crossentropy': 3.9092625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 48846], ['id', 3356], ['id', 8584], ['id', 32504], ['id', 1682]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.551906380853659, 2.735999883238165, 3.5431889842672994, 4.039861170950701, 4.310287695904268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.2016372680664062})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.752793788909912})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.3097872734069824})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.4579200744628906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.5629875659942627})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5969, 'crossentropy': 3.0484005859375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 35314], ['id', 48420], ['id', 16931], ['id', 20894], ['id', 19487]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.533667886745687, 2.638624980831445, 3.4459678690767106, 3.9465073926896768, 4.234705039058486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.5071916580200195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.939342975616455})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.432551860809326})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.728163719177246})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5304641723632812})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5999, 'crossentropy': 3.222543359375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 54719], ['id', 45161], ['id', 29503], ['id', 24172], ['id', 32355]], 'labels': [-1, -1, -1, 4, -1], 'scores': [1.5191608637404026, 2.710010828483549, 3.5402548823912436, 4.041167521880498, 4.322498658737931]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.4844932556152344})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 3.1068780422210693})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 3.735619068145752})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.874074935913086})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.935969829559326})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 4.661554336547852})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.185614585876465})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.266549587249756})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5837, 'crossentropy': 3.821444140625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 17774], ['id', 5684], ['id', 4542], ['id', 36642], ['id', 18501]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6116675297483645, 2.7830688777694563, 3.628199452424755, 4.119239514782958, 4.371750313173064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.464451313018799})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.242039680480957})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.657905340194702})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.046964168548584})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5696, 'crossentropy': 2.565346484375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 44544], ['id', 20331], ['id', 14520], ['id', 51786], ['id', 10070]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.356543065780036, 2.367124776371465, 3.1164771456059857, 3.6536527468087154, 4.002310076273674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.5359137058258057})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.980637311935425})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.4015116691589355})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.168246030807495})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.5862271785736084})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.5312142372131348})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.604383945465088})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5778, 'crossentropy': 3.52604140625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 17774], ['id', 3696], ['id', 33591], ['id', 47953], ['id', 20741]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6251380927702472, 2.82069317245487, 3.6704910535476936, 4.142575809326408, 4.391078157943643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.493713617324829})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.8529438972473145})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.062565326690674})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0539515018463135})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.5646748542785645})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.6464710235595703})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.6031274795532227})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.27443203125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 39046], ['id', 47260], ['id', 9341], ['id', 36985], ['id', 606]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.4953867249631614, 2.5614566132510976, 3.432009300690849, 3.9619859476351653, 4.251859260413205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.3737144470214844})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 3.1230335235595703})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.5995020866394043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.77970552444458})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5748, 'crossentropy': 2.5843447265625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 21817], ['id', 49181], ['id', 4725], ['id', 35802], ['id', 4071]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.4839172328277406, 2.5277443885821347, 3.258673643527084, 3.7721351252321575, 4.102862077358064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 2.4786019325256348})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 3.3770337104797363})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.337003707885742})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.9475576877593994})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.556997060775757})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 3.9688961505889893})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5633, 'crossentropy': 3.5422390625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 14715], ['id', 29261], ['id', 39673], ['id', 30580], ['id', 11044]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.524258090627943, 2.6618119917506, 3.4928363424536313, 4.00574125386643, 4.296733512460236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.5773603916168213})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.2239861488342285})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.6250410079956055})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 4.057567119598389})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.521223068237305})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5701, 'crossentropy': 3.454163671875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 21797], ['id', 24296], ['id', 9056], ['id', 14051], ['id', 49438]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4665052871892632, 2.565042226734949, 3.418910803573058, 3.9220887604713184, 4.2308682263818245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.249314546585083})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.9376206398010254})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.541571855545044})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 4.007542610168457})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.6340837478637695})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5738, 'crossentropy': 3.068375390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 32504], ['id', 4799], ['id', 42091], ['id', 55774], ['id', 13677]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.388858072066098, 2.457537855087786, 3.249370165536682, 3.775580852011413, 4.114447938262291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.4606683254241943})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.9298605918884277})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.3641304969787598})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.069103479385376})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.3794798851013184})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.7702560424804688})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.804955244064331})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.895439624786377})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5862, 'crossentropy': 3.585080078125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 36675], ['id', 35884], ['id', 7327], ['id', 36553], ['id', 8516]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.5830473507696392, 2.8001583456445958, 3.6562140036021837, 4.128093787347234, 4.373994938574663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.0682973861694336})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.4093875885009766})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.844194173812866})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.1498990058898926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5608277320861816})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0245347023010254})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.897289991378784})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.1580631732940674})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.305185317993164})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6041, 'crossentropy': 3.421672265625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 8493], ['id', 5411], ['id', 37074], ['id', 51718], ['id', 6029]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.53509624059119, 2.7694940906608805, 3.6613683728792488, 4.149688926547439, 4.381825311076545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 2.4871740341186523})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.9538581371307373})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.485987663269043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 4.069731712341309})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.558321952819824})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.5826, 'crossentropy': 2.9402857421875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 57880], ['id', 56330], ['id', 55311], ['id', 40744], ['id', 20142]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.436653160706237, 2.6578089536840785, 3.4649547877673514, 3.98164405420777, 4.261606647679822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.356623888015747})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.7760050296783447})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.0137548446655273})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.6213903427124023})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5467281341552734})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.671566963195801})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.239592552185059})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5944, 'crossentropy': 3.703885546875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 37818], ['id', 29764], ['id', 8826], ['id', 11960], ['id', 28483]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4521571096397763, 2.6564736119664505, 3.4750322636342794, 3.973805907377634, 4.256875148293095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.246992588043213})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.72659969329834})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.3696937561035156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 3.410973310470581})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.6801517009735107})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.3827993869781494})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.748121738433838})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.5730156898498535})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 4.084871292114258})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.880849838256836})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.5785, 'crossentropy': 4.056947265625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 56004], ['id', 51088], ['id', 54948], ['id', 24294], ['id', 53100]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5071713048326174, 2.766934793095622, 3.6100764215459638, 4.130745632857739, 4.3815494050427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.0613255500793457})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 2.913276195526123})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 3.2181344032287598})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.704801321029663})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.5786, 'crossentropy': 2.13994296875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 56763], ['id', 44455], ['id', 42335], ['id', 31587], ['id', 23586]], 'labels': [-1, -1, -1, 6, 3], 'scores': [1.1795173061714324, 2.0449028954350714, 2.766609328528795, 3.332299741732884, 3.7452259926689653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.218634605407715})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.940474510192871})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2299628257751465})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.203017473220825})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5484399795532227})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.7493343353271484})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.110028266906738})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6016, 'crossentropy': 3.359766796875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 33126], ['id', 25856], ['id', 10817], ['id', 20816], ['id', 6131]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4796448015862897, 2.6341088527066616, 3.5269846177376536, 4.050078501025681, 4.332600912059945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.1066384315490723})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.7442150115966797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.479379177093506})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.4745640754699707})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.8767518997192383})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.161275386810303})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.5845, 'crossentropy': 3.48504765625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 6306], ['id', 17542], ['id', 6185], ['id', 28347], ['id', 27471]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3572010799531382, 2.4796168549350073, 3.3860578775377546, 3.9383435563822413, 4.26584999440818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.1997504234313965})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.4656078815460205})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.5394551753997803})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.529421329498291})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.3951292037963867})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5934, 'crossentropy': 2.8122556640625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 19952], ['id', 22547], ['id', 16131], ['id', 31677], ['id', 14047]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.398178089160596, 2.4656344067863403, 3.2661909148779893, 3.7949016221159333, 4.13688274440025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.1526687145233154})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.70637845993042})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.3723602294921875})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.3941235542297363})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.518766164779663})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.5873, 'crossentropy': 2.822444921875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 14141], ['id', 222], ['id', 59754], ['id', 42595], ['id', 17542]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2569051552518642, 2.3397196523051607, 3.1793189518639657, 3.7483247136877624, 4.115208816935581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.9960087537765503})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.9166088104248047})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.079251527786255})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.242037773132324})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.576462745666504})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.5666937828063965})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5052297115325928})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.933490514755249})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.8481876850128174})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6003, 'crossentropy': 3.339780078125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 3760], ['id', 23110], ['id', 45177], ['id', 4725], ['id', 15600]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4967136450473353, 2.650930925412491, 3.518609272231428, 4.061626172330428, 4.3312948091038965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 2.1049084663391113})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.6962671279907227})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.7485032081604004})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.302126407623291})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.246967315673828})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.3589560985565186})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.323880672454834})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.3187005519866943})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.6286673545837402})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.9918313026428223})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.118182420730591})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.8678550720214844})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.089131832122803})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.9884395599365234})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.259972095489502})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 4.066102981567383})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.719944477081299})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 4.153152942657471})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 4.595989227294922})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.053254127502441})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.645794868469238})
store['active_learning_steps'][28]['training']['best_epoch']=18
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.5936, 'crossentropy': 4.4960375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 2803], ['id', 51620], ['id', 27539], ['id', 5982], ['id', 15709]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5638138366972298, 2.884540831739952, 3.7919814353018033, 4.264183855095016, 4.468547398288056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.9889605045318604})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.882282257080078})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.028576135635376})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.2744088172912598})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.242185354232788})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.686232089996338})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.615659713745117})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.908097267150879})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 4.023489952087402})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.009219646453857})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.7712788581848145})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.5981, 'crossentropy': 3.930084375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 5553], ['id', 10217], ['id', 9880], ['id', 51463], ['id', 11984]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4501566097805847, 2.6787929893958893, 3.5458527823593364, 4.100778422318571, 4.372778041257732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.62734317779541})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.3177857398986816})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.5943398475646973})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.657305955886841})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.7359933853149414})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 4.559695720672607})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 4.370001792907715})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.374547004699707})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.5771, 'crossentropy': 4.115053515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 35801], ['id', 49858], ['id', 29180], ['id', 59693], ['id', 3613]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.40030238386993, 2.583820928272189, 3.4835970388397035, 4.025783158099001, 4.320392390313527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 2.356001377105713})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.842745304107666})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.9225125312805176})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.019927978515625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 3.801910400390625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.698145866394043})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.707439422607422})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.5843, 'crossentropy': 4.04361015625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 49144], ['id', 4636], ['id', 27407], ['id', 7621], ['id', 21941]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.374509462474535, 2.5802688259034015, 3.4664688313840095, 4.00570911517522, 4.315271295590881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 2.214923858642578})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.690770149230957})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.326305389404297})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.72568941116333})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 4.013431549072266})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 4.567192077636719})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.5656, 'crossentropy': 3.64776796875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 59451], ['id', 38137], ['id', 35671], ['id', 38376], ['id', 54288]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3742476420419196, 2.5662803571308714, 3.5098718066461876, 4.014436816527245, 4.285206174498589]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 2.2462539672851562})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.614664077758789})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.1032521724700928})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.318570137023926})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.818387269973755})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.51165771484375})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.5796, 'crossentropy': 3.498745703125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 26819], ['id', 43560], ['id', 49144], ['id', 10297], ['id', 10283]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4104955642980364, 2.5329901636965286, 3.412876920521734, 3.957340194706396, 4.2656403933331335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 2.5335044860839844})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.375020980834961})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.487743377685547})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.617435932159424})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5323195457458496})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 3.9832472801208496})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.282964706420898})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.5901, 'crossentropy': 3.660402734375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 47663], ['id', 40426], ['id', 23027], ['id', 53015], ['id', 325]], 'labels': [-1, -1, -1, 0, 0], 'scores': [1.4650415189760042, 2.6545671329322893, 3.5218588896861434, 4.020036683765689, 4.299121530993207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.9782744646072388})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.5976438522338867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.7401928901672363})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.754523992538452})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1728971004486084})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.363659381866455})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9950804710388184})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 2.8973154296875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 14047], ['id', 35460], ['id', 11274], ['id', 43742], ['id', 40732]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.4571267954341296, 2.6649611138489457, 3.510988563509706, 4.069485498256308, 4.356849228622078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.0910210609436035})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.573225259780884})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.038684844970703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.658351182937622})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.250913143157959})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.4825291633605957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.5008432865142822})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.5913, 'crossentropy': 3.01036640625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 21776], ['id', 35044], ['id', 22546], ['id', 52694], ['id', 4733]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.2963479741751804, 2.383467094549715, 3.263310395579291, 3.837285276891957, 4.179260682741621]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.929398775100708})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.6878812313079834})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.0459346771240234})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.3491477966308594})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.066446304321289})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.5876, 'crossentropy': 2.793266796875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 17736], ['id', 36155], ['id', 12184], ['id', 1253], ['id', 46295]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3952638679498692, 2.510133847099504, 3.367523819695867, 3.9568372417634645, 4.253680929236765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.003688097000122})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.749535083770752})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.0495736598968506})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.404425859451294})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.18623423576355})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2046144008636475})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.551692008972168})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.5967659950256348})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.057342529296875})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6014, 'crossentropy': 3.2425509765625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 39110], ['id', 42080], ['id', 8495], ['id', 52324], ['id', 37738]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5726763263651424, 2.789615922167235, 3.620882227692425, 4.1377959262893675, 4.378373047123658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.969630479812622})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.9420931339263916})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.364386558532715})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.1990392208099365})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.8840160369873047})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8861169815063477})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5574913024902344})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.479219436645508})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.20368766784668})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6144, 'crossentropy': 3.038851953125}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 43452], ['id', 9699], ['id', 11234], ['id', 347], ['id', 28347]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.5897380941452024, 2.77549219967435, 3.7089073397257284, 4.142209358726428, 4.373486454810136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.1245193481445312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.5423591136932373})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.2462258338928223})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.3685696125030518})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.5192723274230957})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.5847, 'crossentropy': 2.7895072265625}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 38496], ['id', 30322], ['id', 16131], ['id', 47260], ['id', 31677]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4393462779868433, 2.5195421287284665, 3.337606179338729, 3.84576089333461, 4.177906859414344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.999952793121338})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.8859002590179443})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.923565149307251})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.300591468811035})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.693678855895996})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.3628287315368652})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.5489354133605957})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.5971, 'crossentropy': 3.286732421875}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 4757], ['id', 8488], ['id', 19307], ['id', 13650], ['id', 20124]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4313207769923268, 2.5788570261753945, 3.4448272971291534, 3.9677463930067995, 4.273848406991732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.0844998359680176})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.4916346073150635})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.045572280883789})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.2115116119384766})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.561481237411499})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.6115236282348633})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.7274296283721924})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.313023567199707})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.8173484802246094})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.081242561340332})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.9659128189086914})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6013, 'crossentropy': 3.838328515625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 14047], ['id', 18288], ['id', 22797], ['id', 14723], ['id', 14265]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5540925339263123, 2.747487713507689, 3.6097128585264633, 4.144035067764029, 4.403573492670839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.0906195640563965})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.9316606521606445})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.799008846282959})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.4120309352874756})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.428633213043213})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 4.024633407592773})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.5503804683685303})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.8308849334716797})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6014, 'crossentropy': 3.3391234375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 11008], ['id', 24940], ['id', 10716], ['id', 27], ['id', 44644]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.408345878978695, 2.547405575795981, 3.4434720346551204, 4.018403431126856, 4.296380205111109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.1660709381103516})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.521815299987793})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.271892547607422})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.256324529647827})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.349763870239258})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.219644069671631})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.147599458694458})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.4350812435150146})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.5963, 'crossentropy': 3.529058984375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 27077], ['id', 54768], ['id', 21650], ['id', 34678], ['id', 13549]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.460605057236069, 2.6622101927805035, 3.4923149931384625, 4.002049397024657, 4.290807817123861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 2.2797646522521973})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 3.1808457374572754})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.9776740074157715})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.4166946411132812})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.566366672515869})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.3233065605163574})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.5546281337738037})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.314411163330078})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.5929, 'crossentropy': 3.6948265625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 39812], ['id', 1674], ['id', 29766], ['id', 10716], ['id', 53280]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5015720998267816, 2.7353597529534195, 3.6186317786829374, 4.116828149286732, 4.367037460215042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.040191173553467})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.843867540359497})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.832465648651123})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.0939011573791504})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.9890148639678955})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.363853931427002})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.843116283416748})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.6333584785461426})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 3.208605078125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 5982], ['id', 29048], ['id', 26636], ['id', 32162], ['id', 5205]], 'labels': [-1, -1, 9, -1, -1], 'scores': [1.5703193531679287, 2.7760055289362597, 3.6223671820631393, 4.13331898693432, 4.373917529695618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.001365900039673})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.2789974212646484})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.9642844200134277})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.462996244430542})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.3749372959136963})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.526407241821289})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.0923094749450684})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.368495464324951})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6828975677490234})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.5871, 'crossentropy': 3.6585828125}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 9172], ['id', 37738], ['id', 56044], ['id', 30322], ['id', 50231]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5339291345733557, 2.8793245350163934, 3.750178468086336, 4.168762930490263, 4.397288771413971]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.1278128623962402})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.679715633392334})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2929069995880127})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.178225517272949})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.6592302322387695})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.935163736343384})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.5843, 'crossentropy': 3.355402734375}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 18854], ['id', 40862], ['id', 35344], ['id', 22288], ['id', 28682]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3801525825552363, 2.513586455431385, 3.350452032333555, 3.9244175057625466, 4.254751390458487]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.028487205505371})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.8435750007629395})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.897888660430908})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.342616558074951})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.4951319694519043})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.5966, 'crossentropy': 2.8175109375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 45330], ['id', 57114], ['id', 58855], ['id', 32144], ['id', 51288]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5055638979552315, 2.6402884011378607, 3.422514305836426, 3.937924728708805, 4.2395587143413405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.264132499694824})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.8925375938415527})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.041605234146118})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.427638292312622})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.392676830291748})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.599226951599121})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.5738420486450195})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3606317043304443})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.5905, 'crossentropy': 3.656779296875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 19961], ['id', 37738], ['id', 40308], ['id', 15036], ['id', 52556]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.4108408133057657, 2.606143069390228, 3.4795477060264126, 4.0110776127155665, 4.307423571259411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.099205255508423})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.669375419616699})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.339718818664551})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.27207612991333})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.633791446685791})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.857697010040283})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.7463161945343018})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.99459171295166})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.876411199569702})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.5858, 'crossentropy': 3.943560546875}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 18026], ['id', 8890], ['id', 31704], ['id', 24753], ['id', 31947]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.6069247249086147, 2.8534969378311095, 3.730199325966236, 4.2015369253438, 4.426635873468193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.113448143005371})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.4602856636047363})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.689344882965088})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.892709732055664})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.5852532386779785})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.2886152267456055})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.423825740814209})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.701439380645752})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.169198989868164})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.8064308166503906})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.877311944961548})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.948265314102173})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6887831687927246})
store['active_learning_steps'][52]['training']['best_epoch']=10
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6031, 'crossentropy': 3.93248203125}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 26723], ['id', 18846], ['id', 31895], ['id', 27971], ['id', 14619]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5431698538302285, 2.8631996534504784, 3.767671615817739, 4.234051849203155, 4.4513195420769085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.766107201576233})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.2048003673553467})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.905667781829834})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.10932993888855})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.565565586090088})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6089, 'crossentropy': 2.2618951171875}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 4829], ['id', 53266], ['id', 29289], ['id', 10038], ['id', 6456]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.287278984620833, 2.3460574972943675, 3.1918202490421246, 3.787055400507061, 4.131229970940108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.0346992015838623})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.454291343688965})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.790255546569824})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.0819222927093506})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.461276054382324})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.6852962970733643})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.4358153343200684})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.551884889602661})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.525874137878418})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.5969, 'crossentropy': 3.871180859375}
