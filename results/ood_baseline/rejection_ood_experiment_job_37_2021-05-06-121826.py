store = {}
store['timestamp']=1620299906
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=37']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=37
store['worker_id']=37
store['num_workers']=40
store['config']={'seed': 54, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.230677604675293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6202774047851562})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7755603790283203})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4874346256256104})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6887, 'crossentropy': 1.98304765625}
store['active_learning_steps'][0]['acquisition']={'indices': [12226, 45720, 34752, 34540, 22317], 'labels': [-1, 7, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3927178382873535})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.685525417327881})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.732008934020996})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.2488036155700684})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6849, 'crossentropy': 2.1685748046875}
store['active_learning_steps'][1]['acquisition']={'indices': [45397, 50105, 53637, 27861, 39595], 'labels': [-1, -1, -1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.945816993713379})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4736151695251465})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.5559098720550537})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.702362298965454})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7335, 'crossentropy': 1.84929765625}
store['active_learning_steps'][2]['acquisition']={'indices': [15645, 28911, 23273, 44725, 48812], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4948439598083496})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5133135318756104})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2176547050476074})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.9531941413879395})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6626, 'crossentropy': 2.291489453125}
store['active_learning_steps'][3]['acquisition']={'indices': [54954, 53777, 14741, 29115, 17699], 'labels': [8, 6, 7, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.6889541149139404})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9710192680358887})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.090606212615967})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.287480354309082})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7514, 'crossentropy': 1.60662900390625}
store['active_learning_steps'][4]['acquisition']={'indices': [53845, 32331, 24435, 3577, 43581], 'labels': [9, 9, 3, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.4524296522140503})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.7459551095962524})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.8068548440933228})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.7907618284225464})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7722, 'crossentropy': 1.39032451171875}
store['active_learning_steps'][5]['acquisition']={'indices': [40119, 44842, 47761, 20088, 45033], 'labels': [2, -1, 6, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.5412439107894897})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.8867509365081787})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.051321506500244})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.0653042793273926})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7598, 'crossentropy': 1.43590537109375}
store['active_learning_steps'][6]['acquisition']={'indices': [42941, 39998, 54632, 54458, 123], 'labels': [-1, 9, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.738939881324768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9146695137023926})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.234642505645752})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.1214418411254883})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7387, 'crossentropy': 1.56847724609375}
store['active_learning_steps'][7]['acquisition']={'indices': [43028, 6374, 9959, 19205, 12216], 'labels': [9, 5, 3, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.4419628381729126})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7368683815002441})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.945068359375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.166285514831543})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7654, 'crossentropy': 1.39219228515625}
store['active_learning_steps'][8]['acquisition']={'indices': [46249, 42888, 37752, 34526, 32416], 'labels': [-1, 1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.5587202310562134})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.8703778982162476})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.8148857355117798})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.1223254203796387})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.756, 'crossentropy': 1.55679521484375}
store['active_learning_steps'][9]['acquisition']={'indices': [37890, 50713, 15489, 23460, 28204], 'labels': [3, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.6598480939865112})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.0191280841827393})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.2589645385742188})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.2627482414245605})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.763, 'crossentropy': 1.53722314453125}
store['active_learning_steps'][10]['acquisition']={'indices': [46616, 27182, 19123, 54556, 45240], 'labels': [8, -1, 4, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.34451162815094})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.647240400314331})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.8820686340332031})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9380786418914795})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7723, 'crossentropy': 1.33176015625}
store['active_learning_steps'][11]['acquisition']={'indices': [25712, 40891, 42846, 59386, 58449], 'labels': [9, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.5036256313323975})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.6566812992095947})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.7706481218338013})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.0041697025299072})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7543, 'crossentropy': 1.461223046875}
store['active_learning_steps'][12]['acquisition']={'indices': [30847, 42601, 12024, 55531, 43999], 'labels': [1, 1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1578961610794067})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.5084710121154785})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.5741519927978516})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.7600786685943604})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7807, 'crossentropy': 1.18720263671875}
store['active_learning_steps'][13]['acquisition']={'indices': [3586, 12875, 53551, 25630, 35306], 'labels': [-1, 2, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1908077001571655})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.191523551940918})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5346128940582275})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.464825987815857})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7963, 'crossentropy': 1.13103134765625}
store['active_learning_steps'][14]['acquisition']={'indices': [10464, 22432, 13397, 8854, 3279], 'labels': [2, -1, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2039406299591064})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4858074188232422})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.7312393188476562})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6368188858032227})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7881, 'crossentropy': 1.176685546875}
store['active_learning_steps'][15]['acquisition']={'indices': [21418, 37566, 20131, 25962, 16594], 'labels': [6, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3075464963912964})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.4548989534378052})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.5724124908447266})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.649675726890564})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7813, 'crossentropy': 1.21732939453125}
store['active_learning_steps'][16]['acquisition']={'indices': [12866, 6517, 19757, 54989, 58048], 'labels': [6, 6, -1, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2359955310821533})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3689062595367432})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.523837924003601})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.824657678604126})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7772, 'crossentropy': 1.2606560546875}
store['active_learning_steps'][17]['acquisition']={'indices': [30240, 16496, 56982, 56676, 53180], 'labels': [-1, 7, 5, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.2054237127304077})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3625280857086182})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5450842380523682})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.7176623344421387})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7735, 'crossentropy': 1.20033818359375}
store['active_learning_steps'][18]['acquisition']={'indices': [59006, 27602, 45466, 11491, 28317], 'labels': [-1, -1, -1, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.160567045211792})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3410210609436035})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.341578722000122})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.58172607421875})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7992, 'crossentropy': 1.028704296875}
store['active_learning_steps'][19]['acquisition']={'indices': [27812, 4603, 52113, 25051, 53960], 'labels': [6, 2, -1, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0798757076263428})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2887530326843262})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2860597372055054})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.5580027103424072})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7807, 'crossentropy': 1.1117337890625}
store['active_learning_steps'][20]['acquisition']={'indices': [46833, 36606, 51033, 24918, 34776], 'labels': [2, 9, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.20899498462677})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2582976818084717})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4044673442840576})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5218042135238647})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7908, 'crossentropy': 1.1393921875}
store['active_learning_steps'][21]['acquisition']={'indices': [6065, 1331, 38673, 17807, 40406], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1281615495681763})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.4032838344573975})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.543432593345642})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.6156402826309204})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7935, 'crossentropy': 1.0658466796875}
store['active_learning_steps'][22]['acquisition']={'indices': [46675, 10217, 40707, 39655, 49648], 'labels': [5, 8, 6, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.131534218788147})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2660636901855469})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4933016300201416})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6063010692596436})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7976, 'crossentropy': 1.04461591796875}
store['active_learning_steps'][23]['acquisition']={'indices': [36395, 6486, 10261, 38091, 48678], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2224221229553223})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1131917238235474})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3454087972640991})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.264523983001709})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.624035358428955})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8166, 'crossentropy': 1.081359375}
store['active_learning_steps'][24]['acquisition']={'indices': [9821, 51487, 13927, 46481, 49656], 'labels': [4, 8, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0306892395019531})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.121340036392212})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2929425239562988})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2243003845214844})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7998, 'crossentropy': 0.9777177734375}
store['active_learning_steps'][25]['acquisition']={'indices': [32472, 42008, 7596, 56352, 20499], 'labels': [1, -1, 4, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1395050287246704})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2743446826934814})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4375877380371094})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.5914552211761475})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7884, 'crossentropy': 1.1472099609375}
store['active_learning_steps'][26]['acquisition']={'indices': [58053, 22882, 57499, 20752, 33521], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1532490253448486})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3352327346801758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.5654666423797607})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.5049958229064941})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8033, 'crossentropy': 1.04210595703125}
store['active_learning_steps'][27]['acquisition']={'indices': [15422, 41332, 54904, 37634, 3107], 'labels': [7, 1, 5, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0329163074493408})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2852153778076172})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1829423904418945})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.4616634845733643})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8266, 'crossentropy': 0.9644705078125}
store['active_learning_steps'][28]['acquisition']={'indices': [42579, 33042, 21789, 47370, 40877], 'labels': [0, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0141031742095947})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2668070793151855})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2342634201049805})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2850301265716553})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8248, 'crossentropy': 0.9542748046875}
store['active_learning_steps'][29]['acquisition']={'indices': [7985, 22628, 11153, 34931, 29916], 'labels': [0, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2222797870635986})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3015193939208984})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2777907848358154})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3174749612808228})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7868, 'crossentropy': 1.09451015625}
store['active_learning_steps'][30]['acquisition']={'indices': [45950, 48788, 39383, 3763, 6627], 'labels': [4, -1, 6, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1106213331222534})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0646032094955444})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1673901081085205})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2623488903045654})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4571067094802856})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8422, 'crossentropy': 1.04788193359375}
store['active_learning_steps'][31]['acquisition']={'indices': [59876, 7025, 12061, 26826, 59669], 'labels': [6, -1, -1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8948075771331787})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0125377178192139})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.165177345275879})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2559943199157715})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8337, 'crossentropy': 0.8643837890625}
store['active_learning_steps'][32]['acquisition']={'indices': [5840, 35311, 44192, 40684, 9575], 'labels': [-1, -1, 3, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0379680395126343})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.115355372428894})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2003167867660522})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3996272087097168})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8175, 'crossentropy': 0.99092509765625}
store['active_learning_steps'][33]['acquisition']={'indices': [42745, 46716, 54958, 1788, 21865], 'labels': [6, 4, -1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.010401725769043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1432603597640991})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.099644660949707})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.27650785446167})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8311, 'crossentropy': 0.9501517578125}
store['active_learning_steps'][34]['acquisition']={'indices': [3481, 10317, 18699, 30742, 45530], 'labels': [9, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9777442216873169})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0053483247756958})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0992960929870605})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2970638275146484})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8237, 'crossentropy': 0.9040166015625}
store['active_learning_steps'][35]['acquisition']={'indices': [7925, 30207, 34152, 19940, 7826], 'labels': [-1, -1, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9168933629989624})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9990953207015991})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1802951097488403})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1420032978057861})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8459, 'crossentropy': 0.85663583984375}
store['active_learning_steps'][36]['acquisition']={'indices': [23435, 17066, 32300, 16871, 37653], 'labels': [4, 6, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8596112728118896})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0506885051727295})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0352648496627808})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2966063022613525})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8488, 'crossentropy': 0.8209169921875}
store['active_learning_steps'][37]['acquisition']={'indices': [15252, 16861, 51834, 9985, 25350], 'labels': [-1, -1, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0671504735946655})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9536961317062378})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1733505725860596})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2621371746063232})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3540759086608887})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8536, 'crossentropy': 0.93674833984375}
store['active_learning_steps'][38]['acquisition']={'indices': [51780, 39095, 23619, 8707, 33368], 'labels': [-1, -1, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9001671075820923})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1008484363555908})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0756912231445312})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.082483172416687})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8382, 'crossentropy': 0.84333740234375}
store['active_learning_steps'][39]['acquisition']={'indices': [8632, 35422, 31656, 31385, 16130], 'labels': [2, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9252372980117798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9757821559906006})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9818477630615234})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0659501552581787})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8525, 'crossentropy': 0.8113630859375}
store['active_learning_steps'][40]['acquisition']={'indices': [43158, 10646, 4631, 24485, 59316], 'labels': [-1, 9, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9399517774581909})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0575079917907715})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1604747772216797})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.293168306350708})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8379, 'crossentropy': 0.8774876953125}
store['active_learning_steps'][41]['acquisition']={'indices': [25997, 30556, 17700, 7812, 25254], 'labels': [5, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.831429660320282})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0680583715438843})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9880557656288147})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0131571292877197})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.85, 'crossentropy': 0.800219677734375}
store['active_learning_steps'][42]['acquisition']={'indices': [54628, 57990, 53067, 8920, 59053], 'labels': [4, -1, 5, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0198721885681152})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0374468564987183})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1707878112792969})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.150316596031189})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8439, 'crossentropy': 0.8901369140625}
store['active_learning_steps'][43]['acquisition']={'indices': [50071, 6948, 29953, 20452, 35095], 'labels': [5, -1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8696126937866211})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8538439273834229})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9054785966873169})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1030350923538208})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1550884246826172})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8743, 'crossentropy': 0.82021298828125}
store['active_learning_steps'][44]['acquisition']={'indices': [30026, 21867, 53836, 12193, 10534], 'labels': [-1, 4, 7, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8417145609855652})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8768845796585083})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0525271892547607})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0010806322097778})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8618, 'crossentropy': 0.809760107421875}
store['active_learning_steps'][45]['acquisition']={'indices': [29044, 38688, 380, 188, 13516], 'labels': [-1, -1, 4, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8700461387634277})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8599561452865601})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9121384620666504})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9126023054122925})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9733648300170898})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8795, 'crossentropy': 0.747356103515625}
store['active_learning_steps'][46]['acquisition']={'indices': [45631, 36374, 13642, 27506, 1114], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9075328707695007})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8738139867782593})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0559189319610596})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.046441674232483})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0899714231491089})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8743, 'crossentropy': 0.758032421875}
store['active_learning_steps'][47]['acquisition']={'indices': [1406, 35907, 52554, 25078, 38305], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8595553040504456})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9006816744804382})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9931395053863525})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0678789615631104})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8565, 'crossentropy': 0.77999248046875}
store['active_learning_steps'][48]['acquisition']={'indices': [56935, 6717, 49449, 29113, 36807], 'labels': [5, -1, -1, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8541299104690552})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8354846835136414})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.801280677318573})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0056219100952148})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0930713415145874})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0901354551315308})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8925, 'crossentropy': 0.73536845703125}
store['active_learning_steps'][49]['acquisition']={'indices': [12222, 34222, 47982, 24502, 9899], 'labels': [3, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8024513721466064})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8723222613334656})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9314694404602051})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0059300661087036})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.852, 'crossentropy': 0.745968798828125}
store['active_learning_steps'][50]['acquisition']={'indices': [10067, 15015, 34384, 30698, 56765], 'labels': [-1, 0, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8348924517631531})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8837407827377319})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8866615891456604})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.058028221130371})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8596, 'crossentropy': 0.746060888671875}
store['active_learning_steps'][51]['acquisition']={'indices': [46670, 8827, 8598, 20567, 55870], 'labels': [6, 7, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8609872460365295})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8983728885650635})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.994998037815094})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.990083634853363})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8502, 'crossentropy': 0.814509716796875}
store['active_learning_steps'][52]['acquisition']={'indices': [50959, 27207, 28671, 54286, 58455], 'labels': [-1, 1, 0, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8024700880050659})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7399021983146667})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8349259495735168})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9699692726135254})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9537628889083862})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8891, 'crossentropy': 0.682956787109375}
store['active_learning_steps'][53]['acquisition']={'indices': [8730, 54563, 26202, 3693, 56786], 'labels': [8, 4, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7972269654273987})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.734247088432312})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8325037360191345})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.841284453868866})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9164977669715881})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.754116015625}
store['active_learning_steps'][54]['acquisition']={'indices': [24364, 40382, 56621, 17920, 20341], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7921050786972046})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8211759924888611})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9177942276000977})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9625469446182251})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8545, 'crossentropy': 0.73625029296875}
store['active_learning_steps'][55]['acquisition']={'indices': [3970, 48063, 7770, 3535, 42437], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7680097818374634})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7627015113830566})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7831488847732544})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9267295598983765})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9143732786178589})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8838, 'crossentropy': 0.749584375}
store['active_learning_steps'][56]['acquisition']={'indices': [17122, 15956, 25052, 15788, 2385], 'labels': [0, -1, 1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7756017446517944})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7902936935424805})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7872110605239868})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8279415965080261})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8618, 'crossentropy': 0.73410517578125}
store['active_learning_steps'][57]['acquisition']={'indices': [42253, 6872, 31758, 21476, 42231], 'labels': [6, 9, 8, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7923471927642822})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7961544394493103})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9189484119415283})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8605489730834961})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8705, 'crossentropy': 0.752143896484375}
store['active_learning_steps'][58]['acquisition']={'indices': [17408, 3738, 10192, 55528, 36849], 'labels': [-1, 4, 5, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7634730935096741})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7489622235298157})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7736803889274597})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7995548844337463})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7794175148010254})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.66711337890625}
store['active_learning_steps'][59]['acquisition']={'indices': [22515, 12664, 50222, 3646, 58113], 'labels': [7, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7881573438644409})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6678885221481323})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8043252229690552})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8644567728042603})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7956526279449463})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8957, 'crossentropy': 0.61110322265625}
store['active_learning_steps'][60]['acquisition']={'indices': [27781, 53477, 9559, 2392, 53057], 'labels': [-1, -1, -1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7705796957015991})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7903472185134888})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8883862495422363})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9300791621208191})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8691, 'crossentropy': 0.670633642578125}
store['active_learning_steps'][61]['acquisition']={'indices': [13503, 28912, 55219, 5868, 14698], 'labels': [-1, 6, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7731850743293762})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6945000290870667})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8184723854064941})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7169680595397949})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9018388390541077})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8876, 'crossentropy': 0.658655078125}
store['active_learning_steps'][62]['acquisition']={'indices': [38173, 47271, 59983, 38192, 15213], 'labels': [4, 0, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7244365215301514})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6598699688911438})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7999846935272217})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7405271530151367})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7845799922943115})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.593805712890625}
store['active_learning_steps'][63]['acquisition']={'indices': [3283, 58022, 35646, 13420, 59532], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6994571685791016})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6481653451919556})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8675388097763062})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7460397481918335})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.874514639377594})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.5879169921875}
store['active_learning_steps'][64]['acquisition']={'indices': [4197, 3105, 26409, 33769, 53829], 'labels': [4, 2, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7176238298416138})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7755489349365234})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7766245603561401})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7882978916168213})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8752, 'crossentropy': 0.648310595703125}
store['active_learning_steps'][65]['acquisition']={'indices': [41347, 866, 3861, 58580, 1985], 'labels': [8, 2, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7676339745521545})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7939728498458862})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8055552840232849})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7532939910888672})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8066210746765137})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7738959789276123})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.9185495972633362})
store['active_learning_steps'][66]['training']['best_epoch']=4
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.681070458984375}
store['active_learning_steps'][66]['acquisition']={'indices': [36799, 58973, 52015, 48893, 9163], 'labels': [7, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7968579530715942})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6347132921218872})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6440287232398987})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7780811786651611})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8178422451019287})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.595003076171875}
store['active_learning_steps'][67]['acquisition']={'indices': [9248, 44931, 37216, 31719, 5427], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6981085538864136})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6408818364143372})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.697266697883606})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.719616711139679})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7380276918411255})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9018, 'crossentropy': 0.59461552734375}
store['active_learning_steps'][68]['acquisition']={'indices': [57881, 59630, 26816, 38774, 57076], 'labels': [6, -1, 4, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7567558288574219})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7264069318771362})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7429366111755371})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7879794836044312})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6622266173362732})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7668077945709229})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8231486082077026})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6970224380493164})
store['active_learning_steps'][69]['training']['best_epoch']=5
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.66051572265625}
store['active_learning_steps'][69]['acquisition']={'indices': [10708, 41237, 10812, 42547, 4758], 'labels': [-1, 1, -1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7161121368408203})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5992672443389893})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.632083535194397})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7347712516784668})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7647662162780762})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.534444921875}
store['active_learning_steps'][70]['acquisition']={'indices': [54322, 34414, 34036, 15591, 14419], 'labels': [3, 8, 0, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7024351358413696})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6493062973022461})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7801198363304138})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.683439314365387})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.715874433517456})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.5737875}
store['active_learning_steps'][71]['acquisition']={'indices': [4804, 27383, 17655, 36939, 24681], 'labels': [0, -1, 0, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8341143131256104})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6794826984405518})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8007696866989136})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7782214879989624})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8296973705291748})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.589821240234375}
store['active_learning_steps'][72]['acquisition']={'indices': [18442, 22706, 39323, 34469, 51083], 'labels': [1, -1, 2, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6907814741134644})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6311379671096802})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7275974750518799})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7435017824172974})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7772529125213623})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.566391845703125}
store['active_learning_steps'][73]['acquisition']={'indices': [23032, 46578, 9657, 23322, 2620], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7943350076675415})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6247431635856628})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6602804660797119})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7373231649398804})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6355800628662109})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.55856162109375}
store['active_learning_steps'][74]['acquisition']={'indices': [4383, 44951, 41258, 55195, 39007], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7460132241249084})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6736230850219727})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.765034556388855})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7405840158462524})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7024248242378235})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.65838662109375}
store['active_learning_steps'][75]['acquisition']={'indices': [3634, 29438, 18427, 16592, 20410], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7789817452430725})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6671929359436035})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8378945589065552})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6954766511917114})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.701659619808197})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.5978689453125}
store['active_learning_steps'][76]['acquisition']={'indices': [35480, 323, 38983, 46269, 3020], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7595201730728149})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6505566835403442})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7450140714645386})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8018578290939331})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6843676567077637})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.584546630859375}
store['active_learning_steps'][77]['acquisition']={'indices': [16314, 47175, 17265, 17412, 43889], 'labels': [4, -1, -1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.72575843334198})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.688666045665741})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6772674918174744})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7092527151107788})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6683288812637329})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7321405410766602})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8478890657424927})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7650996446609497})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.661872265625}
store['active_learning_steps'][78]['acquisition']={'indices': [32778, 15926, 45141, 51015, 27897], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7538164258003235})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6313966512680054})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7309390306472778})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6630194187164307})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7141699194908142})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.589224462890625}
store['active_learning_steps'][79]['acquisition']={'indices': [26761, 23662, 33780, 31224, 30649], 'labels': [0, 0, 8, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7079868316650391})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6643036603927612})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6871854662895203})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7552074193954468})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8212594985961914})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8981, 'crossentropy': 0.6150982421875}
store['active_learning_steps'][80]['acquisition']={'indices': [58477, 16524, 11368, 43707, 10840], 'labels': [-1, -1, 9, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7618246078491211})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7429815530776978})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6638595461845398})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6786954402923584})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8209485411643982})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7858980894088745})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.594073291015625}
store['active_learning_steps'][81]['acquisition']={'indices': [40239, 8830, 41004, 19518, 41107], 'labels': [-1, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7858108282089233})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6690344214439392})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6562926769256592})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6324828863143921})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7915725708007812})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6573610305786133})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6566038131713867})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.589470166015625}
store['active_learning_steps'][82]['acquisition']={'indices': [28230, 56281, 38816, 8164, 52531], 'labels': [0, 4, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6653650999069214})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6774419546127319})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6448933482170105})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6284708976745605})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7166216373443604})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7512392997741699})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6955535411834717})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.607431201171875}
store['active_learning_steps'][83]['acquisition']={'indices': [17550, 48799, 15349, 54134, 46672], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7447733879089355})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6445349454879761})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6648783087730408})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7073531150817871})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7125946283340454})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.57531591796875}
store['active_learning_steps'][84]['acquisition']={'indices': [53878, 33651, 26173, 27000, 55616], 'labels': [2, -1, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7234179973602295})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6254523396492004})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.639877200126648})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7046528458595276})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6469165086746216})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.550044677734375}
store['active_learning_steps'][85]['acquisition']={'indices': [13512, 49642, 28348, 28929, 1139], 'labels': [7, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6766166687011719})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.737281858921051})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6899029016494751})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6715736389160156})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.706282377243042})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7137237787246704})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7350473403930664})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.61443779296875}
store['active_learning_steps'][86]['acquisition']={'indices': [6212, 16833, 18058, 20603, 49172], 'labels': [2, 8, 6, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.685931921005249})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.603156328201294})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6936216354370117})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7036776542663574})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7799344062805176})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.56024169921875}
store['active_learning_steps'][87]['acquisition']={'indices': [31287, 26276, 45353, 52701, 37658], 'labels': [5, 9, 4, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6756643056869507})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7107127904891968})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7307009696960449})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7510576248168945})
store['active_learning_steps'][88]['training']['best_epoch']=1
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8826, 'crossentropy': 0.654902783203125}
store['active_learning_steps'][88]['acquisition']={'indices': [24147, 55495, 20784, 22978, 31244], 'labels': [8, -1, 5, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7611472606658936})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.583003044128418})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6052839159965515})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7492709159851074})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7369097471237183})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.53822998046875}
store['active_learning_steps'][89]['acquisition']={'indices': [41399, 5589, 34527, 6342, 37933], 'labels': [-1, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7002898454666138})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.584011435508728})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6325081586837769})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.627794623374939})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7027895450592041})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.53267734375}
store['active_learning_steps'][90]['acquisition']={'indices': [12730, 43983, 35316, 26421, 19695], 'labels': [-1, 4, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7601000666618347})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6283682584762573})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6440068483352661})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6114908456802368})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6852260828018188})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7235872745513916})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.663063645362854})
store['active_learning_steps'][91]['training']['best_epoch']=4
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.538163330078125}
store['active_learning_steps'][91]['acquisition']={'indices': [11296, 23665, 6899, 36812, 55765], 'labels': [-1, 1, 2, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.72120201587677})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5849007368087769})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5834439992904663})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6428354978561401})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7120818495750427})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7411353588104248})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.522807177734375}
store['active_learning_steps'][92]['acquisition']={'indices': [16476, 8781, 1435, 55121, 22218], 'labels': [-1, 1, 6, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.68016517162323})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6294713020324707})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6693909168243408})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7007254362106323})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6529756784439087})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.524942138671875}
store['active_learning_steps'][93]['acquisition']={'indices': [5193, 49877, 26155, 6666, 35527], 'labels': [3, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7049252390861511})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6278536319732666})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5995519161224365})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6834522485733032})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7262365818023682})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6931893825531006})
store['active_learning_steps'][94]['training']['best_epoch']=3
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.54246591796875}
store['active_learning_steps'][94]['acquisition']={'indices': [18690, 34402, 49373, 4680, 40822], 'labels': [8, 1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7170537710189819})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6421485543251038})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6508756875991821})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6949609518051147})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6722155213356018})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.573178857421875}
store['active_learning_steps'][95]['acquisition']={'indices': [45392, 40209, 21993, 37934, 32208], 'labels': [-1, 6, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.757520318031311})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6377257108688354})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6160317659378052})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6165140271186829})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6603939533233643})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.731426477432251})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.54019267578125}
store['active_learning_steps'][96]['acquisition']={'indices': [42250, 3772, 42689, 32739, 50556], 'labels': [0, -1, 6, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6862261295318604})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6277551651000977})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5913296937942505})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6850416660308838})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5666512846946716})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5923382639884949})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6005676984786987})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6674475073814392})
store['active_learning_steps'][97]['training']['best_epoch']=5
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9289, 'crossentropy': 0.51945908203125}
store['active_learning_steps'][97]['acquisition']={'indices': [7260, 13504, 16599, 41779, 5178], 'labels': [5, -1, 6, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6933814883232117})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6842402219772339})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6163195371627808})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6595370769500732})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6717782020568848})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6645803451538086})
store['active_learning_steps'][98]['training']['best_epoch']=3
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.523678271484375}
store['active_learning_steps'][98]['acquisition']={'indices': [15564, 25317, 50103, 46684, 55097], 'labels': [0, 6, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6597541570663452})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6072863340377808})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.598462700843811})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6042401790618896})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7118545770645142})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7034758925437927})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.55244609375}
store['active_learning_steps'][99]['acquisition']={'indices': [14773, 12717, 22703, 41035, 39489], 'labels': [-1, 7, 8, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6471844911575317})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6641610860824585})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6523973941802979})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6277263164520264})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6387073993682861})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6522243022918701})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.70417320728302})
store['active_learning_steps'][100]['training']['best_epoch']=4
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.514101611328125}
store['active_learning_steps'][100]['acquisition']={'indices': [55764, 2097, 41360, 50370, 27049], 'labels': [8, 8, 1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6600503921508789})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5941665172576904})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6608803272247314})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6063061952590942})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5849515795707703})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6374989748001099})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7663756608963013})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7219583988189697})
store['active_learning_steps'][101]['training']['best_epoch']=5
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.51031005859375}
store['active_learning_steps'][101]['acquisition']={'indices': [37453, 15576, 20453, 35669, 35792], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6558735966682434})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5535576939582825})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6274204254150391})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6162124872207642})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6361098885536194})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.48870517578125}
store['active_learning_steps'][102]['acquisition']={'indices': [11589, 8526, 30599, 20726, 5422], 'labels': [6, 6, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7651554346084595})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5900290608406067})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6103882193565369})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6548963785171509})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6083316802978516})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.52204443359375}
store['active_learning_steps'][103]['acquisition']={'indices': [9903, 17460, 46353, 33551, 38139], 'labels': [1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.675711989402771})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6296112537384033})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6419048309326172})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5719578266143799})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5665132999420166})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6520272493362427})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6799651384353638})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6931658387184143})
store['active_learning_steps'][104]['training']['best_epoch']=5
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.52868369140625}
store['active_learning_steps'][104]['acquisition']={'indices': [37556, 31713, 34327, 10949, 3222], 'labels': [7, -1, -1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.733055591583252})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6454616785049438})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6054714918136597})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6733000874519348})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6581882834434509})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7204868197441101})
store['active_learning_steps'][105]['training']['best_epoch']=3
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.578396923828125}
store['active_learning_steps'][105]['acquisition']={'indices': [3718, 23656, 53383, 39043, 12515], 'labels': [7, 1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.764984667301178})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5993216037750244})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6634061932563782})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5541584491729736})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5694249868392944})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6289052367210388})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6764678955078125})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.5125904296875}
store['active_learning_steps'][106]['acquisition']={'indices': [46342, 17249, 889, 43202, 23510], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6924101114273071})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5769031047821045})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7232194542884827})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.66969233751297})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.620197594165802})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.51990693359375}
store['active_learning_steps'][107]['acquisition']={'indices': [33298, 37518, 49882, 25345, 40350], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6262513399124146})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5818749666213989})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.663840651512146})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6505508422851562})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7173651456832886})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.531978369140625}
store['active_learning_steps'][108]['acquisition']={'indices': [39353, 43226, 59460, 27773, 32696], 'labels': [6, 8, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.694966197013855})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6277740001678467})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.585708737373352})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5871087312698364})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6619302034378052})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7320244312286377})
store['active_learning_steps'][109]['training']['best_epoch']=3
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.50175986328125}
store['active_learning_steps'][109]['acquisition']={'indices': [58210, 6024, 54181, 57922, 6993], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6764284372329712})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5527778267860413})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6006165742874146})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6322730779647827})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5851030945777893})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.510347119140625}
store['active_learning_steps'][110]['acquisition']={'indices': [12155, 17823, 9392, 2038, 43919], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6530382037162781})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6077514886856079})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6067069172859192})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6141588687896729})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6085015535354614})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6264057159423828})
store['active_learning_steps'][111]['training']['best_epoch']=3
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.5243251953125}
store['active_learning_steps'][111]['acquisition']={'indices': [12678, 2968, 40054, 3821, 44037], 'labels': [-1, -1, 2, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6943511962890625})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5589625835418701})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5461281538009644})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5530555844306946})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5724290609359741})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.645119309425354})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.4801162109375}
store['active_learning_steps'][112]['acquisition']={'indices': [42676, 57131, 24058, 54887, 27290], 'labels': [-1, 3, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7413541078567505})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5753175616264343})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6455143094062805})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5836621522903442})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5629832744598389})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6444957256317139})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7316684722900391})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6817046403884888})
store['active_learning_steps'][113]['training']['best_epoch']=5
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.54213544921875}
store['active_learning_steps'][113]['acquisition']={'indices': [25651, 54873, 54043, 34984, 8736], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6799805164337158})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5680341124534607})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5351876020431519})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6515243053436279})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5829416513442993})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6705964803695679})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.507434033203125}
store['active_learning_steps'][114]['acquisition']={'indices': [57250, 6532, 26955, 8153, 6735], 'labels': [1, 4, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6878689527511597})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5892157554626465})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6061704158782959})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5459738969802856})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5707299113273621})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.630384087562561})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.574764609336853})
store['active_learning_steps'][115]['training']['best_epoch']=4
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.4870763671875}
store['active_learning_steps'][115]['acquisition']={'indices': [16300, 18984, 21236, 30717, 2980], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6547187566757202})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5630102157592773})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6067256927490234})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6219897270202637})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6572713851928711})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9184, 'crossentropy': 0.479786669921875}
store['active_learning_steps'][116]['acquisition']={'indices': [1922, 37087, 35346, 40944, 53387], 'labels': [-1, 4, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6855064630508423})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6248584985733032})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5644222497940063})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6717844009399414})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6321229934692383})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5947335958480835})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.50427060546875}
store['active_learning_steps'][117]['acquisition']={'indices': [5617, 25792, 17738, 42457, 42148], 'labels': [-1, -1, 0, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6735559701919556})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5618722438812256})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5733832120895386})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.608293890953064})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6160734295845032})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.4921263671875}
store['active_learning_steps'][118]['acquisition']={'indices': [35922, 29246, 5357, 700, 44893], 'labels': [3, -1, 2, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7350351810455322})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5738070011138916})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5866602659225464})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5659692883491516})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6443756818771362})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6030552387237549})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6186091899871826})
store['active_learning_steps'][119]['training']['best_epoch']=4
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.485585400390625}
store['active_learning_steps'][119]['acquisition']={'indices': [44903, 48942, 41743, 49813, 27956], 'labels': [3, 4, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6684012413024902})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6079214811325073})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5709301829338074})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5780597925186157})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5860832929611206})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7082276344299316})
store['active_learning_steps'][120]['training']['best_epoch']=3
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.486568896484375}
store['active_learning_steps'][120]['acquisition']={'indices': [24477, 11455, 9823, 31216, 41856], 'labels': [-1, 7, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6408677101135254})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.557925820350647})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5300883054733276})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.574720025062561})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5342167019844055})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6095374822616577})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.4791478515625}
store['active_learning_steps'][121]['acquisition']={'indices': [17509, 12039, 24193, 53370, 9752], 'labels': [-1, 5, 9, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6890310049057007})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5510717630386353})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5564640760421753})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5509839057922363})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5757209658622742})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6712962985038757})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5930241346359253})
store['active_learning_steps'][122]['training']['best_epoch']=4
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.484088720703125}
store['active_learning_steps'][122]['acquisition']={'indices': [54129, 19605, 30525, 55317, 3649], 'labels': [4, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6890038251876831})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5454214811325073})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.587154746055603})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6120097637176514})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6156008243560791})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.502077587890625}
store['active_learning_steps'][123]['acquisition']={'indices': [2617, 660, 9688, 46087, 23820], 'labels': [-1, -1, 0, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6979432106018066})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5490429401397705})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6110467314720154})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5546489953994751})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5927226543426514})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.487915625}
store['active_learning_steps'][124]['acquisition']={'indices': [25798, 30684, 41177, 28718, 41081], 'labels': [-1, 1, 9, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6601965427398682})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5722742080688477})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6019527912139893})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6290009021759033})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6253376007080078})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.51157958984375}
store['active_learning_steps'][125]['acquisition']={'indices': [24622, 46439, 27883, 30960, 21629], 'labels': [6, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.645964503288269})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5248859524726868})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.562785267829895})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5662159323692322})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5769631862640381})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.47839462890625}
store['active_learning_steps'][126]['acquisition']={'indices': [7761, 18626, 15876, 29304, 57128], 'labels': [1, 3, -1, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.711795449256897})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6029230356216431})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5965309143066406})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5575610995292664})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.637465238571167})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5833592414855957})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6469049453735352})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.490465234375}
store['active_learning_steps'][127]['acquisition']={'indices': [4386, 3727, 47607, 53721, 53790], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7062455415725708})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5278139114379883})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6035242080688477})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.604163646697998})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5781477093696594})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.482441748046875}
store['active_learning_steps'][128]['acquisition']={'indices': [32669, 1264, 2098, 56284, 3546], 'labels': [4, -1, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8096160888671875})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6044539213180542})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.534331202507019})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6308997273445129})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5380513668060303})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6529662013053894})
store['active_learning_steps'][129]['training']['best_epoch']=3
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.46157216796875}
store['active_learning_steps'][129]['acquisition']={'indices': [14415, 51667, 23875, 34886, 38701], 'labels': [4, -1, 0, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6713528633117676})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5399916768074036})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5324044227600098})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4913833737373352})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5067051649093628})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5354820489883423})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5380441546440125})
store['active_learning_steps'][130]['training']['best_epoch']=4
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.456868896484375}
store['active_learning_steps'][130]['acquisition']={'indices': [35887, 55099, 52740, 39149, 9359], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6557779312133789})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5559929609298706})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5506691932678223})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5901316404342651})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5648361444473267})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6332310438156128})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.50688671875}
store['active_learning_steps'][131]['acquisition']={'indices': [32322, 44383, 17644, 28106, 35385], 'labels': [5, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7067221403121948})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5698679685592651})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5603262186050415})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5729619860649109})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6214867830276489})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6396286487579346})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.5067525390625}
store['active_learning_steps'][132]['acquisition']={'indices': [9482, 50141, 1590, 1149, 39908], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7209934592247009})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5605571866035461})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6042761206626892})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5679987072944641})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5708375573158264})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.509991796875}
store['active_learning_steps'][133]['acquisition']={'indices': [11752, 24877, 47541, 56040, 38811], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.683980405330658})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6183695793151855})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6092424392700195})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5649582743644714})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.644269585609436})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5977089405059814})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6267575025558472})
store['active_learning_steps'][134]['training']['best_epoch']=4
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.483585693359375}
store['active_learning_steps'][134]['acquisition']={'indices': [57786, 11050, 38702, 18822, 57024], 'labels': [-1, 1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7018023729324341})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5480632781982422})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.559882640838623})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49908560514450073})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6231658458709717})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6036257743835449})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6373981833457947})
store['active_learning_steps'][135]['training']['best_epoch']=4
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.4483185546875}
store['active_learning_steps'][135]['acquisition']={'indices': [11822, 25624, 55756, 12470, 31475], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7167477607727051})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.525078296661377})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5432143807411194})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5867229104042053})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6324114799499512})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.474016015625}
store['active_learning_steps'][136]['acquisition']={'indices': [26697, 52989, 22340, 32757, 51768], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6992059946060181})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5719916820526123})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5368756055831909})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.518894612789154})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6174575090408325})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5682686567306519})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6731710433959961})
store['active_learning_steps'][137]['training']['best_epoch']=4
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9271, 'crossentropy': 0.4774173828125}
store['active_learning_steps'][137]['acquisition']={'indices': [4352, 7936, 16390, 12675, 29517], 'labels': [3, 9, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.634642481803894})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6534417271614075})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5245442986488342})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5448300838470459})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6253869533538818})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.63004469871521})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.460069091796875}
store['active_learning_steps'][138]['acquisition']={'indices': [10924, 1263, 32, 53806, 30938], 'labels': [0, 5, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7038193941116333})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5565170049667358})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.591647207736969})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5665078163146973})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5611934661865234})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.508696435546875}
store['active_learning_steps'][139]['acquisition']={'indices': [14977, 34758, 23693, 9856, 38007], 'labels': [9, 8, 1, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7046844959259033})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5914043188095093})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6018988490104675})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6196862459182739})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6537361145019531})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.533152001953125}
store['active_learning_steps'][140]['acquisition']={'indices': [58894, 36827, 8111, 47097, 7835], 'labels': [5, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7268668413162231})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.543357253074646})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6123605966567993})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5938065052032471})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5920969843864441})
store['active_learning_steps'][141]['training']['best_epoch']=2
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.5365677734375}
store['active_learning_steps'][141]['acquisition']={'indices': [53406, 13523, 6894, 14870, 58136], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7273498773574829})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5380468368530273})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5215967297554016})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5033714175224304})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5755968689918518})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6218138933181763})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6406061053276062})
store['active_learning_steps'][142]['training']['best_epoch']=4
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.4466099609375}
store['active_learning_steps'][142]['acquisition']={'indices': [46506, 4525, 31051, 7529, 15087], 'labels': [3, -1, -1, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7564803957939148})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5737740397453308})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4993134140968323})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5350164771080017})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.571476936340332})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5626100301742554})
store['active_learning_steps'][143]['training']['best_epoch']=3
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.457139306640625}
store['active_learning_steps'][143]['acquisition']={'indices': [39716, 16937, 21962, 49062, 14142], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7158997058868408})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5190271139144897})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5217787623405457})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5314748287200928})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5151335000991821})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5004715323448181})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6034249663352966})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5850088596343994})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6019116640090942})
store['active_learning_steps'][144]['training']['best_epoch']=6
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.4680517578125}
store['active_learning_steps'][144]['acquisition']={'indices': [34583, 15969, 34097, 4476, 652], 'labels': [-1, 5, -1, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.622361421585083})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5662701725959778})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5288684368133545})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5368306636810303})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6222256422042847})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.590994656085968})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.46643408203125}
store['active_learning_steps'][145]['acquisition']={'indices': [42729, 50810, 21753, 55937, 26945], 'labels': [-1, -1, 6, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6718432903289795})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5436630249023438})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5214537382125854})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5160245895385742})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5795042514801025})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5569466948509216})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.559435248374939})
store['active_learning_steps'][146]['training']['best_epoch']=4
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.466226220703125}
store['active_learning_steps'][146]['acquisition']={'indices': [34094, 56779, 54908, 29565, 25645], 'labels': [7, 1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7354422807693481})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5482065081596375})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5612571239471436})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.580686092376709})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5801153779029846})
store['active_learning_steps'][147]['training']['best_epoch']=2
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.488228515625}
store['active_learning_steps'][147]['acquisition']={'indices': [12602, 12775, 39569, 38388, 5377], 'labels': [3, 3, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6598999500274658})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5581105947494507})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5087795853614807})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5185047388076782})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5521214008331299})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6104768514633179})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.476698388671875}
store['active_learning_steps'][148]['acquisition']={'indices': [46490, 7277, 27972, 29830, 14875], 'labels': [-1, 7, 8, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7147183418273926})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5442718863487244})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5355275869369507})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5181902050971985})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5488172769546509})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.593970537185669})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6619840860366821})
store['active_learning_steps'][149]['training']['best_epoch']=4
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.44904404296875}
store['active_learning_steps'][149]['acquisition']={'indices': [25430, 51064, 30494, 56324, 19118], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7301455736160278})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5353123545646667})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.531404972076416})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5087519884109497})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5386285781860352})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5828992128372192})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5557677745819092})
store['active_learning_steps'][150]['training']['best_epoch']=4
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9305, 'crossentropy': 0.444449560546875}
store['active_learning_steps'][150]['acquisition']={'indices': [2691, 50706, 42173, 19219, 53056], 'labels': [-1, 7, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7207628488540649})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.526816725730896})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.590056300163269})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5791869163513184})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6514108777046204})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.4978912109375}
store['active_learning_steps'][151]['acquisition']={'indices': [40775, 7978, 6410, 50204, 13953], 'labels': [-1, 0, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6567092537879944})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5228716731071472})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5287986993789673})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5221524238586426})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5337422490119934})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5202319622039795})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5639891028404236})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5914148688316345})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.569725513458252})
store['active_learning_steps'][152]['training']['best_epoch']=6
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.42237109375}
store['active_learning_steps'][152]['acquisition']={'indices': [25749, 20033, 28556, 28857, 23909], 'labels': [1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6793841123580933})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5435730814933777})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5471543073654175})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5337069034576416})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5454791188240051})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6617683172225952})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5716506242752075})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.470944873046875}
store['active_learning_steps'][153]['acquisition']={'indices': [49957, 51071, 32095, 13808, 8136], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6655021905899048})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5462374687194824})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6079497337341309})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49849700927734375})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5661957263946533})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5389242768287659})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5758832097053528})
store['active_learning_steps'][154]['training']['best_epoch']=4
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9289, 'crossentropy': 0.4658697265625}
store['active_learning_steps'][154]['acquisition']={'indices': [15637, 9026, 1220, 33744, 40520], 'labels': [0, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7080026268959045})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5697762370109558})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6153621673583984})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5234153866767883})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.581378698348999})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6100640892982483})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5663468837738037})
store['active_learning_steps'][155]['training']['best_epoch']=4
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.43993505859375}
store['active_learning_steps'][155]['acquisition']={'indices': [28847, 2709, 53642, 48716, 59893], 'labels': [-1, 0, 5, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6927449703216553})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5365003943443298})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5594918727874756})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.538356602191925})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5975268483161926})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.460473681640625}
store['active_learning_steps'][156]['acquisition']={'indices': [33017, 10950, 24295, 9408, 2545], 'labels': [7, 6, 4, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6689459085464478})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6673711538314819})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5377861857414246})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5742292404174805})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5721286535263062})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6587823629379272})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.455502783203125}
store['active_learning_steps'][157]['acquisition']={'indices': [29195, 32108, 21794, 31439, 20406], 'labels': [9, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6935807466506958})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5729299783706665})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.550622820854187})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.638325572013855})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5570353269577026})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6229538917541504})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.48928193359375}
store['active_learning_steps'][158]['acquisition']={'indices': [47940, 17345, 47237, 15772, 38090], 'labels': [5, -1, -1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.712178111076355})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5712953805923462})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5729691386222839})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5358261466026306})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.56809401512146})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6174771785736084})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6231585741043091})
store['active_learning_steps'][159]['training']['best_epoch']=4
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.4598787109375}
store['active_learning_steps'][159]['acquisition']={'indices': [35387, 18791, 46166, 44435, 38793], 'labels': [9, 6, 0, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6754641532897949})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5172522068023682})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.485650897026062})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4874085485935211})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5443582534790039})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5502969622612})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9305, 'crossentropy': 0.431480126953125}
store['active_learning_steps'][160]['acquisition']={'indices': [41281, 20137, 13217, 12660, 24343], 'labels': [9, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6631483435630798})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5838226079940796})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5188115239143372})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5555492639541626})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5434625148773193})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.598922073841095})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.444997802734375}
store['active_learning_steps'][161]['acquisition']={'indices': [57518, 51198, 3759, 11284, 32067], 'labels': [6, 7, 8, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6770657896995544})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.579839289188385})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5864198207855225})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5738217234611511})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5414897203445435})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5802613496780396})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.553825318813324})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6183567047119141})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.459179736328125}
store['active_learning_steps'][162]['acquisition']={'indices': [22557, 34114, 53904, 21343, 49807], 'labels': [8, 5, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7036691308021545})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5185669660568237})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.528038740158081})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5137913227081299})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5233054757118225})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5652157068252563})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5625518560409546})
store['active_learning_steps'][163]['training']['best_epoch']=4
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.44638232421875}
store['active_learning_steps'][163]['acquisition']={'indices': [22439, 44674, 37850, 56859, 4610], 'labels': [8, -1, -1, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7793242931365967})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5415924787521362})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5691017508506775})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5511441230773926})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5300623178482056})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5610173940658569})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6305564641952515})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6285430192947388})
store['active_learning_steps'][164]['training']['best_epoch']=5
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.4790041015625}
store['active_learning_steps'][164]['acquisition']={'indices': [9704, 47982, 38018, 20849, 8686], 'labels': [4, -1, 7, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7060417532920837})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5926237106323242})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5601853132247925})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.563066840171814})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5379575490951538})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5906193256378174})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6495548486709595})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.624081015586853})
store['active_learning_steps'][165]['training']['best_epoch']=5
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.472390478515625}
store['active_learning_steps'][165]['acquisition']={'indices': [24375, 31866, 17172, 22103, 35424], 'labels': [-1, -1, 5, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6223062872886658})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5453267097473145})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4819803237915039})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5526248216629028})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.566330075263977})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5222569704055786})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9359, 'crossentropy': 0.429888818359375}
store['active_learning_steps'][166]['acquisition']={'indices': [42621, 26082, 5752, 44855, 9135], 'labels': [-1, 9, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6605609655380249})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5294391512870789})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5101430416107178})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.48778146505355835})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5270890593528748})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5180547833442688})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5186633467674255})
store['active_learning_steps'][167]['training']['best_epoch']=4
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.42577021484375}
store['active_learning_steps'][167]['acquisition']={'indices': [24382, 40855, 10472, 39278, 51813], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6569994688034058})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5994052886962891})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.560947060585022})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.505056619644165})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5282809734344482})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5374008417129517})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5985346436500549})
store['active_learning_steps'][168]['training']['best_epoch']=4
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.45309404296875}
store['active_learning_steps'][168]['acquisition']={'indices': [45147, 8599, 42628, 4217, 45758], 'labels': [1, -1, 9, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6762431859970093})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5312981605529785})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5093371272087097})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4808118939399719})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5636278986930847})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5190317034721375})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5730999112129211})
store['active_learning_steps'][169]['training']['best_epoch']=4
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.4045496337890625}
store['active_learning_steps'][169]['acquisition']={'indices': [27050, 22686, 39907, 12521, 34435], 'labels': [0, -1, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6639177799224854})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5453844666481018})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5163252353668213})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48066481947898865})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49919256567955017})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5295550227165222})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5359996557235718})
store['active_learning_steps'][170]['training']['best_epoch']=4
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9342, 'crossentropy': 0.4256947265625}
store['active_learning_steps'][170]['acquisition']={'indices': [38453, 39678, 4604, 35258, 41317], 'labels': [8, -1, 7, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6914798021316528})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5686686038970947})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.555819034576416})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5635724067687988})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5598100423812866})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5666968822479248})
store['active_learning_steps'][171]['training']['best_epoch']=3
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.48040498046875}
