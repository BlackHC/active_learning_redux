store = {}
store['timestamp']=1620259978
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=25']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=25
store['worker_id']=25
store['num_workers']=40
store['config']={'seed': 30, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6353745460510254})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6310830116271973})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.5534510612487793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.824211359024048})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.03212308883667})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9762306213378906})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6929, 'crossentropy': 2.40249921875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 21086], ['id', 28302], ['ood', 41969], ['id', 56505], ['id', 47647]], 'labels': [7, 6, 0, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.860086441040039})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0172197818756104})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.207881450653076})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.2941954135894775})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6796, 'crossentropy': 1.62039990234375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 15232], ['id', 16016], ['id', 54234], ['id', 35562], ['ood', 32418]], 'labels': [9, 7, 4, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3879520893096924})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6566662788391113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.7431124448776245})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.805002212524414})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7393, 'crossentropy': 1.2853681640625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 38001], ['id', 8008], ['id', 30690], ['ood', 59845], ['id', 58239]], 'labels': [3, 8, 2, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3396843671798706})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4306920766830444})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4860100746154785})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.6491329669952393})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7672, 'crossentropy': 1.19259638671875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 5671], ['id', 56769], ['ood', 32439], ['ood', 49661], ['ood', 57577]], 'labels': [5, 7, 1, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1464043855667114})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4071552753448486})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4767358303070068})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.5884358882904053})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7635, 'crossentropy': 1.09487490234375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 31335], ['ood', 34964], ['ood', 30291], ['ood', 14], ['ood', 999]], 'labels': [1, 4, 0, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.2192949056625366})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.386793851852417})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.4344966411590576})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.553114414215088})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7515, 'crossentropy': 1.1032427734375}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 36722], ['ood', 16547], ['id', 29235], ['ood', 3054], ['id', 5666]], 'labels': [6, 6, 0, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.172391414642334})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.3535590171813965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4794261455535889})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.5955195426940918})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7548, 'crossentropy': 1.06976552734375}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 13218], ['ood', 44964], ['id', 43346], ['id', 11159], ['id', 14175]], 'labels': [5, 8, 7, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.118719220161438})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0984458923339844})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.236783504486084})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2842117547988892})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.3722281455993652})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7886, 'crossentropy': 1.026943359375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 59167], ['ood', 15696], ['id', 27086], ['id', 59213], ['id', 56313]], 'labels': [2, 5, 6, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1276235580444336})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1857341527938843})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2930560111999512})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.4049782752990723})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.761, 'crossentropy': 1.0894654296875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 34712], ['id', 21479], ['ood', 16941], ['ood', 32437], ['ood', 44118]], 'labels': [3, 1, 1, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1349374055862427})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2059082984924316})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3636786937713623})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.420250415802002})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7612, 'crossentropy': 1.1093658203125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 34023], ['ood', 53117], ['id', 41810], ['id', 14646], ['id', 31366]], 'labels': [0, 9, 0, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0235776901245117})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.191971778869629})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.295332431793213})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2871687412261963})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7814, 'crossentropy': 1.0077478515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 9827], ['ood', 43314], ['id', 28496], ['ood', 20611], ['id', 15143]], 'labels': [1, 8, 6, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0592128038406372})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2419745922088623})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.2941503524780273})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2990813255310059})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7882, 'crossentropy': 0.9711958984375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 20454], ['id', 1703], ['ood', 46782], ['ood', 55800], ['id', 14116]], 'labels': [2, 1, 2, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0360612869262695})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0412383079528809})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1087911128997803})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2135040760040283})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7894, 'crossentropy': 0.94343486328125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 29041], ['id', 47963], ['id', 31479], ['ood', 4778], ['ood', 57247]], 'labels': [1, 6, 8, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.962934672832489})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9933578968048096})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0878331661224365})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0400645732879639})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.797, 'crossentropy': 0.92627294921875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 15950], ['id', 52633], ['ood', 17745], ['ood', 21591], ['ood', 34365]], 'labels': [3, 7, 2, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9838298559188843})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9473755359649658})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.085989236831665})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1064648628234863})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1194798946380615})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8142, 'crossentropy': 0.8679228515625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 49975], ['id', 13865], ['ood', 28162], ['id', 5195], ['ood', 42350]], 'labels': [1, 6, 6, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9054046869277954})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9599143266677856})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0109667778015137})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0900006294250488})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8087, 'crossentropy': 0.8956443359375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 29540], ['id', 10619], ['id', 25133], ['id', 55006], ['id', 38348]], 'labels': [0, 8, 7, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.95998215675354})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9290615320205688})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0024055242538452})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0484641790390015})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1281383037567139})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8276, 'crossentropy': 0.8531234375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 48754], ['ood', 43014], ['ood', 39686], ['ood', 9982], ['id', 7871]], 'labels': [4, 9, 4, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.896568775177002})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9559808969497681})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0675082206726074})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0616986751556396})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7929, 'crossentropy': 0.89898310546875}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 49429], ['ood', 27392], ['ood', 11232], ['ood', 45416], ['ood', 31744]], 'labels': [7, 2, 3, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9340026378631592})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9802225828170776})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0685584545135498})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.10170578956604})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8029, 'crossentropy': 0.8644099609375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 7274], ['ood', 28591], ['ood', 36598], ['id', 21179], ['id', 11784]], 'labels': [9, 8, 3, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9120638370513916})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0458744764328003})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2008357048034668})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1867796182632446})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8212, 'crossentropy': 0.85680869140625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27198], ['id', 28253], ['id', 50243], ['id', 47403], ['ood', 4611]], 'labels': [6, 4, 4, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0075937509536743})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8841075897216797})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9859479069709778})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9834767580032349})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3207266330718994})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8077, 'crossentropy': 0.89082919921875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 33140], ['ood', 47719], ['ood', 46853], ['id', 44356], ['ood', 39475]], 'labels': [8, 2, 4, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.014690637588501})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9418562650680542})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.948028564453125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0015265941619873})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0870726108551025})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7991, 'crossentropy': 0.909519140625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 31341], ['ood', 50442], ['ood', 36655], ['id', 54201], ['ood', 12791]], 'labels': [0, 3, 8, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.972436785697937})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9647898077964783})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1180307865142822})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0706725120544434})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1554780006408691})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8075, 'crossentropy': 0.8914521484375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 11929], ['id', 22676], ['id', 31963], ['ood', 12041], ['ood', 29536]], 'labels': [8, 4, 1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9199389219284058})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9122487902641296})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.981979250907898})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0482648611068726})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0804574489593506})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8085, 'crossentropy': 0.90118466796875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 2997], ['ood', 5783], ['ood', 25225], ['id', 25015], ['id', 6407]], 'labels': [9, 4, 8, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.9558920860290527})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7916688919067383})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8760443329811096})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.92843097448349})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0143253803253174})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8271, 'crossentropy': 0.799228466796875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 33425], ['id', 20251], ['id', 44553], ['id', 43660], ['id', 21135]], 'labels': [1, 4, 9, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8090349435806274})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7041350603103638})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6820266246795654})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7883702516555786})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7570818066596985})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7806428670883179})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.6070677734375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 22569], ['ood', 20165], ['ood', 35689], ['id', 42919], ['id', 57299]], 'labels': [3, 7, 5, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8515710830688477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7078746557235718})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7746626138687134})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7121868133544922})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7343617677688599})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8661, 'crossentropy': 0.664825}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 57370], ['id', 47408], ['id', 7136], ['id', 39473], ['id', 13938]], 'labels': [2, 2, 8, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8008764982223511})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6668374538421631})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6966180801391602})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6618986129760742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7113048434257507})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6166636943817139})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.726527214050293})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7228333950042725})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6767606735229492})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.574213232421875}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 5058], ['id', 57145], ['ood', 42598], ['ood', 55897], ['ood', 16548]], 'labels': [1, 9, 9, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8088613748550415})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.649103581905365})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5963675379753113})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6237694025039673})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6650940775871277})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6945005059242249})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.579545703125}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 32988], ['ood', 2198], ['id', 49306], ['id', 34848], ['id', 49636]], 'labels': [1, 0, 0, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7685974836349487})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6338375806808472})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6098591089248657})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6703720092773438})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7946118712425232})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7175894975662231})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8832, 'crossentropy': 0.599623291015625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 54446], ['id', 1360], ['id', 14582], ['ood', 55291], ['ood', 45802]], 'labels': [5, 9, 9, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8552707433700562})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6790890693664551})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6817607879638672})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7481623888015747})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7430874705314636})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8761, 'crossentropy': 0.643320556640625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 52758], ['ood', 31835], ['id', 6914], ['ood', 18418], ['id', 52698]], 'labels': [1, 4, 7, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7885279655456543})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6613001823425293})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5750002861022949})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6038517951965332})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6169273853302002})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6108264923095703})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.53215068359375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 1358], ['id', 23841], ['id', 3159], ['id', 53745], ['ood', 53902]], 'labels': [2, 1, 3, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8532270193099976})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6187789440155029})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5763942003250122})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5922863483428955})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6258904933929443})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6281825304031372})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.528611962890625}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 42109], ['id', 33404], ['id', 4086], ['ood', 51446], ['ood', 17337]], 'labels': [2, 5, 2, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8209846019744873})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6390388011932373})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5845776796340942})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5783734321594238})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6517735719680786})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6454706192016602})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6527143716812134})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.554171826171875}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 18086], ['id', 8457], ['ood', 30985], ['id', 36428], ['ood', 29701]], 'labels': [5, 4, 5, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7672982215881348})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6624615788459778})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6640572547912598})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6828006505966187})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.644899308681488})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6925411224365234})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6523125767707825})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7276124954223633})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.898, 'crossentropy': 0.59459052734375}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 11920], ['ood', 44420], ['ood', 7373], ['ood', 13694], ['id', 16457]], 'labels': [9, 8, 7, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8010426759719849})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5758821964263916})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5617642402648926})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5241773128509521})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.603068470954895})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5740222930908203})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5844634771347046})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.49503642578125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 31996], ['ood', 28839], ['id', 14300], ['id', 45371], ['id', 17202]], 'labels': [3, 1, 6, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8159487247467041})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5852019786834717})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.572617769241333})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5928850173950195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5688142776489258})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7077857255935669})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6370224952697754})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6815242767333984})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.531621044921875}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 9362], ['id', 30363], ['ood', 55630], ['id', 33499], ['id', 50720]], 'labels': [4, 0, 3, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7740178108215332})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6016366481781006})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5660789012908936})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5937436819076538})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5880481004714966})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6146701574325562})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.52433740234375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 45570], ['ood', 59390], ['id', 43325], ['ood', 41771], ['ood', 13406]], 'labels': [2, 5, 9, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8090329170227051})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5734480023384094})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5102479457855225})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5606226921081543})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5518828630447388})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5308237671852112})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.503004931640625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 17949], ['id', 50251], ['ood', 56436], ['id', 20464], ['id', 56682]], 'labels': [4, 2, 7, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7985451221466064})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5689807534217834})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5893532037734985})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5399484634399414})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5640398263931274})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6564077138900757})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6399754285812378})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.540535888671875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 57623], ['ood', 37325], ['ood', 37299], ['id', 32646], ['ood', 51321]], 'labels': [9, 8, 8, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8194665908813477})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5956931114196777})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5802719593048096})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5963976383209229})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5818092823028564})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6003000736236572})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.55227568359375}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 15941], ['ood', 32170], ['ood', 16055], ['id', 33436], ['ood', 26198]], 'labels': [6, 7, 3, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8105898499488831})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5556763410568237})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5402891039848328})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.601372480392456})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.575238823890686})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5865087509155273})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.508102880859375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 7109], ['ood', 56401], ['ood', 7802], ['id', 4395], ['ood', 3031]], 'labels': [6, 6, 4, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8214257955551147})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6118394136428833})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5652710795402527})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6037638187408447})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.60313880443573})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6390719413757324})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.5405787109375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 10823], ['ood', 56613], ['ood', 41178], ['id', 16846], ['id', 56149]], 'labels': [5, 4, 9, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.865383505821228})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5790778398513794})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5779047012329102})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.590103030204773})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6206040382385254})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5904836058616638})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9041, 'crossentropy': 0.540839501953125}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 3971], ['ood', 20885], ['ood', 11353], ['id', 41355], ['ood', 35819]], 'labels': [7, 3, 2, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.773274838924408})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5774203538894653})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.60313481092453})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5243241190910339})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5379873514175415})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5928899049758911})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6015785336494446})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9096, 'crossentropy': 0.507881591796875}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 12595], ['id', 37324], ['ood', 28440], ['id', 36833], ['id', 28723]], 'labels': [4, 8, 0, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8149222135543823})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6187825202941895})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6610967516899109})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5884463787078857})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6185022592544556})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6091778874397278})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6125561594963074})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.53026826171875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 6756], ['ood', 52980], ['id', 28894], ['ood', 27991], ['ood', 38824]], 'labels': [7, 8, 1, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8406820893287659})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5717229843139648})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5733135342597961})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.540160059928894})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5979652404785156})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6748725771903992})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6380912661552429})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.524443896484375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 37219], ['ood', 39310], ['ood', 55117], ['id', 10080], ['id', 16789]], 'labels': [8, 7, 3, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8571788668632507})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6299549341201782})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5707838535308838})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6797035932540894})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5885231494903564})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6198770999908447})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.517672314453125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 58022], ['ood', 9632], ['ood', 48898], ['id', 3716], ['id', 26294]], 'labels': [0, 7, 0, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8628801107406616})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6031044125556946})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5849626064300537})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5926793813705444})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5373337864875793})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6276738047599792})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6187760233879089})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6875042915344238})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9146, 'crossentropy': 0.494821728515625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 11144], ['ood', 46621], ['id', 58229], ['id', 15511], ['id', 7601]], 'labels': [4, 5, 0, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8154190182685852})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5857024788856506})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5791038274765015})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5988863706588745})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5960580110549927})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6973851919174194})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9025, 'crossentropy': 0.528512060546875}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 48101], ['id', 6383], ['id', 42051], ['ood', 57043], ['id', 11806]], 'labels': [8, 9, 8, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7563514709472656})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.604960560798645})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5469651222229004})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5945731401443481})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.49799835681915283})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6171847581863403})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6106845736503601})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6206253170967102})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9156, 'crossentropy': 0.496171435546875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 50075], ['ood', 58789], ['ood', 48755], ['id', 18882], ['id', 27001]], 'labels': [8, 9, 4, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8642663359642029})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5941592454910278})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5692851543426514})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5803836584091187})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6168655157089233})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5862376689910889})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.52975986328125}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 5959], ['ood', 16185], ['id', 44649], ['ood', 16845], ['id', 52962]], 'labels': [9, 8, 6, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8978580236434937})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.61275315284729})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6047533750534058})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5589091777801514})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6210350394248962})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5848066806793213})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6334443092346191})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.54189326171875}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 42050], ['id', 19263], ['id', 18843], ['id', 30229], ['id', 34240]], 'labels': [4, 3, 7, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7973763346672058})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6023242473602295})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5496288537979126})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5078279972076416})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5953828692436218})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5477781295776367})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5615164041519165})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.472848291015625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 53642], ['ood', 49390], ['ood', 478], ['ood', 30459], ['id', 38827]], 'labels': [5, 2, 3, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7860856056213379})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5552246570587158})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5527952909469604})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5291433930397034})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5318970084190369})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5515792369842529})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5735551118850708})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.4858388671875}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 42134], ['ood', 5964], ['ood', 38624], ['id', 7007], ['id', 22318]], 'labels': [2, 0, 9, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8054330348968506})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6099646091461182})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5784070491790771})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5549454689025879})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5511747002601624})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5971101522445679})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5825177431106567})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6076391935348511})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.507346630859375}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 51928], ['ood', 23368], ['id', 16170], ['id', 36232], ['ood', 7358]], 'labels': [5, 4, 9, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8482595682144165})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5869359970092773})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6016465425491333})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5953004360198975})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6273348331451416})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8914, 'crossentropy': 0.559857470703125}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 44498], ['ood', 26210], ['id', 4871], ['id', 55382], ['ood', 34755]], 'labels': [6, 3, 6, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7178020477294922})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5856270790100098})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5276252031326294})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5850955247879028})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.643700122833252})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5863221883773804})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9156, 'crossentropy': 0.461536328125}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 13913], ['id', 13009], ['id', 41304], ['ood', 32828], ['id', 56831]], 'labels': [9, 4, 8, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8580987453460693})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6113749146461487})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6434210538864136})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5461756587028503})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6112996339797974})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6587218046188354})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6603035926818848})
store['active_learning_steps'][58]['training']['best_epoch']=4
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9063, 'crossentropy': 0.527720947265625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 41921], ['id', 46146], ['ood', 33628], ['ood', 2176], ['id', 57559]], 'labels': [4, 9, 8, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7850694060325623})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6051915884017944})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.601773738861084})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5881505012512207})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6166952252388})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5832409858703613})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.664380669593811})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7019785046577454})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6287538409233093})
store['active_learning_steps'][59]['training']['best_epoch']=6
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9033, 'crossentropy': 0.550914453125}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 6621], ['id', 36390], ['ood', 16290], ['id', 41667], ['ood', 25037]], 'labels': [4, 6, 7, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9083887338638306})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6714997291564941})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5502536296844482})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6210011839866638})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6936269402503967})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5711432099342346})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.56708525390625}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 11074], ['id', 4621], ['ood', 502], ['id', 8692], ['ood', 10401]], 'labels': [6, 8, 6, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7913147211074829})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.539888322353363})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5756440162658691})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6290874481201172})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5970298051834106})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9081, 'crossentropy': 0.50483232421875}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 54435], ['ood', 2890], ['id', 22815], ['id', 51199], ['ood', 26074]], 'labels': [8, 9, 1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8556129336357117})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.586151123046875})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6298160552978516})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6001776456832886})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5888453722000122})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.543119970703125}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 31431], ['ood', 26961], ['ood', 58131], ['ood', 37950], ['ood', 59184]], 'labels': [0, 2, 7, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7930278182029724})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6424567699432373})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5833080410957336})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5861144065856934})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6295989155769348})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6647404432296753})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.503705517578125}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 29655], ['id', 14388], ['id', 23927], ['id', 59626], ['id', 1198]], 'labels': [9, 3, 5, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8927698135375977})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6587704420089722})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6012738347053528})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.575011134147644})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5633862018585205})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6376935243606567})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6546303033828735})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6212893724441528})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.490055859375}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 26926], ['id', 21346], ['ood', 8950], ['ood', 57713], ['id', 9151]], 'labels': [8, 5, 8, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.861488401889801})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6864423155784607})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.607513427734375})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5805420875549316})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6539089679718018})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6692036390304565})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6193844079971313})
store['active_learning_steps'][65]['training']['best_epoch']=4
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.511865185546875}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 15730], ['id', 21853], ['ood', 26269], ['ood', 59285], ['id', 36659]], 'labels': [7, 3, 9, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.904863715171814})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6348109841346741})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.564497172832489})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6463509798049927})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5593699216842651})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6367436647415161})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5903636813163757})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6377431154251099})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.512665185546875}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 15060], ['id', 4122], ['id', 49044], ['ood', 7863], ['id', 48772]], 'labels': [0, 9, 8, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8716323375701904})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6497688889503479})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6171281337738037})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6538175344467163})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6474689245223999})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6326813697814941})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9016, 'crossentropy': 0.54280390625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 554], ['ood', 17707], ['id', 44788], ['id', 29462], ['id', 1332]], 'labels': [5, 4, 0, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8475313186645508})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6327879428863525})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5592098236083984})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6230031251907349})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5967240333557129})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5826141238212585})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.501058056640625}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 47127], ['ood', 59309], ['id', 51617], ['id', 50935], ['ood', 2488]], 'labels': [3, 1, 3, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9178280234336853})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7011071443557739})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.672761082649231})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6133037805557251})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6578476428985596})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6491271257400513})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6548510789871216})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.541048779296875}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 26432], ['id', 38025], ['ood', 3088], ['id', 31961], ['id', 53602]], 'labels': [5, 0, 5, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8314340114593506})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6091395616531372})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5233112573623657})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5454730987548828})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6131481528282166})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6112087965011597})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.505920166015625}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 23284], ['id', 28788], ['id', 56645], ['id', 477], ['id', 31248]], 'labels': [6, 8, 3, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7959646582603455})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5797343254089355})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5442569255828857})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5048303604125977})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5806204676628113})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5544378757476807})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6059762239456177})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.45865087890625}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 57388], ['ood', 51374], ['ood', 4513], ['id', 7660], ['id', 22424]], 'labels': [4, 2, 2, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8042131066322327})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5929449796676636})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.590567946434021})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5087164640426636})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5267836451530457})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5687702894210815})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5692406892776489})
store['active_learning_steps'][72]['training']['best_epoch']=4
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.43558564453125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 49073], ['ood', 46970], ['ood', 21465], ['ood', 19137], ['id', 51414]], 'labels': [5, 3, 6, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8265576958656311})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6240587830543518})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5315395593643188})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5755778551101685})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.517058789730072})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5675809383392334})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6043122410774231})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6195017099380493})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.46454267578125}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 38492], ['ood', 58679], ['ood', 17817], ['ood', 41530], ['id', 57605]], 'labels': [5, 9, 3, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9143255949020386})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6399973630905151})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6444946527481079})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5656771659851074})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5918682813644409})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.589714765548706})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5745556354522705})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.473854296875}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 21026], ['ood', 38565], ['ood', 20043], ['id', 8958], ['ood', 37234]], 'labels': [9, 4, 8, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8114321231842041})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6179667115211487})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5583392977714539})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5109906792640686})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5296075940132141})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.625929594039917})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.606218695640564})
store['active_learning_steps'][75]['training']['best_epoch']=4
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.466291064453125}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 59473], ['ood', 2177], ['ood', 23784], ['id', 20739], ['id', 37113]], 'labels': [4, 1, 1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.826816201210022})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5969595313072205})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5473612546920776})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5196278095245361})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6259912252426147})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5497183799743652})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5517094135284424})
store['active_learning_steps'][76]['training']['best_epoch']=4
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9205, 'crossentropy': 0.45333916015625}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 36032], ['ood', 19637], ['id', 49800], ['id', 6695], ['ood', 55688]], 'labels': [3, 8, 0, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8202235698699951})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6063531637191772})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6008942127227783})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5554719567298889})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5187549591064453})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5979986786842346})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5672799348831177})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5783795118331909})
store['active_learning_steps'][77]['training']['best_epoch']=5
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.439365625}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 36976], ['id', 1601], ['ood', 625], ['id', 41730], ['ood', 294]], 'labels': [4, 1, 4, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7953152060508728})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5468254089355469})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5647519826889038})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5287185907363892})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5552058219909668})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6644425988197327})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5818266868591309})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.449461474609375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 51237], ['ood', 39479], ['id', 58504], ['id', 13681], ['id', 55666]], 'labels': [3, 7, 4, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8356548547744751})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5849083662033081})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5006154179573059})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5663267970085144})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5358506441116333})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5511140823364258})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.4456072265625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 13357], ['id', 58708], ['ood', 57170], ['ood', 48036], ['id', 51176]], 'labels': [6, 7, 0, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8162606954574585})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5798057317733765})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6030197143554688})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5398966073989868})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5536525249481201})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5371626019477844})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.546192467212677})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5390753149986267})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5667604804039001})
store['active_learning_steps'][80]['training']['best_epoch']=6
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.456363818359375}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 7], ['id', 30688], ['ood', 42534], ['ood', 48477], ['ood', 13803]], 'labels': [3, 8, 4, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8428455591201782})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5765398740768433})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5462080240249634})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5609263777732849})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5915393829345703})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5917472839355469})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.4918232421875}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 24871], ['ood', 52456], ['id', 42278], ['ood', 37705], ['ood', 21243]], 'labels': [6, 4, 2, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8806090354919434})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5493800640106201})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5261188745498657})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.576725959777832})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5517786145210266})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6079579591751099})
store['active_learning_steps'][82]['training']['best_epoch']=3
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.476673779296875}
store['active_learning_steps'][82]['acquisition']={'indices': [['ood', 18584], ['ood', 50337], ['ood', 24416], ['ood', 3573], ['id', 25681]], 'labels': [2, 2, 1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8579411506652832})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5789552330970764})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5709632635116577})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5582179427146912})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5722312331199646})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.590844988822937})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.549746036529541})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6666809320449829})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6196802854537964})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5501614212989807})
store['active_learning_steps'][83]['training']['best_epoch']=7
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.464267919921875}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 59699], ['id', 724], ['ood', 40472], ['id', 43169], ['id', 13034]], 'labels': [3, 7, 0, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8344482779502869})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5835229158401489})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5472234487533569})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5080174207687378})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6090377569198608})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5783189535140991})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5433880090713501})
store['active_learning_steps'][84]['training']['best_epoch']=4
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.43765078125}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 3523], ['ood', 37302], ['ood', 40196], ['ood', 6382], ['ood', 44249]], 'labels': [8, 8, 0, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8475253582000732})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5719821453094482})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5275285840034485})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5329486727714539})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5244709253311157})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5203907489776611})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5115889310836792})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5469958782196045})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5694468021392822})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5198535919189453})
store['active_learning_steps'][85]['training']['best_epoch']=7
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.447279296875}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 41169], ['ood', 42008], ['ood', 19770], ['id', 17248], ['id', 55451]], 'labels': [2, 4, 7, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.885244607925415})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5911682844161987})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5510067939758301})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5020884275436401})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5342128276824951})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.578310489654541})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5716333985328674})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.45904638671875}
