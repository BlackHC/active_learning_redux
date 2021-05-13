store = {}
store['timestamp']=1620260185
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=30']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=30
store['worker_id']=30
store['num_workers']=40
store['config']={'seed': 40, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4047460556030273})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.583082914352417})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6663312911987305})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.791015148162842})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6761, 'crossentropy': 2.0304546875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 12074], ['id', 42248], ['id', 15044], ['id', 26850], ['ood', 3212]], 'labels': [9, 3, 1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7322752475738525})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7855167388916016})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.273296356201172})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4132192134857178})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6866, 'crossentropy': 1.6180609375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 53633], ['id', 58824], ['id', 55476], ['id', 51910], ['id', 57968]], 'labels': [9, 5, 7, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.8617444038391113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.0596261024475098})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.1393418312072754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.2057011127471924})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6846, 'crossentropy': 1.6336359375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 44031], ['ood', 29859], ['ood', 4178], ['id', 42312], ['id', 3972]], 'labels': [1, 4, 8, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4860650300979614})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8917028903961182})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.91868257522583})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.194139242172241})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7305, 'crossentropy': 1.32513369140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 39885], ['ood', 26930], ['ood', 55540], ['ood', 22295], ['ood', 11119]], 'labels': [5, 6, 0, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6107736825942993})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.7816596031188965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9537150859832764})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.9646416902542114})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6994, 'crossentropy': 1.38373759765625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 11121], ['ood', 29520], ['ood', 42214], ['ood', 32526], ['ood', 45993]], 'labels': [8, 4, 4, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.272397518157959})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.723700761795044})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.8452887535095215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7698020935058594})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7346, 'crossentropy': 1.16312783203125}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 15496], ['id', 30963], ['ood', 59462], ['ood', 4901], ['id', 33062]], 'labels': [5, 1, 4, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3492255210876465})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5041489601135254})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.6598610877990723})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.7098102569580078})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.702, 'crossentropy': 1.26360546875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 55357], ['ood', 44753], ['ood', 31794], ['ood', 6062], ['id', 29968]], 'labels': [8, 4, 9, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.199716567993164})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3301565647125244})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4111123085021973})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.597387671470642})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.738, 'crossentropy': 1.1281798828125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19169], ['id', 4420], ['id', 27624], ['ood', 26004], ['id', 48658]], 'labels': [3, 1, 6, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3404077291488647})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3781788349151611})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.594229817390442})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.610898494720459})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6952, 'crossentropy': 1.22620107421875}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 56560], ['id', 23437], ['id', 58256], ['id', 39710], ['ood', 41051]], 'labels': [9, 8, 0, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4211671352386475})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4644792079925537})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6566359996795654})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7470674514770508})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.706, 'crossentropy': 1.261791015625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10517], ['id', 7179], ['ood', 34992], ['id', 29818], ['ood', 46588]], 'labels': [7, 6, 1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.159907579421997})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1855733394622803})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4077961444854736})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3583495616912842})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7366, 'crossentropy': 1.0746373046875}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 44588], ['id', 18939], ['id', 35493], ['id', 35243], ['ood', 34666]], 'labels': [3, 3, 4, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.2014389038085938})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2504920959472656})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3292663097381592})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3900898694992065})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7523, 'crossentropy': 1.06803271484375}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 41268], ['ood', 24820], ['ood', 35818], ['ood', 25393], ['ood', 24540]], 'labels': [7, 5, 4, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9734841585159302})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9670507907867432})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1012202501296997})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1272199153900146})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1630749702453613})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8268, 'crossentropy': 0.85445537109375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 39172], ['ood', 20122], ['id', 54692], ['ood', 5955], ['id', 57566]], 'labels': [9, 2, 1, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0324268341064453})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0782387256622314})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1238209009170532})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2834205627441406})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7997, 'crossentropy': 0.9225943359375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 57874], ['id', 225], ['ood', 10666], ['id', 36509], ['id', 2119]], 'labels': [9, 8, 4, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.05814790725708})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0030423402786255})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0866378545761108})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2277265787124634})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1139283180236816})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8145, 'crossentropy': 0.85335771484375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 26427], ['id', 38459], ['ood', 45068], ['ood', 13332], ['id', 19030]], 'labels': [0, 5, 5, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.966895580291748})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0005402565002441})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1740658283233643})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1563811302185059})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7949, 'crossentropy': 0.8971400390625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 26031], ['ood', 47097], ['ood', 32167], ['ood', 49602], ['ood', 56996]], 'labels': [0, 0, 0, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0526316165924072})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.053559422492981})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2196719646453857})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1286638975143433})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7791, 'crossentropy': 0.95642333984375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 43971], ['id', 46846], ['ood', 47603], ['id', 8347], ['id', 57450]], 'labels': [1, 4, 1, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0726585388183594})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9138943552970886})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9344266653060913})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9799240827560425})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0410311222076416})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8184, 'crossentropy': 0.8077669921875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 9888], ['id', 35700], ['id', 47406], ['ood', 38447], ['id', 16289]], 'labels': [7, 0, 0, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9630744457244873})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9631081819534302})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.003020167350769})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0344316959381104})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8128, 'crossentropy': 0.87593798828125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 18094], ['ood', 5956], ['ood', 46244], ['id', 28994], ['ood', 4548]], 'labels': [6, 5, 8, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8667227029800415})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7919211387634277})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8816885352134705})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9755452871322632})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9842404127120972})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8503, 'crossentropy': 0.70360029296875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 26360], ['ood', 10278], ['ood', 43449], ['ood', 32516], ['id', 45153]], 'labels': [5, 5, 4, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0719985961914062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9882342219352722})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0279760360717773})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1369905471801758})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2096643447875977})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8257, 'crossentropy': 0.83737978515625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 33733], ['id', 41324], ['id', 24530], ['id', 46403], ['id', 48235]], 'labels': [5, 7, 4, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9649296998977661})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8440756797790527})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9418525695800781})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0414493083953857})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9702039957046509})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8463, 'crossentropy': 0.72395244140625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 6798], ['id', 26267], ['ood', 31077], ['ood', 21512], ['ood', 31695]], 'labels': [4, 3, 9, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9021821022033691})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.819622814655304})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8893347382545471})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8940057754516602})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9929928779602051})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8471, 'crossentropy': 0.720601171875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 51932], ['id', 50312], ['ood', 27850], ['ood', 24629], ['id', 35843]], 'labels': [1, 3, 8, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0045726299285889})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8766734600067139})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9639118909835815})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.899940013885498})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9578676819801331})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.843, 'crossentropy': 0.7521486328125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 48188], ['id', 37551], ['id', 34471], ['id', 11917], ['id', 34013]], 'labels': [9, 5, 0, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9248154163360596})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8386434316635132})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8944782018661499})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9602711200714111})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9512107372283936})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8324, 'crossentropy': 0.758872021484375}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 50527], ['id', 34758], ['id', 34802], ['id', 19314], ['ood', 35593]], 'labels': [2, 8, 3, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8471052646636963})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9011979699134827})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9971656799316406})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0165622234344482})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8458, 'crossentropy': 0.769390380859375}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 9374], ['id', 22734], ['id', 50450], ['id', 12364], ['ood', 40802]], 'labels': [0, 5, 4, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9571881294250488})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.868874192237854})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9301259517669678})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9253385663032532})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8935226202011108})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8449, 'crossentropy': 0.757980712890625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 22273], ['ood', 45223], ['ood', 55385], ['ood', 30122], ['ood', 14496]], 'labels': [6, 1, 0, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9461063146591187})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8150568604469299})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8841333985328674})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9569123387336731})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9382989406585693})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8483, 'crossentropy': 0.691140966796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 56395], ['ood', 51672], ['ood', 52232], ['ood', 37447], ['ood', 13310]], 'labels': [4, 6, 2, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9523791074752808})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8800637722015381})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8708781003952026})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9241557121276855})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9384748935699463})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0478638410568237})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8517, 'crossentropy': 0.7168208984375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 28830], ['id', 850], ['ood', 37383], ['ood', 9394], ['ood', 6483]], 'labels': [9, 4, 0, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9782119393348694})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8741577863693237})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9430286884307861})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.925804853439331})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0156447887420654})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8391, 'crossentropy': 0.75201181640625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 25443], ['id', 11923], ['id', 50390], ['ood', 16930], ['id', 11767]], 'labels': [1, 8, 0, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.0101869106292725})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8589785695075989})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.927445650100708})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8341375589370728})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9449880719184875})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9670383334159851})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.938527524471283})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.718699560546875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 22399], ['ood', 1968], ['id', 43187], ['ood', 45919], ['id', 16279]], 'labels': [7, 2, 7, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9972530007362366})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8522976040840149})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8436264991760254})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8841665983200073})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9110836386680603})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9597551822662354})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8402, 'crossentropy': 0.74405625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 42564], ['ood', 3654], ['id', 40882], ['id', 52743], ['id', 48526]], 'labels': [0, 6, 8, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9485554099082947})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8534225225448608})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7927402257919312})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9313901662826538})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9418154954910278})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9829661250114441})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8698, 'crossentropy': 0.672939306640625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 27305], ['id', 16064], ['id', 179], ['id', 15674], ['id', 38439]], 'labels': [0, 6, 3, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8799935579299927})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7848827838897705})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7841750383377075})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8082500100135803})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7816652059555054})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7779291868209839})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8595418930053711})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8869091272354126})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8484474420547485})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8711, 'crossentropy': 0.68125546875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 38379], ['ood', 11940], ['ood', 34586], ['ood', 22066], ['id', 43791]], 'labels': [6, 4, 7, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9180620312690735})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7634725570678711})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8261733055114746})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8486658334732056})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8294007778167725})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8619, 'crossentropy': 0.67777197265625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 34885], ['ood', 6345], ['ood', 56873], ['id', 29939], ['id', 742]], 'labels': [2, 8, 3, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9361082911491394})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8021844625473022})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7768943905830383})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8057018518447876})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7977634072303772})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9072715044021606})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.634592333984375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41814], ['ood', 41277], ['ood', 7515], ['id', 47514], ['ood', 27985]], 'labels': [6, 8, 3, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8910270929336548})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7202643752098083})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7250715494155884})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7726354002952576})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8353004455566406})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8752, 'crossentropy': 0.647143603515625}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 4880], ['ood', 40823], ['id', 7247], ['ood', 49345], ['id', 55309]], 'labels': [2, 6, 0, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9543368816375732})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7803308963775635})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.773390531539917})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8019616603851318})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9131940603256226})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9191063642501831})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8748, 'crossentropy': 0.66194619140625}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 58515], ['ood', 38208], ['ood', 5888], ['ood', 49239], ['ood', 53062]], 'labels': [5, 9, 3, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9091565608978271})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7489084601402283})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7592287063598633})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7881355881690979})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8092644810676575})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8752, 'crossentropy': 0.645351416015625}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 28111], ['ood', 4519], ['id', 37682], ['id', 23733], ['id', 8069]], 'labels': [1, 8, 9, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8991180062294006})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7628940343856812})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8518661856651306})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9040118455886841})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8784369826316833})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8747, 'crossentropy': 0.651017236328125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 8878], ['id', 24953], ['id', 47827], ['id', 5814], ['ood', 25404]], 'labels': [8, 8, 6, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.982768714427948})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7816967964172363})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8752942085266113})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8034804463386536})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8921727538108826})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8576, 'crossentropy': 0.674212255859375}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 58913], ['id', 44718], ['id', 52340], ['id', 36959], ['id', 24467]], 'labels': [2, 2, 9, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8403714895248413})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7172218561172485})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7020390033721924})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6825772523880005})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.757109522819519})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.805740237236023})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7987399101257324})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.58779541015625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 52463], ['id', 23089], ['ood', 44272], ['ood', 54455], ['ood', 30962]], 'labels': [7, 2, 1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9176275730133057})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6818821430206299})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7067959308624268})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6861777305603027})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.727352499961853})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8842, 'crossentropy': 0.6166630859375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 41455], ['ood', 24309], ['id', 31178], ['ood', 49869], ['id', 32261]], 'labels': [8, 7, 3, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9147508144378662})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7079863548278809})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7252790927886963})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6999976634979248})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7268086671829224})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8268605470657349})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7710031270980835})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8921, 'crossentropy': 0.584781201171875}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 40771], ['ood', 34778], ['ood', 33255], ['id', 25114], ['ood', 31916]], 'labels': [8, 3, 7, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9623541235923767})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7209352850914001})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6701096892356873})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7019084692001343})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7561391592025757})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7354292869567871})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8865, 'crossentropy': 0.57638818359375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 1218], ['id', 53873], ['id', 237], ['id', 47985], ['ood', 19953]], 'labels': [3, 4, 4, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9046103954315186})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7198054790496826})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6741042137145996})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7262802124023438})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7613611221313477})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7810828685760498})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8856, 'crossentropy': 0.602487841796875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 26774], ['id', 42716], ['id', 6056], ['id', 38376], ['id', 39713]], 'labels': [1, 1, 2, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9709711670875549})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.712817907333374})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7050849199295044})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6658294200897217})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7525919675827026})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7704904079437256})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.764826774597168})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8862, 'crossentropy': 0.5802310546875}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 43406], ['id', 52150], ['ood', 46254], ['id', 4267], ['id', 55891]], 'labels': [1, 6, 6, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0267765522003174})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7284344434738159})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7084349989891052})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6537955403327942})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7308720350265503})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7249921560287476})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7631694078445435})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8962, 'crossentropy': 0.55020673828125}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 54098], ['ood', 45730], ['id', 50180], ['ood', 35201], ['id', 9234]], 'labels': [9, 9, 8, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.85093092918396})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6610246896743774})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6738851070404053})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6600546836853027})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.753503680229187})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6783000230789185})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7487207055091858})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.5491375}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 10464], ['id', 34282], ['id', 59150], ['id', 4585], ['id', 40150]], 'labels': [2, 1, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9041930437088013})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7051565647125244})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.614668607711792})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6398977041244507})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7289761304855347})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7343097925186157})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8918, 'crossentropy': 0.56260576171875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 50443], ['id', 30068], ['ood', 52927], ['id', 22161], ['ood', 6760]], 'labels': [5, 1, 2, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8348248600959778})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6318323612213135})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7051389217376709})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6817768216133118})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7220438718795776})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.892, 'crossentropy': 0.56641123046875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 18178], ['id', 54716], ['id', 40045], ['id', 27215], ['id', 40071]], 'labels': [5, 1, 1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8582208156585693})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6494467258453369})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6350467801094055})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6827102899551392})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7028516530990601})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7488948106765747})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8843, 'crossentropy': 0.579875830078125}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 21327], ['id', 4052], ['id', 19044], ['id', 38500], ['id', 11482]], 'labels': [6, 8, 4, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9293367862701416})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7069814801216125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6796397566795349})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6503372192382812})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7916703820228577})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.738564670085907})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8011401295661926})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8927, 'crossentropy': 0.566717138671875}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 958], ['ood', 19131], ['ood', 14601], ['ood', 55311], ['id', 5740]], 'labels': [8, 7, 1, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9168765544891357})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6918595433235168})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7012444734573364})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.743158757686615})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7064365744590759})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.889, 'crossentropy': 0.61084765625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 1922], ['id', 41744], ['id', 13363], ['id', 30880], ['ood', 15490]], 'labels': [1, 1, 4, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8396695852279663})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7563390731811523})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6510186195373535})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7089004516601562})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6891292333602905})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7298521995544434})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8882, 'crossentropy': 0.607545654296875}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 14826], ['ood', 13901], ['ood', 51725], ['ood', 38327], ['ood', 53346]], 'labels': [2, 4, 0, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9290596842765808})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7033274173736572})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6849359273910522})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6681342124938965})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7819699048995972})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7391548156738281})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8322927355766296})
store['active_learning_steps'][55]['training']['best_epoch']=4
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.601836572265625}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 8669], ['id', 6357], ['ood', 252], ['ood', 41939], ['ood', 59629]], 'labels': [9, 0, 6, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8917317390441895})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6920230984687805})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6212666034698486})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6984750628471375})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7573251724243164})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7093366384506226})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.535174609375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 1325], ['ood', 27872], ['ood', 33502], ['id', 39551], ['id', 12667]], 'labels': [0, 6, 9, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9013935327529907})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7032973766326904})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.681344747543335})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6593236923217773})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6761343479156494})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.709242582321167})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7504851818084717})
store['active_learning_steps'][57]['training']['best_epoch']=4
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.554767578125}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 13608], ['id', 25687], ['ood', 10591], ['ood', 3427], ['id', 51946]], 'labels': [8, 1, 7, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9502850770950317})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6500301361083984})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6972638964653015})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.658623456954956})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.764951229095459})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.57011923828125}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 29236], ['ood', 38785], ['ood', 28618], ['id', 26600], ['id', 41448]], 'labels': [9, 2, 6, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9035353660583496})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6932384967803955})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.721084713935852})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6439546346664429})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6946170330047607})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7142799496650696})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7383901476860046})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.546158447265625}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 57685], ['id', 28661], ['ood', 59595], ['ood', 9432], ['ood', 3651]], 'labels': [0, 7, 2, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9065879583358765})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7142413854598999})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6484346985816956})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6322910785675049})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7119894027709961})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7093620300292969})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6817153692245483})
store['active_learning_steps'][60]['training']['best_epoch']=4
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9016, 'crossentropy': 0.533722021484375}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 44028], ['ood', 50885], ['ood', 58907], ['id', 55189], ['ood', 58351]], 'labels': [9, 2, 7, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8792115449905396})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6929970979690552})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7226929664611816})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7040873765945435})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6481225490570068})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6877859830856323})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.714136004447937})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6794874668121338})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.531831591796875}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 28900], ['ood', 56730], ['id', 19501], ['id', 18690], ['ood', 50382]], 'labels': [2, 0, 3, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.964819610118866})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7571300864219666})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7260600328445435})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6271963715553284})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7027503848075867})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7005524635314941})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7425302267074585})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.567047802734375}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 46273], ['id', 59043], ['ood', 51052], ['id', 36552], ['id', 2255]], 'labels': [0, 0, 5, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.961701512336731})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.708092451095581})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.68703293800354})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6425869464874268})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7032421827316284})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.662334680557251})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.698900043964386})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.546336181640625}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 41408], ['id', 18335], ['ood', 29815], ['ood', 20973], ['id', 53663]], 'labels': [6, 8, 9, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9782583117485046})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7226758599281311})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7167173624038696})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6974704265594482})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7153590321540833})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7789265513420105})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.738000750541687})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8975, 'crossentropy': 0.583623046875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 32252], ['ood', 45233], ['ood', 49094], ['ood', 43015], ['id', 8776]], 'labels': [7, 1, 3, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.962704062461853})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6859566569328308})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6820839643478394})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6745120882987976})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6275004148483276})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6716040372848511})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7268158793449402})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6846196055412292})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.54703916015625}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 40704], ['ood', 26022], ['id', 12332], ['ood', 21012], ['id', 23621]], 'labels': [9, 5, 4, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9275170564651489})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6623942852020264})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6189058423042297})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6931333541870117})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7306405901908875})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7143582105636597})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.528659619140625}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 2462], ['id', 30635], ['ood', 11062], ['ood', 14436], ['id', 10433]], 'labels': [1, 8, 5, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9060577154159546})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6652535796165466})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6585080623626709})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6681780219078064})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6544836163520813})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6724042296409607})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7067551016807556})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7378078699111938})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9033, 'crossentropy': 0.5354353515625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 26188], ['id', 50175], ['ood', 9143], ['id', 18758], ['id', 27142]], 'labels': [1, 3, 8, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9869954586029053})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6925892233848572})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6385682821273804})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7306508421897888})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6346040964126587})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6484777927398682})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6722010970115662})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7317211627960205})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.553755517578125}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 7154], ['ood', 57340], ['id', 8090], ['ood', 48673], ['ood', 5248]], 'labels': [5, 3, 7, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8502166867256165})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6701846718788147})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.61553955078125})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6405304670333862})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6549386978149414})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6658530831336975})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.529433935546875}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 17863], ['id', 16006], ['id', 44816], ['ood', 49624], ['id', 46605]], 'labels': [0, 9, 5, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9452208280563354})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6998850107192993})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.684502124786377})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6661180257797241})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.653168797492981})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.646493136882782})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6099295616149902})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6532269716262817})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6729668378829956})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6933544278144836})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.554700927734375}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 39939], ['ood', 27429], ['id', 3644], ['id', 6844], ['ood', 44432]], 'labels': [0, 6, 1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9895756244659424})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7574924230575562})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7254654169082642})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6553564667701721})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7337572574615479})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7153714895248413})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7383764982223511})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8967, 'crossentropy': 0.571960205078125}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 19848], ['id', 4453], ['id', 2910], ['ood', 35196], ['ood', 43213]], 'labels': [2, 0, 6, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9868718981742859})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6494505405426025})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6167786121368408})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6422979831695557})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6469540596008301})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6199667453765869})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.517705078125}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 5724], ['ood', 9309], ['ood', 41718], ['id', 27815], ['ood', 39387]], 'labels': [2, 2, 3, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9152601957321167})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6687062382698059})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6370502710342407})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.596717119216919})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5979979634284973})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6359345316886902})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6901261806488037})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9021, 'crossentropy': 0.53808994140625}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 53489], ['id', 13822], ['ood', 49927], ['ood', 55140], ['ood', 6235]], 'labels': [1, 0, 7, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9084669351577759})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6219632625579834})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5881904363632202})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6056700348854065})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6266865730285645})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6644814014434814})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.5007623046875}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 7163], ['id', 32366], ['ood', 7407], ['ood', 31608], ['id', 26023]], 'labels': [9, 9, 9, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9382306337356567})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6629524230957031})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6111277937889099})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5896965265274048})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6258708238601685})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.649303674697876})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6437377333641052})
store['active_learning_steps'][75]['training']['best_epoch']=4
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.506265771484375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 31587], ['id', 6731], ['ood', 4347], ['ood', 53863], ['ood', 48574]], 'labels': [6, 8, 9, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8661575317382812})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6793678998947144})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.664955735206604})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6388935446739197})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5942385196685791})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6761318445205688})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6201466917991638})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6832976341247559})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.491801708984375}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 9913], ['ood', 36783], ['ood', 51336], ['id', 58383], ['id', 15715]], 'labels': [2, 7, 3, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.965430736541748})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6890507936477661})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6153213977813721})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6401301622390747})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6874504685401917})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6047789454460144})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6667133569717407})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6543997526168823})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7142409086227417})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.5010052734375}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 45702], ['ood', 13000], ['ood', 48834], ['ood', 30470], ['id', 53415]], 'labels': [6, 9, 2, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0422556400299072})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6630477905273438})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5846211910247803})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6080812215805054})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5485478043556213})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5925107598304749})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6230116486549377})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5906074643135071})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.478420263671875}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 28338], ['id', 21693], ['ood', 58121], ['ood', 6318], ['id', 6803]], 'labels': [0, 7, 4, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9048317670822144})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.681591808795929})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6297298669815063})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5680677890777588})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5820596218109131})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6129099130630493})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6606435775756836})
store['active_learning_steps'][79]['training']['best_epoch']=4
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.486435791015625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 33462], ['ood', 48941], ['id', 23886], ['id', 58889], ['id', 24995]], 'labels': [1, 1, 1, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8895062208175659})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6869229078292847})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6040005087852478})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.625481903553009})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6334939002990723})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6514331698417664})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.498605615234375}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 28301], ['ood', 52176], ['id', 58238], ['id', 27270], ['ood', 40801]], 'labels': [8, 4, 1, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.030099868774414})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6713005304336548})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5900746583938599})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5863927006721497})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5981266498565674})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6047284603118896})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5769083499908447})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5891183614730835})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6201784610748291})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6062657833099365})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.49815078125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 35346], ['ood', 51394], ['ood', 53647], ['id', 6330], ['ood', 26881]], 'labels': [3, 7, 0, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9503503441810608})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7178093791007996})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6209226250648499})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.634945273399353})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5924297571182251})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6448112726211548})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7278417944908142})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6404232978820801})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.51093935546875}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 8368], ['ood', 6276], ['id', 55358], ['ood', 31854], ['ood', 42054]], 'labels': [0, 8, 1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8702833652496338})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6129112243652344})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5924824476242065})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6277270317077637})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6189846992492676})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6141955852508545})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.504696142578125}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 42833], ['id', 5816], ['ood', 39878], ['ood', 32650], ['ood', 11396]], 'labels': [8, 2, 7, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.924573540687561})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7059405446052551})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6162153482437134})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5674300193786621})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5768195390701294})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6364610195159912})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5857795476913452})
store['active_learning_steps'][84]['training']['best_epoch']=4
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.47988447265625}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 53173], ['id', 22373], ['ood', 51960], ['ood', 3016], ['id', 13669]], 'labels': [7, 0, 9, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8821388483047485})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.641332745552063})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5163357257843018})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5430492162704468})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.549465537071228})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5504201650619507})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.4551330078125}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 15105], ['ood', 37417], ['id', 32802], ['ood', 21388], ['ood', 53322]], 'labels': [1, 6, 4, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0649986267089844})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6942497491836548})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6301037073135376})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.555799126625061})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5926973819732666})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6197313666343689})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6576201915740967})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.50267705078125}
