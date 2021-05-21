store = {}
store['timestamp']=1621477518
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=40']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=40
store['worker_id']=40
store['num_workers']=80
store['config']={'seed': 1276, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.32376766204834})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5265793800354004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.035111904144287})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1663146018981934})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6967, 'crossentropy': 2.0929498046875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36281], ['id', 28520], ['id', 54481], ['id', 12196], ['id', 39103]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1895951721906277, 2.21061362890863, 3.008482816240594, 3.566635630659051, 3.9442681927602976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.085078239440918})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4815385341644287})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.748728036880493})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.4332613945007324})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.319239854812622})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.8492441177368164})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.894515037536621})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8593788146972656})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6949, 'crossentropy': 2.349727734375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 20641], ['id', 6720], ['id', 40457], ['id', 1076], ['id', 14756]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2031417157001654, 2.247586939084791, 3.094252842418065, 3.679447119022284, 4.0551222913306475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8716590404510498})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.2644355297088623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.386603832244873})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8679728507995605})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.6187167167663574})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.695018768310547})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7036, 'crossentropy': 2.26112421875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12514], ['id', 58467], ['id', 11983], ['id', 51633], ['id', 19931]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2577619752587086, 2.315389059241854, 3.169044818132239, 3.7520819816773745, 4.093457971711935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.678970217704773})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8793580532073975})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2653353214263916})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.117832660675049})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7463, 'crossentropy': 1.45866904296875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 45256], ['id', 23104], ['id', 11708], ['id', 35784], ['id', 7891]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1414405507950125, 2.122263552890372, 2.889354448817219, 3.437059366552244, 3.8350766382405554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5682162046432495})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.782495379447937})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.208738327026367})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.0318078994750977})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.105497360229492})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.3318018913269043})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.432814121246338})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7282, 'crossentropy': 1.9917529296875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49202], ['id', 26208], ['id', 22645], ['id', 44404], ['id', 28136]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.351509373840428, 2.4140592038261657, 3.287427125865376, 3.857102865313996, 4.212196664721898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4679803848266602})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.8098175525665283})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.919999599456787})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.139627456665039})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.044649362564087})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.1218268871307373})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.311603546142578})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.276826858520508})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7607, 'crossentropy': 1.8467236328125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 7885], ['id', 12202], ['id', 24531], ['id', 52142], ['id', 11627]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.268861589632646, 2.3454560980125785, 3.204372847430231, 3.8128328823905786, 4.178974029782702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2201391458511353})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3850233554840088})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4056692123413086})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5839046239852905})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6094355583190918})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4659507274627686})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.7211530208587646})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.716278076171875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.020590305328369})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 1.34297216796875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 23140], ['id', 14506], ['id', 47132], ['id', 22579], ['id', 59314]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2239522287389875, 2.2987195838136407, 3.1599252931613986, 3.7645294367560265, 4.143893158864476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.2216359376907349})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2887582778930664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3786009550094604})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.4706250429153442})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.620255947113037})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8159, 'crossentropy': 1.11218955078125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 36810], ['id', 45274], ['id', 3676], ['id', 9318], ['id', 20217]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.113092947311185, 2.078868009499173, 2.86141763722253, 3.4735140398911017, 3.8848094925083636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2346440553665161})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4860475063323975})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.6311177015304565})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.7983026504516602})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9067798852920532})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7974, 'crossentropy': 1.3605326171875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 6598], ['id', 36323], ['id', 150], ['id', 43609], ['id', 16456]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0664025250636369, 2.0019667939643147, 2.8082132896110856, 3.4156411484071754, 3.8393203203798336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0783730745315552})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2104451656341553})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3789516687393188})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2520794868469238})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4171473979949951})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5190255641937256})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5663151741027832})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8413, 'crossentropy': 1.1760232421875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 1075], ['id', 15848], ['id', 12934], ['id', 45046], ['id', 6418]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1458645709924131, 2.2183126392441586, 3.060913230610476, 3.6792493987453767, 4.0633977937822205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1235827207565308})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1387553215026855})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2910773754119873})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4194746017456055})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.334221363067627})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6770455837249756})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3997788429260254})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.531402587890625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.629253625869751})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.41846764087677})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6210596561431885})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.6305289268493652})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.706883192062378})
store['active_learning_steps'][10]['training']['best_epoch']=10
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.851, 'crossentropy': 1.192965625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 42302], ['id', 37383], ['id', 854], ['id', 45502], ['id', 39871]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1838539908340928, 2.2817574118624115, 3.17389725936507, 3.7788547603023783, 4.160224114441502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.150804042816162})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0132514238357544})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1820735931396484})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2269566059112549})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3384368419647217})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 0.88070283203125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 55834], ['id', 30188], ['id', 4153], ['id', 54542], ['id', 16784]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9893045815993387, 1.8634625037981918, 2.6391318073706582, 3.2501633322309846, 3.697348163214887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0225403308868408})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9682254791259766})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9829999804496765})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1509299278259277})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0716798305511475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.123409628868103})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.87974453125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 52169], ['id', 11388], ['id', 15462], ['id', 25960], ['id', 10210]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0644876489103314, 1.9921801307582303, 2.7808739435582437, 3.4144557772616704, 3.8503666304697335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9661150574684143})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8412277698516846})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8903450965881348})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0084059238433838})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.022578477859497})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.062252163887024})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9789701104164124})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1523993015289307})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1153419017791748})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2461636066436768})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8741, 'crossentropy': 0.89204951171875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 12906], ['id', 31301], ['id', 13030], ['id', 57972], ['id', 8736]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1672549731597666, 2.2293188306918332, 3.1228634130424737, 3.731519332248091, 4.111146581728907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1046319007873535})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8682652711868286})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9428902864456177})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9982906579971313})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1889547109603882})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1183080673217773})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0087146759033203})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0407320261001587})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0223820209503174})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1310737133026123})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.179504632949829})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1677846908569336})
store['active_learning_steps'][14]['training']['best_epoch']=9
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8904, 'crossentropy': 0.8635890625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 39700], ['id', 10855], ['id', 38920], ['id', 20171], ['id', 6520]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2502932547037728, 2.3862901079821572, 3.2661323173147743, 3.861491574910003, 4.205542645775188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9958781003952026})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8515526056289673})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9038195610046387})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8137087821960449})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8690789341926575})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9560796022415161})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.949104905128479})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9757269620895386})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0020699501037598})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1149451732635498})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.024682641029358})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.80667421875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 43961], ['id', 44172], ['id', 3382], ['id', 12913], ['id', 29759]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2308013320213111, 2.3640671386905243, 3.282365711820302, 3.889046616936403, 4.2368781188243085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8861169815063477})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7106372117996216})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8225903511047363})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.849382758140564})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8240308165550232})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8913, 'crossentropy': 0.657367041015625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 53379], ['id', 46368], ['id', 38339], ['id', 27429], ['id', 11202]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8346987457330757, 1.62005525559317, 2.334013229527022, 2.927272619029554, 3.3934283649578845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0728594064712524})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8329600691795349})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8202444314956665})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8183717727661133})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.823875904083252})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8537306785583496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8692725300788879})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9521374702453613})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8154076337814331})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.729767236328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 49088], ['id', 49493], ['id', 3719], ['id', 50106], ['id', 49890]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.139153562206191, 2.1737273462725977, 3.0399266835069616, 3.675340761614147, 4.085357970503655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0094101428985596})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8809629678726196})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7269546985626221})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7935322523117065})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9826397895812988})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8652832508087158})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8993, 'crossentropy': 0.663008154296875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 20820], ['id', 12305], ['id', 42078], ['id', 53844], ['id', 30077]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0124056550867844, 1.934602572713203, 2.7528554877719564, 3.362839153789503, 3.8066506113404017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1477553844451904})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8487523198127747})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8852230906486511})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8694915771484375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9014972448348999})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8727895021438599})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9564549922943115})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0957075357437134})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0745141506195068})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9013, 'crossentropy': 0.736232763671875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 15945], ['id', 40732], ['id', 42337], ['id', 57523], ['id', 5842]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1546574762800113, 2.2009534729149682, 3.0751179478529433, 3.6964011043658607, 4.088651487041725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9658501148223877})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7474883794784546})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7295360565185547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7571934461593628})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8061693906784058})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.709066748046875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 16488], ['id', 5129], ['id', 43648], ['id', 224], ['id', 38256]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0069711375000827, 1.8996456597092917, 2.6267504422363395, 3.2001101803649465, 3.6293263238607034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1841862201690674})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9405328035354614})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7910202145576477})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8211215734481812})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8874751925468445})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8642945289611816})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8411683440208435})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8270695805549622})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9272964000701904})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.016108512878418})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9683901071548462})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9001, 'crossentropy': 0.7647001953125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 13719], ['id', 5188], ['id', 4822], ['id', 13335], ['id', 40046]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.2290371429371754, 2.321904397028102, 3.1978362097209043, 3.822203734727549, 4.203355952169826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9682241678237915})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7933814525604248})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8123844265937805})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7469044923782349})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9031227827072144})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8421415686607361})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8296335339546204})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9951626062393188})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9863712787628174})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0773708820343018})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.818112109375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 17079], ['id', 15893], ['id', 46134], ['id', 33383], ['id', 35084]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.233562474417849, 2.3332243155759684, 3.2299647617802716, 3.850448269950074, 4.218260565233129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1167293787002563})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7086923718452454})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7702473402023315})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7165361642837524})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6747943162918091})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7526323199272156})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8144708871841431})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8329054117202759})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.6482126953125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 5684], ['id', 43745], ['id', 31293], ['id', 43427], ['id', 38460]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.094738971139572, 2.091291720324639, 2.938780909057175, 3.5863321058299764, 4.004336195959725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0733826160430908})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6825639605522156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7385309934616089})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6425789594650269})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6772770285606384})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.704083263874054})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6844612956047058})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6626839637756348})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7352923154830933})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7640413641929626})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7371649742126465})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.601697021484375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34252], ['id', 2148], ['id', 20169], ['id', 48154], ['id', 22083]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2253094055622478, 2.3026256326668353, 3.177746124749758, 3.8014051872184114, 4.158967931590037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1148327589035034})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.670029878616333})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5791354179382324})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5788343548774719})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6092071533203125})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6691668033599854})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.67330402135849})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.545100537109375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 49517], ['id', 9180], ['id', 40158], ['id', 1573], ['id', 25622]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0649185599666868, 1.9924817532229584, 2.743470640333687, 3.3377842759114245, 3.7733897116116317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0933544635772705})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6274783611297607})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6156227588653564})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.639796257019043})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6877904534339905})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6650646924972534})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7241769433021545})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6981759071350098})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.612848699092865})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7830045223236084})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.707277774810791})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7030358910560608})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.577146630859375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 21642], ['id', 28194], ['id', 12066], ['id', 40466], ['id', 4123]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.153346134835007, 2.1907247457392787, 3.0657512992572205, 3.716330814678603, 4.120707738154828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.208080768585205})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6627352237701416})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5635493993759155})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5584297180175781})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5659931302070618})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6089974641799927})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6114981770515442})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.485519775390625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 16511], ['id', 1239], ['id', 15252], ['id', 5175], ['id', 22561]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.023049023032923, 1.9478961371375778, 2.7673654994283705, 3.3847206496606272, 3.8165034174741823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0520284175872803})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6097711324691772})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5378110408782959})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6423450708389282})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5649095773696899})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5643342137336731})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5837680101394653})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6525564193725586})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.580073356628418})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6684128046035767})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.484519921875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42703], ['id', 274], ['id', 36818], ['id', 40216], ['id', 33338]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0998334769050673, 2.094942700715279, 2.9382929610704718, 3.5630424265020126, 3.9892362019067296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1403703689575195})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.698436975479126})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.570798933506012})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5872378945350647})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5857967734336853})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6231556534767151})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6323904991149902})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6483736634254456})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6477489471435547})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7277398109436035})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7394014596939087})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.550662353515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 470], ['id', 14726], ['id', 34188], ['id', 46126], ['id', 50431]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.180623640156735, 2.2628887079342896, 3.1584834360745226, 3.772263591889888, 4.155715180329571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2030549049377441})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.652104377746582})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5292573571205139})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5243852138519287})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5267429351806641})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5774922370910645})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5682193040847778})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5825544595718384})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6691316962242126})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.50101220703125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 3070], ['id', 7803], ['id', 44753], ['id', 50930], ['id', 35326]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0164086121993798, 1.9619085409044814, 2.786136251004832, 3.4222796866791416, 3.8716273344677568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1662983894348145})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.666395902633667})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6219273209571838})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5304094552993774})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.634545087814331})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6737162470817566})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6623424291610718})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9341, 'crossentropy': 0.513283154296875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 17958], ['id', 53753], ['id', 45602], ['id', 3762], ['id', 52106]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9518373340650346, 1.8244272658369587, 2.592952656256096, 3.2389422722427037, 3.7182370270433758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1988801956176758})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6712470650672913})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.619365930557251})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5928528308868408})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6075001955032349})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5865929126739502})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6594805121421814})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6894256472587585})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9324, 'crossentropy': 0.516932958984375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 5740], ['id', 5315], ['id', 29294], ['id', 49033], ['id', 39749]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9765943089632723, 1.9035095188306386, 2.7079113174573983, 3.3543977379879433, 3.8015732661686625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2815146446228027})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5925565958023071})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6011580228805542})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5116815567016602})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5699013471603394})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5895990133285522})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5899652242660522})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5749633312225342})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6041035056114197})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.50521904296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 17518], ['id', 11482], ['id', 55906], ['id', 26527], ['id', 8093]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.004577547583719, 1.9395726530308943, 2.749786158385037, 3.3830863553901604, 3.842474137737578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2561869621276855})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.594262957572937})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5161775350570679})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.559443473815918})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5002381205558777})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5046731233596802})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5875506401062012})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6139642000198364})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.46024599609375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 19942], ['id', 24462], ['id', 50618], ['id', 26850], ['id', 966]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0392710791043425, 1.9838205338116994, 2.8077311087649264, 3.439884698494989, 3.882005060418658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3495395183563232})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6600630283355713})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5657087564468384})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.533441424369812})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5078819394111633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5420822501182556})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.566292405128479})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5420634150505066})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5363479852676392})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5977342128753662})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6185514330863953})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.481226123046875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 15771], ['id', 56082], ['id', 10044], ['id', 50417], ['id', 13942]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0587998700531234, 2.056608592307679, 2.883432348320671, 3.5279563484610232, 3.9737017788740463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2505353689193726})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6197154521942139})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5419250726699829})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5203391909599304})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5238155126571655})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5361645221710205})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5804217457771301})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.552771806716919})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6067994832992554})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.472881640625}
