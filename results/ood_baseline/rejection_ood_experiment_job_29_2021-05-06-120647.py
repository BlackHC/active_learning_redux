store = {}
store['timestamp']=1620299207
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=29']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=29
store['worker_id']=29
store['num_workers']=40
store['config']={'seed': 38, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.15743350982666})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.6802871227264404})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5976855754852295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7688896656036377})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6785, 'crossentropy': 1.9545232421875}
store['active_learning_steps'][0]['acquisition']={'indices': [15169, 51671, 50915, 27049, 2391], 'labels': [0, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.3878602981567383})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5919036865234375})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8769311904907227})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.842276096343994})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.662, 'crossentropy': 2.1034841796875}
store['active_learning_steps'][1]['acquisition']={'indices': [53114, 59352, 15322, 38505, 51518], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.209324359893799})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6716136932373047})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.780777931213379})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.134316921234131})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6837, 'crossentropy': 2.0395927734375}
store['active_learning_steps'][2]['acquisition']={'indices': [52192, 5439, 52762, 26247, 18698], 'labels': [5, 1, -1, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.140425682067871})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.439061164855957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.1023082733154297})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.826986789703369})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7258, 'crossentropy': 1.81363125}
store['active_learning_steps'][3]['acquisition']={'indices': [23030, 24371, 47337, 1476, 57771], 'labels': [-1, 0, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.154606819152832})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.61191463470459})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.657966136932373})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.9039645195007324})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7146, 'crossentropy': 1.864022265625}
store['active_learning_steps'][4]['acquisition']={'indices': [18478, 25501, 11680, 32083, 50273], 'labels': [-1, -1, 6, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.14096736907959})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.681980609893799})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.7833127975463867})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.0273399353027344})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6959, 'crossentropy': 1.99383203125}
store['active_learning_steps'][5]['acquisition']={'indices': [43338, 40700, 52419, 31277, 50998], 'labels': [2, 7, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.2037742137908936})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.2414231300354004})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.6607747077941895})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.567258834838867})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.723, 'crossentropy': 1.8276255859375}
store['active_learning_steps'][6]['acquisition']={'indices': [56557, 42674, 28606, 20077, 56558], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9299625158309937})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.4081249237060547})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.851811647415161})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.6395273208618164})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7331, 'crossentropy': 1.6837966796875}
store['active_learning_steps'][7]['acquisition']={'indices': [38998, 11178, 45646, 10209, 24584], 'labels': [3, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.96760094165802})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0823118686676025})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.667933464050293})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.663907527923584})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7201, 'crossentropy': 1.7888095703125}
store['active_learning_steps'][8]['acquisition']={'indices': [17462, 35264, 54824, 34246, 12937], 'labels': [0, 8, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1416144371032715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.2813432216644287})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.5522537231445312})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.8483941555023193})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.74, 'crossentropy': 1.8658330078125}
store['active_learning_steps'][9]['acquisition']={'indices': [18985, 34079, 252, 31094, 24047], 'labels': [-1, 7, 2, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.6710679531097412})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.9980441331863403})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.0644218921661377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.0824010372161865})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7775, 'crossentropy': 1.3795421875}
store['active_learning_steps'][10]['acquisition']={'indices': [51864, 14975, 33219, 31706, 35638], 'labels': [8, -1, -1, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8616065979003906})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.9216755628585815})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.1262738704681396})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.127681255340576})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 1.594797265625}
store['active_learning_steps'][11]['acquisition']={'indices': [8428, 24707, 43759, 52067, 12078], 'labels': [2, 1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8428882360458374})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.8720682859420776})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.1188430786132812})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.1299448013305664})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7495, 'crossentropy': 1.51340107421875}
store['active_learning_steps'][12]['acquisition']={'indices': [41892, 41088, 45335, 35828, 9843], 'labels': [7, 7, -1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.434938669204712})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5801453590393066})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7497996091842651})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.100811004638672})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7832, 'crossentropy': 1.29797919921875}
store['active_learning_steps'][13]['acquisition']={'indices': [58123, 44098, 23472, 55678, 31575], 'labels': [1, -1, -1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.478130578994751})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.755907654762268})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.7444977760314941})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.9326622486114502})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7602, 'crossentropy': 1.33469814453125}
store['active_learning_steps'][14]['acquisition']={'indices': [12001, 9929, 52464, 42111, 41501], 'labels': [4, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3467589616775513})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6515755653381348})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.9843827486038208})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.1192445755004883})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7873, 'crossentropy': 1.288555859375}
store['active_learning_steps'][15]['acquisition']={'indices': [44329, 27106, 15685, 26962, 45216], 'labels': [-1, -1, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2188773155212402})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6107354164123535})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.9217190742492676})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.701460599899292})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8076, 'crossentropy': 1.17344873046875}
store['active_learning_steps'][16]['acquisition']={'indices': [54304, 47797, 16906, 48387, 54047], 'labels': [3, 0, 1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3849867582321167})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.586871862411499})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.5420687198638916})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.7632169723510742})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7814, 'crossentropy': 1.23641171875}
store['active_learning_steps'][17]['acquisition']={'indices': [17569, 13412, 49636, 12188, 5974], 'labels': [3, 8, -1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2808220386505127})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5264778137207031})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.67084801197052})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6565080881118774})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8054, 'crossentropy': 1.19367763671875}
store['active_learning_steps'][18]['acquisition']={'indices': [38804, 42892, 40108, 31030, 32846], 'labels': [-1, 7, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3062174320220947})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.6529655456542969})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.2525415420532227})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 2.0745270252227783})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7896, 'crossentropy': 1.35435390625}
store['active_learning_steps'][19]['acquisition']={'indices': [36987, 56634, 56378, 18995, 28312], 'labels': [5, 9, 8, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1699728965759277})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3211272954940796})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.4401922225952148})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6495107412338257})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8165, 'crossentropy': 1.07158134765625}
store['active_learning_steps'][20]['acquisition']={'indices': [12886, 29271, 39719, 11853, 46331], 'labels': [8, -1, 2, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.170605182647705})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3420974016189575})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.5018484592437744})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.5595057010650635})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8176, 'crossentropy': 1.0174857421875}
store['active_learning_steps'][21]['acquisition']={'indices': [18803, 31263, 833, 34008, 4996], 'labels': [2, -1, 1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1925697326660156})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4117079973220825})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.54608154296875})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.6306777000427246})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8077, 'crossentropy': 1.09068525390625}
store['active_learning_steps'][22]['acquisition']={'indices': [21996, 48543, 16033, 24169, 22493], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1188147068023682})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3853428363800049})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.4540762901306152})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.5148282051086426})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8209, 'crossentropy': 1.00682666015625}
store['active_learning_steps'][23]['acquisition']={'indices': [55818, 33936, 51600, 40496, 6971], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.218083381652832})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.393446922302246})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.8750147819519043})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6377975940704346})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8089, 'crossentropy': 1.0793810546875}
store['active_learning_steps'][24]['acquisition']={'indices': [19851, 48404, 31961, 41681, 8180], 'labels': [6, 7, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1887553930282593})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4052090644836426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4150280952453613})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4607853889465332})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.816, 'crossentropy': 1.07879423828125}
store['active_learning_steps'][25]['acquisition']={'indices': [42245, 39238, 17199, 19989, 29153], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2102608680725098})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.396125078201294})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5549451112747192})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.626225233078003})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8241, 'crossentropy': 1.06748759765625}
store['active_learning_steps'][26]['acquisition']={'indices': [52466, 25757, 17461, 53285, 47562], 'labels': [7, -1, 5, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1829025745391846})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3104890584945679})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5708398818969727})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.59260892868042})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8173, 'crossentropy': 1.124144140625}
store['active_learning_steps'][27]['acquisition']={'indices': [42424, 1993, 26341, 9659, 5164], 'labels': [1, 5, 2, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1346089839935303})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2292261123657227})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3342885971069336})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.7026246786117554})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8166, 'crossentropy': 1.053914453125}
store['active_learning_steps'][28]['acquisition']={'indices': [42846, 57396, 11110, 59374, 25472], 'labels': [-1, 3, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1520448923110962})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2492510080337524})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.456925630569458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.65342378616333})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8218, 'crossentropy': 1.0662466796875}
store['active_learning_steps'][29]['acquisition']={'indices': [47060, 25035, 24790, 13967, 58048], 'labels': [-1, 6, 2, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0158374309539795})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.283313512802124})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.241544246673584})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.30525541305542})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.833, 'crossentropy': 0.94336845703125}
store['active_learning_steps'][30]['acquisition']={'indices': [12279, 51368, 14853, 58365, 44833], 'labels': [-1, 4, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1138582229614258})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.279043436050415})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3408925533294678})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.5252411365509033})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8338, 'crossentropy': 0.9904595703125}
store['active_learning_steps'][31]['acquisition']={'indices': [28792, 53813, 6494, 57933, 36669], 'labels': [1, 7, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.136265516281128})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2794266939163208})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.3227500915527344})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.4054088592529297})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8178, 'crossentropy': 1.05243984375}
store['active_learning_steps'][32]['acquisition']={'indices': [9765, 38630, 11230, 11473, 35845], 'labels': [-1, -1, 2, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1483529806137085})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1470153331756592})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.3223869800567627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.415940284729004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.4474639892578125})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8611, 'crossentropy': 0.98803310546875}
store['active_learning_steps'][33]['acquisition']={'indices': [37837, 2977, 51602, 43959, 20634], 'labels': [0, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0075628757476807})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.034886360168457})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2924273014068604})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.3081605434417725})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8331, 'crossentropy': 0.93983046875}
store['active_learning_steps'][34]['acquisition']={'indices': [20060, 21133, 52576, 27424, 22215], 'labels': [-1, 7, 9, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9899594783782959})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.182525873184204})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1990530490875244})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.3920478820800781})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8279, 'crossentropy': 0.91388466796875}
store['active_learning_steps'][35]['acquisition']={'indices': [50329, 26949, 13872, 9883, 11841], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1099742650985718})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2807399034500122})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3410619497299194})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.5177704095840454})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8224, 'crossentropy': 0.97921572265625}
store['active_learning_steps'][36]['acquisition']={'indices': [36115, 56142, 1626, 19885, 25752], 'labels': [-1, 4, 0, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0766541957855225})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1337788105010986})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.374709129333496})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3737128973007202})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8257, 'crossentropy': 0.924691015625}
store['active_learning_steps'][37]['acquisition']={'indices': [40830, 43825, 40015, 50003, 39283], 'labels': [-1, -1, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.970838189125061})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1835777759552002})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.271394968032837})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2345683574676514})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8318, 'crossentropy': 0.8999048828125}
store['active_learning_steps'][38]['acquisition']={'indices': [49747, 2282, 56461, 25350, 6666], 'labels': [9, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.070043921470642})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1885685920715332})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.27522611618042})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3927897214889526})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8232, 'crossentropy': 0.95607998046875}
store['active_learning_steps'][39]['acquisition']={'indices': [42322, 19566, 39525, 42018, 59624], 'labels': [-1, 8, 4, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9025378823280334})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0763323307037354})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1399662494659424})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.258117437362671})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8568, 'crossentropy': 0.8126701171875}
store['active_learning_steps'][40]['acquisition']={'indices': [14183, 19664, 50272, 842, 8565], 'labels': [-1, 0, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9455820322036743})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0764479637145996})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.098738431930542})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2354710102081299})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8476, 'crossentropy': 0.82997041015625}
store['active_learning_steps'][41]['acquisition']={'indices': [37705, 19294, 54866, 40719, 37447], 'labels': [-1, -1, -1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9599807262420654})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0702801942825317})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0967912673950195})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.5004980564117432})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8431, 'crossentropy': 0.869825}
store['active_learning_steps'][42]['acquisition']={'indices': [8094, 48314, 49231, 42325, 47062], 'labels': [-1, 4, 2, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9368448257446289})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9620484113693237})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.141366720199585})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1144969463348389})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8561, 'crossentropy': 0.819378125}
store['active_learning_steps'][43]['acquisition']={'indices': [17887, 35434, 8618, 34073, 4481], 'labels': [-1, 3, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9632712006568909})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9935864210128784})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0723297595977783})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.034305214881897})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.8562201171875}
store['active_learning_steps'][44]['acquisition']={'indices': [40088, 41851, 45520, 26550, 12048], 'labels': [-1, -1, 8, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0295343399047852})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0422790050506592})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.035041332244873})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3248169422149658})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8392, 'crossentropy': 0.87218525390625}
store['active_learning_steps'][45]['acquisition']={'indices': [4771, 35434, 52846, 34411, 7976], 'labels': [-1, -1, 9, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9421815872192383})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.063521146774292})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1689366102218628})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0765827894210815})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8473, 'crossentropy': 0.8312154296875}
store['active_learning_steps'][46]['acquisition']={'indices': [18491, 28840, 21590, 57444, 13584], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8776243925094604})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9139938950538635})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9177237153053284})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.001240849494934})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8412, 'crossentropy': 0.82024228515625}
store['active_learning_steps'][47]['acquisition']={'indices': [13658, 51594, 19142, 47749, 4488], 'labels': [3, -1, 6, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8859266638755798})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9174214005470276})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9809849858283997})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.069954752922058})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8581, 'crossentropy': 0.808273095703125}
store['active_learning_steps'][48]['acquisition']={'indices': [23488, 54792, 52959, 52503, 20916], 'labels': [-1, -1, 2, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8236852884292603})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.759243905544281})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9500245451927185})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9560840725898743})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0419220924377441})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.6860958984375}
store['active_learning_steps'][49]['acquisition']={'indices': [32350, 53318, 3981, 3059, 50164], 'labels': [9, 6, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8892922401428223})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8533348441123962})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9465462565422058})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0730526447296143})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.083862066268921})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8784, 'crossentropy': 0.763322216796875}
store['active_learning_steps'][50]['acquisition']={'indices': [40068, 56157, 21129, 58745, 48053], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9112337827682495})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8884051442146301})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9706480503082275})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1445313692092896})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1625417470932007})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8843, 'crossentropy': 0.75130537109375}
store['active_learning_steps'][51]['acquisition']={'indices': [48795, 43666, 16469, 24428, 8417], 'labels': [9, -1, 6, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8502912521362305})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8509255647659302})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9206564426422119})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0306248664855957})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8551, 'crossentropy': 0.792669384765625}
store['active_learning_steps'][52]['acquisition']={'indices': [50830, 3293, 32835, 5276, 14192], 'labels': [1, 8, 7, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8660421371459961})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8254387974739075})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9300416707992554})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0357518196105957})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.095585823059082})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.73336044921875}
store['active_learning_steps'][53]['acquisition']={'indices': [20438, 3007, 23838, 58949, 50567], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8019832372665405})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.850277304649353})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0375220775604248})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8882737159729004})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8668, 'crossentropy': 0.7313771484375}
store['active_learning_steps'][54]['acquisition']={'indices': [40660, 6424, 25153, 12106, 3513], 'labels': [-1, 4, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8950638771057129})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9532654285430908})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9909628033638})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.1405431032180786})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8333, 'crossentropy': 0.81374169921875}
store['active_learning_steps'][55]['acquisition']={'indices': [36929, 2813, 29540, 39566, 30059], 'labels': [0, 2, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8616362810134888})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8392220139503479})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.833571195602417})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9312425255775452})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9855707883834839})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.949195384979248})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8928, 'crossentropy': 0.723355908203125}
store['active_learning_steps'][56]['acquisition']={'indices': [5567, 14497, 14175, 30376, 14790], 'labels': [3, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8589964509010315})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7846591472625732})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8875119090080261})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0592732429504395})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.080955147743225})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8859, 'crossentropy': 0.67636328125}
store['active_learning_steps'][57]['acquisition']={'indices': [19487, 52742, 31981, 39088, 11603], 'labels': [5, 6, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8356341123580933})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8691514134407043})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9276865720748901})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8751887083053589})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8623, 'crossentropy': 0.785767724609375}
store['active_learning_steps'][58]['acquisition']={'indices': [36086, 35022, 52253, 48874, 871], 'labels': [5, 3, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7212568521499634})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7883307337760925})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7730624079704285})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8302333354949951})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.66274658203125}
store['active_learning_steps'][59]['acquisition']={'indices': [32902, 36605, 34611, 44189, 12633], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.837428092956543})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9034222364425659})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8997683525085449})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9402238130569458})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8638, 'crossentropy': 0.758603857421875}
store['active_learning_steps'][60]['acquisition']={'indices': [64, 50907, 27876, 1057, 14779], 'labels': [4, -1, 9, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7915168404579163})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8021621704101562})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8526871204376221})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8513137102127075})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8604, 'crossentropy': 0.742968408203125}
store['active_learning_steps'][61]['acquisition']={'indices': [19744, 42367, 24225, 9071, 26315], 'labels': [0, -1, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8248045444488525})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7930624485015869})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8857190012931824})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8401798605918884})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9752949476242065})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8924, 'crossentropy': 0.680960888671875}
store['active_learning_steps'][62]['acquisition']={'indices': [48920, 44241, 51025, 1501, 26443], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8075364828109741})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8347232341766357})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7631129622459412})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9160624742507935})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9620671272277832})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9293962121009827})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9023, 'crossentropy': 0.6661849609375}
store['active_learning_steps'][63]['acquisition']={'indices': [23577, 29021, 914, 45489, 42299], 'labels': [-1, 5, 4, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7570916414260864})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7577658891677856})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8255858421325684})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8886752128601074})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8654, 'crossentropy': 0.703982861328125}
store['active_learning_steps'][64]['acquisition']={'indices': [33734, 28837, 50822, 46922, 17601], 'labels': [5, 1, 7, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8414555788040161})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7314955592155457})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8075909614562988})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8233687877655029})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8656675219535828})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8849, 'crossentropy': 0.65964560546875}
store['active_learning_steps'][65]['acquisition']={'indices': [46025, 43504, 22878, 12457, 51517], 'labels': [8, -1, 2, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7510920763015747})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7466510534286499})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7488202452659607})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8797767162322998})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8216497898101807})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.6139875}
store['active_learning_steps'][66]['acquisition']={'indices': [40482, 26173, 9408, 1403, 23371], 'labels': [1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7558338046073914})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6599838733673096})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8036437630653381})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8659965395927429})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9330648183822632})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.60625791015625}
store['active_learning_steps'][67]['acquisition']={'indices': [27153, 42072, 58942, 13918, 54930], 'labels': [-1, 6, 8, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8244996070861816})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7471034526824951})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.769182562828064})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8702386617660522})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7915326356887817})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8971, 'crossentropy': 0.64539287109375}
store['active_learning_steps'][68]['acquisition']={'indices': [44069, 37390, 31425, 44959, 30858], 'labels': [8, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8342351913452148})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8096257448196411})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7720305919647217})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.835579514503479})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8767166137695312})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8797863721847534})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.639306396484375}
store['active_learning_steps'][69]['acquisition']={'indices': [27848, 8234, 6685, 32273, 49128], 'labels': [9, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8688562512397766})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.771135687828064})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7896164059638977})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7447443008422852})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9217171669006348})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8632413148880005})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.962929368019104})
store['active_learning_steps'][70]['training']['best_epoch']=4
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.644638623046875}
store['active_learning_steps'][70]['acquisition']={'indices': [2186, 25962, 35759, 21414, 24964], 'labels': [5, 6, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7933039665222168})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7563085556030273})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8513652682304382})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7262803912162781})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.887453019618988})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9367263913154602})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8919034004211426})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.644973388671875}
store['active_learning_steps'][71]['acquisition']={'indices': [7893, 4903, 55125, 58502, 22072], 'labels': [-1, -1, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7997734546661377})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7083632349967957})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6928935050964355})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8104029297828674})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7177249193191528})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8735564947128296})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.64941103515625}
store['active_learning_steps'][72]['acquisition']={'indices': [27641, 14980, 16173, 58118, 17765], 'labels': [2, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.804484486579895})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.775511622428894})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7781823873519897})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7684442400932312})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9449598789215088})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.925475001335144})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.890791654586792})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9011, 'crossentropy': 0.6984806640625}
store['active_learning_steps'][73]['acquisition']={'indices': [3623, 23188, 6671, 30606, 25780], 'labels': [6, 4, 5, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7521510124206543})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6997820138931274})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7867298126220703})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8020520210266113})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8701692819595337})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.60380185546875}
store['active_learning_steps'][74]['acquisition']={'indices': [27072, 22164, 12436, 59273, 41849], 'labels': [-1, 1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7660347819328308})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7623368501663208})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8082525730133057})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8092876672744751})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9184872508049011})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8979, 'crossentropy': 0.642036376953125}
store['active_learning_steps'][75]['acquisition']={'indices': [9010, 27658, 12223, 50139, 31136], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7343457937240601})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6971502304077148})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8298475742340088})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8827482461929321})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8901585340499878})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.616026220703125}
store['active_learning_steps'][76]['acquisition']={'indices': [16288, 43944, 25607, 616, 43650], 'labels': [7, 8, 8, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8095519542694092})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7515370845794678})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7519429922103882})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7571075558662415})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7558912038803101})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.652558740234375}
store['active_learning_steps'][77]['acquisition']={'indices': [23322, 11964, 46293, 30085, 19129], 'labels': [3, 6, 2, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7486065626144409})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6704657673835754})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6983636617660522})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7309759855270386})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7380185127258301})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.59479794921875}
store['active_learning_steps'][78]['acquisition']={'indices': [31608, 4040, 55589, 40594, 658], 'labels': [2, 8, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6662713289260864})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6479934453964233})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7039213180541992})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6734604239463806})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7362593412399292})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.563937109375}
store['active_learning_steps'][79]['acquisition']={'indices': [18486, 331, 59024, 30680, 31875], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.776826024055481})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6942105293273926})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6677338480949402})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6505247354507446})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7861084938049316})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8088918924331665})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8287004828453064})
store['active_learning_steps'][80]['training']['best_epoch']=4
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.53835185546875}
store['active_learning_steps'][80]['acquisition']={'indices': [32819, 10904, 34871, 8080, 40601], 'labels': [7, 5, 2, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7617798447608948})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6387328505516052})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6376590728759766})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7534854412078857})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8158135414123535})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8440957069396973})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.566373388671875}
store['active_learning_steps'][81]['acquisition']={'indices': [43518, 14761, 35479, 14347, 41939], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7239936590194702})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6487598419189453})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6989010572433472})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7749348878860474})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.703842282295227})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9005, 'crossentropy': 0.5635990234375}
store['active_learning_steps'][82]['acquisition']={'indices': [10582, 16763, 43540, 25787, 17382], 'labels': [-1, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6685652732849121})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6357709765434265})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6158847808837891})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6429444551467896})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7220134735107422})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7735638618469238})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.570951611328125}
store['active_learning_steps'][83]['acquisition']={'indices': [13081, 49309, 12164, 31861, 6053], 'labels': [-1, -1, -1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6791378259658813})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6327203512191772})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6550405025482178})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6402954459190369})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7025176882743835})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.5699703125}
store['active_learning_steps'][84]['acquisition']={'indices': [35156, 30043, 53122, 15077, 42378], 'labels': [3, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6925135850906372})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6433917284011841})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7164510488510132})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7431918382644653})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8173699975013733})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.56800361328125}
store['active_learning_steps'][85]['acquisition']={'indices': [48152, 25724, 43359, 58056, 26031], 'labels': [-1, -1, 6, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7898540496826172})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6488059759140015})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6941693425178528})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6901277303695679})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7305529713630676})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.5710873046875}
store['active_learning_steps'][86]['acquisition']={'indices': [6171, 46698, 26579, 5787, 31707], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6983060836791992})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6244902014732361})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6694501638412476})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6257258057594299})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6791951060295105})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9063, 'crossentropy': 0.55974130859375}
store['active_learning_steps'][87]['acquisition']={'indices': [28381, 19046, 51304, 17291, 39762], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7836201786994934})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6730763912200928})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.672753095626831})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6498079299926758})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6462767124176025})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7318000793457031})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6974335312843323})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8256672620773315})
store['active_learning_steps'][88]['training']['best_epoch']=5
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.57183134765625}
store['active_learning_steps'][88]['acquisition']={'indices': [41277, 24459, 59395, 4752, 21760], 'labels': [-1, 9, 8, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7385542392730713})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6356952786445618})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6440238952636719})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6589140892028809})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7092592120170593})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.53008486328125}
store['active_learning_steps'][89]['acquisition']={'indices': [23556, 15275, 35578, 40560, 50011], 'labels': [3, -1, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7290787100791931})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6414936780929565})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5969097018241882})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6588985919952393})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6432793736457825})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7213823795318604})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9136, 'crossentropy': 0.539960595703125}
store['active_learning_steps'][90]['acquisition']={'indices': [55736, 29909, 34215, 10464, 55002], 'labels': [4, -1, 1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7176769971847534})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6750556230545044})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6533807516098022})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.665747880935669})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7030948996543884})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7295129299163818})
store['active_learning_steps'][91]['training']['best_epoch']=3
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.572092236328125}
store['active_learning_steps'][91]['acquisition']={'indices': [35549, 34009, 9994, 6932, 35597], 'labels': [-1, 6, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7267024517059326})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6372144818305969})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6248299479484558})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5996503829956055})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7056945562362671})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7309854030609131})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6748848557472229})
store['active_learning_steps'][92]['training']['best_epoch']=4
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.553147998046875}
store['active_learning_steps'][92]['acquisition']={'indices': [21062, 5773, 18205, 54369, 30743], 'labels': [7, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8042944669723511})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6804024577140808})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6715211272239685})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6306698322296143})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6846833229064941})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7207385301589966})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.727866530418396})
store['active_learning_steps'][93]['training']['best_epoch']=4
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.558418408203125}
store['active_learning_steps'][93]['acquisition']={'indices': [30328, 43647, 37511, 28653, 58980], 'labels': [-1, 8, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7484143972396851})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5511118173599243})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6131901741027832})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6250566244125366})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6983479261398315})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.50813740234375}
store['active_learning_steps'][94]['acquisition']={'indices': [234, 38167, 33713, 39680, 55439], 'labels': [0, -1, 5, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.765998125076294})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6265670657157898})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6296537518501282})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6660398244857788})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6769614219665527})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.56685986328125}
store['active_learning_steps'][95]['acquisition']={'indices': [47402, 47813, 54340, 39096, 57039], 'labels': [-1, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7084136009216309})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6562097072601318})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6373093128204346})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.692101240158081})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6782864332199097})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7174566984176636})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.548607421875}
store['active_learning_steps'][96]['acquisition']={'indices': [45817, 12349, 43942, 414, 25185], 'labels': [-1, 3, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.736247181892395})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.625110387802124})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6222753524780273})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6179482936859131})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6419084072113037})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.730811595916748})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6066780090332031})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7284750938415527})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7132232785224915})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6532011032104492})
store['active_learning_steps'][97]['training']['best_epoch']=7
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9261, 'crossentropy': 0.57305048828125}
store['active_learning_steps'][97]['acquisition']={'indices': [9356, 41391, 53418, 12936, 3733], 'labels': [7, -1, 7, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6830905675888062})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5855550765991211})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.609498918056488})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6534732580184937})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7010401487350464})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.5425048828125}
store['active_learning_steps'][98]['acquisition']={'indices': [3714, 45342, 14727, 51882, 57780], 'labels': [-1, 2, 7, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6896462440490723})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6473474502563477})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5975362062454224})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6332796812057495})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6672419905662537})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6691573858261108})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.56816513671875}
store['active_learning_steps'][99]['acquisition']={'indices': [47399, 55298, 49601, 5711, 52832], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7208251953125})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6205297708511353})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7132561206817627})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6391793489456177})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7248090505599976})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.54956669921875}
store['active_learning_steps'][100]['acquisition']={'indices': [26739, 55249, 8347, 16459, 30093], 'labels': [-1, 3, 6, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7926559448242188})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6144673824310303})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6421834230422974})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7525014877319336})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8095202445983887})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.568174658203125}
store['active_learning_steps'][101]['acquisition']={'indices': [59004, 56203, 59428, 34048, 55100], 'labels': [2, -1, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7392414808273315})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6052385568618774})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5928909778594971})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6696277856826782})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6697263717651367})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.721936047077179})
store['active_learning_steps'][102]['training']['best_epoch']=3
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.5320353515625}
store['active_learning_steps'][102]['acquisition']={'indices': [35416, 24835, 662, 42849, 23470], 'labels': [7, 3, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.74802565574646})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.680229902267456})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6298502087593079})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.730302095413208})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6969568133354187})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6795303821563721})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.55732802734375}
store['active_learning_steps'][103]['acquisition']={'indices': [14025, 44535, 53890, 43284, 2652], 'labels': [3, -1, -1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7719694375991821})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6777582168579102})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6147422790527344})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.664958119392395})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7199026942253113})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.666317343711853})
store['active_learning_steps'][104]['training']['best_epoch']=3
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.513239013671875}
store['active_learning_steps'][104]['acquisition']={'indices': [23915, 46659, 5476, 14070, 33430], 'labels': [6, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.701079249382019})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6175984740257263})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6429215669631958})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7415386438369751})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6589747071266174})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.566144775390625}
store['active_learning_steps'][105]['acquisition']={'indices': [39879, 48225, 32038, 7678, 13764], 'labels': [-1, 9, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7345061898231506})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.690091609954834})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6743574142456055})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6626425981521606})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7497454285621643})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.736849308013916})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7724940776824951})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.5320509765625}
store['active_learning_steps'][106]['acquisition']={'indices': [44694, 52040, 7998, 45882, 37425], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7350389361381531})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6453681588172913})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6602270603179932})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6310821771621704})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6938956379890442})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6940574049949646})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7321281433105469})
store['active_learning_steps'][107]['training']['best_epoch']=4
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.52707646484375}
store['active_learning_steps'][107]['acquisition']={'indices': [57355, 14974, 41397, 26066, 28176], 'labels': [8, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7381899952888489})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.632633626461029})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.650892972946167})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6985644698143005})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6745188236236572})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.567734423828125}
store['active_learning_steps'][108]['acquisition']={'indices': [37527, 59489, 44942, 16403, 45392], 'labels': [8, -1, 4, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6844322681427002})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.603145182132721})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.647773265838623})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6692836880683899})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6381765604019165})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.54027451171875}
store['active_learning_steps'][109]['acquisition']={'indices': [6705, 53109, 53896, 27920, 33356], 'labels': [6, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8430154323577881})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7007980942726135})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6331746578216553})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6887317895889282})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6931366920471191})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6597726941108704})
store['active_learning_steps'][110]['training']['best_epoch']=3
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.5616888671875}
store['active_learning_steps'][110]['acquisition']={'indices': [42203, 38462, 41752, 40796, 48781], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6877568364143372})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6287596821784973})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.64424729347229})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6084344387054443})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6395372748374939})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6463438868522644})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6544541120529175})
store['active_learning_steps'][111]['training']['best_epoch']=4
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.565070458984375}
store['active_learning_steps'][111]['acquisition']={'indices': [37312, 36639, 16792, 33036, 29469], 'labels': [-1, 5, 6, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7094347476959229})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.610700786113739})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5953782796859741})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.595634937286377})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7026259899139404})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7627823352813721})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.544943701171875}
store['active_learning_steps'][112]['acquisition']={'indices': [38156, 52105, 2587, 9960, 41021], 'labels': [6, 0, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.735752284526825})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6065452098846436})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6070156097412109})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6429531574249268})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6935348510742188})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.569614990234375}
store['active_learning_steps'][113]['acquisition']={'indices': [45992, 59482, 48408, 34491, 34107], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7840284109115601})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6062924861907959})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5802041292190552})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.631201982498169})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6336668729782104})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6432193517684937})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.48344775390625}
store['active_learning_steps'][114]['acquisition']={'indices': [47879, 31834, 19366, 57303, 1392], 'labels': [-1, 9, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7242715954780579})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5602378845214844})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6645203828811646})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.590656042098999})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5887480974197388})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.508487353515625}
store['active_learning_steps'][115]['acquisition']={'indices': [40245, 38826, 3289, 16145, 23359], 'labels': [-1, 2, 5, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6943819522857666})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5933349132537842})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5699877142906189})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5982763767242432})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6459420919418335})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6677263379096985})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9184, 'crossentropy': 0.521770166015625}
store['active_learning_steps'][116]['acquisition']={'indices': [56606, 57740, 57851, 53797, 20048], 'labels': [-1, 1, 7, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7635218501091003})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5658296346664429})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5653301477432251})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6231319904327393})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5582486987113953})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6174531579017639})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6442446708679199})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6629096269607544})
store['active_learning_steps'][117]['training']['best_epoch']=5
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.47539736328125}
store['active_learning_steps'][117]['acquisition']={'indices': [2704, 28488, 48251, 4586, 53109], 'labels': [7, 1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7133740186691284})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5650501847267151})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5929805040359497})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6392767429351807})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.650620698928833})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.506702783203125}
store['active_learning_steps'][118]['acquisition']={'indices': [48879, 41560, 6146, 45133, 2343], 'labels': [6, -1, 0, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7599115371704102})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5939739942550659})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6230117082595825})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.650020956993103})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6150223612785339})
store['active_learning_steps'][119]['training']['best_epoch']=2
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.52858642578125}
store['active_learning_steps'][119]['acquisition']={'indices': [3296, 42471, 13542, 2678, 4982], 'labels': [-1, -1, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6873139142990112})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5518121123313904})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6544575095176697})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6177340149879456})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6547298431396484})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.50713056640625}
store['active_learning_steps'][120]['acquisition']={'indices': [20199, 58752, 21840, 49088, 1203], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6746802926063538})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5820557475090027})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5970678329467773})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6477456092834473})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6577975749969482})
store['active_learning_steps'][121]['training']['best_epoch']=2
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.51935341796875}
store['active_learning_steps'][121]['acquisition']={'indices': [7090, 51230, 42242, 28359, 48171], 'labels': [-1, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7217826247215271})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6414909362792969})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5928884148597717})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6144020557403564})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6123204231262207})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6161360740661621})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.487317138671875}
store['active_learning_steps'][122]['acquisition']={'indices': [38888, 10331, 41902, 49343, 20609], 'labels': [5, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6627993583679199})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5687752962112427})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5854157209396362})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5753406882286072})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5906561017036438})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.51287978515625}
store['active_learning_steps'][123]['acquisition']={'indices': [11505, 53840, 35248, 21894, 38370], 'labels': [5, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7402759790420532})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5808730125427246})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5786813497543335})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6315088868141174})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6047585010528564})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6461181044578552})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.488443115234375}
store['active_learning_steps'][124]['acquisition']={'indices': [12689, 38904, 11128, 37946, 10882], 'labels': [-1, -1, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7893617153167725})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6133604049682617})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6179180145263672})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6215686798095703})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6611776351928711})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9034, 'crossentropy': 0.571072998046875}
store['active_learning_steps'][125]['acquisition']={'indices': [26789, 45144, 52028, 17698, 17226], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7255131006240845})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5661067962646484})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6188340187072754})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6931617259979248})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6671098470687866})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.512097314453125}
store['active_learning_steps'][126]['acquisition']={'indices': [56228, 30452, 45646, 45806, 59640], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6656805276870728})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5919341444969177})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5387269258499146})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5998014211654663})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.643315851688385})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6559154987335205})
store['active_learning_steps'][127]['training']['best_epoch']=3
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.463039501953125}
store['active_learning_steps'][127]['acquisition']={'indices': [1602, 12193, 16844, 39951, 47965], 'labels': [-1, 0, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6886434555053711})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5433812141418457})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5523806214332581})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5623021125793457})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5940719842910767})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.480049609375}
store['active_learning_steps'][128]['acquisition']={'indices': [46870, 4642, 30031, 21678, 58098], 'labels': [-1, 0, -1, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7580013275146484})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5645465850830078})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.571008563041687})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5601459741592407})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.681921124458313})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6619449853897095})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5896368026733398})
store['active_learning_steps'][129]['training']['best_epoch']=4
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9268, 'crossentropy': 0.48071220703125}
store['active_learning_steps'][129]['acquisition']={'indices': [50715, 45459, 27509, 44531, 52376], 'labels': [8, 2, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7240240573883057})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5838659405708313})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5981085300445557})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5954266786575317})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6092987656593323})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9122, 'crossentropy': 0.49042109375}
store['active_learning_steps'][130]['acquisition']={'indices': [40635, 34008, 4406, 3476, 55824], 'labels': [-1, 1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7061423063278198})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5847093462944031})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5870136022567749})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5958031415939331})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6567891836166382})
store['active_learning_steps'][131]['training']['best_epoch']=2
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.5190306640625}
store['active_learning_steps'][131]['acquisition']={'indices': [26046, 53917, 2794, 51046, 22095], 'labels': [2, 0, 1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6821168661117554})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5586128830909729})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5585201978683472})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5595663785934448})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5839946269989014})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6598271131515503})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.484117431640625}
store['active_learning_steps'][132]['acquisition']={'indices': [41726, 26642, 43057, 3595, 5347], 'labels': [-1, -1, -1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7210108637809753})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5874727368354797})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5530602931976318})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5590823292732239})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5984255075454712})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48346754908561707})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5910817980766296})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5598523616790771})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6306905746459961})
store['active_learning_steps'][133]['training']['best_epoch']=6
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.4127888671875}
store['active_learning_steps'][133]['acquisition']={'indices': [44847, 27724, 53243, 7095, 39196], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6507081389427185})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6537353992462158})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5702784657478333})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5935095548629761})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6516233682632446})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6512677669525146})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.4974431640625}
store['active_learning_steps'][134]['acquisition']={'indices': [22579, 20652, 42310, 55668, 23906], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7502833604812622})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.598387598991394})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5548070669174194})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5889310836791992})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6116737127304077})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6094728708267212})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.44972197265625}
store['active_learning_steps'][135]['acquisition']={'indices': [26668, 5167, 54423, 14121, 565], 'labels': [7, 0, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6897794604301453})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6261586546897888})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.547850489616394})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6010096073150635})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6094219088554382})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6011309623718262})
store['active_learning_steps'][136]['training']['best_epoch']=3
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.461164501953125}
store['active_learning_steps'][136]['acquisition']={'indices': [47649, 15506, 9444, 6603, 1861], 'labels': [2, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7330024242401123})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5211044549942017})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5312026739120483})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5324515700340271})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5349698066711426})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.46613310546875}
store['active_learning_steps'][137]['acquisition']={'indices': [22257, 28560, 36502, 16209, 48300], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6835043430328369})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.596552848815918})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5984204411506653})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5938986539840698})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6522588729858398})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6228637099266052})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6853035092353821})
store['active_learning_steps'][138]['training']['best_epoch']=4
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.5027306640625}
store['active_learning_steps'][138]['acquisition']={'indices': [27199, 51817, 2086, 38404, 19341], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7501327395439148})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5333878993988037})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5481808185577393})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5706168413162231})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5755854249000549})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.473099365234375}
store['active_learning_steps'][139]['acquisition']={'indices': [17898, 35737, 59793, 17272, 18828], 'labels': [4, 1, 8, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6043920516967773})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.49300602078437805})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5355538725852966})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5297223925590515})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5422996282577515})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.4523419921875}
store['active_learning_steps'][140]['acquisition']={'indices': [20704, 20274, 18790, 38699, 9199], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7162169218063354})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6369929909706116})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5534240007400513})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5680623054504395})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5775616765022278})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5862927436828613})
store['active_learning_steps'][141]['training']['best_epoch']=3
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.478522607421875}
store['active_learning_steps'][141]['acquisition']={'indices': [12897, 45368, 215, 24171, 15742], 'labels': [0, -1, 3, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6928304433822632})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.544571578502655})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5638309717178345})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5958771109580994})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5394626259803772})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5711629986763})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5947368144989014})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6061902046203613})
store['active_learning_steps'][142]['training']['best_epoch']=5
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.494134765625}
store['active_learning_steps'][142]['acquisition']={'indices': [19879, 57462, 26482, 55443, 18773], 'labels': [-1, -1, 6, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6868832111358643})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5317718386650085})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5344520807266235})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5531026721000671})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5433424115180969})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.47777705078125}
store['active_learning_steps'][143]['acquisition']={'indices': [8058, 34352, 5439, 21888, 41871], 'labels': [2, 0, -1, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6764719486236572})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5425772070884705})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5432747006416321})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5152610540390015})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5787969827651978})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4914174973964691})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5131494998931885})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5740208029747009})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5510708689689636})
store['active_learning_steps'][144]['training']['best_epoch']=6
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.45300634765625}
store['active_learning_steps'][144]['acquisition']={'indices': [46841, 47114, 54607, 45912, 893], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.7641042470932007})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5604285001754761})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5220852494239807})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5246206521987915})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5115095376968384})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5706754922866821})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5741263628005981})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6325304508209229})
store['active_learning_steps'][145]['training']['best_epoch']=5
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.46222470703125}
store['active_learning_steps'][145]['acquisition']={'indices': [35741, 24834, 52001, 48974, 34780], 'labels': [-1, 1, 2, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7409636974334717})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5214552283287048})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5799590349197388})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5870851874351501})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5959926843643188})
store['active_learning_steps'][146]['training']['best_epoch']=2
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.496000439453125}
store['active_learning_steps'][146]['acquisition']={'indices': [26231, 4898, 48413, 28231, 51892], 'labels': [8, -1, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7018436193466187})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5598434805870056})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49205952882766724})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5539076328277588})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5103734135627747})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5100410580635071})
store['active_learning_steps'][147]['training']['best_epoch']=3
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.464789306640625}
store['active_learning_steps'][147]['acquisition']={'indices': [37289, 55769, 12284, 41097, 42185], 'labels': [-1, -1, 5, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7419198751449585})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6224477291107178})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5109007358551025})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5171405076980591})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5433323979377747})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.577385663986206})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.439340625}
store['active_learning_steps'][148]['acquisition']={'indices': [20034, 14078, 27173, 49603, 2664], 'labels': [5, 5, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6437216997146606})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5421613454818726})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5431293845176697})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.599708080291748})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6124805212020874})
store['active_learning_steps'][149]['training']['best_epoch']=2
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.4924576171875}
store['active_learning_steps'][149]['acquisition']={'indices': [21498, 47130, 35468, 46119, 29703], 'labels': [-1, 5, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6920680999755859})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5522358417510986})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5915961265563965})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.545164942741394})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.512523889541626})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5931196212768555})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6009299159049988})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6273283958435059})
store['active_learning_steps'][150]['training']['best_epoch']=5
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.4198904296875}
store['active_learning_steps'][150]['acquisition']={'indices': [15915, 2524, 43528, 11640, 52185], 'labels': [-1, 3, 7, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6908203363418579})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5541435480117798})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.540797770023346})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5732817649841309})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5475749969482422})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5659177303314209})
store['active_learning_steps'][151]['training']['best_epoch']=3
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.455794140625}
store['active_learning_steps'][151]['acquisition']={'indices': [55370, 7565, 26057, 25691, 1821], 'labels': [9, 7, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7235969305038452})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5913630723953247})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5527455806732178})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4973064661026001})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5342281460762024})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5662533640861511})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5717569589614868})
store['active_learning_steps'][152]['training']['best_epoch']=4
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.445437255859375}
store['active_learning_steps'][152]['acquisition']={'indices': [47076, 14314, 5398, 17288, 21740], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6945888996124268})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5783734321594238})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5319905281066895})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5187450647354126})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5563266277313232})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6022549867630005})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5586386322975159})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.4475099609375}
store['active_learning_steps'][153]['acquisition']={'indices': [54574, 36487, 45534, 38715, 15521], 'labels': [-1, -1, 5, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.684863269329071})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5325222611427307})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.576807975769043})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5080704689025879})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5633972883224487})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5585042238235474})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5305211544036865})
store['active_learning_steps'][154]['training']['best_epoch']=4
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.41402900390625}
store['active_learning_steps'][154]['acquisition']={'indices': [18336, 16636, 34298, 16694, 38004], 'labels': [-1, 1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6677293181419373})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.515247106552124})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.538107693195343})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5837823152542114})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5083503723144531})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5741617679595947})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5301469564437866})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5193520784378052})
store['active_learning_steps'][155]['training']['best_epoch']=5
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.46348310546875}
store['active_learning_steps'][155]['acquisition']={'indices': [48570, 14168, 32882, 34941, 39371], 'labels': [-1, 5, 9, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.722242534160614})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5285727977752686})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44530755281448364})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.47766655683517456})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5374367237091064})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5699711441993713})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.41409482421875}
store['active_learning_steps'][156]['acquisition']={'indices': [7972, 30972, 5299, 56999, 40956], 'labels': [-1, 2, 8, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6129065752029419})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.544922947883606})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5395920276641846})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5501259565353394})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6211912631988525})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6360123157501221})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.443952392578125}
store['active_learning_steps'][157]['acquisition']={'indices': [16055, 8164, 51913, 2242, 43061], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6734756827354431})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5215033888816833})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5560243129730225})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4985811114311218})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4937386214733124})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4897492527961731})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49977725744247437})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49466684460639954})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5407374501228333})
store['active_learning_steps'][158]['training']['best_epoch']=6
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.41869765625}
store['active_learning_steps'][158]['acquisition']={'indices': [44171, 35330, 40544, 56166, 45262], 'labels': [-1, 9, 0, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6798073053359985})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5725435018539429})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5399408340454102})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5383175015449524})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5155731439590454})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5934786796569824})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5690115094184875})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6027309894561768})
store['active_learning_steps'][159]['training']['best_epoch']=5
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.935, 'crossentropy': 0.44831875}
store['active_learning_steps'][159]['acquisition']={'indices': [37117, 49094, 13916, 5085, 21949], 'labels': [-1, 5, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6705357432365417})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5416953563690186})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5181348919868469})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5630561709403992})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5138158202171326})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5349007844924927})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6064125299453735})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5927004814147949})
store['active_learning_steps'][160]['training']['best_epoch']=5
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.454780419921875}
store['active_learning_steps'][160]['acquisition']={'indices': [4216, 24136, 45425, 45221, 30580], 'labels': [-1, 1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6344113945960999})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5244389176368713})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5082231760025024})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5268312692642212})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4996779263019562})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.561744213104248})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5797847509384155})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5910483598709106})
store['active_learning_steps'][161]['training']['best_epoch']=5
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9379, 'crossentropy': 0.4021384033203125}
store['active_learning_steps'][161]['acquisition']={'indices': [55174, 32573, 31000, 20100, 2001], 'labels': [7, 8, 6, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7319227457046509})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.550344705581665})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5113178491592407})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5449675917625427})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45945900678634644})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5185378789901733})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5262798070907593})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.562760591506958})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.417193603515625}
store['active_learning_steps'][162]['acquisition']={'indices': [10406, 9214, 58890, 4679, 9090], 'labels': [-1, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6079711318016052})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.48374658823013306})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45972418785095215})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5426162481307983})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5065727233886719})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5575277209281921})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.39041689453125}
store['active_learning_steps'][163]['acquisition']={'indices': [22694, 48093, 50758, 12451, 13570], 'labels': [4, 7, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6509109735488892})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5592367649078369})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4923339784145355})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4840965270996094})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4423139691352844})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49415281414985657})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5558379888534546})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5086525678634644})
store['active_learning_steps'][164]['training']['best_epoch']=5
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9423, 'crossentropy': 0.386794384765625}
store['active_learning_steps'][164]['acquisition']={'indices': [15439, 43101, 6018, 28131, 5954], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6490718126296997})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5376698970794678})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5331535339355469})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5297986268997192})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5437226891517639})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5449318289756775})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5497527122497559})
store['active_learning_steps'][165]['training']['best_epoch']=4
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9341, 'crossentropy': 0.453723876953125}
store['active_learning_steps'][165]['acquisition']={'indices': [34972, 6421, 59275, 1654, 9871], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7029769420623779})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.509748637676239})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5018781423568726})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4627070724964142})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5277793407440186})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4844208359718323})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5392067432403564})
store['active_learning_steps'][166]['training']['best_epoch']=4
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.422611083984375}
store['active_learning_steps'][166]['acquisition']={'indices': [5531, 33861, 44352, 1381, 32144], 'labels': [3, 1, 4, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.653901994228363})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5127395391464233})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5023162364959717})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5276082754135132})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5369239449501038})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46744704246520996})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4949135184288025})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.539400041103363})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5645286440849304})
store['active_learning_steps'][167]['training']['best_epoch']=6
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.4133451171875}
store['active_learning_steps'][167]['acquisition']={'indices': [20590, 3183, 22129, 52989, 21389], 'labels': [5, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6881667375564575})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5019928216934204})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48814764618873596})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5144418478012085})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.532051146030426})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5168375968933105})
store['active_learning_steps'][168]['training']['best_epoch']=3
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.4067717529296875}
