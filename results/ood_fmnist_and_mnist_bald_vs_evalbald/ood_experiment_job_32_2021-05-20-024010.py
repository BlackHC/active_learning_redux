store = {}
store['timestamp']=1621474810
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=32']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=32
store['worker_id']=32
store['num_workers']=80
store['config']={'seed': 1268, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.3598804473876953})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.683375120162964})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9188051223754883})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8829994201660156})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.935363292694092})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6856, 'crossentropy': 2.2940955078125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3854200839996338})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4756916761398315})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3629670143127441})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4473313093185425})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 38256], ['id', 56848], ['id', 50537], ['id', 9249], ['id', 9437]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9145617948456173, 1.5507251874658308, 2.0321621720945604, 2.3710747653694657, 2.5958273899655158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8561797142028809})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.084665060043335})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.276087999343872})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7701399326324463})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.727783679962158})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6882, 'crossentropy': 1.917065234375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.482334852218628})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4274318218231201})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4255770444869995})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3429471254348755})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 16095], ['id', 1076], ['id', 14538], ['id', 24107], ['id', 29925]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7879518457759978, 1.404203287105298, 1.921785208220232, 2.306398184931072, 2.508865074981621]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.8334351778030396})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.111893653869629})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.370419502258301})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.5780091285705566})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.4700984954833984})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6862, 'crossentropy': 1.910718359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5387150049209595})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.6697900295257568})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.649959921836853})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5432929992675781})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 50740], ['id', 41993], ['id', 48752], ['id', 21304], ['id', 23863]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7279932112304754, 1.3300266842433648, 1.7718460219758203, 2.119541905952902, 2.338859202862645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8204892873764038})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9593868255615234})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.234100341796875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.425689697265625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4961719512939453})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.4820566177368164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.491720199584961})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.570817470550537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.7774300575256348})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7295, 'crossentropy': 2.1026845703125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5936203002929688})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.523747444152832})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6109273433685303})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6152675151824951})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.582388162612915})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.469491958618164})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.5476737022399902})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5952856540679932})
store['active_learning_steps'][3]['eval_training']['best_epoch']=6
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 43245], ['id', 56508], ['id', 59256], ['id', 4859], ['id', 1721]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8407868830136761, 1.5757932626325677, 2.1623224378868224, 2.578350612814832, 2.8411224112767615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.714028000831604})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9011600017547607})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5631794929504395})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.3569397926330566})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7289, 'crossentropy': 1.486307421875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3143134117126465})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.167364239692688})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.219771385192871})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 2634], ['id', 5277], ['id', 42796], ['id', 34391], ['id', 51345]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6398405432935301, 1.1894268521129376, 1.648057432030749, 2.0046707536907764, 2.2244190582298016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8264193534851074})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9863882064819336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.9674137830734253})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2527217864990234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.415431499481201})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.364157199859619})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.260908842086792})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.296786308288574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.5435585975646973})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7481, 'crossentropy': 2.1600525390625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4930691719055176})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.2541873455047607})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5259606838226318})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3981516361236572})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4608511924743652})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 22638], ['id', 14383], ['id', 38567], ['id', 19426], ['id', 43691]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7407363172866118, 1.3471587150561077, 1.8876504168790422, 2.278178676506392, 2.520425263727992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.577522873878479})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.6564905643463135})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6043460369110107})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.062838554382324})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8474984169006348})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.161628484725952})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7816, 'crossentropy': 1.42643681640625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4277020692825317})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.23061203956604})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.266206979751587})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2610918283462524})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.225447416305542})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 46187], ['id', 37567], ['id', 3094], ['id', 28992], ['id', 25207]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7127038895791409, 1.2987322124468723, 1.7987573856144712, 2.1347651174506073, 2.3768489896868896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3953114748001099})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.5314996242523193})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.4874112606048584})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5914350748062134})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7116930484771729})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6514602899551392})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8459830284118652})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7937, 'crossentropy': 1.321700390625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3435709476470947})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2100199460983276})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1568127870559692})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0763912200927734})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1267191171646118})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.037409782409668})
store['active_learning_steps'][7]['eval_training']['best_epoch']=6
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 11084], ['id', 5316], ['id', 13030], ['id', 11398], ['id', 10503]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.671994691599902, 1.2868342854309485, 1.7616566372143772, 2.11778193154294, 2.3593479880623525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3904929161071777})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3416810035705566})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.4256243705749512})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5691677331924438})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.741398572921753})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7947, 'crossentropy': 1.1378576171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2715665102005005})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1838656663894653})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1214942932128906})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1228735446929932})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 32022], ['id', 4489], ['id', 30371], ['id', 30530], ['id', 12906]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.649610279638815, 1.1778920790140917, 1.5889055239118406, 1.8820092029058175, 2.0878749618552526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2812700271606445})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.5498385429382324})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.6399831771850586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.6775400638580322})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.72088623046875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.9855480194091797})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7551088333129883})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.8686957359313965})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.799, 'crossentropy': 1.35202734375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.291128396987915})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.2828927040100098})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2376985549926758})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2133262157440186})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2283332347869873})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 20171], ['id', 12607], ['id', 43537], ['id', 27912], ['id', 47787]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9773716020772059, 1.5778294958446617, 2.038687580726189, 2.370860394086522, 2.5739631253300614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2655937671661377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.422945499420166})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.468841314315796})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.6555266380310059})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.6610302925109863})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7379661798477173})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.8922619819641113})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.8777906894683838})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8380076885223389})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8029, 'crossentropy': 1.39231279296875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.185304880142212})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.0541399717330933})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.0784235000610352})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.067255973815918})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0772578716278076})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0511232614517212})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0174059867858887})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9565373659133911})
store['active_learning_steps'][10]['eval_training']['best_epoch']=8
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 11167], ['id', 20659], ['id', 19276], ['id', 52722], ['id', 33584]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7802283221995601, 1.4815199317829317, 2.0414928522651032, 2.4213400643149026, 2.639383167115801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0774396657943726})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0669362545013428})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.173187255859375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.371673583984375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.304328203201294})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4135388135910034})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.5326588153839111})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.5081768035888672})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8518, 'crossentropy': 1.045584765625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0502281188964844})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9408808946609497})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8987263441085815})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9283403754234314})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8070086240768433})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8567606210708618})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8439481258392334})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 12035], ['id', 31988], ['id', 3824], ['id', 17278], ['id', 50556]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6992295818900486, 1.3277358735971387, 1.8155463301932344, 2.1642942731645767, 2.3981775680294115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0353808403015137})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9739545583724976})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2196483612060547})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3215742111206055})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.272266149520874})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.2822755575180054})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4524221420288086})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3991992473602295})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8476, 'crossentropy': 0.973537109375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0208110809326172})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.958476185798645})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9391405582427979})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9523781538009644})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9566828012466431})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8457033634185791})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8343580961227417})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 46291], ['id', 15406], ['id', 57580], ['id', 28455], ['id', 26184]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6482066587503588, 1.2639604911967819, 1.7276385201368716, 2.0205713331100155, 2.2159189040052922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0247489213943481})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.184603214263916})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.234062910079956})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.210627794265747})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.406482219696045})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5443885326385498})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.6676816940307617})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8606, 'crossentropy': 0.93759873046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9634866714477539})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9233986139297485})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8693608045578003})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9052798748016357})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7989065647125244})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8997455835342407})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 24155], ['id', 25538], ['id', 36492], ['id', 11853], ['id', 38780]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7398375064357288, 1.3799852148028797, 1.9173688319228361, 2.280140853313353, 2.4918631361586394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0109002590179443})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8463783264160156})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9458080530166626})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1191496849060059})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.145072102546692})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8705, 'crossentropy': 0.714839892578125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9824961423873901})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8006536960601807})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7242849469184875})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7111963033676147})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 48681], ['id', 36323], ['id', 48431], ['id', 32047], ['id', 31314]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6158698023614262, 1.1408018506023612, 1.5585813874145913, 1.8920756332425501, 2.1121229747491164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9589588642120361})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8826736211776733})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9939233064651489})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9837610721588135})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9996488094329834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.999977171421051})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0989181995391846})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.2396507263183594})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1709473133087158})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.2667524814605713})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.1199076175689697})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.88317744140625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9056326746940613})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8008687496185303})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7500722408294678})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7382690906524658})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7777318954467773})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7082581520080566})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 22506], ['id', 31148], ['id', 30646], ['id', 11877], ['id', 5170]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6840162815674444, 1.263851536334331, 1.7153072706985575, 2.077050654979944, 2.3264764264373303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8741718530654907})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7904188632965088})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.816814124584198})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8800786733627319})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8201240301132202})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9759988784790039})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0583832263946533})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8797890543937683})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.680846826171875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9042853116989136})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7516194581985474})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7312902212142944})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6965060830116272})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6744731068611145})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 43126], ['id', 13945], ['id', 40334], ['id', 43860], ['id', 12877]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6462041315795717, 1.2059709364811035, 1.6380904226788058, 1.9676336351615262, 2.1789067870515133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8611840009689331})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7554807662963867})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6584358215332031})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7537273168563843})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8295397162437439})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7368618249893188})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8816401958465576})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7414411902427673})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8171464204788208})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9182199239730835})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8094466924667358})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.60893046875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8659217357635498})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6733978390693665})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6012424230575562})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5576452612876892})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5390852689743042})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5232056379318237})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5260090827941895})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5175353288650513})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5017226338386536})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5029071569442749})
store['active_learning_steps'][17]['eval_training']['best_epoch']=9
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 37534], ['id', 48279], ['id', 46724], ['id', 52172], ['id', 49633]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6580210940238178, 1.241209071208979, 1.7319067289556989, 2.104360325732234, 2.3614034946596085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8416728377342224})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6518427133560181})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7603113055229187})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7899394035339355})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8527981042861938})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.891716718673706})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.834394097328186})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9447509050369263})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9184708595275879})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9048452377319336})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9151253700256348})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9278558492660522})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8902174830436707})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9282410144805908})
store['active_learning_steps'][18]['training']['best_epoch']=11
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.666895263671875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8529476523399353})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6975407600402832})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7375779151916504})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6561903953552246})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6207368969917297})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6075640916824341})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6010482311248779})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6294447183609009})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.585723876953125})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5992496013641357})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5893776416778564})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5809590816497803})
store['active_learning_steps'][18]['eval_training']['best_epoch']=9
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 7700], ['id', 55471], ['id', 27149], ['id', 46435], ['id', 15676]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7803530631957432, 1.4248040417780632, 2.00586673877902, 2.4559854633971776, 2.7584091706472877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8261644840240479})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7106920480728149})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6972459554672241})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7904341220855713})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8188703060150146})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7662352919578552})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9041, 'crossentropy': 0.607888720703125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8202418088912964})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6029611825942993})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5627902746200562})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5462015271186829})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5029202103614807})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 10804], ['id', 45203], ['id', 22609], ['id', 20867], ['id', 4997]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6896966876646768, 1.281613582836271, 1.771309608144798, 2.088484799696075, 2.289748887171358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8067491054534912})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.715368390083313})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.772952675819397})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6691201329231262})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7526382207870483})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7996531128883362})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7682651281356812})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.61913525390625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7960398197174072})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5899515151977539})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5889143347740173})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5448899269104004})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5283269882202148})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5144432783126831})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 36818], ['id', 5600], ['id', 38598], ['id', 11025], ['id', 12569]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6463139138503242, 1.2084258012229663, 1.6870103805367496, 2.0493180739416257, 2.2793191714317595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8448615074157715})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6369822025299072})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6934268474578857})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.69930100440979})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7152422666549683})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7522029876708984})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8432682752609253})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8376712799072266})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8688911199569702})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.64598076171875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8329211473464966})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6114237308502197})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6152984499931335})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5493935346603394})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5564670562744141})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.531017005443573})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5284287333488464})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 38568], ['id', 26918], ['id', 33505], ['id', 26135], ['id', 16406]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.573041487961085, 1.078040749071492, 1.4812682659947507, 1.778837014662522, 1.9566934298057816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9227583408355713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6290766000747681})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6364818811416626})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7092778086662292})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6986116170883179})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.557964453125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8170210123062134})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6158630847930908})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5906271934509277})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5571625232696533})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 424], ['id', 23104], ['id', 5355], ['id', 28581], ['id', 7768]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5309396239436313, 0.9642847100634224, 1.3327252610141045, 1.6285138378677004, 1.8373232659450256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9936213493347168})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7151116728782654})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6098602414131165})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6648356914520264})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7232989072799683})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7345478534698486})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7245148420333862})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.560378076171875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8578009605407715})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.611024022102356})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5437833070755005})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5035873651504517})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4594709873199463})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.47096776962280273})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 6520], ['id', 59747], ['id', 15210], ['id', 26865], ['id', 23551]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7051561091183156, 1.294516187710574, 1.768104089986041, 2.13212797015911, 2.3659756194448036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8577488660812378})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6249113082885742})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5553300380706787})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.596499502658844})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.66985684633255})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5821199417114258})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5766360759735107})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6247212886810303})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6431918740272522})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.4951658203125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.866234302520752})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5799951553344727})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5647306442260742})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4886873960494995})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4653540849685669})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4414992332458496})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4498518705368042})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.45283567905426025})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 44438], ['id', 17518], ['id', 3676], ['id', 47690], ['id', 34750]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6226842569775222, 1.1740439266221196, 1.6159726133301886, 1.9719817345744772, 2.186751948487557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8556265830993652})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6295815110206604})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5898659825325012})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6431561708450317})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6461098194122314})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7342891693115234})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.508683056640625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8478646278381348})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5692453384399414})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5075992345809937})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.48292258381843567})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.482286274433136})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 15487], ['id', 25724], ['id', 20172], ['id', 22883], ['id', 8715]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5271430691673433, 0.9836701831317676, 1.3419023010833637, 1.5999728763441823, 1.7748137102823378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9247744083404541})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5810199975967407})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5804396271705627})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5608663558959961})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5487450361251831})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5606812834739685})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6379954218864441})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6339079141616821})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6209415793418884})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.5612943359375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.859955906867981})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5707328915596008})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4964519143104553})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4771724343299866})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.46676602959632874})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.43900877237319946})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 51736], ['id', 1239], ['id', 13165], ['id', 28210], ['id', 29770]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6324402658230854, 1.230306914770253, 1.7033932169309174, 2.0540306945193127, 2.260826425139058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9228876829147339})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6022734642028809})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5989764928817749})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5886062979698181})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6691590547561646})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.543076611328125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8859952092170715})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6492916941642761})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5195745229721069})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5665251016616821})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 36744], ['id', 22579], ['id', 49064], ['id', 22824], ['id', 6574]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6458243253735891, 1.2049603833200866, 1.703044285703017, 2.0739584650058323, 2.340560529297365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9526635408401489})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6302322745323181})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5276484489440918})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6157785654067993})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5628144145011902})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5906322002410889})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.466119580078125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7998369932174683})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.580668568611145})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5517435669898987})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5110684633255005})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48034265637397766})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42141], ['id', 56454], ['id', 4842], ['id', 43042], ['id', 14760]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6288989069537245, 1.178155323955083, 1.6015258929011678, 1.9206261496975534, 2.145396452652901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8722725510597229})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5828534364700317})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.529639482498169})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5952463746070862})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5588783025741577})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5876919627189636})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.465445556640625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9123166799545288})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.554074764251709})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5154334306716919})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5016563534736633})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4697625935077667})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 47140], ['id', 8887], ['id', 12345], ['id', 14825], ['id', 9180]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6091894955023089, 1.1637238817448603, 1.6217115246061065, 1.9665172713643937, 2.204576540319005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9044733047485352})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.58351069688797})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6129222512245178})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4930340051651001})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5327650308609009})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5689235925674438})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6477592587471008})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.717280387878418})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6324566602706909})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.516015625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8272131681442261})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5662935972213745})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4864804148674011})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.456676185131073})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.44902682304382324})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.45436304807662964})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.454933762550354})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4242976903915405})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 34743], ['id', 33389], ['id', 47597], ['id', 485], ['id', 16198]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6164607031467262, 1.1816756222831457, 1.6129869756973054, 1.9042382758829346, 2.0941473160174153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9771042466163635})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5527561902999878})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5352034568786621})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5175923109054565})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5154081583023071})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5125768184661865})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.49166005859375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9298041462898254})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6096975803375244})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5425900816917419})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.49771955609321594})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5444123148918152})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 20120], ['id', 31757], ['id', 45180], ['id', 13080], ['id', 43648]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5860783152531674, 1.0784086619841387, 1.5363008137042682, 1.8690936481335898, 2.115741033346562]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9368640184402466})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6088610887527466})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5828115344047546})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5651687383651733})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5609883069992065})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.536669909954071})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5801573991775513})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6250860691070557})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7176585793495178})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9327, 'crossentropy': 0.48698359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9065232872962952})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5714603066444397})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4777764678001404})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5066520571708679})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.42766183614730835})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44466525316238403})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.42251262068748474})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.40398508310317993})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 26738], ['id', 41276], ['id', 10064], ['id', 1380], ['id', 34096]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7318861442856617, 1.2967355709815531, 1.7636119765318918, 2.0999579280700704, 2.3073257549535766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0642881393432617})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6592516899108887})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5994582176208496})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5988948345184326})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5929337739944458})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6154471635818481})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6197528839111328})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6590403318405151})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.496037158203125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0050150156021118})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6074477434158325})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5657322406768799})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5475687384605408})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.48667916655540466})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4612695574760437})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4737565517425537})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 17958], ['id', 30525], ['id', 48726], ['id', 6480], ['id', 40158]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6557021661150713, 1.2066871283254006, 1.6591427741772202, 1.964593762016798, 2.1710778246549065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.922974705696106})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6561785936355591})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5613548755645752})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6550147533416748})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5968541502952576})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5910864472389221})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5682289004325867})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6322953701019287})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7046119570732117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7309192419052124})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.531231298828125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8587314486503601})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5485836267471313})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.46777546405792236})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4631727933883667})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.48618048429489136})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.44674158096313477})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.428496778011322})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50391], ['id', 4153], ['id', 36281], ['id', 4654], ['id', 6150]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6279438330415217, 1.1827821511174985, 1.6477039976234633, 1.9969534783699672, 2.2064846257429584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0278737545013428})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5764943361282349})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5623311996459961})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5602169036865234})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5672598481178284})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49895256757736206})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5457370281219482})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5668213367462158})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6109110116958618})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.479466357421875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8879534006118774})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.600907564163208})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5034830570220947})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4697028696537018})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4646714925765991})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43007877469062805})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4371131360530853})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 14956], ['id', 8011], ['id', 50202], ['id', 15408], ['id', 58971]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6721262615794583, 1.2402598059072836, 1.7390724714550325, 2.101618009301541, 2.3142194261135316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9635500311851501})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6506006717681885})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5778330564498901})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5258380174636841})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5186704993247986})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4819810390472412})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5482673645019531})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5873473882675171})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.525740385055542})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9324, 'crossentropy': 0.459100830078125}
