store = {}
store['timestamp']=1621481078
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=67']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=67
store['worker_id']=67
store['num_workers']=80
store['config']={'seed': 1305, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.2634224891662598})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.715231418609619})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.986576557159424})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.086203098297119})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2633886337280273})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.6103734970092773})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.754478931427002})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3615665435791016})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.617, 'crossentropy': 3.303621484375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.805608868598938})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8403372764587402})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8670669794082642})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.0697784423828125})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.9299631118774414})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.959956169128418})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.811739444732666})
store['active_learning_steps'][0]['eval_training']['best_epoch']=6
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36733], ['id', 21776], ['id', 5321], ['id', 19570], ['id', 40648]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1715014040755485, 2.0708932746847384, 2.757118939146995, 3.2624967997893464, 3.491428623713203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.5718932151794434})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.4045324325561523})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.643765926361084})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.8715755939483643})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.206596612930298})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.303409576416016})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.113945007324219})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.109189987182617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.51107931137085})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5806, 'crossentropy': 4.498509765625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1124067306518555})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.093174934387207})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.0031769275665283})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0104594230651855})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 57184], ['id', 33479], ['id', 50308], ['id', 57576], ['id', 25746]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.1010433481105222, 1.9454490924257033, 2.57114787541687, 2.8812622086193542, 3.0538310479672495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.232351303100586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.0455479621887207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.4556403160095215})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6423988342285156})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5926, 'crossentropy': 2.32558671875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.456669807434082})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4033732414245605})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4394428730010986})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 18486], ['id', 639], ['id', 54187], ['id', 50154], ['id', 23113]], 'labels': [5, 0, 9, 2, 7], 'scores': [0.8346282742226323, 1.3719033752853869, 1.7533923589203853, 2.054391475012091, 2.243396930793958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.299631118774414})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.7069082260131836})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.025294065475464})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.5685462951660156})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.522064208984375})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.7350542545318604})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.683143138885498})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.5665721893310547})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.6880455017089844})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6089, 'crossentropy': 3.91061796875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.162489414215088})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.96945321559906})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.210264205932617})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.344305992126465})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.176237106323242})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 40969], ['id', 59431], ['id', 37591], ['id', 26174], ['id', 24195]], 'labels': [-1, -1, -1, 0, 7], 'scores': [1.0041896288643184, 1.6922781201264288, 2.1895831629051754, 2.5116135705347897, 2.696051775736428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.271155834197998})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.916050672531128})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.861273765563965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.3317184448242188})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.63887357711792})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3502743244171143})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.5683557987213135})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.732860803604126})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.6939616203308105})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6006, 'crossentropy': 3.535490625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9502553939819336})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7925548553466797})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8448762893676758})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9675031900405884})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8700757026672363})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 14637], ['id', 20636], ['id', 6891], ['id', 12438], ['id', 3830]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.7836510414885646, 1.367248453059037, 1.7735009503808588, 2.0531081073565316, 2.2720495358100368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.161250114440918})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.669696807861328})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0104730129241943})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0692501068115234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6605749130249023})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.319822311401367})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2922580242156982})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.440518379211426})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.6946582794189453})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.7645719051361084})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2577309608459473})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5523619651794434})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.280470371246338})
store['active_learning_steps'][5]['training']['best_epoch']=10
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5965, 'crossentropy': 4.0709171875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9985027313232422})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.1036195755004883})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.15921950340271})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.1106321811676025})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1954901218414307})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.260464668273926})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 36339], ['id', 26613], ['id', 23187], ['id', 22098], ['id', 32311]], 'labels': [-1, -1, 4, -1, 5], 'scores': [1.1350928380508094, 1.932644651926756, 2.538661217607413, 2.886476972673925, 3.09754796673736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9128336906433105})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.547788381576538})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.704235076904297})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0375165939331055})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.9299542903900146})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.3182311058044434})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.138340473175049})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6084, 'crossentropy': 3.175689453125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.6845371723175049})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.7362431287765503})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.7722978591918945})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8105010986328125})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.8107233047485352})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6918410062789917})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 34829], ['id', 27325], ['id', 47164], ['id', 25002], ['id', 23294]], 'labels': [-1, -1, 9, -1, -1], 'scores': [1.0196511337315886, 1.7841807490113974, 2.319067482875098, 2.6921583990281186, 2.9612547997283234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.2873640060424805})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.7863073348999023})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.300915002822876})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 3.741255283355713})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.927549362182617})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 4.319397926330566})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5806, 'crossentropy': 3.582087109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.8132679462432861})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8245043754577637})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.6484386920928955})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.610356092453003})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.6424126625061035})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 6152], ['id', 7621], ['id', 49875], ['id', 53015], ['id', 36158]], 'labels': [-1, -1, -1, 0, 3], 'scores': [0.9635679954919173, 1.6568410348526412, 2.162076576375401, 2.4362672394450415, 2.5891167699450577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9731872081756592})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.759718418121338})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.10139536857605})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.183748483657837})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.1806678771972656})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.607487916946411})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.594970941543579})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.492276906967163})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.5412492752075195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.484386444091797})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.5375165939331055})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6004, 'crossentropy': 3.56049921875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.628735899925232})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.789567232131958})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6975462436676025})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7302491664886475})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.7379356622695923})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.768100619316101})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7712293863296509})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 42707], ['id', 46555], ['id', 11446], ['id', 31774], ['id', 46258]], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.9882394777162188, 1.751895974065543, 2.3401436748707556, 2.6627731826287753, 2.863378598502236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.286041736602783})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.0402801036834717})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.5027458667755127})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.4935245513916016})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.886345386505127})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.812082290649414})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.94836163520813})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.256387233734131})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.177263259887695})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.130769729614258})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5806, 'crossentropy': 4.290594140625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8636499643325806})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.162754535675049})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.1854329109191895})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.014183282852173})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 4290], ['id', 27120], ['id', 12934], ['id', 35453], ['id', 19842]], 'labels': [-1, -1, -1, 8, 8], 'scores': [1.0648184337079516, 1.7453346697171808, 2.2886099939289473, 2.631424636657674, 2.8203397375528327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.239758014678955})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.867202043533325})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.036634922027588})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5575060844421387})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.9310898780822754})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.6551108360290527})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7376511096954346})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.746227741241455})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 4.192630767822266})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 4.40457820892334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.06887674331665})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8068222999572754})
store['active_learning_steps'][10]['training']['best_epoch']=9
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5883, 'crossentropy': 4.680129296875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9820590019226074})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.303445339202881})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.2078897953033447})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.2422871589660645})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.3319060802459717})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.2922120094299316})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.211981773376465})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.3983993530273438})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 12406], ['id', 3334], ['id', 24589], ['id', 55062], ['id', 10992]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0055390306847323, 1.774077235179136, 2.3658438139624933, 2.722888836955641, 2.9217590414058527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.1412770748138428})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.9084603786468506})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.7685513496398926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.424910545349121})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.2965645790100098})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5955862998962402})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.789320468902588})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 4.01909065246582})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.04626989364624})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5942, 'crossentropy': 4.116673828125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.9722685813903809})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.108574867248535})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.035907030105591})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.202700138092041})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.937363624572754})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9896047115325928})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 17915], ['id', 1772], ['id', 18682], ['id', 50895], ['id', 11798]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.212396885309916, 2.192706331420618, 2.7814449409194295, 3.1997446945200085, 3.4919621515367947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.0488619804382324})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.96663761138916})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.560476779937744})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.7301645278930664})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.915635585784912})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.6754016876220703})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.8992557525634766})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.305768966674805})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.517375469207764})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.594, 'crossentropy': 3.83648359375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.7029446363449097})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8600857257843018})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.848523497581482})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.8733839988708496})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8752305507659912})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6126035451889038})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22336], ['id', 56516], ['id', 165], ['id', 18658], ['id', 14191]], 'labels': [-1, -1, 2, 5, -1], 'scores': [0.932359190893128, 1.7538404297814687, 2.3313111234763855, 2.7684723366420014, 3.06143794037818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 2.0068633556365967})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.838561534881592})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4888434410095215})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.9737305641174316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.05872106552124})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.184020042419434})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.9076991081237793})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 4.067793846130371})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 4.093940734863281})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.301844596862793})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 4.022271633148193})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.385145664215088})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.46394157409668})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 4.275969505310059})
store['active_learning_steps'][13]['training']['best_epoch']=11
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6061, 'crossentropy': 4.211245703125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9669406414031982})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.9381072521209717})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.100593090057373})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9584739208221436})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.0168981552124023})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.8770756721496582})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.0065505504608154})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 36384], ['id', 33469], ['id', 45482], ['id', 42858], ['id', 45262]], 'labels': [-1, -1, -1, 5, 2], 'scores': [1.2544099171732297, 2.1750008550066267, 2.8386884011402436, 3.1936623650120683, 3.384816875669712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.0813117027282715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.330740213394165})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.3430423736572266})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.9782943725585938})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5808, 'crossentropy': 2.211762109375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.3930085897445679})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3407621383666992})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3132474422454834})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 58390], ['id', 45577], ['id', 3231], ['id', 7528], ['id', 4311]], 'labels': [-1, -1, 5, -1, 5], 'scores': [0.6625392742584311, 1.1959194822608046, 1.5827710632453442, 1.8551744158031642, 2.0419372918458167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.626840353012085})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.392853260040283})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.4230637550354004})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.43141508102417})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8528590202331543})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0313968658447266})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6943869590759277})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6263, 'crossentropy': 2.7681740234375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.8493956327438354})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8552298545837402})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8577229976654053})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8842047452926636})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.6367814540863037})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.6439223289489746})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 48982], ['id', 3334], ['id', 4619], ['id', 56825], ['id', 55976]], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.9718585051065014, 1.7053142453400592, 2.2096315499747, 2.4984309885990563, 2.674291768512375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.9799244403839111})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.2234387397766113})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.711331367492676})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9506313800811768})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.126774311065674})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.218451499938965})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.4575319290161133})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.242732524871826})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.561929702758789})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.191178798675537})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2708396911621094})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.317610263824463})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.7410483360290527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.5651111602783203})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 4.094892501831055})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.748577356338501})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.632741928100586})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.918095111846924})
store['active_learning_steps'][16]['training']['best_epoch']=15
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6197, 'crossentropy': 4.144951953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.7429354190826416})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.1063826084136963})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3802762031555176})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.144225835800171})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.140886068344116})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.254873275756836})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.2276270389556885})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 27076], ['id', 47962], ['id', 29642], ['id', 12453], ['id', 49094]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.0004830842496844, 1.8738633148112154, 2.4706972019503706, 2.8156583301653457, 3.006787330709176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.9468971490859985})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.530003547668457})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.9221653938293457})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.4356746673583984})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.365976333618164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.437126636505127})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.748176097869873})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.678419351577759})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6292, 'crossentropy': 3.830818359375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.899125337600708})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.849631667137146})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.8828754425048828})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.8024852275848389})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7671477794647217})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9043567180633545})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7864500284194946})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 37747], ['id', 37071], ['id', 13025], ['id', 16322], ['id', 29871]], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.9465049831675377, 1.7107599837373906, 2.2873729131678067, 2.631324916177749, 2.8338952127196517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.7588214874267578})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4531235694885254})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7920336723327637})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.967797040939331})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3241169452667236})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.632827043533325})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.3819541931152344})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.3891119956970215})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.3125197887420654})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.514244318008423})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6305, 'crossentropy': 3.904384765625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.9287629127502441})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.996997594833374})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9702225923538208})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8833792209625244})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.94752836227417})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0159037113189697})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.9635645151138306})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 4459], ['id', 12645], ['id', 48562], ['id', 15731], ['id', 36712]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.124001404248845, 1.8445057256827455, 2.400470947620759, 2.7920682812426776, 3.0178017673630455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.7366397380828857})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.997969150543213})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.252689838409424})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.506995439529419})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.471559524536133})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.731947898864746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.675684928894043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.5430221557617188})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.8860483169555664})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.646, 'crossentropy': 3.0414818359375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.703080415725708})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.024993896484375})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.70521879196167})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8426342010498047})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8757290840148926})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.7105329036712646})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7860238552093506})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.652203917503357})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 43665], ['id', 58001], ['id', 13882], ['id', 10042], ['id', 15031]], 'labels': [-1, 8, 6, -1, 8], 'scores': [1.0288091912941746, 1.9484962227202436, 2.6214860726436164, 2.996014451808387, 3.2002731510776385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5513970851898193})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.103022336959839})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.1814889907836914})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.4551587104797363})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.6153817176818848})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.9390053749084473})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.5684986114501953})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.1543397903442383})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.003326177597046})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.781264066696167})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6736, 'crossentropy': 2.86948671875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.446559190750122})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.54458749294281})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6362545490264893})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8050477504730225})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.754460096359253})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6250169277191162})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 27164], ['id', 49311], ['id', 25783], ['id', 58877], ['id', 3784]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0099430049233207, 1.8695613367568806, 2.5032765319769075, 2.8315281017009157, 3.018910143824708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.5637949705123901})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.8549250364303589})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.648502826690674})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.642554521560669})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7567875385284424})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 2.006282421875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.281954288482666})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2754606008529663})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1881623268127441})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.226639747619629})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 26842], ['id', 57806], ['id', 25927], ['id', 20111], ['id', 58510]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.8180491122243888, 1.4897922183176244, 1.9577269932412298, 2.3213347868266236, 2.5891165148562]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.5974467992782593})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.828721523284912})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.3858931064605713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.137357234954834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6045894622802734})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.782975673675537})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.786332607269287})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.0734453201293945})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.944990634918213})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.0345025062561035})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6645, 'crossentropy': 3.0611490234375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7663671970367432})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.785007119178772})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.6731467247009277})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7424628734588623})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.6246366500854492})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7960245609283447})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6538561582565308})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 42796], ['id', 9073], ['id', 40183], ['id', 47646], ['id', 55176]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2005707803319967, 2.0740963700420627, 2.663762607132597, 2.9577700250153267, 3.0979244348802633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.6444134712219238})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.051814556121826})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.1616921424865723})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.4236016273498535})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7715330123901367})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7705631256103516})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6502, 'crossentropy': 2.39714296875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2678560018539429})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3003690242767334})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2673194408416748})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2479820251464844})
store['active_learning_steps'][23]['eval_training']['best_epoch']=1
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 57628], ['id', 37262], ['id', 59356], ['id', 33033], ['id', 8838]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8132465745717312, 1.4811141959253713, 1.9201836261510619, 2.1719166932326273, 2.324086915912856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.6815898418426514})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1601741313934326})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.285184383392334})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.817795753479004})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.9320240020751953})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.018096923828125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.000119686126709})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2719345092773438})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.137190818786621})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.158123731613159})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.36926531791687})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.2358453273773193})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.641, 'crossentropy': 3.49243671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5702860355377197})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7589218616485596})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.880820870399475})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8661551475524902})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7746531963348389})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.816114902496338})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34793], ['id', 4727], ['id', 28880], ['id', 13374], ['id', 46375]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.9087416252041571, 1.642030707400697, 2.1891936421339615, 2.5477704263619163, 2.7444007831099637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4803097248077393})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9576839208602905})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.201604127883911})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1379339694976807})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.425114870071411})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.7091026306152344})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.9291396141052246})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.444912910461426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.680331230163574})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.7969741821289062})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.01151704788208})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.8801565170288086})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6607, 'crossentropy': 2.723759375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.374943494796753})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6580517292022705})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.6752979755401611})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.57196044921875})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.597714900970459})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5262913703918457})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.5646331310272217})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.583216905593872})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.5655570030212402})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.600294589996338})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.680206537246704})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 3236], ['id', 30332], ['id', 57158], ['id', 56213], ['id', 27468]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.9322429777841235, 1.6934513500491244, 2.2709974101669124, 2.637240669965693, 2.8059618678961167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3469507694244385})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.6776913404464722})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.0610904693603516})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1668648719787598})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.309569835662842})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.4954442977905273})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.2697339057922363})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.5571789741516113})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4402871131896973})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.4037888050079346})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.8361387252807617})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.9605026245117188})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.532048225402832})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 3.087413787841797})
store['active_learning_steps'][26]['training']['best_epoch']=11
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6719, 'crossentropy': 2.955221875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4821763038635254})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6901752948760986})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8041884899139404})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6304378509521484})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6467070579528809})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6873817443847656})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7023088932037354})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.762882947921753})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6639015674591064})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 19298], ['id', 17697], ['id', 31699], ['id', 22841], ['id', 44013]], 'labels': [-1, -1, -1, 4, -1], 'scores': [1.005342023982775, 1.8397482721471148, 2.395175150121212, 2.726309282906623, 2.8888529953310043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3935691118240356})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7717918157577515})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.147230863571167})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.055630683898926})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.3158376216888428})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.30849027633667})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.247899293899536})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.596975564956665})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4576973915100098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.4731078147888184})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8683362007141113})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.3362162113189697})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.417746067047119})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.614830255508423})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6518921852111816})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.596992015838623})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.790285587310791})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.7251431941986084})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.950225353240967})
store['active_learning_steps'][27]['training']['best_epoch']=16
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 3.00245078125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4408199787139893})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7141027450561523})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6413726806640625})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6033613681793213})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.6507697105407715})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6057381629943848})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.468926191329956})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5278302431106567})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6738862991333008})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5017380714416504})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5730539560317993})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5803961753845215})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 2418], ['id', 33020], ['id', 18332], ['id', 49983], ['id', 14829]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2022120743970972, 2.186601104373624, 2.819982103124589, 3.206557326036449, 3.3863802771429956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4281151294708252})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8314491510391235})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.2028350830078125})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5357165336608887})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.5169787406921387})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.705017566680908})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6634, 'crossentropy': 2.5423310546875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3381783962249756})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3937702178955078})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.330063819885254})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.370004653930664})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.314624547958374})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 11302], ['id', 33400], ['id', 49942], ['id', 52898], ['id', 11734]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9414702764310388, 1.6366630393221184, 2.1645933548483205, 2.4727307148083835, 2.6380225025118893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.422984004020691})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9259190559387207})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1936275959014893})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.787442445755005})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.2945752143859863})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.2043709754943848})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.853144645690918})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.0554215908050537})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.229010581970215})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6588, 'crossentropy': 3.306614453125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2573277950286865})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4629744291305542})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.487501859664917})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4027645587921143})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.418416976928711})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4057323932647705})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4245469570159912})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4359266757965088})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 6181], ['id', 13087], ['id', 46261], ['id', 11532], ['id', 48912]], 'labels': [-1, 0, -1, -1, -1], 'scores': [1.143938065084338, 1.9514718755987421, 2.5513460585173195, 2.975909588728737, 3.2458056846652497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5481598377227783})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7571239471435547})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.076131820678711})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.420999050140381})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.392202854156494})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6454, 'crossentropy': 1.90911796875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.297320008277893})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1865053176879883})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.153519868850708})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0796266794204712})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 47945], ['id', 21385], ['id', 46384], ['id', 56561], ['id', 59657]], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.7288926087206662, 1.3819151934957055, 1.8930600146147807, 2.2328352410658843, 2.4518796304031047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2044198513031006})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.9658832550048828})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.030769109725952})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.2620182037353516})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6684, 'crossentropy': 1.33756171875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.115602970123291})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.06711745262146})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0182240009307861})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 52659], ['id', 30791], ['id', 11852], ['id', 15521], ['id', 55069]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7898130696977739, 1.3207638163546864, 1.7195588787091207, 2.0163781694303484, 2.216987682695021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4785921573638916})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8815491199493408})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.3159236907958984})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9926323890686035})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.5986385345458984})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3508758544921875})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.64688777923584})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.605414628982544})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.6977334022521973})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6648, 'crossentropy': 2.38335546875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3626161813735962})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.552918791770935})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6385722160339355})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5898836851119995})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6231272220611572})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5750999450683594})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6179213523864746})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4820555448532104})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 14807], ['id', 59192], ['id', 14619], ['id', 43781], ['id', 57965]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1090851242028776, 1.8674037905250929, 2.4621379313272156, 2.8743233876920358, 3.0630749979250016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.481123924255371})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8537817001342773})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.8967230319976807})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0939207077026367})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.1646885871887207})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4453072547912598})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6708, 'crossentropy': 2.298094921875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2414953708648682})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3384727239608765})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.28965163230896})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2352228164672852})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2110803127288818})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 6875], ['id', 45488], ['id', 47486], ['id', 59757], ['id', 40624]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9694587418345613, 1.7383751303387238, 2.3442279946507414, 2.71955763740425, 2.9290465925919413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.457883596420288})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7760120630264282})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.149397850036621})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.3887991905212402})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.777015447616577})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.5890986919403076})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.85219669342041})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.3042044639587402})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6693, 'crossentropy': 2.924541015625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3646669387817383})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3613872528076172})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.485366940498352})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.594658374786377})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.490124225616455})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4273760318756104})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 46398], ['id', 3066], ['id', 3916], ['id', 2121], ['id', 52722]], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.8307410493270273, 1.514791014917147, 2.0829309484278293, 2.419336939072063, 2.6438121675832367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2795629501342773})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6836576461791992})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.7700358629226685})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.867382287979126})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.01906681060791})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6754, 'crossentropy': 1.7042314453125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2579867839813232})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3146982192993164})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1945414543151855})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.240427017211914})
store['active_learning_steps'][35]['eval_training']['best_epoch']=3
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 32695], ['id', 11436], ['id', 50752], ['id', 25309], ['id', 44853]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.861467918375711, 1.516909222541411, 1.9826668740659734, 2.3013473408042975, 2.4878986665217204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5056294202804565})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.6418328285217285})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8408079147338867})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0341074466705322})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.0782034397125244})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5339505672454834})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6628031730651855})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.595822334289551})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.4200010299682617})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.6549441814422607})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.729214668273926})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.793614387512207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.835759162902832})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.5306150913238525})
store['active_learning_steps'][36]['training']['best_epoch']=11
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6849, 'crossentropy': 2.88505078125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.406713604927063})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.498338222503662})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5085316896438599})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7898476123809814})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.699044108390808})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.6509313583374023})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 23363], ['id', 53977], ['id', 8756], ['id', 26760], ['id', 31037]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.989852922831129, 1.8239019820972617, 2.4114370344142806, 2.701547059840216, 2.868011914693175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2623863220214844})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5287679433822632})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9516150951385498})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.089797019958496})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.25352144241333})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.433802604675293})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6765, 'crossentropy': 2.0885021484375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2436692714691162})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1875519752502441})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2136814594268799})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.256533145904541})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2574033737182617})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 51600], ['id', 53863], ['id', 40228], ['id', 51828], ['id', 23487]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.7951200810836851, 1.402311390139244, 1.8238913385713023, 2.142033027691192, 2.329204596239326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3641180992126465})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5608808994293213})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0084290504455566})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.9922643899917603})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.2529377937316895})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1788063049316406})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4809494018554688})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5261945724487305})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.3679591796875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3077443838119507})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4241235256195068})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3611122369766235})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.398391604423523})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3425495624542236})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3245203495025635})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3386911153793335})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 19187], ['id', 30842], ['id', 37837], ['id', 31177], ['id', 22554]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9797271126473976, 1.7079415828201756, 2.3084185576436647, 2.6808914221534645, 2.903884653430456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3357653617858887})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.675508975982666})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.865851640701294})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.9688308238983154})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.621084213256836})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2429447174072266})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.448516368865967})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.228337287902832})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.444578170776367})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.8402976989746094})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.635643482208252})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.751950263977051})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6813, 'crossentropy': 2.839897265625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3603627681732178})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6515768766403198})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6744859218597412})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.693103551864624})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.612722396850586})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6565358638763428})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6614190340042114})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4919979572296143})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 53872], ['id', 14644], ['id', 3641], ['id', 5153], ['id', 11570]], 'labels': [-1, -1, -1, 2, 8], 'scores': [0.952708180115696, 1.7337065613635732, 2.2454274224500645, 2.6031124122274267, 2.8649478192338393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4492816925048828})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6173911094665527})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.8606168031692505})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.0005555152893066})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.4155638217926025})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.2006430625915527})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.239473342895508})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2623062133789062})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.338350296020508})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.876657009124756})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.38326096534729})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6877, 'crossentropy': 2.8742181640625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.352697491645813})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5914006233215332})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.675243616104126})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5214837789535522})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5849418640136719})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5957573652267456})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5802314281463623})
store['active_learning_steps'][40]['eval_training']['best_epoch']=4
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 22524], ['id', 50943], ['id', 51323], ['id', 19973], ['id', 31117]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1192780438344054, 1.9321460602032752, 2.5388523154450358, 2.9326966976721818, 3.1430677432538525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3901004791259766})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5934224128723145})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0794315338134766})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.2318572998046875})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.49477219581604})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6873, 'crossentropy': 1.807876171875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1725064516067505})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.19050931930542})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1456412076950073})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1073020696640015})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 19241], ['id', 11066], ['id', 6364], ['id', 47314], ['id', 31778]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7049138681121747, 1.3433451469177276, 1.8326111677438615, 2.1341962585086938, 2.34983780695861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3885998725891113})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7652854919433594})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.034428119659424})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.333037853240967})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.5517189502716064})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6192431449890137})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.9072258472442627})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.8417747020721436})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.789012908935547})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6721, 'crossentropy': 2.760519140625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2392096519470215})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3558118343353271})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4086277484893799})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3105876445770264})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3074562549591064})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3472669124603271})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2402453422546387})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.325425386428833})
store['active_learning_steps'][42]['eval_training']['best_epoch']=5
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 42198], ['id', 19904], ['id', 32637], ['id', 24410], ['id', 6598]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2001248893237684, 2.152824864141402, 2.795158787423283, 3.148006896003759, 3.3004018746781787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3398903608322144})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.6976145505905151})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9162170886993408})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9621164798736572})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5322751998901367})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.595933437347412})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.337517261505127})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6736, 'crossentropy': 2.33844765625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3333745002746582})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.382431983947754})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4768129587173462})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3945107460021973})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3172354698181152})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3104650974273682})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 5852], ['id', 51452], ['id', 2605], ['id', 35424], ['id', 51315]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9934757311962545, 1.8208588591498358, 2.37787885736259, 2.724655009935625, 2.8925011839217394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.491180419921875})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.709324598312378})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8279590606689453})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.9949010610580444})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.3679351806640625})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.3661365509033203})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.403813362121582})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4486188888549805})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6649, 'crossentropy': 2.475724609375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2358429431915283})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.416869044303894})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3916428089141846})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.3425774574279785})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.348520278930664})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3771765232086182})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3899177312850952})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 32812], ['id', 4767], ['id', 39074], ['id', 48047], ['id', 25280]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.8854631397886239, 1.6162617282384861, 2.1519562672005286, 2.4516821464747998, 2.6313298236589837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3822972774505615})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.6921136379241943})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.06748104095459})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0837106704711914})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.372812509536743})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.821920156478882})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1577811241149902})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.5089142322540283})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.5861597061157227})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.743793487548828})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.681095600128174})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6888887882232666})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.8335304260253906})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.941460609436035})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.215322732925415})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.898453712463379})
store['active_learning_steps'][45]['training']['best_epoch']=13
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6742, 'crossentropy': 3.086318359375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3666534423828125})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.7023168802261353})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.6306841373443604})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7227472066879272})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7105661630630493})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.6260120868682861})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5547491312026978})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.6955723762512207})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.584864616394043})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5952436923980713})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 13030], ['id', 15988], ['id', 6860], ['id', 10210], ['id', 49569]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0630335328688298, 1.9434862398031243, 2.6212941210257465, 3.0559463894247236, 3.2701586031771375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3573262691497803})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.632460355758667})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9970381259918213})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.1038098335266113})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.336930274963379})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.3974742889404297})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.671905994415283})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.8199894428253174})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.0840749740600586})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4262523651123047})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.7800731658935547})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.846879005432129})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 3.051614761352539})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.961080551147461})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.6313633918762207})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 3.1853437423706055})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.9281387329101562})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 3.384248733520508})
store['active_learning_steps'][46]['training']['best_epoch']=15
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6827, 'crossentropy': 3.0134712890625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2837071418762207})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2923648357391357})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3811124563217163})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4483973979949951})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.30873703956604})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.312233805656433})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2929871082305908})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2751672267913818})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2514324188232422})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3634475469589233})
store['active_learning_steps'][46]['eval_training']['best_epoch']=7
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 21241], ['id', 38086], ['id', 42415], ['id', 59029], ['id', 20161]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.048044924811999, 1.8930474436919191, 2.4518632567860257, 2.8445682380982285, 3.091034374252299]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2854225635528564})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.680143117904663})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9736744165420532})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.385465145111084})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.5153563022613525})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1260910034179688})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.5154075622558594})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.280189037322998})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.640632152557373})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6816, 'crossentropy': 2.515583984375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3704922199249268})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.477919578552246})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5576164722442627})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4650532007217407})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.5318104028701782})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5171587467193604})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.443790078163147})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5747066736221313})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 28511], ['id', 52800], ['id', 30570], ['id', 3616], ['id', 43193]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.8948645217248898, 1.5379915069506378, 2.042133723276752, 2.4062950428868253, 2.6364572569610756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.362086534500122})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7018687725067139})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9834668636322021})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.3246212005615234})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.4118001461029053})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6821, 'crossentropy': 1.7947849609375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2257356643676758})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2428016662597656})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1405978202819824})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1247398853302002})
store['active_learning_steps'][48]['eval_training']['best_epoch']=3
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 37306], ['id', 1254], ['id', 26756], ['id', 43898], ['id', 34422]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.802435362883769, 1.427683045069061, 1.8710515250124793, 2.1598071258575517, 2.376649470061283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.344112515449524})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.658913016319275})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7618294954299927})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9211792945861816})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.090327024459839})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1368229389190674})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6775, 'crossentropy': 1.94228984375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3147203922271729})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2966375350952148})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2331931591033936})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1318979263305664})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1985113620758057})
store['active_learning_steps'][49]['eval_training']['best_epoch']=4
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 19903], ['id', 1050], ['id', 4381], ['id', 31891], ['id', 3978]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.0938198471506575, 1.8947473982583523, 2.4434974893121546, 2.8018837429516448, 2.9860050002765073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2862772941589355})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6776180267333984})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0632877349853516})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.1451549530029297})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4642701148986816})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.237738609313965})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5077009201049805})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.3606624603271484})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.7788636684417725})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6854, 'crossentropy': 2.441494140625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3323110342025757})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4657585620880127})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.5000379085540771})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4421205520629883})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.350754976272583})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5400002002716064})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5342204570770264})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.4818778038024902})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 8586], ['id', 55304], ['id', 18838], ['id', 46140], ['id', 7128]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0107980626981106, 1.9078832153392433, 2.522774179326956, 2.901552541660254, 3.103196810729812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.400842308998108})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.5217995643615723})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.941072940826416})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2726821899414062})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.203287124633789})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2835166454315186})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.351860523223877})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6792, 'crossentropy': 2.342871484375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.4631246328353882})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4354562759399414})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4862518310546875})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4470158815383911})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4092838764190674})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3395922183990479})
store['active_learning_steps'][51]['eval_training']['best_epoch']=6
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 53494], ['id', 23152], ['id', 33362], ['id', 33549], ['id', 893]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.867650422574133, 1.5734941589136429, 2.063242380469945, 2.3599823322158153, 2.516958666370098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.479020595550537})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.7505898475646973})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0082778930664062})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.28717041015625})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4127960205078125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.755070209503174})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.6472902297973633})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.6889076232910156})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.7578351497650146})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.760777235031128})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.88877010345459})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 3.410649299621582})
store['active_learning_steps'][52]['training']['best_epoch']=9
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6804, 'crossentropy': 3.1054421875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4663445949554443})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.607001543045044})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7204937934875488})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.838742971420288})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.7016124725341797})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.69773268699646})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7188928127288818})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.6234630346298218})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4347805976867676})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6338104009628296})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6428394317626953})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 45353], ['id', 38946], ['id', 15752], ['id', 39169], ['id', 20181]], 'labels': [-1, -1, 8, 8, -1], 'scores': [0.9136930545676861, 1.620269379133914, 2.175820282569271, 2.548856940959469, 2.7553721817055354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2781097888946533})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.6142125129699707})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.090463161468506})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.1271395683288574})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.1012067794799805})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.327620267868042})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6705, 'crossentropy': 2.1713810546875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1899527311325073})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2670929431915283})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2226769924163818})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2522400617599487})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2266936302185059})
store['active_learning_steps'][53]['eval_training']['best_epoch']=4
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 10026], ['id', 48668], ['id', 26427], ['id', 38716], ['id', 10840]], 'labels': [1, -1, -1, -1, -1], 'scores': [0.7712613958546508, 1.4351532760174062, 1.9974847665913404, 2.388328994102783, 2.629981286780705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.353834629058838})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.650137186050415})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.96218740940094})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.0961828231811523})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.260589122772217})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.1699037551879883})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4830117225646973})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.413496971130371})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.618553638458252})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.712562322616577})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.681637763977051})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.922848701477051})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6757, 'crossentropy': 2.8870826171875}
