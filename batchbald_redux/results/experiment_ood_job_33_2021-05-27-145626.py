store = {}
store['timestamp']=1622123786
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=33']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=33
store['worker_id']=33
store['num_workers']=80
store['config']={'seed': 1269, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.4352900981903076})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.0573983192443848})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.461904287338257})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1190996170043945})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.505178928375244})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2118725776672363})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.94419527053833})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5896, 'crossentropy': 3.47516171875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.8857426643371582})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9750988483428955})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.9860484600067139})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.8529114723205566})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.918762445449829})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 46487], ['ood', 2835], ['ood', 39806], ['ood', 20905], ['id', 24202]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0158160956010944, 1.7861062733886781, 2.258436026042346, 2.51557489897454, 2.6587982316137806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.861043930053711})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.439403533935547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.822017192840576})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.8965635299682617})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5813, 'crossentropy': 1.821228515625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.4708056449890137})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4072222709655762})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.33111572265625})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 44998], ['id', 6052], ['id', 36985], ['id', 25420], ['id', 24008]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4886624523827864, 0.9010092614643987, 1.218706378284434, 1.4870753651266213, 1.6970380276284152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.9045439958572388})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.562704563140869})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.109713077545166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.148768901824951})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.4846529960632324})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.7206263542175293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.6928775310516357})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.7881851196289062})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.8167574405670166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.8520355224609375})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5811, 'crossentropy': 3.876657421875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.6799962520599365})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.9069101810455322})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.006544589996338})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.087167739868164})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 3359], ['id', 27147], ['id', 23371], ['id', 4641], ['id', 15274]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6879809553499188, 1.263835871671696, 1.6938414076727897, 2.025476817227174, 2.2417029312830454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5150883197784424})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7001302242279053})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.084718704223633})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2381181716918945})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.3697307109832764})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.380810260772705})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.4618213176727295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.296715259552002})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.3892693519592285})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9461488723754883})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.498260736465454})
store['active_learning_steps'][3]['training']['best_epoch']=8
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6579, 'crossentropy': 2.42241328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3826096057891846})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5098912715911865})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.481156826019287})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6387814283370972})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4898531436920166})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5102877616882324})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 8546], ['ood', 10237], ['id', 2434], ['id', 42830], ['id', 13734]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6368978421081697, 1.1320820298908032, 1.5667037211821055, 1.8964668225727808, 2.1583275549061014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.6507060527801514})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7579425573349})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.3788652420043945})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.466036796569824})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.4276585578918457})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.633, 'crossentropy': 1.9122498046875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2974600791931152})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2997491359710693})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3213274478912354})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3299576044082642})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 40966], ['id', 5199], ['id', 30128], ['id', 50911], ['id', 48666]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6380533622088209, 1.1034899059804348, 1.4922647945939227, 1.7772451892750007, 2.0158154993709205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3433337211608887})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.529860019683838})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9118614196777344})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.117431402206421})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6454, 'crossentropy': 1.3561765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2463306188583374})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1742188930511475})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1697707176208496})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 42521], ['id', 41210], ['id', 57620], ['id', 17263], ['id', 56937]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4218298461096188, 0.753838906271795, 1.031393772124508, 1.2824861453400214, 1.4960388070021242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3619422912597656})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6666145324707031})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9211041927337646})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.070173978805542})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.245720863342285})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6215, 'crossentropy': 1.67402890625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2500776052474976})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2089020013809204})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1856861114501953})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.171326994895935})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 45029], ['id', 35427], ['id', 14019], ['id', 22613], ['ood', 31370]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6116301702894386, 1.0274551641462466, 1.3696171314327095, 1.651318490531854, 1.8847920720772873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.335885763168335})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5739152431488037})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7170748710632324})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8764314651489258})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8092243671417236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.9580744504928589})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2636961936950684})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.1767477989196777})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.304478645324707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.342240333557129})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6679, 'crossentropy': 2.210398046875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2063138484954834})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2774115800857544})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2184360027313232})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2887641191482544})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2652376890182495})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.213806390762329})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2731904983520508})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2155412435531616})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.24376380443573})
store['active_learning_steps'][7]['eval_training']['best_epoch']=8
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 23694], ['id', 15143], ['id', 50913], ['id', 4713], ['id', 24584]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6221708136766453, 1.1333308596279323, 1.584198399444471, 1.9138606621971128, 2.1478233294762212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3031673431396484})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.564278483390808})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.5725374221801758})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.9194934368133545})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.968841552734375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.173694610595703})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.188546657562256})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.31459379196167})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6842, 'crossentropy': 1.9074822265625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1902556419372559})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3396391868591309})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.334219217300415})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2648937702178955})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.267298936843872})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1944472789764404})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 39335], ['id', 14174], ['id', 44410], ['ood', 2941], ['id', 15635]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4399977746744379, 0.8316244397819248, 1.1784717395983986, 1.4696187673156267, 1.6958009513795336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2676730155944824})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3065332174301147})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.53565514087677})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9003803730010986})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9097466468811035})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6635, 'crossentropy': 1.38248115234375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.252551794052124})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1199827194213867})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.117661476135254})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0615761280059814})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 39819], ['id', 1625], ['id', 16876], ['id', 39944], ['id', 31797]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47813018649594397, 0.8158180131152823, 1.1170344390292666, 1.3871823666238399, 1.6209158533353447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2559895515441895})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4422646760940552})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6754615306854248})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8341906070709229})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.1050209999084473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9210853576660156})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.054576873779297})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.253539562225342})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.1658010482788086})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.200131893157959})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6757, 'crossentropy': 2.21694609375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2116737365722656})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.246598243713379})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2889584302902222})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2898128032684326})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2702380418777466})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3104751110076904})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2684414386749268})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 34503], ['id', 28908], ['ood', 29434], ['id', 43187], ['id', 56104]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6663233484037329, 1.1962471924679576, 1.6796704700445981, 2.05494283759129, 2.331034437982348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1900928020477295})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3008038997650146})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3672287464141846})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4663136005401611})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.7505738735198975})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8748703002929688})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.008052349090576})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7001, 'crossentropy': 1.6084802734375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1594715118408203})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.232947587966919})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1458590030670166})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1344102621078491})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1034355163574219})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1177303791046143})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 31251], ['id', 21906], ['id', 43735], ['id', 55968], ['id', 35971]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.534262827355323, 1.0221545374660819, 1.4268154978234024, 1.7582940659968145, 1.9898720031277692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2113196849822998})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2107934951782227})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4327110052108765})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6653470993041992})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.94578218460083})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.0075719356536865})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6823, 'crossentropy': 1.478961328125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.186963677406311})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.147559642791748})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1360416412353516})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0746004581451416})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.049785852432251})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 55765], ['id', 36424], ['id', 43934], ['id', 29184], ['id', 32276]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6128853826308958, 1.0754018669438214, 1.4494771811927176, 1.764486856183959, 1.9993393209432657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.298940658569336})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.3039271831512451})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4008346796035767})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6392693519592285})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.7574336528778076})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8772610425949097})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.9450314044952393})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.0074825286865234})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.069592237472534})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.1670656204223633})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.401822566986084})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6852, 'crossentropy': 2.1294865234375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2049869298934937})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.195387840270996})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2450053691864014})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2833373546600342})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2662599086761475})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2462244033813477})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2917213439941406})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.324368953704834})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.313492774963379})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 18233], ['id', 1877], ['id', 3234], ['id', 33674], ['id', 31717]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6299676861359789, 1.2248559182771204, 1.6993673655659602, 2.0357457459758943, 2.229413651526823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.210325837135315})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1619751453399658})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4539051055908203})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5409290790557861})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7728009223937988})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.78428316116333})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.0405449867248535})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.169297218322754})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6949, 'crossentropy': 1.7881630859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.199610948562622})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1318144798278809})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.186805009841919})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1635205745697021})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2162675857543945})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1923965215682983})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 18183], ['id', 19320], ['id', 12467], ['ood', 37794], ['id', 18913]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5140068363263093, 0.9857992928525166, 1.381551077621066, 1.6362543489804846, 1.8220580809555091]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.246732234954834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.186673641204834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4513752460479736})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5256826877593994})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6696869134902954})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6832836866378784})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8170263767242432})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6921, 'crossentropy': 1.5881779296875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2509667873382568})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0962878465652466})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.014258861541748})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0694472789764404})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0562641620635986})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0485976934432983})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 39272], ['id', 58300], ['id', 42984], ['id', 54720], ['id', 34841]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4993072119457469, 0.967562489935442, 1.3622123142729308, 1.6805928243882775, 1.877723989450895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2131338119506836})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2617003917694092})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3523602485656738})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.694045066833496})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7226721048355103})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.967441439628601})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1315054893493652})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3734281063079834})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1031618118286133})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6771, 'crossentropy': 2.004571875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.196571707725525})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0901672840118408})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.13071870803833})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.16989004611969})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1081804037094116})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.192496418952942})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1346633434295654})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 56754], ['id', 49630], ['id', 48256], ['id', 43284], ['id', 36339]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5578454266318675, 1.0693442554846895, 1.489980365610486, 1.8307611266936927, 2.0724504746501493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2877013683319092})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2334845066070557})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5341882705688477})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6184890270233154})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.7775588035583496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.085183620452881})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.127171039581299})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.0508196353912354})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.9214709997177124})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1335175037384033})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6975, 'crossentropy': 2.014862890625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1723295450210571})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1236157417297363})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.160963773727417})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1737984418869019})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1874431371688843})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2066590785980225})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 51415], ['id', 30247], ['id', 3410], ['id', 19995], ['id', 3225]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.647177156413365, 1.1472241276642565, 1.5650987103566818, 1.8931921230710884, 2.135484913770366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1669830083847046})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1666549444198608})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3214781284332275})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4123406410217285})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5519561767578125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7158644199371338})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6937, 'crossentropy': 1.3264314453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2111549377441406})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0689029693603516})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0915701389312744})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.056082010269165})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9887197017669678})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 40241], ['ood', 51415], ['id', 59671], ['id', 43193], ['ood', 22677]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.48801527466640504, 0.9055557577471163, 1.2631303484818606, 1.5660169496521128, 1.8033789827075477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.231203317642212})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1377415657043457})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.212900161743164})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4295859336853027})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6128909587860107})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6015048027038574})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8040844202041626})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8041505813598633})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6957, 'crossentropy': 1.54215712890625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2136893272399902})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.100166916847229})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0523629188537598})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0734992027282715})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0928702354431152})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.033433437347412})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.085322380065918})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 31557], ['id', 31662], ['id', 4645], ['id', 2572], ['id', 44716]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5586579866164922, 1.0453556721860586, 1.470501305176997, 1.7770152544947742, 1.9977525008443937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2988394498825073})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.147611379623413})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2818751335144043})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4534204006195068})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6476893424987793})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.798008918762207})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.815586805343628})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8922903537750244})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.029048442840576})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.9371449947357178})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.3030428886413574})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.127917528152466})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.144083261489868})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3154845237731934})
store['active_learning_steps'][20]['training']['best_epoch']=11
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6999, 'crossentropy': 2.1225751953125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2288376092910767})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0888185501098633})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1293011903762817})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1650640964508057})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1724529266357422})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1391072273254395})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1510040760040283})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 54227], ['id', 32330], ['id', 55510], ['ood', 2324], ['ood', 35750]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6629752320398079, 1.2868105845584532, 1.797658219963763, 2.183358723751426, 2.4504815138442035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.262857437133789})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.115748405456543})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2385764122009277})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.3556580543518066})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5121777057647705})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5927797555923462})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.618719220161438})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7679107189178467})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8219621181488037})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9931484460830688})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8828132152557373})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7015, 'crossentropy': 1.8476759765625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2365374565124512})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.129544973373413})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.123154640197754})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1549031734466553})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.124328851699829})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1085824966430664})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1177310943603516})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1178284883499146})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0867195129394531})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0702548027038574})
store['active_learning_steps'][21]['eval_training']['best_epoch']=9
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 20145], ['id', 34122], ['id', 40395], ['id', 59703], ['id', 15631]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6401813825920113, 1.2069934971244218, 1.673607399162771, 2.0607780984156356, 2.3470844524626804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.4083867073059082})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.239685297012329})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.3457499742507935})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5322710275650024})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.422147512435913})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.7477359771728516})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6890333890914917})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.919049620628357})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.699, 'crossentropy': 1.5388103515625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2567408084869385})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.106513261795044})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0742931365966797})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.047867774963379})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0214861631393433})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0423647165298462})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0226705074310303})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 10251], ['id', 5323], ['id', 22547], ['id', 26279], ['id', 10625]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5773513151063491, 1.0934496527133546, 1.5180755188106998, 1.866307344856307, 2.1140006373436826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2565369606018066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0888915061950684})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2251348495483398})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3719933032989502})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5545635223388672})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.666579246520996})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.705, 'crossentropy': 1.26598818359375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2460577487945557})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.044952392578125})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9733011722564697})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9881715774536133})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9538916349411011})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 3357], ['id', 9862], ['id', 4380], ['id', 33596], ['id', 34817]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46260443893976233, 0.8685999698531948, 1.2426564091572745, 1.5545035637370388, 1.7956641228369472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3006837368011475})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1078567504882812})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1796436309814453})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.28394615650177})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3627588748931885})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.6484524011611938})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.84092116355896})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.7468628883361816})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6997, 'crossentropy': 1.4716982421875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2493778467178345})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.008608102798462})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9952801465988159})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9792463779449463})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9688032269477844})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9578834176063538})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9479382038116455})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 35334], ['id', 40742], ['id', 27800], ['id', 19469], ['ood', 14458]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5030252210758037, 0.9654653596021392, 1.3644597795438553, 1.7091692211852765, 1.9671480379962691]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2691307067871094})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.019381046295166})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1692235469818115})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1756502389907837})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3619904518127441})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.3501629829406738})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.508066177368164})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.5340871810913086})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6558897495269775})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.6048953533172607})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.7095913887023926})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7227, 'crossentropy': 1.56439658203125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1432726383209229})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0665059089660645})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0554161071777344})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.994647741317749})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0671510696411133})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0208839178085327})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9859633445739746})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0319430828094482})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0258564949035645})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0205498933792114})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 8718], ['ood', 7782], ['id', 5413], ['id', 34009], ['id', 8168]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5642309608163314, 1.0656395270906707, 1.48593047667626, 1.7812475245487525, 2.013160516859333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3260579109191895})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1378165483474731})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.193265438079834})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3597173690795898})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4122716188430786})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6467198133468628})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6596500873565674})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.802544116973877})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7063, 'crossentropy': 1.5147205078125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.309349536895752})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0709810256958008})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0823042392730713})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0042492151260376})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0067293643951416})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0076727867126465})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9575037956237793})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 48763], ['id', 16858], ['id', 23846], ['id', 17267], ['id', 58204]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5600069000457273, 1.0489635849794396, 1.4641220105706871, 1.7990028205078623, 2.0288383902122265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4108586311340332})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1684298515319824})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2147910594940186})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2473809719085693})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4620625972747803})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3354103565216064})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.464644432067871})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 1.312215625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.185484528541565})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0807174444198608})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.007439374923706})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0064942836761475})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9562951326370239})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9791586399078369})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 39706], ['id', 25195], ['id', 36075], ['id', 40677], ['id', 2985]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.47869750046397375, 0.8920113567644465, 1.2714235104856737, 1.6140550656409722, 1.9046666058350699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.338356375694275})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.070603847503662})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1601612567901611})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2263593673706055})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3003653287887573})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.516911506652832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4608150720596313})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6823124885559082})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.58553946018219})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.8889782428741455})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.6602251529693604})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.8444212675094604})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7201, 'crossentropy': 1.58445751953125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.205330729484558})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9914891719818115})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.087480902671814})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9978270530700684})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9899835586547852})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0986523628234863})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.039625644683838})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.062561273574829})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 5374], ['id', 125], ['id', 43340], ['id', 16169], ['id', 22615]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.628604435818644, 1.1425116514779234, 1.5647552696033085, 1.9019126336878864, 2.149968616509609]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2571433782577515})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0381381511688232})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.048398494720459})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.1822187900543213})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2045482397079468})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.344865322113037})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3517425060272217})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 1.239375390625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1987966299057007})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9834335446357727})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9655719995498657})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9243360757827759})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.8806447982788086})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8972020149230957})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20302], ['id', 31637], ['id', 58636], ['id', 57000], ['id', 168]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.566534067070799, 1.0813100565413163, 1.4947926076738476, 1.8263804443083655, 2.064003419088303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.403886079788208})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0712255239486694})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0396759510040283})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1085598468780518})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.145682692527771})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.2117077112197876})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3787553310394287})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.5351719856262207})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.508171796798706})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.546318769454956})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.624243974685669})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7312, 'crossentropy': 1.5639708984375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.3707809448242188})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.064664602279663})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0122531652450562})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0025479793548584})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0423129796981812})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0630559921264648})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0563150644302368})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 18533], ['id', 4511], ['id', 27590], ['id', 16246], ['id', 21502]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5822464799021714, 1.1068387552526375, 1.5362942487198903, 1.8796494053968784, 2.155318919148381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.381324291229248})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0584648847579956})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0569989681243896})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0577538013458252})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2050890922546387})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.187981128692627})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.3564974069595337})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.2806919813156128})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.604682445526123})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.624343991279602})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7345, 'crossentropy': 1.380048046875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2597432136535645})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0421559810638428})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.061600685119629})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0011980533599854})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.004069447517395})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.967583179473877})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9540995359420776})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.014326572418213})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0165727138519287})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 39750], ['id', 56454], ['id', 15306], ['id', 35807], ['id', 12854]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7948322115099109, 1.314325925078677, 1.7542282540272636, 2.0904592232830765, 2.279721076785825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.246221899986267})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0024559497833252})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.031253457069397})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.123192310333252})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2057974338531494})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.331191062927246})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.373173475265503})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4388688802719116})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4004004001617432})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7201, 'crossentropy': 1.31290126953125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2993202209472656})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0110403299331665})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.00836980342865})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0122363567352295})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9358483552932739})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9677556753158569})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9155749082565308})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9504725933074951})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 7609], ['id', 21901], ['id', 52384], ['id', 19138], ['id', 59007]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4783409520169284, 0.9284535586108031, 1.3398404311779135, 1.671428950436595, 1.9206503102106813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.4569728374481201})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0584354400634766})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.06252121925354})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.087195873260498})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1588231325149536})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2459146976470947})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4441180229187012})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.322091817855835})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5555996894836426})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.444645881652832})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7325, 'crossentropy': 1.38755234375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2264806032180786})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0056612491607666})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8944265842437744})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9137224555015564})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8923190236091614})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8800197839736938})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.8937768340110779})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.869154155254364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8657982349395752})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 49891], ['id', 26462], ['id', 53054], ['id', 22605], ['id', 36660]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5241966637836895, 0.9855990864287971, 1.383129164881323, 1.695410681351058, 1.9328060127984816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.2841565608978271})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.074404001235962})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0306655168533325})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1431002616882324})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0755565166473389})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.183626413345337})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3627936840057373})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.4221715927124023})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5044281482696533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5382747650146484})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5368030071258545})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7148, 'crossentropy': 1.4962263671875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2949535846710205})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9798904657363892})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9655113816261292})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.94930100440979})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.958352267742157})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.030210018157959})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9849551916122437})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 226], ['ood', 10207], ['id', 5643], ['ood', 17849], ['id', 53463]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5600043331320466, 1.018626689054086, 1.4244558434901737, 1.7319268343658223, 1.9453121699811522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.3596563339233398})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.045082926750183})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0704357624053955})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.029543161392212})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2449402809143066})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3222655057907104})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2628533840179443})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5368338823318481})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.483499526977539})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6117579936981201})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.6966338157653809})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7174, 'crossentropy': 1.5185587890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2834649085998535})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0639472007751465})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9803658127784729})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.930201530456543})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9309539794921875})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9284963607788086})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.945640504360199})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9318788051605225})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.950308084487915})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 2223], ['id', 4689], ['id', 20430], ['id', 20918], ['id', 33804]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.571708445027791, 1.0908459183900527, 1.5359653398483175, 1.884718685392702, 2.135485659437837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3760871887207031})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0706366300582886})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9509196281433105})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0885844230651855})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.1878042221069336})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.2647063732147217})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1525778770446777})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4052263498306274})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.4707894325256348})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4919430017471313})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7387, 'crossentropy': 1.224372265625}
