store = {}
store['timestamp']=1620260454
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=38']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=38
store['worker_id']=38
store['num_workers']=40
store['config']={'seed': 56, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.122427463531494})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.489058256149292})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.77932071685791})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.615347146987915})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7009, 'crossentropy': 1.9213984375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 25184], ['id', 49311], ['ood', 46478], ['id', 31132], ['ood', 56586]], 'labels': [3, 0, 3, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.735244870185852})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0032529830932617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.219703197479248})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4591684341430664})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6874, 'crossentropy': 1.53985390625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 29389], ['id', 22830], ['id', 49292], ['id', 12446], ['id', 19931]], 'labels': [6, 6, 1, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6571860313415527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.0675277709960938})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.290520668029785})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.392289638519287})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6996, 'crossentropy': 1.53468037109375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 18281], ['id', 23252], ['id', 34140], ['ood', 31976], ['id', 54164]], 'labels': [8, 5, 3, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4304232597351074})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6454482078552246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7188187837600708})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7704455852508545})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7366, 'crossentropy': 1.29808076171875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 4882], ['id', 30197], ['id', 23261], ['ood', 41829], ['id', 37781]], 'labels': [6, 5, 6, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4479451179504395})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.6816176176071167})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8330113887786865})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.922743797302246})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7097, 'crossentropy': 1.33829072265625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 17145], ['id', 55372], ['ood', 22497], ['ood', 29548], ['ood', 46993]], 'labels': [8, 6, 4, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5026460886001587})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6762051582336426})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.940201997756958})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8725122213363647})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.702, 'crossentropy': 1.333089453125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 9970], ['id', 59132], ['id', 51152], ['id', 9449], ['id', 12914]], 'labels': [8, 6, 6, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4429562091827393})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8353711366653442})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.818516731262207})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.242727279663086})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6991, 'crossentropy': 1.375482421875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 3936], ['id', 31884], ['ood', 15154], ['id', 1951], ['id', 44434]], 'labels': [6, 2, 5, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.2303681373596191})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3825944662094116})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3805851936340332})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6640269756317139})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7539, 'crossentropy': 1.13416591796875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 22120], ['id', 55843], ['ood', 24232], ['ood', 13200], ['ood', 57336]], 'labels': [1, 7, 9, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1802091598510742})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3106757402420044})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.4266769886016846})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5521095991134644})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.739, 'crossentropy': 1.15488955078125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 286], ['ood', 19827], ['ood', 16937], ['id', 13065], ['ood', 21833]], 'labels': [6, 5, 4, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.321584939956665})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3807355165481567})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.521122932434082})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.6816699504852295})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7241, 'crossentropy': 1.29248447265625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 57314], ['id', 18156], ['ood', 45922], ['id', 59973], ['id', 15171]], 'labels': [3, 8, 0, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3450038433074951})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4758586883544922})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.7799298763275146})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.725887417793274})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7285, 'crossentropy': 1.3240609375}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 56739], ['ood', 28556], ['ood', 2615], ['ood', 49915], ['ood', 29691]], 'labels': [8, 4, 0, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2910358905792236})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4224629402160645})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5768883228302002})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.6601402759552002})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6977, 'crossentropy': 1.2767724609375}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 26776], ['id', 8035], ['id', 10999], ['ood', 47570], ['ood', 44245]], 'labels': [2, 9, 2, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4146873950958252})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5659575462341309})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.518155813217163})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6238772869110107})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7125, 'crossentropy': 1.32116748046875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22697], ['id', 33427], ['ood', 28925], ['id', 58565], ['id', 23575]], 'labels': [4, 0, 1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1031513214111328})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.213651418685913})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3372693061828613})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.3486454486846924})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7527, 'crossentropy': 1.07491806640625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 40939], ['ood', 27347], ['id', 29526], ['id', 29982], ['ood', 41466]], 'labels': [5, 8, 6, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.106820821762085})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2048901319503784})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2879140377044678})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3801069259643555})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7573, 'crossentropy': 1.04102802734375}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 22603], ['id', 46258], ['ood', 21084], ['id', 32062], ['id', 31628]], 'labels': [8, 8, 4, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0361462831497192})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1670780181884766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.272955298423767})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.4516899585723877})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7737, 'crossentropy': 0.9918345703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 15109], ['id', 49439], ['ood', 34345], ['ood', 6719], ['id', 1299]], 'labels': [4, 8, 2, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1785991191864014})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.192492961883545})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2694294452667236})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.348514437675476})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7525, 'crossentropy': 1.161392578125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 37927], ['id', 8047], ['ood', 39651], ['ood', 7146], ['id', 18034]], 'labels': [3, 8, 4, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0901362895965576})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2509477138519287})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.4857721328735352})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.3889992237091064})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7645, 'crossentropy': 1.02939365234375}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 44497], ['ood', 9452], ['ood', 31124], ['id', 50149], ['id', 26761]], 'labels': [3, 2, 4, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.04709792137146})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1114518642425537})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1568386554718018})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.2202165126800537})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7713, 'crossentropy': 1.0103375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 504], ['ood', 27181], ['id', 29950], ['id', 42414], ['ood', 30498]], 'labels': [0, 8, 6, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0240739583969116})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1208765506744385})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2426756620407104})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3294401168823242})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7642, 'crossentropy': 1.03950732421875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 33044], ['ood', 26671], ['id', 20474], ['ood', 57350], ['ood', 33017]], 'labels': [5, 5, 1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0195149183273315})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1587022542953491})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3452470302581787})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.335843801498413})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7673, 'crossentropy': 1.00934140625}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 32517], ['id', 35670], ['ood', 4312], ['ood', 19461], ['id', 36427]], 'labels': [1, 2, 3, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1142081022262573})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0830726623535156})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.051539421081543})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2864940166473389})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2450857162475586})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.3743343353271484})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7904, 'crossentropy': 1.08118193359375}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 52938], ['ood', 49977], ['ood', 16596], ['id', 43370], ['ood', 11662]], 'labels': [7, 9, 7, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9006549119949341})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9570779800415039})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.013946533203125})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0579009056091309})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.785, 'crossentropy': 0.9195396484375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 12558], ['id', 41831], ['ood', 36796], ['ood', 53316], ['id', 52742]], 'labels': [1, 8, 8, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0048400163650513})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9667062759399414})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2108170986175537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1960701942443848})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2315974235534668})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7903, 'crossentropy': 0.98525498046875}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 43685], ['ood', 41423], ['ood', 57319], ['ood', 50765], ['id', 1797]], 'labels': [2, 4, 5, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9304906725883484})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0260279178619385})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0298728942871094})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1166701316833496})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7796, 'crossentropy': 0.96495751953125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 27070], ['id', 42375], ['id', 23668], ['id', 2200], ['ood', 44884]], 'labels': [0, 3, 5, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9508600234985352})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8948361873626709})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8979157209396362})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9735504388809204})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0181922912597656})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8098, 'crossentropy': 0.84715244140625}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 24180], ['ood', 27891], ['id', 30996], ['id', 56784], ['ood', 57424]], 'labels': [8, 5, 1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9109055995941162})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8166164755821228})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.857698917388916})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9530417323112488})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9829279184341431})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8326, 'crossentropy': 0.82419033203125}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 658], ['ood', 37777], ['ood', 20200], ['id', 33071], ['ood', 19129]], 'labels': [4, 8, 1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8933107852935791})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8236500024795532})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8384799957275391})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.876897931098938})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0387532711029053})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8347, 'crossentropy': 0.8016494140625}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 22826], ['ood', 2168], ['id', 5385], ['id', 5283], ['id', 56935]], 'labels': [1, 2, 6, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9775716066360474})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7524167895317078})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8516815900802612})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9045597314834595})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7961837649345398})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8527, 'crossentropy': 0.73608515625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 22872], ['ood', 9740], ['ood', 38997], ['id', 35228], ['id', 8344]], 'labels': [6, 4, 9, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9164087772369385})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7114992141723633})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7850689888000488})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8273788094520569})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8519567251205444})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8541, 'crossentropy': 0.725750537109375}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 10531], ['id', 700], ['ood', 30545], ['id', 23384], ['ood', 33424]], 'labels': [3, 4, 7, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9553149938583374})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6925463676452637})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.699161171913147})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7880070209503174})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8196132183074951})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8518, 'crossentropy': 0.715289208984375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 45955], ['ood', 26562], ['ood', 19402], ['id', 15950], ['ood', 14712]], 'labels': [1, 5, 6, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8249483108520508})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7655471563339233})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7503811120986938})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7462499737739563})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8233909010887146})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8972313404083252})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9580184817314148})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8729, 'crossentropy': 0.71816123046875}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 25178], ['ood', 42940], ['ood', 32744], ['id', 57575], ['id', 2284]], 'labels': [8, 6, 9, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8853482604026794})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.739025890827179})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.801663875579834})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8386415243148804})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8403754830360413})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.684368994140625}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 15936], ['ood', 4107], ['id', 53494], ['ood', 40508], ['ood', 50314]], 'labels': [7, 9, 2, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8510243892669678})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6986805200576782})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7064714431762695})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7265013456344604})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8999404311180115})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8638, 'crossentropy': 0.652311865234375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 41968], ['ood', 32818], ['id', 59], ['id', 8437], ['ood', 8159]], 'labels': [4, 6, 1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8919965624809265})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7273771166801453})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7691325545310974})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8268431425094604})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8065916299819946})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8618, 'crossentropy': 0.680569873046875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 55283], ['id', 21108], ['ood', 40504], ['id', 31423], ['id', 26252]], 'labels': [3, 9, 5, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8339859843254089})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.732094407081604})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.760527491569519})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8141976594924927})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.852616012096405})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8518, 'crossentropy': 0.6897064453125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 18940], ['ood', 23822], ['ood', 56895], ['ood', 49429], ['ood', 53294]], 'labels': [2, 0, 1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8392093181610107})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.687030553817749})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6939218044281006})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7374283671379089})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8171358108520508})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8609, 'crossentropy': 0.702453857421875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 13446], ['id', 29163], ['id', 33665], ['id', 55488], ['id', 56361]], 'labels': [4, 6, 0, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9349708557128906})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7109895944595337})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6721572875976562})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7507994174957275})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7741173505783081})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7486253976821899})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8802, 'crossentropy': 0.621811865234375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 37177], ['id', 58301], ['ood', 5923], ['id', 7658], ['id', 25453]], 'labels': [1, 6, 3, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8554216623306274})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6973544359207153})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8007291555404663})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7478861212730408})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8096528053283691})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 0.6875734375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 4151], ['id', 26552], ['id', 18023], ['ood', 53955], ['ood', 18844]], 'labels': [8, 5, 6, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.799532413482666})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7131903767585754})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6876974701881409})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7378793954849243})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7565025687217712})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8381123542785645})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8771, 'crossentropy': 0.631313818359375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 33406], ['ood', 47181], ['id', 22831], ['id', 11277], ['id', 43286]], 'labels': [7, 3, 1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8130524158477783})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7384691834449768})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7111492156982422})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.688264787197113})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7703686952590942})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7552429437637329})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8097469806671143})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8769, 'crossentropy': 0.67718828125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 8340], ['id', 57924], ['id', 15899], ['id', 41789], ['id', 32005]], 'labels': [8, 0, 9, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8034330606460571})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7702534198760986})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7244569063186646})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7740585207939148})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8247535228729248})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7845258712768555})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.627609912109375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 5022], ['ood', 44319], ['id', 7935], ['id', 58581], ['id', 41649]], 'labels': [7, 6, 3, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8822877407073975})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7425408959388733})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6992261409759521})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.758425235748291})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7850179672241211})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7396329641342163})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8644, 'crossentropy': 0.695021875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 17362], ['id', 10606], ['id', 21377], ['ood', 20245], ['id', 36388]], 'labels': [8, 3, 9, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8968716859817505})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7717552781105042})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7573860883712769})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7431632280349731})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7736830711364746})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8521496057510376})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7954651713371277})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.68992490234375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 46145], ['id', 30156], ['ood', 18509], ['ood', 26778], ['ood', 13220]], 'labels': [3, 0, 4, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8607334494590759})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7193188667297363})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7215189933776855})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7614461183547974})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7418209314346313})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8566, 'crossentropy': 0.6870435546875}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 34569], ['ood', 45675], ['id', 32207], ['ood', 40895], ['ood', 4646]], 'labels': [9, 6, 0, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8823281526565552})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6966769099235535})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7266802787780762})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7644208669662476})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8013176918029785})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8607, 'crossentropy': 0.66686357421875}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 48061], ['id', 37444], ['ood', 38248], ['ood', 49290], ['id', 43593]], 'labels': [1, 8, 7, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8338565826416016})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6476250290870667})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6532724499702454})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7398646473884583})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6614357233047485})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8652, 'crossentropy': 0.62763056640625}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 5473], ['id', 34629], ['ood', 45368], ['id', 38424], ['ood', 12032]], 'labels': [7, 3, 7, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9018430709838867})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6934000253677368})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6474854350090027})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6943320035934448})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7596949338912964})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7509740591049194})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8813, 'crossentropy': 0.61494072265625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 34096], ['id', 59832], ['ood', 2657], ['id', 41274], ['id', 30807]], 'labels': [1, 1, 2, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8735268115997314})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7236560583114624})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7359043955802917})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7467226982116699})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6777951717376709})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.781320333480835})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8165974617004395})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7493231296539307})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8848, 'crossentropy': 0.656126123046875}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 28319], ['ood', 49310], ['ood', 19452], ['id', 32037], ['ood', 28986]], 'labels': [9, 5, 2, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8590781688690186})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6943842172622681})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7890213131904602})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7265753746032715})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.776993989944458})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8703, 'crossentropy': 0.643530517578125}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 58626], ['ood', 57802], ['id', 12586], ['ood', 20362], ['id', 22573]], 'labels': [2, 1, 8, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.884206235408783})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6997179985046387})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7257700562477112})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7011432647705078})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6479392051696777})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7217930555343628})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7883563041687012})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8074121475219727})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.64780166015625}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 31146], ['id', 6703], ['ood', 50968], ['ood', 4030], ['id', 49966]], 'labels': [4, 8, 7, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8352043628692627})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6871972680091858})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6398969888687134})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.677830159664154})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7832138538360596})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7539701461791992})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8889, 'crossentropy': 0.60517119140625}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 34279], ['id', 28235], ['id', 5067], ['id', 43663], ['id', 35358]], 'labels': [2, 1, 3, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8244495987892151})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6392014026641846})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6759973168373108})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6761410236358643})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7506383657455444})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8711, 'crossentropy': 0.647065673828125}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 34237], ['id', 48844], ['ood', 41714], ['ood', 19036], ['ood', 23787]], 'labels': [0, 1, 6, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9014689922332764})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6820489764213562})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6242066621780396})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7381867170333862})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7287532687187195})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6678928732872009})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8884, 'crossentropy': 0.58503623046875}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 12186], ['ood', 46903], ['id', 36823], ['ood', 44359], ['id', 17513]], 'labels': [1, 6, 7, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8110823631286621})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6872156858444214})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6163773536682129})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.637300968170166})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7845168113708496})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8390704393386841})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8874, 'crossentropy': 0.614708642578125}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 32760], ['id', 57964], ['ood', 48080], ['id', 39647], ['ood', 2219]], 'labels': [9, 2, 3, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8381991386413574})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6544492244720459})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.642632007598877})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6035703420639038})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6065572500228882})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7489440441131592})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7132513523101807})
store['active_learning_steps'][55]['training']['best_epoch']=4
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8964, 'crossentropy': 0.5838068359375}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 55050], ['ood', 46416], ['id', 44294], ['ood', 19976], ['id', 37839]], 'labels': [1, 5, 4, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8471629619598389})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6295819878578186})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6970120668411255})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6571361422538757})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7013353109359741})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8835, 'crossentropy': 0.61282216796875}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 18238], ['id', 54904], ['id', 55067], ['ood', 25842], ['ood', 40795]], 'labels': [6, 5, 1, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8717752695083618})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.708160400390625})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6483151912689209})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6609450578689575})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6607669591903687})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6611289978027344})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.60855283203125}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 26821], ['id', 14334], ['id', 56878], ['ood', 42415], ['ood', 13324]], 'labels': [5, 0, 6, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8303486704826355})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6616708040237427})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5787630081176758})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6108707785606384})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6384453773498535})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6152248978614807})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8946, 'crossentropy': 0.6001833984375}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 33655], ['id', 26032], ['ood', 17804], ['id', 24903], ['ood', 55298]], 'labels': [3, 6, 5, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9591808915138245})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6702768802642822})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6576297283172607})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7026244401931763})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7236883640289307})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7045934200286865})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8795, 'crossentropy': 0.6233412109375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 23280], ['ood', 39525], ['id', 43210], ['ood', 14228], ['ood', 23315]], 'labels': [1, 4, 9, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.798302412033081})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6809256076812744})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5990651845932007})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7522652745246887})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6072432994842529})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6801514625549316})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8879, 'crossentropy': 0.57923701171875}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 22243], ['id', 751], ['ood', 8049], ['id', 38872], ['id', 59227]], 'labels': [4, 5, 6, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8462458848953247})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7048578858375549})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6186144351959229})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7214775681495667})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6454916000366211})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6461881995201111})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.626149462890625}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 42755], ['id', 11598], ['id', 28693], ['ood', 20472], ['ood', 31967]], 'labels': [3, 4, 3, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8631156086921692})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6064484119415283})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6358306407928467})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5863274335861206})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6461679339408875})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.697809100151062})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6776735782623291})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.601828759765625}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 45594], ['ood', 3330], ['ood', 10118], ['ood', 18518], ['id', 13777]], 'labels': [1, 7, 2, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.868262767791748})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6350439190864563})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6146963834762573})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6690114736557007})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.616265058517456})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6373792290687561})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.565008935546875}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 8575], ['id', 45549], ['ood', 1942], ['id', 57213], ['ood', 12532]], 'labels': [1, 6, 0, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8197234869003296})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6647228598594666})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5811810493469238})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5956306457519531})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6209980249404907})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6214722990989685})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.557644384765625}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 32706], ['id', 57516], ['ood', 9024], ['ood', 30286], ['ood', 44300]], 'labels': [1, 1, 6, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.935052216053009})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.661338210105896})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6191898584365845})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6253237724304199})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5958526134490967})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6185787320137024})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6683748960494995})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6570372581481934})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.561849609375}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 34504], ['ood', 52552], ['id', 13634], ['ood', 20473], ['ood', 27304]], 'labels': [9, 7, 4, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8556399345397949})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5891024470329285})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5991010665893555})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6235013604164124})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6451191306114197})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.569638330078125}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 25700], ['ood', 41383], ['id', 34088], ['id', 21145], ['id', 10724]], 'labels': [7, 5, 7, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7344112396240234})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5807502865791321})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5623654723167419})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5721664428710938})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5660275220870972})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5537695288658142})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6296952366828918})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5826377272605896})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6286568641662598})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.524940576171875}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 32476], ['ood', 49222], ['id', 26983], ['ood', 17619], ['id', 13529]], 'labels': [5, 2, 6, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8085106611251831})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6178526878356934})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6091815233230591})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6262972354888916})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5838736295700073})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5805763006210327})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6182399392127991})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6517404317855835})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6271708011627197})
store['active_learning_steps'][68]['training']['best_epoch']=6
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.56406201171875}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 48872], ['ood', 2247], ['id', 13913], ['id', 21923], ['ood', 19163]], 'labels': [1, 1, 0, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9087094068527222})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7095305919647217})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6860489249229431})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7165006399154663})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6227428913116455})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6930049061775208})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6416870355606079})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6723982691764832})
store['active_learning_steps'][69]['training']['best_epoch']=5
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.5874314453125}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 47953], ['ood', 36636], ['ood', 25619], ['ood', 28717], ['id', 46909]], 'labels': [1, 3, 0, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7621487975120544})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5640393495559692})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6047557592391968})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6428755521774292})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5883090496063232})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.532302685546875}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 17582], ['id', 55020], ['id', 8876], ['ood', 58529], ['id', 59322]], 'labels': [3, 8, 5, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7928070425987244})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5868507623672485})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5575398802757263})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.528952419757843})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5300459265708923})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5566428899765015})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6661605834960938})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.490721484375}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 10629], ['id', 35834], ['id', 2457], ['ood', 24186], ['id', 26948]], 'labels': [0, 7, 2, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.798004150390625})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5679277777671814})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6039353013038635})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5908313989639282})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5989068746566772})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.57239365234375}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 20558], ['ood', 36430], ['id', 50965], ['id', 273], ['ood', 338]], 'labels': [2, 7, 8, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7788297533988953})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5974307656288147})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.611726701259613})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6369292140007019})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5875215530395508})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6338454484939575})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5985393524169922})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6619963049888611})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.55775419921875}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 3093], ['id', 49981], ['id', 57835], ['ood', 26816], ['ood', 31949]], 'labels': [8, 3, 4, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8534266948699951})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5748686790466309})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5990171432495117})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5899310111999512})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5371903777122498})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5929415225982666})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5835471749305725})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5460952520370483})
store['active_learning_steps'][74]['training']['best_epoch']=5
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.502600341796875}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 15006], ['id', 37072], ['id', 5999], ['id', 10010], ['id', 7736]], 'labels': [6, 5, 9, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8361820578575134})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.575218915939331})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5257065296173096})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5555934906005859})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5490083694458008})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6054888367652893})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.487537109375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 22775], ['ood', 49156], ['ood', 3921], ['ood', 15488], ['ood', 31636]], 'labels': [1, 3, 9, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8469473719596863})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6041855812072754})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5867087841033936})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6162546873092651})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5656846761703491})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5512576699256897})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5987398624420166})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.606631875038147})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.587328314781189})
store['active_learning_steps'][76]['training']['best_epoch']=6
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.529992333984375}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 18925], ['ood', 45067], ['ood', 53152], ['id', 26869], ['ood', 54929]], 'labels': [5, 5, 4, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8332480192184448})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5967100858688354})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5913174152374268})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5541955828666687})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6111136674880981})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5367379784584045})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5436019897460938})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5457360744476318})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5947321653366089})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9209, 'crossentropy': 0.498348388671875}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 11962], ['ood', 49404], ['ood', 58256], ['ood', 17003], ['id', 23478]], 'labels': [2, 3, 9, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8264667987823486})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6382998824119568})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5337352752685547})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5528361797332764})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.636981189250946})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.544450044631958})
store['active_learning_steps'][78]['training']['best_epoch']=3
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.520093896484375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 50375], ['ood', 45963], ['ood', 37982], ['id', 19751], ['ood', 39286]], 'labels': [7, 7, 8, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9029926061630249})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.597480297088623})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.558165967464447})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.604698121547699})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6012436151504517})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5955654382705688})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.52092216796875}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 27123], ['id', 40424], ['ood', 4367], ['id', 52109], ['ood', 46187]], 'labels': [1, 4, 2, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8677543997764587})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6248721480369568})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5756412744522095})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5704275965690613})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.530709981918335})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6226791143417358})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5732927322387695})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5156888961791992})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5610202550888062})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5836809873580933})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5936434268951416})
store['active_learning_steps'][80]['training']['best_epoch']=8
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.4847083984375}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 54084], ['ood', 47647], ['ood', 19454], ['ood', 44767], ['ood', 3311]], 'labels': [3, 2, 2, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8571596741676331})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6034866571426392})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5341084003448486})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5451259016990662})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5607519149780273})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6466610431671143})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.49122861328125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 45827], ['id', 19149], ['ood', 51626], ['id', 31], ['ood', 22636]], 'labels': [4, 2, 2, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8219640254974365})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5376782417297363})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4915143847465515})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4974632263183594})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5323492884635925})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5076169967651367})
store['active_learning_steps'][82]['training']['best_epoch']=3
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.486490576171875}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 6593], ['ood', 56656], ['id', 13087], ['id', 42303], ['ood', 45624]], 'labels': [0, 9, 6, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8338304162025452})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6532068252563477})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5817497968673706})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6342068314552307})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6481717824935913})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6112985014915466})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.53848154296875}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 2661], ['ood', 50246], ['ood', 52132], ['ood', 28193], ['ood', 10052]], 'labels': [3, 8, 8, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.814401388168335})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6099135875701904})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5628520846366882})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5509018301963806})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5422507524490356})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5661243796348572})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5542119145393372})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5692850351333618})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.47543720703125}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 58083], ['ood', 36149], ['id', 44190], ['id', 21607], ['ood', 15050]], 'labels': [1, 9, 4, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8463749289512634})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6165355443954468})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5874900221824646})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5559953451156616})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48978191614151})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5559308528900146})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.619194507598877})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5937159061431885})
store['active_learning_steps'][85]['training']['best_epoch']=5
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9156, 'crossentropy': 0.48431416015625}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 23276], ['id', 49058], ['ood', 28397], ['id', 9711], ['id', 56040]], 'labels': [4, 7, 7, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.783767819404602})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6173980236053467})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.578343391418457})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5358400344848633})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.532757043838501})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5599439740180969})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5326610803604126})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5589293241500854})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5662573575973511})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6180206537246704})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.92, 'crossentropy': 0.4885822265625}
