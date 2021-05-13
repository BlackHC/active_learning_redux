store = {}
store['timestamp']=1620299606
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=34']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=34
store['worker_id']=34
store['num_workers']=40
store['config']={'seed': 48, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.3060903549194336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.823085308074951})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9566354751586914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9516611099243164})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6789, 'crossentropy': 1.99866796875}
store['active_learning_steps'][0]['acquisition']={'indices': [19278, 16666, 11739, 53885, 10082], 'labels': [1, 6, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1555376052856445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3311212062835693})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.525296211242676})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 3.0142111778259277})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6977, 'crossentropy': 1.87469921875}
store['active_learning_steps'][1]['acquisition']={'indices': [17445, 34112, 50287, 14235, 11153], 'labels': [-1, -1, 2, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8881036043167114})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.467794179916382})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.454202175140381})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.5244812965393066})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7331, 'crossentropy': 1.7027744140625}
store['active_learning_steps'][2]['acquisition']={'indices': [44810, 32352, 2175, 52443, 46610], 'labels': [-1, -1, 8, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.781309962272644})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.0497589111328125})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.0870797634124756})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.3773012161254883})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7584, 'crossentropy': 1.62906181640625}
store['active_learning_steps'][3]['acquisition']={'indices': [8752, 32976, 39380, 52342, 19617], 'labels': [2, 4, 5, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7615013122558594})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.9803037643432617})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.1290431022644043})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.1884169578552246})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7551, 'crossentropy': 1.50288310546875}
store['active_learning_steps'][4]['acquisition']={'indices': [12029, 54768, 1558, 53615, 50797], 'labels': [9, -1, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5751652717590332})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.9998629093170166})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.1529767513275146})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.973698616027832})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7564, 'crossentropy': 1.41117001953125}
store['active_learning_steps'][5]['acquisition']={'indices': [46836, 59405, 15547, 1811, 33855], 'labels': [7, 7, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.6790636777877808})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.6288838386535645})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.96036958694458})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9154051542282104})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.3339555263519287})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7764, 'crossentropy': 1.50545498046875}
store['active_learning_steps'][6]['acquisition']={'indices': [16479, 49567, 20088, 29247, 3469], 'labels': [2, -1, 0, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.590123176574707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.7071278095245361})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.80082106590271})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.0638065338134766})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.772, 'crossentropy': 1.35958134765625}
store['active_learning_steps'][7]['acquisition']={'indices': [39035, 6448, 13518, 37878, 40241], 'labels': [8, 4, 8, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3956239223480225})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.709674596786499})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.7824209928512573})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.726914644241333})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.807, 'crossentropy': 1.17978076171875}
store['active_learning_steps'][8]['acquisition']={'indices': [58053, 15540, 42898, 45061, 29552], 'labels': [-1, -1, 3, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.6557328701019287})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.6925382614135742})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.076040506362915})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.9063507318496704})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7747, 'crossentropy': 1.405611328125}
store['active_learning_steps'][9]['acquisition']={'indices': [25924, 26597, 47693, 3198, 37338], 'labels': [-1, 0, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.452919602394104})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5708537101745605})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.7881619930267334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.9603798389434814})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7856, 'crossentropy': 1.32607978515625}
store['active_learning_steps'][10]['acquisition']={'indices': [46180, 50637, 26235, 2945, 49631], 'labels': [-1, 0, 4, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3467236757278442})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.656575322151184})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.7180142402648926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.8478634357452393})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7883, 'crossentropy': 1.141194921875}
store['active_learning_steps'][11]['acquisition']={'indices': [8526, 20449, 6384, 6566, 5509], 'labels': [6, -1, 1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.3204431533813477})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.511056661605835})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6546618938446045})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.6285165548324585})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.79, 'crossentropy': 1.117493359375}
store['active_learning_steps'][12]['acquisition']={'indices': [17583, 26014, 51288, 38388, 3642], 'labels': [5, 3, 4, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1781256198883057})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5583643913269043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.5166780948638916})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.6596357822418213})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8118, 'crossentropy': 1.072708984375}
store['active_learning_steps'][13]['acquisition']={'indices': [16409, 24549, 30248, 43040, 23485], 'labels': [9, 9, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.424662470817566})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.5606935024261475})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.8047322034835815})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.838343620300293})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7991, 'crossentropy': 1.1993478515625}
store['active_learning_steps'][14]['acquisition']={'indices': [42077, 47552, 34790, 57996, 1154], 'labels': [7, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3078269958496094})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5026116371154785})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5724260807037354})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.7442452907562256})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7908, 'crossentropy': 1.088777734375}
store['active_learning_steps'][15]['acquisition']={'indices': [19159, 23336, 59774, 42614, 39877], 'labels': [8, -1, 7, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.138305902481079})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.417571783065796})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5473889112472534})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4527697563171387})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8204, 'crossentropy': 0.998453125}
store['active_learning_steps'][16]['acquisition']={'indices': [38140, 53958, 6826, 59901, 10516], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1031097173690796})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3897935152053833})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6141599416732788})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7034103870391846})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8168, 'crossentropy': 1.0089861328125}
store['active_learning_steps'][17]['acquisition']={'indices': [45322, 1875, 4635, 26337, 1833], 'labels': [9, 9, 6, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1199662685394287})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.4712848663330078})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.429335594177246})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.5826497077941895})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.824, 'crossentropy': 0.98124169921875}
store['active_learning_steps'][18]['acquisition']={'indices': [16038, 51989, 10352, 57560, 15606], 'labels': [-1, 5, 0, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1110422611236572})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4484314918518066})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4761521816253662})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.7224838733673096})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8226, 'crossentropy': 0.9922509765625}
store['active_learning_steps'][19]['acquisition']={'indices': [27933, 45676, 39036, 8168, 11260], 'labels': [1, -1, 6, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0446163415908813})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3020899295806885})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3185031414031982})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.610196828842163})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8329, 'crossentropy': 0.93694501953125}
store['active_learning_steps'][20]['acquisition']={'indices': [36096, 43203, 28911, 38338, 16019], 'labels': [8, -1, 9, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.000015139579773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0919768810272217})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3272275924682617})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.44809091091156})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.834, 'crossentropy': 0.88739267578125}
store['active_learning_steps'][21]['acquisition']={'indices': [50070, 56355, 8541, 12739, 1020], 'labels': [-1, 2, 3, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0459587574005127})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1738402843475342})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1251847743988037})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2117841243743896})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8314, 'crossentropy': 0.878268359375}
store['active_learning_steps'][22]['acquisition']={'indices': [21330, 58494, 42915, 101, 47278], 'labels': [-1, -1, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.056839942932129})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9901238679885864})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1666386127471924})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2356030941009521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.335223913192749})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.89656181640625}
store['active_learning_steps'][23]['acquisition']={'indices': [43105, 1451, 35129, 667, 38130], 'labels': [2, 7, 8, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0365599393844604})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0998780727386475})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.245696783065796})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5236036777496338})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8188, 'crossentropy': 0.88930517578125}
store['active_learning_steps'][24]['acquisition']={'indices': [3922, 11989, 16147, 38683, 22874], 'labels': [5, 8, 9, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8713816404342651})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0619473457336426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1603293418884277})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1235015392303467})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8624, 'crossentropy': 0.787088671875}
store['active_learning_steps'][25]['acquisition']={'indices': [38936, 53581, 36444, 20537, 17928], 'labels': [6, 6, 6, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8846317529678345})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9315709471702576})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0504286289215088})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1982625722885132})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8527, 'crossentropy': 0.80099501953125}
store['active_learning_steps'][26]['acquisition']={'indices': [54309, 29846, 41221, 55240, 24777], 'labels': [4, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8709455132484436})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1041569709777832})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2018940448760986})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.210331678390503})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8588, 'crossentropy': 0.78142578125}
store['active_learning_steps'][27]['acquisition']={'indices': [47266, 52863, 44302, 35166, 1704], 'labels': [7, -1, 2, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9444311261177063})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0051898956298828})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0695736408233643})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1078405380249023})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8563, 'crossentropy': 0.8264671875}
store['active_learning_steps'][28]['acquisition']={'indices': [49097, 12956, 53450, 35412, 5249], 'labels': [0, 7, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8995779752731323})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.943223237991333})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9794360399246216})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1127814054489136})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.746195556640625}
store['active_learning_steps'][29]['acquisition']={'indices': [41719, 4976, 14974, 35478, 4416], 'labels': [5, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8790782690048218})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9992296695709229})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0671721696853638})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.206020712852478})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.844, 'crossentropy': 0.764231103515625}
store['active_learning_steps'][30]['acquisition']={'indices': [16883, 54442, 4158, 2214, 54094], 'labels': [8, 5, 9, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8405846357345581})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9033581614494324})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0319151878356934})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9299405813217163})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8501, 'crossentropy': 0.7554484375}
store['active_learning_steps'][31]['acquisition']={'indices': [34976, 35483, 33402, 644, 15012], 'labels': [2, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8682379722595215})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8954919576644897})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0149338245391846})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9308694005012512})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8581, 'crossentropy': 0.777304248046875}
store['active_learning_steps'][32]['acquisition']={'indices': [36782, 29299, 38974, 7435, 24214], 'labels': [9, 8, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8483270406723022})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0025737285614014})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0522639751434326})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0175635814666748})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8484, 'crossentropy': 0.759471533203125}
store['active_learning_steps'][33]['acquisition']={'indices': [57893, 20269, 50669, 1600, 29773], 'labels': [-1, 8, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8033772706985474})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7597395777702332})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9504495859146118})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.054656982421875})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.104689121246338})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8971, 'crossentropy': 0.669790771484375}
store['active_learning_steps'][34]['acquisition']={'indices': [21899, 12319, 9793, 5435, 20623], 'labels': [-1, 6, 7, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8456679582595825})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8505809307098389})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9175052642822266})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0439566373825073})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8484, 'crossentropy': 0.76102158203125}
store['active_learning_steps'][35]['acquisition']={'indices': [15229, 48288, 46553, 23374, 35013], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7604718208312988})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8240371346473694})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.947543740272522})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0160057544708252})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8617, 'crossentropy': 0.721449365234375}
store['active_learning_steps'][36]['acquisition']={'indices': [52471, 53750, 52502, 57355, 38185], 'labels': [7, -1, 6, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9156560897827148})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.998751163482666})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.020854115486145})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.075972080230713})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.838, 'crossentropy': 0.83481630859375}
store['active_learning_steps'][37]['acquisition']={'indices': [39244, 13485, 19262, 24802, 39860], 'labels': [-1, 8, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7924070954322815})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8004618883132935})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8827068209648132})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9011936783790588})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8681, 'crossentropy': 0.71874072265625}
store['active_learning_steps'][38]['acquisition']={'indices': [36981, 49407, 18094, 49245, 7327], 'labels': [-1, 8, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8425840139389038})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9485461711883545})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8613101243972778})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0537384748458862})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8632, 'crossentropy': 0.77972138671875}
store['active_learning_steps'][39]['acquisition']={'indices': [2932, 11076, 6432, 3909, 23431], 'labels': [-1, 7, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7583528757095337})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9043281078338623})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8853132724761963})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8968790769577026})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8393, 'crossentropy': 0.745822705078125}
store['active_learning_steps'][40]['acquisition']={'indices': [28039, 37894, 36220, 45640, 3806], 'labels': [6, 5, 6, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8217425346374512})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8647360801696777})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9577387571334839})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9680050015449524})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8527, 'crossentropy': 0.76361884765625}
store['active_learning_steps'][41]['acquisition']={'indices': [8916, 4242, 53840, 7338, 51715], 'labels': [1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8115799427032471})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8073303699493408})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.904096245765686})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.986356258392334})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0148868560791016})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.74993857421875}
store['active_learning_steps'][42]['acquisition']={'indices': [15076, 53272, 53472, 37049, 30271], 'labels': [3, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8198819756507874})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8444143533706665})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0046806335449219})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.872635006904602})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8621, 'crossentropy': 0.78863740234375}
store['active_learning_steps'][43]['acquisition']={'indices': [33508, 13470, 20469, 27574, 48927], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8639984130859375})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8433887958526611})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9186587929725647})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0809659957885742})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.040912389755249})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8854, 'crossentropy': 0.680523291015625}
store['active_learning_steps'][44]['acquisition']={'indices': [16993, 51465, 57928, 46591, 21252], 'labels': [5, -1, 2, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8655142784118652})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.940436601638794})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0757615566253662})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0281848907470703})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8435, 'crossentropy': 0.80331484375}
store['active_learning_steps'][45]['acquisition']={'indices': [35255, 25340, 44549, 42468, 24957], 'labels': [-1, 6, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9085679054260254})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8039830923080444})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8873586058616638})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9498714208602905})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0444321632385254})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8744, 'crossentropy': 0.7109216796875}
store['active_learning_steps'][46]['acquisition']={'indices': [29051, 57231, 5685, 17874, 31102], 'labels': [-1, 5, 5, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9017713069915771})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0506818294525146})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9413354992866516})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9743691682815552})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 0.773728173828125}
store['active_learning_steps'][47]['acquisition']={'indices': [44641, 20559, 49073, 7634, 59013], 'labels': [9, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8723157644271851})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9093711376190186})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8967260122299194})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9895585775375366})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8554, 'crossentropy': 0.76665556640625}
store['active_learning_steps'][48]['acquisition']={'indices': [7259, 25082, 32783, 54599, 22239], 'labels': [2, -1, 6, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.752555251121521})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8176835775375366})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9169023633003235})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9551047682762146})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8512, 'crossentropy': 0.71569091796875}
store['active_learning_steps'][49]['acquisition']={'indices': [3931, 31636, 16509, 41757, 27565], 'labels': [8, -1, 1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7509068250656128})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.838250994682312})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9165205955505371})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1635723114013672})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8716, 'crossentropy': 0.703670654296875}
store['active_learning_steps'][50]['acquisition']={'indices': [14257, 33328, 27333, 51612, 7060], 'labels': [-1, 6, 3, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7620826959609985})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8092778921127319})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8855063915252686})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8483802080154419})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8535, 'crossentropy': 0.703325}
store['active_learning_steps'][51]['acquisition']={'indices': [29896, 33206, 21799, 19443, 37368], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8767520189285278})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7598164677619934})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0139915943145752})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9965166449546814})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0666840076446533})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.698291845703125}
store['active_learning_steps'][52]['acquisition']={'indices': [27322, 28446, 55346, 36121, 34244], 'labels': [0, 9, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7934912443161011})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9385602474212646})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9195225238800049})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.074215054512024})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8514, 'crossentropy': 0.760457373046875}
store['active_learning_steps'][53]['acquisition']={'indices': [11911, 10084, 43140, 16679, 53645], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8105261325836182})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8128396272659302})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8822841048240662})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0031180381774902})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.715366015625}
store['active_learning_steps'][54]['acquisition']={'indices': [16989, 31796, 57332, 19883, 15974], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8802653551101685})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8917652368545532})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8706451654434204})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8733570575714111})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0070734024047852})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0316174030303955})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8944, 'crossentropy': 0.718861474609375}
store['active_learning_steps'][55]['acquisition']={'indices': [7879, 51402, 10887, 3918, 19684], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7935986518859863})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8990601301193237})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8951503038406372})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9526811838150024})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8632, 'crossentropy': 0.749545751953125}
store['active_learning_steps'][56]['acquisition']={'indices': [37831, 35787, 21195, 52786, 46947], 'labels': [6, 5, 6, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8545127511024475})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8262268304824829})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8521952629089355})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0471420288085938})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9548466205596924})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8876, 'crossentropy': 0.711724169921875}
store['active_learning_steps'][57]['acquisition']={'indices': [13773, 5369, 11145, 56973, 57655], 'labels': [-1, -1, 4, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8486083149909973})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7862999439239502})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9599722623825073})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0301305055618286})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9515035152435303})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8896, 'crossentropy': 0.686930126953125}
store['active_learning_steps'][58]['acquisition']={'indices': [19957, 12602, 40458, 49496, 30150], 'labels': [-1, 3, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7951162457466125})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.856398344039917})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8505245447158813})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9672588109970093})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8391, 'crossentropy': 0.74041328125}
store['active_learning_steps'][59]['acquisition']={'indices': [48148, 50735, 27842, 22172, 17883], 'labels': [-1, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7297943234443665})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7722911834716797})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9310230016708374})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.935686469078064})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8848, 'crossentropy': 0.648202734375}
store['active_learning_steps'][60]['acquisition']={'indices': [3202, 40045, 22679, 28826, 35823], 'labels': [-1, 1, 5, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8935012817382812})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.859430193901062})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0612021684646606})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9297125935554504})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.021569013595581})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8867, 'crossentropy': 0.69700458984375}
store['active_learning_steps'][61]['acquisition']={'indices': [8783, 28490, 31087, 16557, 48360], 'labels': [7, 8, -1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7958916425704956})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9662752151489258})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8949710130691528})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8378059267997742})
store['active_learning_steps'][62]['training']['best_epoch']=1
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8679, 'crossentropy': 0.721432275390625}
store['active_learning_steps'][62]['acquisition']={'indices': [31778, 47837, 43839, 31963, 54718], 'labels': [0, 1, 6, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8040534257888794})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7753711938858032})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.798647403717041})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8991165161132812})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8606941103935242})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8831, 'crossentropy': 0.6764900390625}
store['active_learning_steps'][63]['acquisition']={'indices': [12701, 17432, 2245, 20089, 2787], 'labels': [-1, 2, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7563568353652954})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7734766602516174})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9062780141830444})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.923619270324707})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8696, 'crossentropy': 0.6798615234375}
store['active_learning_steps'][64]['acquisition']={'indices': [58676, 39533, 6968, 55077, 17231], 'labels': [7, -1, -1, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.808287501335144})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7986920475959778})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7931729555130005})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8002812266349792})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8518248796463013})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9363075494766235})
store['active_learning_steps'][65]['training']['best_epoch']=3
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.659411865234375}
store['active_learning_steps'][65]['acquisition']={'indices': [29322, 41904, 32187, 58693, 9109], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7866727113723755})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8092800378799438})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8093465566635132})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.787173867225647})
store['active_learning_steps'][66]['training']['best_epoch']=1
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8748, 'crossentropy': 0.680991455078125}
store['active_learning_steps'][66]['acquisition']={'indices': [38462, 16085, 43290, 57185, 53386], 'labels': [1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8114719390869141})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8100988864898682})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8500824570655823})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8286906480789185})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.920872688293457})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.67462099609375}
store['active_learning_steps'][67]['acquisition']={'indices': [52007, 34869, 16989, 36503, 4522], 'labels': [4, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7591719627380371})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7961906790733337})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8380781412124634})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.895957350730896})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8744, 'crossentropy': 0.669511669921875}
store['active_learning_steps'][68]['acquisition']={'indices': [59566, 51230, 25032, 26079, 14183], 'labels': [9, 3, -1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7330564856529236})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7044179439544678})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8532389998435974})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8392287492752075})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8998500108718872})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.60382021484375}
store['active_learning_steps'][69]['acquisition']={'indices': [51531, 53385, 35143, 53996, 32545], 'labels': [-1, 3, 3, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6989973783493042})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.756348729133606})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7871318459510803})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8428299427032471})
store['active_learning_steps'][70]['training']['best_epoch']=1
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8805, 'crossentropy': 0.64695234375}
store['active_learning_steps'][70]['acquisition']={'indices': [36376, 19567, 27203, 54146, 54821], 'labels': [-1, 9, 7, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7601990699768066})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7432833313941956})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7256385087966919})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9078131318092346})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8392808437347412})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.902704119682312})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.62253955078125}
store['active_learning_steps'][71]['acquisition']={'indices': [24468, 42098, 13278, 34187, 10826], 'labels': [9, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7397811412811279})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7022961378097534})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7532014846801758})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8227442502975464})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7681267261505127})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9072, 'crossentropy': 0.58097119140625}
store['active_learning_steps'][72]['acquisition']={'indices': [22961, 6322, 35675, 30898, 17693], 'labels': [9, 8, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7509480714797974})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8072429895401001})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8558732271194458})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8454543352127075})
store['active_learning_steps'][73]['training']['best_epoch']=1
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8596, 'crossentropy': 0.708891943359375}
store['active_learning_steps'][73]['acquisition']={'indices': [59763, 16660, 5569, 41389, 48396], 'labels': [-1, -1, 7, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8181450366973877})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7849723100662231})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7531934976577759})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8482513427734375})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8672678470611572})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8170871734619141})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.623268505859375}
store['active_learning_steps'][74]['acquisition']={'indices': [18973, 58410, 9867, 3462, 19412], 'labels': [-1, 3, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7492172718048096})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.772499680519104})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7653411626815796})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8295888900756836})
store['active_learning_steps'][75]['training']['best_epoch']=1
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.883, 'crossentropy': 0.662591064453125}
store['active_learning_steps'][75]['acquisition']={'indices': [25651, 9681, 12817, 10487, 37256], 'labels': [1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8367992043495178})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8261220455169678})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7984035015106201})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9864884614944458})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.91684490442276})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.903031051158905})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.649049072265625}
store['active_learning_steps'][76]['acquisition']={'indices': [40966, 8760, 28837, 34642, 58407], 'labels': [5, 1, 1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7182602286338806})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7056041955947876})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6988393068313599})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8987631797790527})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8362285494804382})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8533129692077637})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.56021142578125}
store['active_learning_steps'][77]['acquisition']={'indices': [51601, 53785, 51702, 23132, 1628], 'labels': [8, -1, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6855565309524536})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6882278919219971})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6955468058586121})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6942195296287537})
store['active_learning_steps'][78]['training']['best_epoch']=1
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.652555126953125}
store['active_learning_steps'][78]['acquisition']={'indices': [15359, 55875, 33819, 16398, 58123], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7546390295028687})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7470242977142334})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8824986219406128})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8477884531021118})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8803331851959229})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.5863}
store['active_learning_steps'][79]['acquisition']={'indices': [27661, 4377, 3906, 50229, 50694], 'labels': [9, 9, 0, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7768306136131287})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6632370948791504})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8107055425643921})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8611534237861633})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8338010311126709})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.575382421875}
store['active_learning_steps'][80]['acquisition']={'indices': [2680, 9095, 24771, 49262, 16226], 'labels': [-1, -1, 1, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.761714518070221})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.744605541229248})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7275238037109375})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8058907985687256})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7767742872238159})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8795442581176758})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.5983787109375}
store['active_learning_steps'][81]['acquisition']={'indices': [26164, 18811, 32241, 10811, 6383], 'labels': [-1, 8, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7048325538635254})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7124841213226318})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7996060848236084})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8192778825759888})
store['active_learning_steps'][82]['training']['best_epoch']=1
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.888, 'crossentropy': 0.638781640625}
store['active_learning_steps'][82]['acquisition']={'indices': [10295, 25601, 23049, 52774, 23949], 'labels': [7, -1, 6, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7715709805488586})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7375022172927856})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8285566568374634})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8958479762077332})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7710827589035034})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8925, 'crossentropy': 0.62475087890625}
store['active_learning_steps'][83]['acquisition']={'indices': [52481, 43118, 24417, 20923, 32675], 'labels': [-1, -1, 3, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7480297684669495})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7188695669174194})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7361981868743896})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7696433663368225})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8489522337913513})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.5952927734375}
store['active_learning_steps'][84]['acquisition']={'indices': [12889, 19611, 58250, 26708, 4274], 'labels': [-1, 7, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7603278160095215})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7442377805709839})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7502727508544922})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7634084224700928})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8133156299591064})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.589809130859375}
store['active_learning_steps'][85]['acquisition']={'indices': [42605, 59453, 16622, 51660, 9792], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7492160797119141})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7352719306945801})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7113382816314697})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8105748891830444})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8846461772918701})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8611223697662354})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.56227890625}
store['active_learning_steps'][86]['acquisition']={'indices': [5399, 15539, 30054, 4946, 16619], 'labels': [-1, 1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7898011207580566})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7043639421463013})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7392534613609314})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.807552695274353})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8056856393814087})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.5939669921875}
store['active_learning_steps'][87]['acquisition']={'indices': [38357, 49042, 13237, 39584, 6896], 'labels': [1, -1, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7714924812316895})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6798620820045471})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7227067947387695})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7630561590194702})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7888885140419006})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.5693390625}
store['active_learning_steps'][88]['acquisition']={'indices': [6115, 21470, 3539, 50364, 10476], 'labels': [-1, 2, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8166650533676147})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8191269636154175})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7234474420547485})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8137285113334656})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8044546842575073})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9847583770751953})
store['active_learning_steps'][89]['training']['best_epoch']=3
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.567068115234375}
store['active_learning_steps'][89]['acquisition']={'indices': [59490, 25062, 24915, 5257, 44312], 'labels': [3, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7610516548156738})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7175637483596802})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7344920635223389})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7401332855224609})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7483329772949219})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.568497900390625}
store['active_learning_steps'][90]['acquisition']={'indices': [55991, 33758, 31021, 13392, 23084], 'labels': [0, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8727768659591675})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7796577215194702})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6522101163864136})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7613130807876587})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8067485094070435})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7331548929214478})
store['active_learning_steps'][91]['training']['best_epoch']=3
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.561153564453125}
store['active_learning_steps'][91]['acquisition']={'indices': [4253, 43700, 7455, 6294, 58836], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7431962490081787})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7250505685806274})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7761303782463074})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8821111917495728})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8090677857398987})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.57087490234375}
store['active_learning_steps'][92]['acquisition']={'indices': [48468, 44848, 26036, 21684, 27337], 'labels': [-1, 3, 8, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8231860399246216})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6622982621192932})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.669927179813385})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7028339505195618})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8695859909057617})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.56384619140625}
store['active_learning_steps'][93]['acquisition']={'indices': [32960, 17545, 9490, 25373, 18779], 'labels': [-1, 8, 8, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7002037763595581})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6445254683494568})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7818753123283386})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7088313102722168})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8129212856292725})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.52408310546875}
store['active_learning_steps'][94]['acquisition']={'indices': [28352, 45931, 5471, 28115, 2942], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.781866192817688})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6820244193077087})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7442642450332642})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6787402629852295})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7679914832115173})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8397339582443237})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8276941180229187})
store['active_learning_steps'][95]['training']['best_epoch']=4
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.5857833984375}
store['active_learning_steps'][95]['acquisition']={'indices': [47930, 17344, 16903, 15331, 44207], 'labels': [3, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7880239486694336})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6810699701309204})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7347971200942993})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7351276278495789})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.836867094039917})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.596799755859375}
store['active_learning_steps'][96]['acquisition']={'indices': [10138, 3082, 14320, 50920, 2556], 'labels': [2, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7911087274551392})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6809637546539307})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7149077653884888})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.752595067024231})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8207315802574158})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.56067060546875}
store['active_learning_steps'][97]['acquisition']={'indices': [8538, 12077, 1831, 56942, 31549], 'labels': [1, 4, 1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.752007007598877})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7507706880569458})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7375198602676392})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7406901121139526})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7756912708282471})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7323094606399536})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8861939907073975})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8727378845214844})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9892183542251587})
store['active_learning_steps'][98]['training']['best_epoch']=6
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.61257607421875}
store['active_learning_steps'][98]['acquisition']={'indices': [21881, 1810, 23992, 28162, 52409], 'labels': [2, 5, -1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7049954533576965})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7096346616744995})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.731606125831604})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7446407675743103})
store['active_learning_steps'][99]['training']['best_epoch']=1
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.8721, 'crossentropy': 0.669368896484375}
store['active_learning_steps'][99]['acquisition']={'indices': [13962, 17510, 38582, 54180, 46354], 'labels': [-1, 6, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7072387933731079})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6489427089691162})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5727336406707764})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6953654289245605})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7060258388519287})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6958214044570923})
store['active_learning_steps'][100]['training']['best_epoch']=3
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.505126123046875}
store['active_learning_steps'][100]['acquisition']={'indices': [6181, 25287, 7571, 59285, 56993], 'labels': [-1, 1, 6, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.747148871421814})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6873711347579956})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7359350323677063})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7547187805175781})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8242212533950806})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.58266083984375}
store['active_learning_steps'][101]['acquisition']={'indices': [19172, 10555, 21991, 19997, 50256], 'labels': [7, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7736066579818726})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6881174445152283})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6996816992759705})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6997007131576538})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7788537740707397})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.58657490234375}
store['active_learning_steps'][102]['acquisition']={'indices': [39603, 17257, 21720, 41356, 34106], 'labels': [1, 3, -1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7298930883407593})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6173728704452515})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6885042190551758})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7642422914505005})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7312908172607422})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.55181083984375}
store['active_learning_steps'][103]['acquisition']={'indices': [23299, 19317, 46319, 30726, 13292], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.667339563369751})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6378037929534912})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7015784978866577})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7249365448951721})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7653573155403137})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9081, 'crossentropy': 0.53444892578125}
store['active_learning_steps'][104]['acquisition']={'indices': [18393, 1486, 55118, 16994, 59390], 'labels': [1, 3, 8, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7687863111495972})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.628478467464447})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6906824111938477})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6821531057357788})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7469251751899719})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.53696708984375}
store['active_learning_steps'][105]['acquisition']={'indices': [971, 29383, 53972, 18079, 27618], 'labels': [-1, 3, -1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6996618509292603})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6894953846931458})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6572908163070679})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6731787919998169})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7418999075889587})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7125037908554077})
store['active_learning_steps'][106]['training']['best_epoch']=3
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.548495703125}
store['active_learning_steps'][106]['acquisition']={'indices': [35406, 56722, 51454, 32611, 57207], 'labels': [5, 7, 4, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7251072525978088})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.567513108253479})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5994679927825928})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5617669224739075})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5969012379646301})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6736922264099121})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7311733961105347})
store['active_learning_steps'][107]['training']['best_epoch']=4
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.51986201171875}
store['active_learning_steps'][107]['acquisition']={'indices': [55044, 45837, 10736, 37836, 20102], 'labels': [2, 0, -1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7338959574699402})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6496942043304443})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.643971860408783})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6410850286483765})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6933214664459229})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7259100675582886})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7309598326683044})
store['active_learning_steps'][108]['training']['best_epoch']=4
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.5459216796875}
store['active_learning_steps'][108]['acquisition']={'indices': [34686, 55171, 40603, 40979, 15721], 'labels': [6, -1, -1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6736072897911072})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5641734600067139})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6415631771087646})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6317298412322998})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7003112435340881})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.508880810546875}
store['active_learning_steps'][109]['acquisition']={'indices': [15892, 31144, 20660, 54995, 10284], 'labels': [-1, -1, -1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8106565475463867})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6661555767059326})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7309318780899048})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6825923919677734})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7445687651634216})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.545182568359375}
store['active_learning_steps'][110]['acquisition']={'indices': [13749, 59497, 3805, 56350, 3156], 'labels': [-1, -1, 7, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7068765759468079})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6038827300071716})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6533493995666504})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7108204364776611})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7181576490402222})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.534839404296875}
store['active_learning_steps'][111]['acquisition']={'indices': [58421, 26898, 20393, 28014, 19038], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7245846390724182})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.63956618309021})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6686281561851501})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7155483365058899})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6658836603164673})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.538420654296875}
store['active_learning_steps'][112]['acquisition']={'indices': [794, 15854, 34807, 56593, 30115], 'labels': [6, -1, 7, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7035087943077087})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.655346155166626})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6739729046821594})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7042760848999023})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7666451930999756})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.551596044921875}
store['active_learning_steps'][113]['acquisition']={'indices': [21439, 47259, 25132, 23514, 51358], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7773263454437256})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6554277539253235})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6633800268173218})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7315647602081299})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7025562524795532})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.54563369140625}
store['active_learning_steps'][114]['acquisition']={'indices': [27926, 24139, 29998, 53630, 34668], 'labels': [9, -1, 7, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7425634860992432})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7474185824394226})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6618189811706543})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6861091256141663})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.710265040397644})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8452720642089844})
store['active_learning_steps'][115]['training']['best_epoch']=3
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.54417431640625}
store['active_learning_steps'][115]['acquisition']={'indices': [53099, 26468, 8749, 34824, 33919], 'labels': [8, -1, -1, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7862535119056702})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6988418102264404})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6108924150466919})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6686820387840271})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7515419125556946})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7307480573654175})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.524684326171875}
store['active_learning_steps'][116]['acquisition']={'indices': [39194, 35828, 41015, 52982, 54647], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7059213519096375})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7513760328292847})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6132992506027222})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6520934104919434})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7580824494361877})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7472103834152222})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9205, 'crossentropy': 0.54324677734375}
store['active_learning_steps'][117]['acquisition']={'indices': [9568, 13525, 54201, 1569, 21933], 'labels': [-1, 2, 3, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7804741859436035})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.662981390953064})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6369965076446533})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6801556348800659})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6888594627380371})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7108310461044312})
store['active_learning_steps'][118]['training']['best_epoch']=3
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.51685009765625}
store['active_learning_steps'][118]['acquisition']={'indices': [8455, 28314, 57320, 28761, 52245], 'labels': [3, 7, 5, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7238044738769531})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6728686094284058})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6494903564453125})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6638213396072388})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.688025176525116})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7201611399650574})
store['active_learning_steps'][119]['training']['best_epoch']=3
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.542822412109375}
store['active_learning_steps'][119]['acquisition']={'indices': [24583, 14694, 54433, 57201, 3915], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7239211797714233})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6279599070549011})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6554972529411316})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7096476554870605})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6786248683929443})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.51493740234375}
store['active_learning_steps'][120]['acquisition']={'indices': [55444, 35360, 39940, 34867, 1700], 'labels': [7, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7260302305221558})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7245869636535645})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6785604953765869})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7199710607528687})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7668040990829468})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7716565132141113})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.563925146484375}
store['active_learning_steps'][121]['acquisition']={'indices': [52235, 30771, 32332, 34608, 24038], 'labels': [7, -1, 1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6611498594284058})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6121624708175659})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6915106773376465})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6194687485694885})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8179135322570801})
store['active_learning_steps'][122]['training']['best_epoch']=2
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.52271396484375}
store['active_learning_steps'][122]['acquisition']={'indices': [19570, 12893, 55874, 2798, 49670], 'labels': [8, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7663074731826782})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6158329248428345})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6137336492538452})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6936826109886169})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6968123316764832})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6624040603637695})
store['active_learning_steps'][123]['training']['best_epoch']=3
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.510453759765625}
store['active_learning_steps'][123]['acquisition']={'indices': [36599, 58058, 51257, 20170, 32823], 'labels': [-1, -1, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6793621778488159})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6038812398910522})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7330251932144165})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.634526252746582})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6916000843048096})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.521168896484375}
store['active_learning_steps'][124]['acquisition']={'indices': [41860, 28331, 59664, 22434, 23595], 'labels': [2, 1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7134991884231567})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6150140762329102})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6161940097808838})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7065927982330322})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6686828136444092})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.543627685546875}
store['active_learning_steps'][125]['acquisition']={'indices': [55777, 26311, 28287, 45139, 41356], 'labels': [6, 3, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7316399216651917})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6231766939163208})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.609389066696167})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6719962954521179})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.70469069480896})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6863113045692444})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.5143423828125}
store['active_learning_steps'][126]['acquisition']={'indices': [7771, 57755, 47415, 13319, 12854], 'labels': [-1, 2, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7867261171340942})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6189954280853271})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5914908647537231})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.62010657787323})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6138323545455933})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6777195930480957})
store['active_learning_steps'][127]['training']['best_epoch']=3
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.479737158203125}
store['active_learning_steps'][127]['acquisition']={'indices': [33941, 47282, 19667, 14674, 29696], 'labels': [-1, 4, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7808603644371033})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5808970928192139})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6784220933914185})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6274194717407227})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5576436519622803})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6833769083023071})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7009285688400269})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6987794041633606})
store['active_learning_steps'][128]['training']['best_epoch']=5
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9261, 'crossentropy': 0.498538037109375}
store['active_learning_steps'][128]['acquisition']={'indices': [47246, 10381, 38699, 22296, 20581], 'labels': [2, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7929048538208008})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5904097557067871})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6297916769981384})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5479120016098022})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5986418128013611})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7058137059211731})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6474772095680237})
store['active_learning_steps'][129]['training']['best_epoch']=4
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.48651083984375}
store['active_learning_steps'][129]['acquisition']={'indices': [47031, 33480, 38252, 19890, 5447], 'labels': [0, 1, -1, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6782768964767456})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6024396419525146})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5854966640472412})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6122877597808838})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6727016568183899})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6769425272941589})
store['active_learning_steps'][130]['training']['best_epoch']=3
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.492892041015625}
store['active_learning_steps'][130]['acquisition']={'indices': [5547, 29645, 52311, 33211, 34351], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.695048451423645})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5996425747871399})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6099720001220703})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6413146257400513})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6320250630378723})
store['active_learning_steps'][131]['training']['best_epoch']=2
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.5309041015625}
store['active_learning_steps'][131]['acquisition']={'indices': [12591, 8823, 18542, 8048, 720], 'labels': [-1, 1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7419506311416626})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5604137182235718})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5994716882705688})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6760640740394592})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5992621183395386})
store['active_learning_steps'][132]['training']['best_epoch']=2
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.486200048828125}
store['active_learning_steps'][132]['acquisition']={'indices': [45439, 45581, 48694, 47572, 8955], 'labels': [2, 6, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6886541843414307})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6839948892593384})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6334588527679443})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5652201175689697})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6727471351623535})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7209863662719727})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6767110824584961})
store['active_learning_steps'][133]['training']['best_epoch']=4
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.486239501953125}
store['active_learning_steps'][133]['acquisition']={'indices': [12658, 13102, 23993, 6076, 50059], 'labels': [8, -1, 1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7502923011779785})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6438738107681274})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6028909087181091})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6884065866470337})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6441556215286255})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6142146587371826})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.5089845703125}
store['active_learning_steps'][134]['acquisition']={'indices': [50474, 24236, 20569, 5984, 41631], 'labels': [-1, 7, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7340443730354309})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5530911087989807})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5777119994163513})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5855851173400879})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.613709568977356})
store['active_learning_steps'][135]['training']['best_epoch']=2
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.47426533203125}
store['active_learning_steps'][135]['acquisition']={'indices': [46432, 21122, 49153, 46483, 17171], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6697155237197876})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6304585933685303})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.608483076095581})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6200910806655884})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6059027910232544})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7095769643783569})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6609959602355957})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.806425929069519})
store['active_learning_steps'][136]['training']['best_epoch']=5
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.473891796875}
store['active_learning_steps'][136]['acquisition']={'indices': [5664, 32488, 58418, 17981, 5861], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7497043609619141})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5804603695869446})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5950878262519836})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6564285755157471})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6120220422744751})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.506361767578125}
store['active_learning_steps'][137]['acquisition']={'indices': [41700, 31302, 14173, 12734, 7690], 'labels': [-1, -1, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6604890823364258})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5996665954589844})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5490976572036743})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6012503504753113})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6384179592132568})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5970152616500854})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.483208349609375}
store['active_learning_steps'][138]['acquisition']={'indices': [43384, 30272, 32512, 1799, 13609], 'labels': [-1, 4, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7015990018844604})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5987395644187927})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6157896518707275})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6291091442108154})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6229974627494812})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.48195673828125}
store['active_learning_steps'][139]['acquisition']={'indices': [19100, 24736, 35668, 18499, 13873], 'labels': [-1, 9, 7, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7689558863639832})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6062228083610535})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.61253821849823})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6801190972328186})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6320328712463379})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.490646484375}
store['active_learning_steps'][140]['acquisition']={'indices': [3315, 51554, 36703, 8913, 7708], 'labels': [4, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7108293175697327})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5907204747200012})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.580134391784668})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6397650241851807})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6310257911682129})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.680443286895752})
store['active_learning_steps'][141]['training']['best_epoch']=3
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.47234375}
store['active_learning_steps'][141]['acquisition']={'indices': [12934, 30023, 17625, 9314, 27914], 'labels': [8, -1, 0, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6727901697158813})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.547877848148346})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5775023698806763})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5459936261177063})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6050904989242554})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5958386659622192})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6259090304374695})
store['active_learning_steps'][142]['training']['best_epoch']=4
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.48944501953125}
store['active_learning_steps'][142]['acquisition']={'indices': [31215, 16102, 53733, 51420, 37014], 'labels': [9, 6, 2, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.721405029296875})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5916893482208252})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5499582290649414})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.544519305229187})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5787981748580933})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6181537508964539})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5824561715126038})
store['active_learning_steps'][143]['training']['best_epoch']=4
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.4794775390625}
store['active_learning_steps'][143]['acquisition']={'indices': [17301, 33722, 49885, 54391, 37006], 'labels': [-1, 3, 5, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7178179025650024})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5948376655578613})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5400792956352234})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5518049597740173})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5578542947769165})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5289723873138428})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5833191871643066})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.647612452507019})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6220141053199768})
store['active_learning_steps'][144]['training']['best_epoch']=6
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.437746875}
store['active_learning_steps'][144]['acquisition']={'indices': [41014, 13404, 25711, 15122, 21386], 'labels': [9, -1, 5, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.703789234161377})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5877727270126343})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5754225850105286})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5650433301925659})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6207706928253174})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6280261874198914})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6135843992233276})
store['active_learning_steps'][145]['training']['best_epoch']=4
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.477051806640625}
store['active_learning_steps'][145]['acquisition']={'indices': [13511, 23718, 43746, 47286, 15193], 'labels': [-1, 2, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6755411624908447})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5395245552062988})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5406343936920166})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5554201602935791})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5888286828994751})
store['active_learning_steps'][146]['training']['best_epoch']=2
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.92, 'crossentropy': 0.483310693359375}
store['active_learning_steps'][146]['acquisition']={'indices': [16977, 24883, 52876, 24767, 25384], 'labels': [4, -1, 4, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7032792568206787})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5104382038116455})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.568422794342041})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.527866005897522})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6308001279830933})
store['active_learning_steps'][147]['training']['best_epoch']=2
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.492014501953125}
store['active_learning_steps'][147]['acquisition']={'indices': [39851, 49203, 43836, 40564, 54508], 'labels': [-1, 5, 1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6647210121154785})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5848894119262695})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5183629989624023})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4990941882133484})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.53116774559021})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5825731754302979})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.667731523513794})
store['active_learning_steps'][148]['training']['best_epoch']=4
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9342, 'crossentropy': 0.442075}
store['active_learning_steps'][148]['acquisition']={'indices': [4715, 9562, 33284, 31291, 45677], 'labels': [-1, 1, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6968781352043152})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5411872863769531})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48214319348335266})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5074905157089233})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.500037670135498})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5355734825134277})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.413913525390625}
store['active_learning_steps'][149]['acquisition']={'indices': [39023, 7001, 30578, 48998, 26087], 'labels': [0, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.675434947013855})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.49549129605293274})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4900702238082886})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.537855863571167})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5646981596946716})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5405797958374023})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.430821337890625}
store['active_learning_steps'][150]['acquisition']={'indices': [12822, 19735, 42971, 34555, 5608], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.687813401222229})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5115564465522766})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.48438307642936707})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5566731095314026})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5525548458099365})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5178318619728088})
store['active_learning_steps'][151]['training']['best_epoch']=3
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.4073400634765625}
store['active_learning_steps'][151]['acquisition']={'indices': [17182, 55850, 22530, 12122, 4414], 'labels': [-1, 9, -1, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6303330659866333})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5265727043151855})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5157483816146851})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5165278315544128})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5043150186538696})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4727577567100525})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6848692893981934})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.516993522644043})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5476957559585571})
store['active_learning_steps'][152]['training']['best_epoch']=6
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.413511572265625}
store['active_learning_steps'][152]['acquisition']={'indices': [14802, 47697, 59580, 18664, 12603], 'labels': [-1, -1, 4, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.751137375831604})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5791710019111633})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5064109563827515})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5681661367416382})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.596044659614563})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5344988107681274})
store['active_learning_steps'][153]['training']['best_epoch']=3
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.44914853515625}
store['active_learning_steps'][153]['acquisition']={'indices': [4978, 13718, 17959, 2348, 50313], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6713985204696655})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5518589615821838})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48216137290000916})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4924132823944092})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5526548624038696})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5710361003875732})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.433001416015625}
store['active_learning_steps'][154]['acquisition']={'indices': [316, 23453, 23363, 13166, 36359], 'labels': [5, -1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6944212317466736})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5526642799377441})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5203744769096375})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49911659955978394})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5154780149459839})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48197948932647705})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5383118391036987})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5623356699943542})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5490348935127258})
store['active_learning_steps'][155]['training']['best_epoch']=6
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.4038004150390625}
store['active_learning_steps'][155]['acquisition']={'indices': [56664, 21334, 21990, 30305, 26357], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.680350661277771})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5171645283699036})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48910340666770935})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4870988726615906})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5073636174201965})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5486415028572083})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5211337208747864})
store['active_learning_steps'][156]['training']['best_epoch']=4
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.415467822265625}
store['active_learning_steps'][156]['acquisition']={'indices': [35672, 20732, 48102, 50711, 16665], 'labels': [-1, 8, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6956189870834351})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5545005798339844})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4708179235458374})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5034049153327942})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5092426538467407})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5109909176826477})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9335, 'crossentropy': 0.39255009765625}
store['active_learning_steps'][157]['acquisition']={'indices': [23887, 56256, 51325, 21021, 6052], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7416167259216309})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5027479529380798})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5105720162391663})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5499283075332642})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5257174968719482})
store['active_learning_steps'][158]['training']['best_epoch']=2
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.435363720703125}
store['active_learning_steps'][158]['acquisition']={'indices': [40514, 7893, 21655, 38416, 57496], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6673682928085327})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5113314390182495})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.537265419960022})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5332046747207642})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6039000749588013})
store['active_learning_steps'][159]['training']['best_epoch']=2
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.463416357421875}
store['active_learning_steps'][159]['acquisition']={'indices': [37589, 40302, 41093, 41786, 40362], 'labels': [5, -1, 4, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.618064284324646})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5028439164161682})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.47004085779190063})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5482834577560425})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5153614282608032})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4839428663253784})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.4057979248046875}
store['active_learning_steps'][160]['acquisition']={'indices': [44773, 17910, 15903, 5091, 25588], 'labels': [-1, 6, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7033573389053345})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4999346137046814})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49576255679130554})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5052399039268494})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5067377090454102})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4955807328224182})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5325738787651062})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5201882123947144})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5151282548904419})
store['active_learning_steps'][161]['training']['best_epoch']=6
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.438905224609375}
store['active_learning_steps'][161]['acquisition']={'indices': [24763, 17792, 46060, 55949, 3014], 'labels': [-1, -1, 5, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6875910758972168})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5378720164299011})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48269224166870117})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5215606689453125})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45075297355651855})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5617763996124268})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5576905608177185})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5461984872817993})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.4039389892578125}
