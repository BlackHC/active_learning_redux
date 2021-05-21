store = {}
store['timestamp']=1621471708
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=27']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
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
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5948984622955322})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.046952247619629})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.471802234649658})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6009, 'crossentropy': 3.883953515625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 48240], ['id', 6580], ['id', 6935], ['id', 8875], ['id', 14129]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6279843619372918, 2.8160071570149956, 3.6668274882548104, 4.133792624104126, 4.380029380519442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.3904190063476562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.6635847091674805})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.961785316467285})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.240204334259033})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.711061954498291})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.8355445861816406})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 3.1838990234375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 44544], ['id', 8027], ['id', 30511], ['id', 39467], ['id', 4797]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5967527625509765, 2.7677422555088187, 3.5834254957152254, 4.097622535640635, 4.350420986867927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.2603702545166016})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.902705192565918})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.175992965698242})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3204469680786133})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3806910514831543})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5699758529663086})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 3.27104453125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 19202], ['id', 25907], ['id', 32776], ['id', 8338], ['id', 50069]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5603870671090712, 2.690625134623029, 3.538385969880025, 4.06457556908198, 4.316450776428441]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.408717632293701})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.965134620666504})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.4881882667541504})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.410871982574463})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5807, 'crossentropy': 2.4955197265625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 14260], ['id', 4799], ['id', 25627], ['id', 27652], ['id', 48608]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3266226497085554, 2.352225978505383, 3.1153529832447138, 3.634716256067729, 4.008593044714361]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.6428210735321045})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.4600565433502197})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.7100119590759277})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.986227512359619})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.218148231506348})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5899, 'crossentropy': 3.415515234375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 4737], ['id', 32393], ['id', 4799], ['id', 17728], ['id', 30454]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5160612687931514, 2.5857806125608116, 3.437623565327181, 3.9871865040200998, 4.302718319139304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.425680637359619})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.9220352172851562})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.131615161895752})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.506711721420288})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3152997493743896})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3201112747192383})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.147634983062744})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.4426212310791016})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.846139430999756})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.751284599304199})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.637023046875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 222], ['id', 8787], ['id', 47534], ['id', 20752], ['id', 3397]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5573302993701408, 2.8011886890166675, 3.6816291992894428, 4.149521076804461, 4.388109026709618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.311349630355835})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9763312339782715})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.755619525909424})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.6130080223083496})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.8314015865325928})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5895, 'crossentropy': 3.411803125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 47741], ['id', 56833], ['id', 5728], ['id', 24276], ['id', 52590]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.5172141548541922, 2.7061113074645844, 3.475530986098586, 3.990322243298981, 4.287640320562879]}
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
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 44544], ['id', 53516], ['id', 4353], ['id', 25868], ['id', 16911]], 'labels': [-1, -1, 6, -1, -1], 'scores': [1.36631737909032, 2.461302448888646, 3.30254531848054, 3.8478607157387383, 4.177237728207267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.4771337509155273})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 3.48228120803833})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.6220667362213135})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.194455146789551})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 4.717330455780029})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 4.182755470275879})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.326857566833496})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.776214599609375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.4368486404418945})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 4.483603477478027})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5696, 'crossentropy': 4.47199375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 24113], ['id', 17491], ['id', 18564], ['id', 47260], ['id', 42450]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.57286440378914, 2.768830991297686, 3.610841422717293, 4.1540745540868045, 4.408174755259161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1860148906707764})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.530993938446045})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3767099380493164})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5118815898895264})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6033, 'crossentropy': 2.3703908203125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 44332], ['id', 1479], ['id', 53120], ['id', 51786], ['id', 8729]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2987491257029897, 2.346641036138555, 3.0880635775579837, 3.6189260605331572, 3.975535578984724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.3679563999176025})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.5973503589630127})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.7730934619903564})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.750978469848633})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.3590927124023438})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.316290855407715})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.7102627754211426})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.806100845336914})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.8978981971740723})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.2279586791992188})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7473816871643066})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5989, 'crossentropy': 3.917724609375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 33282], ['id', 6245], ['id', 4833], ['id', 50523], ['id', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6755055602635416, 2.887466659687007, 3.7306337334606328, 4.210872903703306, 4.441315499923123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.499919891357422})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.9009642601013184})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.2412023544311523})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.132462501525879})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.7012014389038086})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.802828311920166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.5682191848754883})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.598, 'crossentropy': 3.590476953125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 31216], ['id', 15452], ['id', 45209], ['id', 1254], ['id', 27393]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.5242647430826561, 2.807940343035429, 3.695166799323893, 4.171082581705521, 4.408737654570224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.350371837615967})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0528268814086914})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.8170199394226074})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.440351963043213})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.566819667816162})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5965, 'crossentropy': 3.042337109375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 49092], ['id', 46861], ['id', 58353], ['id', 39750], ['id', 16268]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.6290072767304231, 2.7867041995539843, 3.5469601639818844, 4.0512282932082435, 4.318529114678399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.0974414348602295})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.0567126274108887})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 3.2869160175323486})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.308865785598755})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5967, 'crossentropy': 2.249949609375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 32578], ['id', 44914], ['id', 24944], ['id', 2089], ['id', 45255]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.355325638172138, 2.3533098625490663, 3.0931649727369734, 3.6326747054240656, 4.00285203271298]}
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
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 41716], ['id', 25830], ['id', 1303], ['id', 53077], ['id', 35560]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4936354105542708, 2.795051859088126, 3.5743064272044354, 4.056584092157948, 4.3175736521882895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.316408634185791})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.218703031539917})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.210330009460449})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.8186240196228027})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.14585542678833})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.666146755218506})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5788, 'crossentropy': 3.338342578125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 4252], ['id', 25382], ['id', 28204], ['id', 16590], ['id', 49200]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.597019501434974, 2.7268850887079665, 3.5824559822633075, 4.089385651240104, 4.341176448762441]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.2320151329040527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.1379783153533936})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.171100378036499})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.109302282333374})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5103187561035156})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.512559175491333})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6115, 'crossentropy': 3.1307365234375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 6454], ['id', 45998], ['id', 5982], ['id', 36553], ['id', 16921]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5069510803538746, 2.717359959870504, 3.6230884723263905, 4.1423275458523765, 4.396633285295097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1249282360076904})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.848389148712158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.846055269241333})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.555753231048584})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5998, 'crossentropy': 2.378633203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 45148], ['id', 19337], ['id', 41937], ['id', 56823], ['id', 5684]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3793800811044892, 2.4527804469061243, 3.220399403576635, 3.7540150694030263, 4.090128039228258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.119595527648926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.850900650024414})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.1175379753112793})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3392333984375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8628435134887695})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.5886, 'crossentropy': 3.009748828125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 28396], ['id', 59010], ['id', 59355], ['id', 23884], ['id', 55729]], 'labels': [-1, 5, -1, -1, -1], 'scores': [1.4091382910528618, 2.5471838008440377, 3.355410901107663, 3.930719539905704, 4.242168601204812]}
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
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6239, 'crossentropy': 3.01428125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 55024], ['id', 25325], ['id', 2202], ['id', 30295], ['id', 14175]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5987542085007482, 2.729373295730147, 3.5721719110511128, 4.068458598289824, 4.354120356091836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.194216251373291})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.1072216033935547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.4911489486694336})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.7236127853393555})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6011, 'crossentropy': 2.31846953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42809], ['id', 52423], ['id', 54547], ['id', 54066], ['id', 54832]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3601353545444823, 2.3456166910560308, 3.0710032118649764, 3.6096869395496958, 3.9719905313538852]}
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
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 4781], ['id', 31665], ['id', 54813], ['id', 28030], ['id', 16816]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.630769718667525, 3.010703707384698, 3.743020674536938, 4.160901471695109, 4.386312509960852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.307438611984253})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.7151172161102295})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.982187032699585})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.191948413848877})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.3227949142456055})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.245497703552246})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6717543601989746})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2949414253234863})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.61, 'crossentropy': 3.376618359375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 39046], ['id', 55709], ['id', 54288], ['id', 20357], ['id', 17728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5391370201898682, 2.7253026461161447, 3.6082055049620934, 4.1292250398223125, 4.390618692573318]}
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
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.7000770568847656})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6021, 'crossentropy': 4.018530078125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 25180], ['id', 19429], ['id', 39720], ['id', 35916], ['id', 25325]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.6699946903830298, 2.9582802552924106, 3.8161154108720208, 4.242391368648317, 4.457340720729527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1200106143951416})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.639385223388672})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.567059278488159})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8793373107910156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.2825539112091064})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.226158380508423})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0947065353393555})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.478395462036133})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1928908824920654})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6311, 'crossentropy': 3.32982265625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 8584], ['id', 55699], ['id', 11193], ['id', 6857], ['id', 21977]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4145763949327796, 2.67206891807776, 3.539313199124021, 4.088001002134297, 4.3586017937925945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.047011137008667})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.507356643676758})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8231801986694336})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.7737069129943848})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2638235092163086})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1842408180236816})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.7816903591156006})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 2.8345404296875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 32504], ['id', 25022], ['id', 54224], ['id', 42639], ['id', 46570]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4482040528782396, 2.6509613616374113, 3.545607065172863, 4.072270473188661, 4.359926436168927]}
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
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2918922901153564})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.2068095207214355})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.076132297515869})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.361929416656494})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.535428524017334})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.118966579437256})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.6128652095794678})
store['active_learning_steps'][26]['training']['best_epoch']=12
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6371, 'crossentropy': 3.519689453125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 45518], ['id', 47636], ['id', 37080], ['id', 14072], ['id', 20476]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.62122104534759, 2.9352379099736616, 3.770253810171388, 4.235410232459425, 4.448537212115736]}
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
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 27925], ['id', 44560], ['id', 56545], ['id', 31217], ['id', 1158]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4732025464023644, 2.6687282028438277, 3.549694230971431, 4.060342417450771, 4.337550615625437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.0762710571289062})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5547988414764404})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.076617956161499})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0101213455200195})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.784043788909912})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.316148281097412})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7313027381896973})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.0111398696899414})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.8437819480895996})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.6008386611938477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.567060947418213})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6583, 'crossentropy': 3.2114470703125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 27645], ['id', 9699], ['id', 24653], ['id', 30188], ['id', 29564]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5700847139403042, 2.8659607062020527, 3.750013799622846, 4.245814853071554, 4.446060524399645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.0463719367980957})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.4142324924468994})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.013716220855713})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.343686819076538})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9105234146118164})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.440732002258301})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.070202350616455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.3121726512908936})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6449, 'crossentropy': 3.1565287109375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 13242], ['id', 51151], ['id', 54066], ['id', 37382], ['id', 36147]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5068005823614814, 2.6935669168617054, 3.5215985112465393, 4.033812756090137, 4.320222027450356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.9982049465179443})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.420401096343994})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6383299827575684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.131932020187378})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0890793800354004})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.549083709716797})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6356, 'crossentropy': 2.5947796875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 59031], ['id', 48435], ['id', 36894], ['id', 22752], ['id', 8617]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4721708954675252, 2.6108267463261106, 3.4351949800252006, 3.980063449073894, 4.275932515181559]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7778990268707275})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.37099552154541})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.825934886932373})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7965359687805176})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.995134115219116})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 2.5272111328125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 54805], ['id', 45048], ['id', 36685], ['id', 31806], ['id', 48926]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4486741940664196, 2.5176638591451677, 3.3420148668739946, 3.8634169904496023, 4.195232161946486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.0177934169769287})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.577380657196045})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.814688205718994})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1188392639160156})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9928460121154785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.169736623764038})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3492467403411865})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.38108491897583})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.735962390899658})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6391, 'crossentropy': 3.31141953125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 13158], ['id', 29246], ['id', 23080], ['id', 47156], ['id', 56888]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4622609765249521, 2.679754528804986, 3.6119429066233044, 4.1154790002889925, 4.372721278190891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9308440685272217})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8474221229553223})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.914405345916748})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0969276428222656})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.3531477451324463})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5866591930389404})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0641391277313232})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.9023966789245605})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.905031681060791})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3542017936706543})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6378, 'crossentropy': 3.2291130859375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 21483], ['id', 41502], ['id', 11091], ['id', 47636], ['id', 5728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4825162777135292, 2.6995761266966807, 3.603418282062102, 4.123250244012381, 4.3930950769060555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8733484745025635})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.2720813751220703})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8452439308166504})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8553714752197266})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6151, 'crossentropy': 1.9112837890625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 28053], ['id', 49196], ['id', 46837], ['id', 4719], ['id', 49224]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.2292065368264007, 2.1716516583414656, 2.8907731512262638, 3.428542979110172, 3.813838720859195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.0414724349975586})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.321484088897705})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.614593029022217})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.602555990219116})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2158026695251465})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0930404663085938})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.635, 'crossentropy': 2.69596328125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 31677], ['id', 47585], ['id', 23479], ['id', 45942], ['id', 22918]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4036310300020833, 2.5169950960286895, 3.333939437238678, 3.8932388443285246, 4.209203891515207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.7576675415039062})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.42712140083313})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.436509609222412})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.670881986618042})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8589425086975098})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0291595458984375})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6411, 'crossentropy': 2.676143359375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 6270], ['id', 9699], ['id', 43636], ['id', 58936], ['id', 55282]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4242229939253446, 2.5928031701711944, 3.4563194606513754, 3.981951690439918, 4.290165516266336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.0262362957000732})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5506129264831543})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6772372722625732})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.298762321472168})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.941493511199951})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2847442626953125})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6164, 'crossentropy': 2.80071796875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 14851], ['id', 47636], ['id', 20493], ['id', 6612], ['id', 18923]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4030890267783978, 2.5677230768720616, 3.4182162068669317, 3.963792588383999, 4.268936185542129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.909669280052185})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.2760095596313477})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.4163594245910645})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.533599615097046})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.782259225845337})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.794339656829834})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8486530780792236})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.661, 'crossentropy': 2.58991484375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 44520], ['id', 17051], ['id', 16952], ['id', 41497], ['id', 36685]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4642349047263974, 2.7592666061229933, 3.6475420571394466, 4.12590456323535, 4.379096479604101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.3866472244262695})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4532763957977295})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.320117950439453})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.987433671951294})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.4235143661499023})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6149, 'crossentropy': 2.744687890625}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 31879], ['id', 10334], ['id', 39601], ['id', 39587], ['id', 19566]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.3613717414252335, 2.488862011492813, 3.3020714666601787, 3.8586702441395397, 4.184584494261701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7900714874267578})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4150590896606445})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5663514137268066})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.910331964492798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.675868511199951})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.898245096206665})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8733696937561035})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.9076194763183594})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.753573417663574})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.076558828353882})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.1675615310668945})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.3422207832336426})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0884385108947754})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.239589214324951})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.455883026123047})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.1400840282440186})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.502963066101074})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.9532506465911865})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.5295395851135254})
store['active_learning_steps'][40]['training']['best_epoch']=16
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6519, 'crossentropy': 3.399283203125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 42365], ['id', 36685], ['id', 51415], ['id', 28], ['id', 26017]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5498651639246948, 2.8113043721498885, 3.7609802204138285, 4.25100841645763, 4.467689863039381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.8925869464874268})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.394545555114746})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9258406162261963})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9093575477600098})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8192195892333984})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 2.3416919921875}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 37382], ['id', 20977], ['id', 40576], ['id', 49474], ['id', 16210]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4088694114963696, 2.559624990994656, 3.3430133026203324, 3.8664719932066367, 4.184946362957348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8986397981643677})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2267189025878906})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5765342712402344})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.943824291229248})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.807718276977539})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7485148906707764})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.5959575176239014})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.936192512512207})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.5140624046325684})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6544, 'crossentropy': 2.70009296875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 33376], ['id', 9327], ['id', 41376], ['id', 8509], ['id', 20294]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.49020955990376, 2.788228356596763, 3.7396845685322404, 4.216471230304938, 4.42777722299067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.0657119750976562})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.457883834838867})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.902538299560547})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0183842182159424})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9610257148742676})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.486666679382324})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.450756549835205})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5740914344787598})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6353, 'crossentropy': 3.119791015625}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 27195], ['id', 18087], ['id', 28257], ['id', 56210], ['id', 39700]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4643984108986148, 2.7145169524917985, 3.6184269375046796, 4.1533570023800905, 4.391587949753246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9376049041748047})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.3561043739318848})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.680983066558838})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.827150821685791})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.153353214263916})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6203, 'crossentropy': 2.6646484375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 8214], ['id', 17602], ['id', 40262], ['id', 25013], ['id', 47412]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.426250570370372, 2.5465115748004736, 3.3711155532915846, 3.915918611314635, 4.235284354869619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7510592937469482})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.462035655975342})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7536983489990234})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.721928596496582})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9134457111358643})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.12984299659729})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.062882423400879})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6431, 'crossentropy': 2.6638462890625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 27247], ['id', 14851], ['id', 18038], ['id', 57907], ['id', 53510]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.435926331549509, 2.718743405996063, 3.6112341131707346, 4.11233422712848, 4.364037880558324]}
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
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 18289], ['id', 8584], ['id', 52941], ['id', 1189], ['id', 56691]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4462721593723191, 2.6343519889385947, 3.415501170206726, 3.9564918918739966, 4.257448404571327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0621070861816406})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5153589248657227})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0568079948425293})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9535136222839355})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.912224531173706})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0120677947998047})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.4276797771453857})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.2573165893554688})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6361, 'crossentropy': 2.92789375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 46593], ['id', 8954], ['id', 56379], ['id', 30827], ['id', 8338]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4539859186801645, 2.690474138869136, 3.5942516539310745, 4.151515862749787, 4.392881478178063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.155216693878174})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.6530649662017822})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.549983024597168})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.122865676879883})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.1704189777374268})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.183917999267578})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.622621536254883})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.259223699569702})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6533, 'crossentropy': 3.1148578125}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 45518], ['id', 12670], ['id', 4031], ['id', 53646], ['id', 50391]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5735977992675725, 2.822556863301689, 3.71668275045902, 4.184640388260345, 4.416014824512054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.791257619857788})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4240503311157227})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4259817600250244})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8332157135009766})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0637271404266357})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.957253932952881})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9954545497894287})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.227308511734009})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.859832286834717})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6359, 'crossentropy': 2.981118359375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 35903], ['id', 6857], ['id', 13627], ['id', 21179], ['id', 36817]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5033458566525302, 2.811652623810476, 3.785189794912272, 4.28634278967299, 4.477089234230121]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.027277946472168})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.2937464714050293})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5866470336914062})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0466554164886475})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.964959144592285})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0268421173095703})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6234, 'crossentropy': 2.573544921875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 47895], ['id', 37382], ['id', 10524], ['id', 51786], ['id', 2548]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3816427790227253, 2.596532658497787, 3.4869680987685907, 3.986338660470693, 4.291650131891138]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.1328959465026855})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3245131969451904})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.435516357421875})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.935713291168213})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.513307809829712})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.0295920372009277})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.6713061332702637})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.254911422729492})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6592, 'crossentropy': 2.6488517578125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 42699], ['id', 17324], ['id', 6944], ['id', 37382], ['id', 30211]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4980886554503943, 2.740940336443869, 3.6137382706692893, 4.130643826570635, 4.393966626489662]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.829050064086914})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.154629945755005})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.521378993988037})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.880495309829712})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.6248912811279297})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6502785682678223})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8438210487365723})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9291343688964844})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.0146236419677734})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.026620864868164})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6435, 'crossentropy': 2.9374525390625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 27274], ['id', 52688], ['id', 6143], ['id', 38338], ['id', 4038]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4776163694591764, 2.697057383416025, 3.6180405157158004, 4.153002095262491, 4.408232337547932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.1821165084838867})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.422438144683838})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.1273555755615234})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.846271276473999})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1443519592285156})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2335281372070312})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5075314044952393})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6008172035217285})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6169, 'crossentropy': 3.2573384765625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 40378], ['id', 18827], ['id', 6296], ['id', 54068], ['id', 15123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5168391765384293, 2.7341605592257214, 3.6747744682317807, 4.164099120069713, 4.397421720291039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.957420825958252})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7684924602508545})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.4662086963653564})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9285123348236084})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.470015048980713})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.241278886795044})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.154758930206299})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.3063395023345947})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6453, 'crossentropy': 2.6678462890625}
