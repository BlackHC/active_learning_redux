store = {}
store['timestamp']=1621034426
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=12']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=30
store['config']={'seed': 1250, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.636814594268799})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6288998126983643})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.4489307403564453})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.803103446960449})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.573, 'crossentropy': 2.925276171875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3690613508224487})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.4087109565734863})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.353629231452942})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 14715], ['ood', 8968], ['ood', 2337], ['ood', 7274], ['ood', 33126], ['ood', 41846], ['ood', 47474], ['ood', 13868], ['ood', 25180], ['ood', 17204]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.3373347520828247, 1.2299131751060486, 1.2275902032852173, 1.2241957187652588, 1.2187885642051697, 1.216581106185913, 1.2152146697044373, 1.214340627193451, 1.2121531963348389, 1.2097673416137695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.8499670028686523})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.5180184841156006})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.929457187652588})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.3303885459899902})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.581, 'crossentropy': 1.8873583984375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.2521781921386719})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.213322401046753})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.2130095958709717})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 40979], ['id', 32462], ['id', 9290], ['id', 46434], ['id', 20150], ['id', 19443], ['id', 58300], ['id', 21376], ['id', 18007], ['id', 44751]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6536327600479126, 0.6317813992500305, 0.6114594340324402, 0.6077322959899902, 0.5998212099075317, 0.586658775806427, 0.5837255120277405, 0.5802438259124756, 0.5745127201080322, 0.5703388452529907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.5768640041351318})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.248525381088257})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.537705898284912})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.8750619888305664})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.573, 'crossentropy': 1.58497451171875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2940690517425537})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2299233675003052})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.217487096786499})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 29715], ['id', 25420], ['id', 14832], ['id', 12890], ['id', 35207], ['id', 10960], ['id', 22097], ['id', 50045], ['id', 36761], ['id', 58802]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.49691832065582275, 0.4878718852996826, 0.473987340927124, 0.46980828046798706, 0.46772611141204834, 0.46516191959381104, 0.46106594800949097, 0.45942240953445435, 0.4587939977645874, 0.45741069316864014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4890419244766235})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.1026010513305664})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.3675999641418457})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.6207938194274902})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.593, 'crossentropy': 1.4807048828125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.310220718383789})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.254171371459961})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.255641222000122})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 49919], ['id', 28880], ['id', 4161], ['id', 13199], ['ood', 40418], ['id', 58915], ['id', 16524], ['id', 50122], ['id', 51389], ['id', 18729]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4409693479537964, 0.4347568154335022, 0.4176591634750366, 0.41422784328460693, 0.41368186473846436, 0.41170620918273926, 0.4116479754447937, 0.4113883972167969, 0.4088281989097595, 0.4067748188972473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.473097324371338})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.6875437498092651})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.9754997491836548})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.1878676414489746})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5624, 'crossentropy': 1.48518759765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.411115050315857})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.3165128231048584})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.275003433227539})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 1669], ['ood', 54705], ['ood', 36605], ['id', 56461], ['id', 850], ['id', 4619], ['id', 59682], ['id', 57392], ['ood', 37253], ['id', 59902]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45258182287216187, 0.42570269107818604, 0.4154731035232544, 0.41226136684417725, 0.4087699055671692, 0.4065420627593994, 0.406282901763916, 0.4057425856590271, 0.4036593437194824, 0.40345680713653564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.5076351165771484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5089523792266846})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9116921424865723})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.2709732055664062})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5055, 'crossentropy': 1.51322265625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.4755859375, 'crossentropy': 1.5237013101577759})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.48046875, 'crossentropy': 1.4805824756622314})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.4990234375, 'crossentropy': 1.4445819854736328})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 57486], ['id', 5355], ['id', 55098], ['id', 37549], ['id', 49472], ['id', 10251], ['id', 1707], ['id', 4034], ['id', 22991], ['id', 55765]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3206171989440918, 0.31594419479370117, 0.3068227767944336, 0.304587721824646, 0.3026334047317505, 0.29791951179504395, 0.2969827651977539, 0.2958153486251831, 0.2944457530975342, 0.2935616970062256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.421324610710144})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5867043733596802})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7758870124816895})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.1134395599365234})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5689, 'crossentropy': 1.4539798828125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.4478929042816162})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.3932914733886719})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.3975119590759277})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 32110], ['id', 24108], ['ood', 3734], ['id', 43039], ['id', 27800], ['id', 4123], ['ood', 21029], ['id', 22163], ['id', 46439], ['ood', 9440]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3125789165496826, 0.3038123846054077, 0.302820086479187, 0.301224946975708, 0.29987120628356934, 0.2959831953048706, 0.2940387725830078, 0.29383599758148193, 0.2932550311088562, 0.29254865646362305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.4340566396713257})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3499720096588135})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.63246488571167})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.8182011842727661})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8326184749603271})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6155, 'crossentropy': 1.3990501953125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.3183603286743164})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.202422857284546})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.175952672958374})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.1451754570007324})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 55812], ['ood', 38688], ['id', 28869], ['ood', 28632], ['id', 28297], ['id', 17871], ['ood', 45744], ['id', 50582], ['ood', 52866], ['id', 31587]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.43984806537628174, 0.4387991428375244, 0.41324102878570557, 0.4123653173446655, 0.4118553400039673, 0.40723133087158203, 0.39505255222320557, 0.393696665763855, 0.39229297637939453, 0.3911181688308716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.399880051612854})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3223559856414795})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4768421649932861})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.593058466911316})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.7549493312835693})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6388, 'crossentropy': 1.3211861328125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.3086142539978027})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1930243968963623})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.177915334701538})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1536331176757812})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 36311], ['id', 19649], ['ood', 3851], ['id', 50665], ['ood', 45116], ['id', 23040], ['ood', 54963], ['id', 30885], ['id', 41663], ['ood', 23931]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.44341421127319336, 0.4379011392593384, 0.43518269062042236, 0.4310038685798645, 0.4280247688293457, 0.428006649017334, 0.4270296096801758, 0.4252586364746094, 0.4238780736923218, 0.4213827848434448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.4859641790390015})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3563117980957031})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5259250402450562})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.8211472034454346})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9329360723495483})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6178, 'crossentropy': 1.37273349609375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.3307384252548218})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2361706495285034})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1759532690048218})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.1722443103790283})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 56440], ['ood', 10350], ['id', 1361], ['id', 48671], ['ood', 27335], ['ood', 48608], ['id', 38006], ['id', 31228], ['id', 52223], ['ood', 52708]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3960607051849365, 0.37512993812561035, 0.36794352531433105, 0.365645170211792, 0.3611949682235718, 0.3590049743652344, 0.3575674295425415, 0.356681764125824, 0.35387200117111206, 0.3505558967590332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.4677734375, 'crossentropy': 1.5384188890457153})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3581730127334595})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5398521423339844})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.8066984415054321})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8888401985168457})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6252, 'crossentropy': 1.32937978515625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.3478751182556152})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2919833660125732})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2498869895935059})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2502241134643555})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 56], ['id', 49130], ['id', 49078], ['id', 3895], ['id', 58636], ['id', 25974], ['id', 39471], ['id', 23586], ['id', 15030], ['id', 44540]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.27660679817199707, 0.27135157585144043, 0.2637929916381836, 0.26022279262542725, 0.257763147354126, 0.25702667236328125, 0.25636887550354004, 0.2562394142150879, 0.2525104284286499, 0.2512187957763672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.4880704879760742})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.318774938583374})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.6386053562164307})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.73503839969635})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.099893808364868})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6289, 'crossentropy': 1.35958125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3690884113311768})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2543116807937622})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.236452579498291})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2216708660125732})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 30860], ['id', 55768], ['id', 40994], ['id', 44919], ['id', 31462], ['id', 33819], ['id', 27717], ['id', 54033], ['id', 4770], ['id', 33716]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41010570526123047, 0.3995671272277832, 0.3960491418838501, 0.395064115524292, 0.3945498466491699, 0.38949263095855713, 0.38736075162887573, 0.3868962526321411, 0.38418376445770264, 0.3831596374511719]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.5534913539886475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.297277808189392})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3281974792480469})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3570237159729004})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5599250793457031})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5846, 'crossentropy': 1.29763623046875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.3632181882858276})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.2943822145462036})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2679145336151123})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.238072395324707})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 28173], ['id', 58110], ['id', 57297], ['id', 26636], ['id', 37015], ['id', 51328], ['id', 8485], ['id', 55157], ['id', 27609], ['id', 53134]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3060349225997925, 0.30448782444000244, 0.30378973484039307, 0.3024085760116577, 0.299100399017334, 0.29725217819213867, 0.2964261770248413, 0.2948564291000366, 0.29072320461273193, 0.2906876802444458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.474123477935791})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1904977560043335})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2501869201660156})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2814029455184937})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3730416297912598})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.629, 'crossentropy': 1.1917666015625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3363304138183594})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2363998889923096})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.176856279373169})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1812447309494019})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 58220], ['ood', 53467], ['ood', 37629], ['ood', 31384], ['ood', 53018], ['ood', 20802], ['ood', 34531], ['ood', 3954], ['ood', 56688], ['ood', 45754]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3746163845062256, 0.3653038740158081, 0.3640601634979248, 0.3624509572982788, 0.35412776470184326, 0.3520573377609253, 0.3507993221282959, 0.34766685962677, 0.34687042236328125, 0.3463979959487915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.4990234375, 'crossentropy': 1.5538603067398071})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2322213649749756})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1962939500808716})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.26018226146698})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3979274034500122})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4186944961547852})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6553, 'crossentropy': 1.21715654296875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2912806272506714})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.157127857208252})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.0849097967147827})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0234651565551758})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0754847526550293})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 7511], ['id', 18913], ['id', 39766], ['id', 52644], ['id', 55576], ['id', 70], ['id', 20624], ['id', 19995], ['id', 13384], ['id', 45157]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4345935583114624, 0.42950212955474854, 0.42229294776916504, 0.4016224145889282, 0.40070462226867676, 0.3992549180984497, 0.3953975439071655, 0.394234299659729, 0.3893241882324219, 0.3890039324760437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.4910715818405151})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1294115781784058})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1827168464660645})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1797239780426025})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3294804096221924})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6794, 'crossentropy': 1.1303103515625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3101370334625244})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.143208622932434})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1268473863601685})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1355955600738525})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 47079], ['id', 24953], ['id', 1344], ['id', 7456], ['id', 49135], ['id', 16154], ['id', 12078], ['id', 58560], ['id', 9302], ['id', 28543]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35733771324157715, 0.32920777797698975, 0.3256044387817383, 0.3146270513534546, 0.31316542625427246, 0.3127117156982422, 0.31079649925231934, 0.299923300743103, 0.2976943254470825, 0.28867483139038086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.466796875, 'crossentropy': 1.5143909454345703})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2158552408218384})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1952686309814453})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2765367031097412})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4186785221099854})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3395767211914062})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6858, 'crossentropy': 1.17793486328125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.352685570716858})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.118833303451538})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1071101427078247})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.083836317062378})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0307129621505737})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 50829], ['ood', 40272], ['id', 4361], ['ood', 48463], ['ood', 48383], ['ood', 25088], ['ood', 30762], ['id', 28962], ['id', 14569], ['ood', 10249]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.36520469188690186, 0.3648874759674072, 0.35327839851379395, 0.3528563976287842, 0.3455495834350586, 0.3452332019805908, 0.343395471572876, 0.34118902683258057, 0.3397153615951538, 0.3362680673599243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.423828125, 'crossentropy': 1.6609208583831787})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.262014389038086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1912102699279785})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.191270351409912})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2277617454528809})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2604191303253174})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6775, 'crossentropy': 1.1938470703125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3418407440185547})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1945180892944336})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1655480861663818})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.089461326599121})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0639216899871826})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 35684], ['id', 56561], ['id', 29457], ['id', 9924], ['id', 24172], ['id', 29031], ['id', 24282], ['id', 530], ['id', 31394], ['id', 29501]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.37570035457611084, 0.3583030700683594, 0.35042107105255127, 0.3325352668762207, 0.32696568965911865, 0.3258904218673706, 0.32507848739624023, 0.32224762439727783, 0.3199425935745239, 0.319527268409729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.4819104671478271})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2254273891448975})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.131498098373413})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1083593368530273})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1729824542999268})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1694774627685547})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2652859687805176})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6948, 'crossentropy': 1.13196064453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2978684902191162})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0951359272003174})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0568335056304932})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0310012102127075})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0083837509155273})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0043789148330688})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 16693], ['id', 35305], ['id', 49891], ['id', 34189], ['id', 39955], ['id', 47405], ['id', 13137], ['id', 58130], ['id', 38518], ['id', 22805]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38093388080596924, 0.37730252742767334, 0.37294864654541016, 0.3536006212234497, 0.3526427149772644, 0.35153549909591675, 0.35067427158355713, 0.35038745403289795, 0.3484005331993103, 0.34824156761169434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.4670195579528809})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1428250074386597})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1158056259155273})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0492689609527588})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1483538150787354})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1887907981872559})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.1815143823623657})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7072, 'crossentropy': 1.05771337890625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1868138313293457})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.002541422843933})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0011613368988037})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9554764628410339})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.928359866142273})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9588977098464966})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14502], ['id', 1590], ['id', 26518], ['id', 32994], ['id', 11534], ['id', 48674], ['id', 6175], ['id', 22129], ['id', 36294], ['id', 46267]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.46748822927474976, 0.4615226984024048, 0.4576342701911926, 0.4556398391723633, 0.45373427867889404, 0.45146167278289795, 0.4506996273994446, 0.44262391328811646, 0.4386356472969055, 0.43848180770874023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.4402037858963013})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1773200035095215})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0860493183135986})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0304558277130127})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0657787322998047})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1007614135742188})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.255504846572876})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.702, 'crossentropy': 1.04318876953125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.3294799327850342})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1069130897521973})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0280225276947021})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0109035968780518})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9989609718322754})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9449841380119324})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 54405], ['id', 41355], ['id', 13340], ['id', 20638], ['id', 36419], ['id', 22412], ['id', 13691], ['id', 20578], ['id', 40656], ['id', 22674]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.472806453704834, 0.43603515625, 0.40987062454223633, 0.39305049180984497, 0.384988009929657, 0.3837510943412781, 0.3836591839790344, 0.3831336498260498, 0.38011324405670166, 0.37688255310058594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.460749626159668})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.163116455078125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0737318992614746})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0383535623550415})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1462876796722412})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1158242225646973})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2025771141052246})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6975, 'crossentropy': 1.07375869140625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2257909774780273})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0295275449752808})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9806723594665527})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9572113156318665})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9493247270584106})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9618765115737915})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 16490], ['id', 48304], ['id', 6156], ['id', 33914], ['id', 58455], ['id', 41997], ['id', 14432], ['id', 37371], ['id', 21539], ['id', 37818]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4631422758102417, 0.43419528007507324, 0.42952513694763184, 0.4277406930923462, 0.422970712184906, 0.41844630241394043, 0.41401785612106323, 0.411324679851532, 0.41020190715789795, 0.4094039797782898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.501953125, 'crossentropy': 1.491959810256958})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1907987594604492})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1072144508361816})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0969393253326416})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.093887448310852})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.178751826286316})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2473359107971191})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2228028774261475})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6906, 'crossentropy': 1.1254220703125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3188741207122803})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.125086784362793})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.081141471862793})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.055690050125122})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0278675556182861})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 0.9887665510177612})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 0.9826505184173584})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 59677], ['id', 13660], ['id', 2207], ['id', 3680], ['id', 57290], ['id', 144], ['id', 10092], ['id', 49446], ['id', 13011], ['id', 43647]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5478788614273071, 0.5440272092819214, 0.5389500856399536, 0.534273624420166, 0.5302261114120483, 0.5238742828369141, 0.5218260288238525, 0.5207345485687256, 0.5187511444091797, 0.5156036019325256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.4360058307647705})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1064989566802979})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0947270393371582})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.022960901260376})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.065718173980713})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1079539060592651})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1141622066497803})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7085, 'crossentropy': 1.0358224609375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1962430477142334})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0319623947143555})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9850521087646484})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9706835746765137})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9359771609306335})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.8878636360168457})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 9312], ['id', 50403], ['id', 12617], ['id', 22576], ['id', 59924], ['id', 5893], ['id', 51188], ['id', 5111], ['id', 33978], ['id', 36899]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.45837926864624023, 0.4536561965942383, 0.43378114700317383, 0.43100690841674805, 0.42563992738723755, 0.41837286949157715, 0.41001152992248535, 0.40891194343566895, 0.4063001871109009, 0.406116247177124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.3882863521575928})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1177647113800049})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0872445106506348})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1169655323028564})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0860228538513184})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0959243774414062})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1361969709396362})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.362104892730713})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7093, 'crossentropy': 1.1155703125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2603602409362793})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0272533893585205})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0057023763656616})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.984686017036438})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9515697956085205})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9606242775917053})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9578927159309387})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 20968], ['id', 14436], ['id', 28218], ['id', 32930], ['id', 7641], ['id', 36212], ['id', 42223], ['id', 7145], ['id', 42347], ['id', 5708]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.41547393798828125, 0.390039324760437, 0.3830454349517822, 0.3749603033065796, 0.3717004060745239, 0.3683699369430542, 0.3666243553161621, 0.3651195168495178, 0.362859845161438, 0.3598950505256653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.4169065952301025})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0842311382293701})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0486490726470947})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0237408876419067})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1336431503295898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0893988609313965})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.260375738143921})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.72, 'crossentropy': 1.06293828125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2151763439178467})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0488810539245605})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9926789402961731})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9524420499801636})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9308360815048218})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9257256984710693})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 34952], ['id', 13482], ['id', 25184], ['id', 46092], ['id', 54455], ['id', 37710], ['id', 54667], ['id', 34793], ['id', 38697], ['id', 49228]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4357340335845947, 0.4063841700553894, 0.4055227041244507, 0.40227407217025757, 0.39326196908950806, 0.3893807530403137, 0.3889128565788269, 0.38318151235580444, 0.3791271448135376, 0.3759860396385193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.4345639944076538})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2317473888397217})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0863161087036133})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0583686828613281})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1105575561523438})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.152571201324463})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2801027297973633})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7193, 'crossentropy': 1.049175390625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2013275623321533})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0522669553756714})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0068756341934204})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0118088722229004})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.016085147857666})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0334360599517822})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 3913], ['id', 45967], ['id', 56086], ['id', 37979], ['id', 35280], ['id', 52556], ['id', 4436], ['id', 246], ['id', 37149], ['id', 57751]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3468102216720581, 0.34679484367370605, 0.3415031433105469, 0.3378998041152954, 0.33495402336120605, 0.32037413120269775, 0.319324254989624, 0.3178723454475403, 0.31260764598846436, 0.3119335174560547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.353173017501831})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.081864356994629})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0109620094299316})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9437527060508728})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9547749161720276})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9607536196708679})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.000386118888855})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7274, 'crossentropy': 0.9795587890625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2201495170593262})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0252535343170166})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9792681932449341})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9423570036888123})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9438295364379883})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9106217622756958})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 54813], ['id', 55968], ['id', 18533], ['id', 10127], ['id', 34050], ['id', 45171], ['id', 2782], ['id', 50385], ['id', 23126], ['id', 46995]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3981379270553589, 0.3936941623687744, 0.3647908568382263, 0.3600780963897705, 0.3479740619659424, 0.3421456813812256, 0.3386268615722656, 0.32848823070526123, 0.32744675874710083, 0.3266040086746216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.4127038717269897})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.123412013053894})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0374047756195068})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9945094585418701})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0624356269836426})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9910167455673218})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.0510525703430176})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.055567979812622})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1409506797790527})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7473, 'crossentropy': 1.0046162109375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.248798131942749})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0502140522003174})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9447107911109924})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9478466510772705})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9055747389793396})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.933637261390686})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9107083082199097})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.8800804615020752})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 57358], ['id', 47537], ['id', 59741], ['id', 39761], ['id', 33048], ['id', 52474], ['id', 14826], ['id', 59034], ['id', 57009], ['id', 52799]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5532634258270264, 0.5177456140518188, 0.5100821256637573, 0.48920905590057373, 0.48844683170318604, 0.4854167699813843, 0.48251426219940186, 0.4680943489074707, 0.467043399810791, 0.4643823504447937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.353118658065796})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0979870557785034})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0262545347213745})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9291966557502747})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9879317283630371})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9838739633560181})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9556650519371033})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7301, 'crossentropy': 0.93300693359375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1648083925247192})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0201643705368042})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9729951024055481})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.901975154876709})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.8870551586151123})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8784449100494385})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 45176], ['id', 20009], ['id', 34753], ['id', 17122], ['id', 14265], ['id', 52590], ['id', 4219], ['id', 49481], ['id', 51152], ['id', 2613]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.375545859336853, 0.3730810880661011, 0.3703552484512329, 0.3666731119155884, 0.3637888431549072, 0.3617180585861206, 0.3583107590675354, 0.3538035750389099, 0.35046374797821045, 0.3475792407989502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.3531591892242432})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1091704368591309})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9986765384674072})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9506145119667053})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9540156126022339})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9203815460205078})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9765479564666748})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.074385166168213})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9784563779830933})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7486, 'crossentropy': 0.93732119140625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2301334142684937})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0141279697418213})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9075672626495361})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9363159537315369})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.8692725300788879})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.8732695579528809})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8194488286972046})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.8156419992446899})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 1799], ['id', 16608], ['id', 30379], ['id', 43069], ['id', 42700], ['id', 52127], ['id', 15738], ['id', 33964], ['id', 19836], ['id', 35995]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.43258166313171387, 0.4276908040046692, 0.42635953426361084, 0.40987664461135864, 0.4075428247451782, 0.4071494936943054, 0.40560221672058105, 0.3914831280708313, 0.3883960247039795, 0.3810316324234009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.3481080532073975})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1026179790496826})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0072154998779297})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9401196241378784})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9314340949058533})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9316213130950928})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9460818767547607})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9452078342437744})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7337, 'crossentropy': 0.95354716796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1851449012756348})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.007453441619873})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9322246313095093})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9064690470695496})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.8877567052841187})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9177846908569336})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8690657615661621})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 33141], ['id', 9461], ['id', 33781], ['id', 59012], ['id', 52961], ['id', 39750], ['id', 22224], ['id', 8904], ['id', 19138], ['id', 46216]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.45968472957611084, 0.453525185585022, 0.4442441463470459, 0.4365208148956299, 0.4159708023071289, 0.41174745559692383, 0.39022159576416016, 0.3821389675140381, 0.37439870834350586, 0.37185871601104736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.451887845993042})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.117830514907837})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9837415814399719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9276304244995117})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.8996940851211548})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9719747304916382})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.982754647731781})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9449819326400757})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7318, 'crossentropy': 0.9161078125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1682007312774658})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0147647857666016})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9141566753387451})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9055088758468628})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.8958715200424194})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.8820539712905884})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.860454797744751})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 5973], ['ood', 40515], ['ood', 10229], ['ood', 38676], ['ood', 24451], ['ood', 32477], ['ood', 42335], ['id', 26219], ['ood', 1309], ['id', 59860]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4064183235168457, 0.3911123275756836, 0.39057910442352295, 0.3765174150466919, 0.3659123182296753, 0.36419010162353516, 0.360162615776062, 0.3597773015499115, 0.35425734519958496, 0.35277706384658813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.4315203428268433})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1404399871826172})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0220086574554443})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9713889956474304})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9652495384216309})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0089585781097412})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9800221920013428})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9724949598312378})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.72, 'crossentropy': 0.9653453125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2000055313110352})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.020113468170166})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9618366956710815})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9219205379486084})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.89268559217453})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9026221036911011})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9056191444396973})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 27719], ['id', 51145], ['id', 48480], ['id', 39272], ['id', 24609], ['id', 52602], ['id', 53839], ['id', 42555], ['id', 49864], ['id', 25216]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35938239097595215, 0.3571784496307373, 0.35338789224624634, 0.35314369201660156, 0.3447309732437134, 0.3394615650177002, 0.3374515771865845, 0.3370550274848938, 0.3368537425994873, 0.33579134941101074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.5007736682891846})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.195784330368042})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.077986478805542})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0105384588241577})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9969503879547119})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.024890422821045})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9294768571853638})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9810712933540344})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.0161504745483398})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.051932692527771})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7428, 'crossentropy': 0.92792119140625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.2983746528625488})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0744423866271973})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9819735884666443})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9391800165176392})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9184988737106323})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.8825390338897705})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.8940505981445312})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.874013364315033})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.8464037775993347})
store['active_learning_steps'][34]['eval_training']['best_epoch']=9
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 51890], ['id', 48083], ['id', 30703], ['id', 19842], ['id', 20606], ['id', 46975], ['id', 22900], ['id', 8698], ['id', 32330], ['id', 734]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4551728367805481, 0.41369450092315674, 0.3863014578819275, 0.35212576389312744, 0.3501988649368286, 0.34230494499206543, 0.34081900119781494, 0.33990228176116943, 0.3389248847961426, 0.33778512477874756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4065520763397217})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1695337295532227})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9845903515815735})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9200410842895508})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8939840793609619})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.887934684753418})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.8736887574195862})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9561480283737183})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9548203349113464})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.027745008468628})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7444, 'crossentropy': 0.8923490234375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.212094783782959})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0431888103485107})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9164032936096191})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.856147050857544})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.8754076361656189})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.8243955969810486})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.8105666637420654})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.8335293531417847})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.826727032661438})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 35947], ['id', 30767], ['id', 27629], ['id', 56380], ['id', 9425], ['id', 59953], ['id', 19888], ['id', 43215], ['id', 38307], ['id', 59858]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4136599898338318, 0.4069359302520752, 0.40543532371520996, 0.3996450901031494, 0.38291436433792114, 0.37913453578948975, 0.37771159410476685, 0.3668050169944763, 0.36588382720947266, 0.3650050163269043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.3808115720748901})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.060460090637207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.958774209022522})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.856149435043335})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8961405158042908})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 0.8675886988639832})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.8772499561309814})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7418, 'crossentropy': 0.87028857421875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2060723304748535})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9774275422096252})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9244410991668701})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.88560950756073})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8978914618492126})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.8643608689308167})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 17076], ['id', 63], ['id', 52722], ['id', 7298], ['id', 17383], ['id', 380], ['id', 43863], ['id', 15622], ['id', 24887], ['id', 9173]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3449726104736328, 0.32371246814727783, 0.31977224349975586, 0.31675148010253906, 0.310092568397522, 0.3096487522125244, 0.30859053134918213, 0.3036724328994751, 0.29976487159729004, 0.29944753646850586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.4235129356384277})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.128753423690796})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0171351432800293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8824779987335205})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.8836883306503296})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.8798923492431641})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9065281748771667})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9585757255554199})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.9219003915786743})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7442, 'crossentropy': 0.88435126953125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.193712830543518})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0004363059997559})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9357077479362488})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.897413969039917})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8413835763931274})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8746952414512634})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.814354658126831})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8085350394248962})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 52419], ['id', 56873], ['id', 11434], ['id', 32127], ['id', 1053], ['id', 8766], ['id', 7593], ['id', 16017], ['id', 54785], ['id', 29062]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3907897472381592, 0.39048492908477783, 0.3855292797088623, 0.384655237197876, 0.38083481788635254, 0.3792945146560669, 0.37651413679122925, 0.3704526424407959, 0.3700307607650757, 0.3662923574447632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3855626583099365})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0511410236358643})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9878824949264526})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9338773488998413})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.8903818130493164})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.8917965888977051})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.879652738571167})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9005322456359863})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.9573132991790771})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9708541631698608})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7545, 'crossentropy': 0.8731771484375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3449211120605469})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.995964765548706})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9346767067909241})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8963452577590942})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8437304496765137})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8172427415847778})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.7969268560409546})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8075348138809204})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.7781798839569092})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 35913], ['id', 35309], ['id', 39688], ['ood', 5972], ['id', 25469], ['id', 10052], ['id', 47410], ['id', 47513], ['id', 13237], ['id', 51180]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4068392515182495, 0.4027252197265625, 0.38345927000045776, 0.380132794380188, 0.37880486249923706, 0.37805426120758057, 0.3712807893753052, 0.36424314975738525, 0.36130261421203613, 0.3594616651535034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.4612711668014526})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1481465101242065})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9775627851486206})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8877853155136108})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.8811219334602356})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.8508239984512329})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.8553828001022339})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8694366216659546})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8450912237167358})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9364780187606812})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9168733358383179})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0045416355133057})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7633, 'crossentropy': 0.8717935546875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.217477560043335})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.936018705368042})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8880568146705627})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.8270186185836792})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.8116289377212524})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.7992010712623596})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.8215290307998657})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.7639622688293457})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.7644299268722534})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.7713810205459595})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.7708328366279602})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 40009], ['id', 165], ['id', 2789], ['id', 26986], ['id', 3553], ['id', 22836], ['id', 12210], ['id', 5346], ['ood', 56677], ['id', 27593]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4069647789001465, 0.3873679041862488, 0.38568949699401855, 0.3780803680419922, 0.37629014253616333, 0.3698684573173523, 0.36405694484710693, 0.36118626594543457, 0.36011993885040283, 0.3594151735305786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.4063951969146729})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.173743486404419})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0020009279251099})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9316616058349609})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.8928220272064209})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9034038186073303})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.8565563559532166})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.8882708549499512})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.8833169341087341})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 0.9432666301727295})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7501, 'crossentropy': 0.85814658203125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1541547775268555})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0006463527679443})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9150128364562988})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8788363337516785})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.829291582107544})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.8028925657272339})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.8062511682510376})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.7928556203842163})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.7703135013580322})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 27747], ['id', 13257], ['id', 57213], ['id', 7182], ['id', 15405], ['id', 47659], ['id', 11174], ['id', 7577], ['id', 32171], ['id', 125]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3942934274673462, 0.38013672828674316, 0.37473607063293457, 0.3646056652069092, 0.35902899503707886, 0.3537316918373108, 0.34866058826446533, 0.3461105227470398, 0.34597277641296387, 0.3453591465950012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3662407398223877})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0728461742401123})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.9143438935279846})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.8558858036994934})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8380841016769409})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8418192863464355})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.8908785581588745})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8869822025299072})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7472, 'crossentropy': 0.85646025390625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.195321798324585})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9910380840301514})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9027748107910156})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.8641517758369446})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9143925905227661})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.8370484709739685})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.8924167156219482})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 22801], ['ood', 10233], ['id', 33778], ['id', 23444], ['id', 10103], ['ood', 32329], ['id', 26028], ['id', 59731], ['id', 15716], ['id', 46064]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.345436692237854, 0.3359076976776123, 0.33338427543640137, 0.325234055519104, 0.32352936267852783, 0.32249653339385986, 0.31205451488494873, 0.3073744773864746, 0.30596065521240234, 0.3049885034561157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.4847038984298706})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.237034559249878})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0859936475753784})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.962931752204895})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9085639715194702})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.886206328868866})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.8703470826148987})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.9028346538543701})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9256910681724548})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9032443761825562})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.7393, 'crossentropy': 0.88596630859375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2722657918930054})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.015580654144287})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9532281756401062})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8727996945381165})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.8270795345306396})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.8369958400726318})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8031859397888184})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.8169238567352295})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8310160636901855})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 51646], ['id', 38374], ['id', 37064], ['id', 11015], ['id', 2527], ['id', 7924], ['id', 55855], ['id', 2435], ['id', 57099], ['id', 3979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.37460070848464966, 0.3660764694213867, 0.3569023609161377, 0.3532322645187378, 0.35232627391815186, 0.3516496419906616, 0.3515530824661255, 0.3513139486312866, 0.34934425354003906, 0.3489382266998291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.505835771560669})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.1918456554412842})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1430368423461914})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9538532495498657})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.887740969657898})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9183645248413086})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9145742654800415})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.8516344428062439})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9209868907928467})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.892368733882904})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.8930652141571045})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7585, 'crossentropy': 0.87008427734375}
