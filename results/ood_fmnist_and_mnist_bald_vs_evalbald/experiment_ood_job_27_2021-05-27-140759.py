store = {}
store['timestamp']=1622120879
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=27']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=27
store['worker_id']=27
store['num_workers']=80
store['config']={'seed': 1262, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.416628837585449})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.129458427429199})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6179609298706055})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5014255046844482})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.594898223876953})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.046952247619629})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4718017578125})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6009, 'crossentropy': 3.88395390625}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 48240], ['ood', 6580], ['ood', 6935], ['ood', 8875], ['ood', 14129]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6279843610870381, 2.8160071481490165, 3.666827462319839, 4.133792596950831, 4.380029341116835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.3904190063476562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.6635847091674805})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.961785316467285})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.240204334259033})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.711061477661133})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.8355448246002197})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 3.1838990234375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 44544], ['ood', 8027], ['ood', 30511], ['ood', 39467], ['ood', 4797]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5967527599353097, 2.7677422485655763, 3.583425483918335, 4.0976225188777615, 4.350420962033201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.2603700160980225})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.902705192565918})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.175992965698242})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3204469680786133})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3806910514831543})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5699758529663086})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 3.27104453125}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 19202], ['ood', 25907], ['ood', 32776], ['ood', 8338], ['ood', 50069]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5603870671039135, 2.6906251361291464, 3.5383859599726026, 4.06457555467171, 4.316450762108975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.4087178707122803})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.965134382247925})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.4881882667541504})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.410871982574463})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5807, 'crossentropy': 2.4955201171875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 14260], ['ood', 4799], ['ood', 25627], ['ood', 27652], ['ood', 48608]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3266226497124904, 2.3522259756833708, 3.115352972158643, 3.6347162368246204, 4.008592997231563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.6428213119506836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.4600563049316406})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.7100119590759277})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.986227512359619})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.218148231506348})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5899, 'crossentropy': 3.41551484375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 4737], ['ood', 32393], ['ood', 4799], ['ood', 17728], ['ood', 30454]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5160612683355352, 2.5857806094226707, 3.4376235662275896, 3.9871864966337522, 4.3027183687095825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.425680637359619})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.9220352172851562})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.131615161895752})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.50671124458313})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3152999877929688})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3201112747192383})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.147634744644165})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.4426212310791016})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.846139430999756})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.751284599304199})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.637023046875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 222], ['ood', 8787], ['ood', 47534], ['ood', 20752], ['ood', 3397]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5573302990124724, 2.8011886798193624, 3.681629179394152, 4.149521064071945, 4.3881090156128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.311349630355835})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9763312339782715})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.755619525909424})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.6130082607269287})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.8314015865325928})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5895, 'crossentropy': 3.411803125}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 47741], ['ood', 56833], ['ood', 5728], ['ood', 24276], ['id', 52590]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.517214152945529, 2.706111302188245, 3.4755309706243143, 3.9903222187700678, 4.287640280064391]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.3617358207702637})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.697056770324707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.307931900024414})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.6640563011169434})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 4.003352165222168})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5906, 'crossentropy': 3.17242265625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 44544], ['ood', 53516], ['id', 4353], ['ood', 25868], ['ood', 16911]], 'labels': [-1, -1, 6, -1, -1], 'scores': [1.3663173764150425, 2.461302432280429, 3.3025452911031277, 3.8478607904282933, 4.177237787722085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.4771339893341064})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 3.48228120803833})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.6220664978027344})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.194455623626709})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 4.717330455780029})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 4.182755470275879})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.326858043670654})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.776214599609375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.4368486404418945})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 4.483603477478027})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5696, 'crossentropy': 4.471993359375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 24113], ['ood', 17491], ['ood', 18564], ['ood', 47260], ['ood', 42450]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5728644006892702, 2.768830976343174, 3.610841401418716, 4.154074527725859, 4.408174722760172]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1860148906707764})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.530993938446045})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3767099380493164})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5118818283081055})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6033, 'crossentropy': 2.3703908203125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 44332], ['ood', 1479], ['ood', 53120], ['ood', 51786], ['ood', 8729]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2987491260823378, 2.346641046229635, 3.0880635901018554, 3.618926066154825, 3.9755355837338486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.3679566383361816})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.597350597381592})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.7730937004089355})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.7509782314300537})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.3590927124023438})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.316290855407715})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.7102630138397217})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.806100845336914})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.8978981971740723})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.2279582023620605})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.747382164001465})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5989, 'crossentropy': 3.917724609375}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 33282], ['ood', 6245], ['ood', 4833], ['ood', 50523], ['ood', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6755055590069352, 2.887466652648519, 3.730633717099609, 4.21087288427824, 4.441315469948131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.499920129776001})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.9009642601013184})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.2412028312683105})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.132462501525879})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.7012014389038086})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.802828311920166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.5682196617126465})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.598, 'crossentropy': 3.590476953125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 31216], ['ood', 15452], ['ood', 45209], ['id', 1254], ['ood', 27393]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.5242647431649188, 2.8079403329907677, 3.6951667870367793, 4.17108255349713, 4.408737622973829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.3503715991973877})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0528266429901123})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.8170199394226074})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.440351963043213})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.566819667816162})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5965, 'crossentropy': 3.042337109375}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 49092], ['ood', 46861], ['ood', 58353], ['id', 39750], ['ood', 16268]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.6290072766777568, 2.786704196710018, 3.5469601575619345, 4.0512282844938134, 4.318529096386018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.0974416732788086})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.0567126274108887})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 3.2869160175323486})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.308866024017334})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5967, 'crossentropy': 2.249949609375}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 32578], ['ood', 44914], ['ood', 24944], ['ood', 2089], ['ood', 45255]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3553256374804716, 2.353309855838558, 3.0931649523078635, 3.632674682274043, 4.002852007514207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.08573055267334})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.807715892791748})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.541515827178955})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0056684017181396})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.9952714443206787})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.970661163330078})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6166, 'crossentropy': 2.5786375}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 41716], ['ood', 25830], ['ood', 1303], ['ood', 53077], ['ood', 35560]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.493635408434927, 2.7950518461450367, 3.57430640844151, 4.056584067805423, 4.317573610917761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.316408634185791})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.218702793121338})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.21032977104187})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.8186237812042236})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.14585542678833})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.666147232055664})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5788, 'crossentropy': 3.33834296875}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 4252], ['ood', 25382], ['ood', 28204], ['ood', 16590], ['ood', 49200]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5970195008468293, 2.726885084366616, 3.5824559675264025, 4.089385629415955, 4.341176424802184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.2320151329040527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.1379785537719727})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.171100378036499})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.109302520751953})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5103187561035156})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.512558937072754})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6115, 'crossentropy': 3.1307365234375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 6454], ['ood', 45998], ['ood', 5982], ['ood', 36553], ['ood', 16921]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5069510787021594, 2.717359954728171, 3.623088462886627, 4.142327530574441, 4.396633267583919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1249282360076904})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.848389148712158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.846055269241333})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.555753231048584})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5998, 'crossentropy': 2.378633203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 45148], ['ood', 19337], ['ood', 41937], ['ood', 56823], ['ood', 5684]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3793800823722142, 2.452780447866467, 3.220399398327287, 3.75401504880986, 4.090128012990071]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.119595527648926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.850900888442993})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.1175379753112793})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3392333984375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8628435134887695})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.5886, 'crossentropy': 3.009748828125}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 28396], ['id', 59010], ['ood', 59355], ['ood', 23884], ['ood', 55729]], 'labels': [-1, 5, -1, -1, -1], 'scores': [1.4091382895659557, 2.547183788597492, 3.3554108910215863, 3.930719513802904, 4.242168566880902]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.019047260284424})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5721287727355957})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7006168365478516})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7575936317443848})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.957305908203125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.250159502029419})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.362682342529297})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3586111068725586})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6239, 'crossentropy': 3.0142814453125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 55024], ['ood', 25325], ['ood', 2202], ['ood', 30295], ['ood', 14175]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.598754206647551, 2.729373287398082, 3.572171898853828, 4.068458571899932, 4.354120311484596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.194216012954712})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.1072216033935547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.491149425506592})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.7236127853393555})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6011, 'crossentropy': 2.31846953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 42809], ['ood', 52423], ['ood', 54547], ['ood', 54066], ['ood', 54832]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3601353538311467, 2.345616683196309, 3.0710031917654197, 3.6096869070337876, 3.9719904872647156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8959261178970337})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.6564180850982666})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7407803535461426})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5581789016723633})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1003518104553223})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.2393407821655273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0690081119537354})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6313, 'crossentropy': 2.8058306640625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 4781], ['ood', 31665], ['ood', 54813], ['ood', 28030], ['ood', 16816]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6307697171692555, 3.0107036944783605, 3.7430206461453377, 4.160901497647362, 4.3863125290945915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.307438611984253})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.7151169776916504})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.982186794281006})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.191948413848877})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.3227946758270264})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.245497703552246})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6717543601989746})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2949411869049072})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.61, 'crossentropy': 3.376618359375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 39046], ['ood', 55709], ['ood', 54288], ['ood', 20357], ['ood', 17728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5391370191469387, 2.7253026427105445, 3.6082054990216683, 4.12922502646328, 4.390618665161707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.362140655517578})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.737255334854126})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.4754538536071777})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3518106937408447})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.653262138366699})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.52471661567688})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.429163932800293})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.8868370056152344})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.9861907958984375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.906771659851074})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.700077533721924})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6021, 'crossentropy': 4.018530078125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 25180], ['ood', 19429], ['ood', 39720], ['id', 35916], ['ood', 25325]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.6699946909441148, 2.958280258269887, 3.8161154111575737, 4.242391358934377, 4.457340701295162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1200106143951416})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.639385223388672})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.567059278488159})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8793373107910156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.2825536727905273})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.226158618927002})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0947065353393555})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.478395462036133})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1928911209106445})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6311, 'crossentropy': 3.32982265625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 8584], ['ood', 55699], ['ood', 11193], ['ood', 6857], ['ood', 21977]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4145763918560552, 2.6720689107548248, 3.5393131801354762, 4.088000969310018, 4.358601746651329]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.047011137008667})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.507356643676758})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8231801986694336})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.773707151412964})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2638235092163086})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1842408180236816})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.7816901206970215})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 2.834540234375}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 32504], ['ood', 25022], ['ood', 54224], ['ood', 42639], ['ood', 46570]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4482040514624566, 2.6509613530648135, 3.545607048787895, 4.072270447942096, 4.359926399505836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.888875961303711})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4392614364624023})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.7268733978271484})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.499286651611328})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3378539085388184})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8189353942871094})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.255385160446167})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.032700777053833})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2918925285339355})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.2068095207214355})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.076132297515869})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.361929178237915})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.535428524017334})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.118966579437256})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.612865447998047})
store['active_learning_steps'][26]['training']['best_epoch']=12
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6371, 'crossentropy': 3.519689453125}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 45518], ['ood', 47636], ['ood', 37080], ['ood', 14072], ['ood', 20476]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6212210461524075, 2.9352379121203827, 3.770253813293003, 4.235410236896318, 4.4485372184398795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.058716058731079})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.233278274536133})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.569697856903076})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.704598903656006})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9264464378356934})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0797677040100098})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6331, 'crossentropy': 2.6295328125}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 27925], ['ood', 44560], ['ood', 56545], ['ood', 31217], ['ood', 1158]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4732025499531822, 2.668728214698024, 3.549694253943759, 4.060342437557332, 4.33755062990938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.0762710571289062})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5547988414764404})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.07661771774292})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0101213455200195})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.784043788909912})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.316148519515991})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7313027381896973})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.0111398696899414})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.8437819480895996})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.6008386611938477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.567060947418213})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6583, 'crossentropy': 3.2114466796875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 27645], ['ood', 9699], ['ood', 24653], ['ood', 30188], ['ood', 29564]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5700847090743864, 2.8659606885681326, 3.750013773439198, 4.245814815976248, 4.446060479079815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.0463719367980957})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.4142327308654785})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.013716697692871})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.343686819076538})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9105236530303955})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.440732002258301})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.070202350616455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.3121724128723145})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6449, 'crossentropy': 3.1565287109375}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 13242], ['ood', 51151], ['ood', 54066], ['ood', 37382], ['ood', 36147]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5068005800428788, 2.69356690816071, 3.521598493674328, 4.03381273359941, 4.320221993720905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.9982048273086548})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.420400857925415})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6383299827575684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.131932020187378})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0890798568725586})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.549083709716797})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6356, 'crossentropy': 2.5947794921875}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 59031], ['ood', 48435], ['ood', 36894], ['ood', 22752], ['ood', 8617]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4721708920523642, 2.6108267359372594, 3.4351949599011053, 3.980063421761754, 4.2759325015308765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7778990268707275})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.37099552154541})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.825934886932373})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7965357303619385})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.995134115219116})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 2.5272109375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 54805], ['ood', 45048], ['ood', 36685], ['ood', 31806], ['ood', 48926]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4486742534278516, 2.5176639189159005, 3.3420149187501345, 3.8634170357005786, 4.195232195076454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.0177934169769287})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.577380657196045})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.814688205718994})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1188392639160156})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9928460121154785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.169736385345459})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3492467403411865})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.38108491897583})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.735962390899658})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6391, 'crossentropy': 3.311419140625}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 13158], ['ood', 29246], ['ood', 23080], ['ood', 47156], ['ood', 56888]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4622609763586267, 2.67975452319119, 3.6119428877198505, 4.115478973412002, 4.372721251900616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9308441877365112})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8474221229553223})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.914405345916748})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0969276428222656})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.3531477451324463})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5866591930389404})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.064138889312744})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.9023966789245605})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.905031681060791})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3542017936706543})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6378, 'crossentropy': 3.2291130859375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 21483], ['ood', 41502], ['ood', 11091], ['ood', 47636], ['ood', 5728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4825162781093142, 2.6995761293324283, 3.6034182855552643, 4.123250244848247, 4.393095076571891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8733484745025635})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.2720813751220703})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8452439308166504})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8553714752197266})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6151, 'crossentropy': 1.911283984375}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 28053], ['ood', 49196], ['ood', 46837], ['ood', 4719], ['id', 49224]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.2292065352523789, 2.1716516528720806, 2.890773142605708, 3.428542958779488, 3.8138386904401846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.0414724349975586})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.321484088897705})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.614593029022217})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.602555751800537})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2158026695251465})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0930404663085938})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.635, 'crossentropy': 2.69596328125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 31677], ['ood', 47585], ['ood', 23479], ['ood', 45942], ['ood', 22918]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4036310259952005, 2.5169950831003662, 3.3339394043010913, 3.8932387979298593, 4.2092038175158235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.7576674222946167})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.42712140083313})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.436509609222412})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.670882225036621})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8589425086975098})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0291595458984375})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6411, 'crossentropy': 2.676143359375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 6270], ['ood', 9699], ['ood', 43636], ['ood', 58936], ['ood', 55282]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.424222992822702, 2.5928031632006356, 3.4563194473684478, 3.9819516727108173, 4.290165498979647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.0262362957000732})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5506129264831543})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.677237033843994})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.298762321472168})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.941493511199951})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2847442626953125})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6164, 'crossentropy': 2.80071796875}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 14851], ['ood', 47636], ['ood', 20493], ['ood', 6612], ['ood', 18923]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4030890245993421, 2.5677230627982652, 3.4182161798054116, 3.9637925495968727, 4.268936162738793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9096693992614746})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.2760095596313477})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.4163594245910645})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.533599615097046})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.782259225845337})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.794339656829834})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8486528396606445})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.661, 'crossentropy': 2.58991484375}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 44520], ['ood', 17051], ['ood', 16952], ['ood', 41497], ['ood', 36685]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4642349015572123, 2.7592665970343253, 3.6475420468307664, 4.125904551438884, 4.379096465324897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.3866472244262695})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4532763957977295})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.320117950439453})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.987433671951294})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.4235146045684814})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6149, 'crossentropy': 2.744687890625}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 31879], ['ood', 10334], ['ood', 39601], ['ood', 39587], ['id', 19566]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.361371741773085, 2.4888620149945204, 3.3020714697639786, 3.8586702465146114, 4.184584476986661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7900714874267578})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4150588512420654})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5663514137268066})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.910331964492798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.675868511199951})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.898244857788086})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8733696937561035})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.9076194763183594})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.753573417663574})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.0765585899353027})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.1675610542297363})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.3422207832336426})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0884385108947754})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.239589214324951})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.4558827877044678})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.1400840282440186})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.502963066101074})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.9532506465911865})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.5295395851135254})
store['active_learning_steps'][40]['training']['best_epoch']=16
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6519, 'crossentropy': 3.399283203125}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 42365], ['ood', 36685], ['ood', 51415], ['ood', 28], ['ood', 26017]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5498651625248132, 2.8113043686477925, 3.760980185760207, 4.25100837374031, 4.467689817865167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.8925869464874268})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.394545555114746})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.925840377807617})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9093575477600098})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8192195892333984})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 2.3416919921875}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 37382], ['ood', 20977], ['ood', 40576], ['ood', 49474], ['ood', 16210]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4088694116569815, 2.5596249886522298, 3.3430132908551276, 3.866471973943999, 4.1849463345246445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8986397981643677})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2267189025878906})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5765342712402344})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.943824291229248})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8077187538146973})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7485148906707764})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.5959577560424805})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.936192274093628})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.5140624046325684})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6544, 'crossentropy': 2.7000927734375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 33376], ['ood', 9327], ['ood', 41376], ['ood', 8509], ['ood', 20294]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.49020955925966, 2.7882283518119575, 3.739684561436281, 4.2164712287331865, 4.427777216977537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.0657119750976562})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.457883834838867})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9025380611419678})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0183842182159424})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9610257148742676})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.486666440963745})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.450756549835205})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5740914344787598})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6353, 'crossentropy': 3.119791015625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 27195], ['ood', 18087], ['ood', 28257], ['ood', 56210], ['ood', 39700]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4643984102232088, 2.7145169540458887, 3.618426934591122, 4.1533569982129634, 4.391587933404372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9376046657562256})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.3561043739318848})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.680983066558838})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.827150821685791})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.153353214263916})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6203, 'crossentropy': 2.6646486328125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 8214], ['ood', 17602], ['ood', 40262], ['ood', 25013], ['ood', 47412]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4262505686056643, 2.5465115671192473, 3.371115534532496, 3.9159185889279717, 4.235284322699156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7510595321655273})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.462035655975342})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7536983489990234})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.721928596496582})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9134459495544434})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.12984299659729})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.062882423400879})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6431, 'crossentropy': 2.6638462890625}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 27247], ['ood', 14851], ['ood', 18038], ['ood', 57907], ['ood', 53510]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.435926331892866, 2.718743400343403, 3.6112341035770434, 4.112334206976511, 4.364037853729394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.03639554977417})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.423065662384033})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.6729226112365723})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.391761302947998})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.502718448638916})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6257, 'crossentropy': 2.6004546875}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 18289], ['ood', 8584], ['ood', 52941], ['ood', 1189], ['ood', 56691]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4462721587891612, 2.6343519838317677, 3.4155011564667666, 3.956491880649738, 4.257448387430056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0621070861816406})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5153586864471436})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0568079948425293})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9535136222839355})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.912224531173706})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0120677947998047})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.4276795387268066})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.257316827774048})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6361, 'crossentropy': 2.9278939453125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 46593], ['ood', 8954], ['ood', 56379], ['ood', 30827], ['ood', 8338]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4539859182763104, 2.690474133368111, 3.594251639790607, 4.151515828967454, 4.392881432607091]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.155216693878174})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.6530649662017822})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.549983024597168})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.122865676879883})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.1704187393188477})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.183917999267578})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.622621536254883})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.259223699569702})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6533, 'crossentropy': 3.1148580078125}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 45518], ['ood', 12670], ['ood', 4031], ['ood', 53646], ['ood', 50391]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.573597796193173, 2.822556853711606, 3.71668272715187, 4.184640358347586, 4.416014783609444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.7912577390670776})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4240503311157227})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4259815216064453})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8332157135009766})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0637271404266357})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.957253932952881})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9954543113708496})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.227308511734009})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.859832286834717})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6359, 'crossentropy': 2.9811181640625}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 35903], ['ood', 6857], ['ood', 13627], ['ood', 21179], ['ood', 36817]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.503345855827555, 2.8116526174259926, 3.785189784692415, 4.286342773947369, 4.477089237999401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.027277946472168})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.2937464714050293})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5866470336914062})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0466551780700684})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.964959144592285})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0268421173095703})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6234, 'crossentropy': 2.573544921875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 47895], ['ood', 37382], ['ood', 10524], ['ood', 51786], ['ood', 2548]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.381642777431604, 2.596532650280322, 3.4869680859406724, 3.9863386334752837, 4.2916500963445525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.1328959465026855})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3245131969451904})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.435516357421875})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.935713291168213})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.513307809829712})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.0295920372009277})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.6713058948516846})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.254911422729492})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6592, 'crossentropy': 2.6488517578125}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 42699], ['ood', 17324], ['ood', 6944], ['ood', 37382], ['ood', 30211]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.498088655437329, 2.740940329402099, 3.6137382610066098, 4.130643812143273, 4.393966614209092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.829050064086914})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.154629945755005})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.521378993988037})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.880495548248291})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.6248912811279297})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.650278329849243})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8438210487365723})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9291343688964844})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.0146236419677734})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.026620864868164})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6435, 'crossentropy': 2.93745234375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 27274], ['ood', 52688], ['ood', 6143], ['ood', 38338], ['ood', 4038]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4776163688268444, 2.6970573861987424, 3.6180405223527146, 4.153002100658287, 4.408232336484648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.1821165084838867})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.422438144683838})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.1273555755615234})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.846271276473999})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1443521976470947})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2335281372070312})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5075314044952393})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6008172035217285})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6169, 'crossentropy': 3.2573384765625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 40378], ['ood', 18827], ['ood', 6296], ['ood', 54068], ['ood', 15123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5168391768363185, 2.7341605573560233, 3.67477446655759, 4.164099121988779, 4.397421722826656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.957420825958252})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7684924602508545})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.4662089347839355})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9285123348236084})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.470015048980713})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.241279125213623})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.154758930206299})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.3063395023345947})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6453, 'crossentropy': 2.6678462890625}
