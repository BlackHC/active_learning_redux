store = {}
store['timestamp']=1621030100
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=3']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=30
store['config']={'seed': 1238, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.4226536750793457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.8806400299072266})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9664621353149414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4383935928344727})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5837, 'crossentropy': 2.574746875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2943627834320068})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.2682485580444336})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2963720560073853})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 56792], ['ood', 45148], ['ood', 28928], ['ood', 50752], ['ood', 54422], ['ood', 46777], ['ood', 17774], ['ood', 44086], ['ood', 22034], ['ood', 4781]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0479626059532166, 1.047625482082367, 1.0406580567359924, 1.0330522060394287, 1.0291480422019958, 1.0289705395698547, 1.0232709050178528, 1.0186039209365845, 1.0124918222427368, 1.003955364227295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0803916454315186})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.6864094734191895})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.980869770050049})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.4080138206481934})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5861, 'crossentropy': 2.0718283203125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.375760555267334})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.3318108320236206})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3025319576263428})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 2312], ['id', 18486], ['id', 13754], ['id', 46518], ['id', 1191], ['id', 53867], ['id', 9302], ['id', 21376], ['id', 9832], ['id', 23416]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7251344919204712, 0.7194203734397888, 0.7084306478500366, 0.7083511352539062, 0.7040889859199524, 0.6957235932350159, 0.6935679912567139, 0.6870337128639221, 0.6853129267692566, 0.6825796365737915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.9693185091018677})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.7164626121520996})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.163422107696533})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.5663819313049316})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5676, 'crossentropy': 1.8487359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.3021174669265747})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2879748344421387})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.2737832069396973})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 46212], ['ood', 2073], ['id', 54905], ['id', 23988], ['id', 18584], ['id', 7402], ['id', 10860], ['id', 28812], ['id', 40744], ['id', 29383]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.53525710105896, 0.5313105583190918, 0.5249048471450806, 0.5128342509269714, 0.5117242932319641, 0.5083378553390503, 0.5056760311126709, 0.5022730827331543, 0.4979782700538635, 0.49792683124542236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.705809473991394})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.2137436866760254})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.669450283050537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.2281980514526367})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5868, 'crossentropy': 1.68071640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.2679564952850342})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2683331966400146})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2657660245895386})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 20652], ['id', 43193], ['id', 59054], ['id', 58670], ['id', 59818], ['id', 1204], ['id', 56328], ['id', 45570], ['id', 21074], ['id', 34393]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.556110680103302, 0.5467342138290405, 0.5325790643692017, 0.5193260908126831, 0.5059857964515686, 0.5038959980010986, 0.5004856586456299, 0.4991278648376465, 0.49122917652130127, 0.4857996702194214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3692514896392822})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.7951159477233887})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.080411195755005})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2304930686950684})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5896, 'crossentropy': 1.3962759765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3027091026306152})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2263851165771484})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.281484842300415})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 28018], ['id', 40304], ['id', 42695], ['id', 37740], ['id', 43265], ['id', 11926], ['id', 59838], ['id', 22547], ['ood', 56917], ['id', 1799]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4436551332473755, 0.4381905794143677, 0.4243687391281128, 0.4182605743408203, 0.4171900749206543, 0.4158581495285034, 0.4155944585800171, 0.4118729829788208, 0.4107552766799927, 0.4035811424255371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.4167790412902832})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.7296212911605835})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.8601634502410889})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.244967460632324})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5915, 'crossentropy': 1.43242119140625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.305694818496704})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.311838150024414})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.2815148830413818})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 57832], ['ood', 55481], ['ood', 12603], ['ood', 54476], ['ood', 22663], ['ood', 22679], ['ood', 58313], ['ood', 24755], ['ood', 23296], ['ood', 57910]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.45125067234039307, 0.44737374782562256, 0.4463297128677368, 0.4402191638946533, 0.43995511531829834, 0.43993234634399414, 0.43988513946533203, 0.4369020462036133, 0.43689870834350586, 0.4354597330093384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4568226337432861})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.5819698572158813})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6275148391723633})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.12197208404541})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.4927, 'crossentropy': 1.50165625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.4775390625, 'crossentropy': 1.4816174507141113})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.4400296211242676})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.459930419921875})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 34314], ['id', 55765], ['id', 59324], ['id', 47772], ['id', 41067], ['id', 35305], ['id', 2181], ['id', 14286], ['id', 56332], ['id', 30872]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.36142897605895996, 0.3561394214630127, 0.3559650182723999, 0.3558851480484009, 0.3554370403289795, 0.34208178520202637, 0.34141719341278076, 0.3403428792953491, 0.33621323108673096, 0.33017921447753906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.5338714122772217})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.6506609916687012})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7030556201934814})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0733096599578857})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5023, 'crossentropy': 1.54585087890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.490234375, 'crossentropy': 1.6185367107391357})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.4833984375, 'crossentropy': 1.5753567218780518})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.48828125, 'crossentropy': 1.5454585552215576})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 27800], ['id', 13598], ['id', 54881], ['id', 49891], ['id', 13829], ['id', 6554], ['id', 53781], ['id', 17709], ['id', 32252], ['id', 59806]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37643396854400635, 0.3757263422012329, 0.35357344150543213, 0.35206353664398193, 0.34212398529052734, 0.33121252059936523, 0.33040082454681396, 0.3279992341995239, 0.3271219730377197, 0.3265117406845093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.5814757347106934})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5829764604568481})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5486890077590942})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9415286779403687})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.12827205657959})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.408143997192383})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6347, 'crossentropy': 1.6533271484375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2700474262237549})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2060277462005615})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.206943392753601})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2015776634216309})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1868126392364502})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 43304], ['id', 28248], ['id', 16767], ['id', 52387], ['id', 42926], ['id', 44325], ['id', 43294], ['id', 45843], ['ood', 14677], ['id', 32330]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5466512441635132, 0.5372287034988403, 0.5317394733428955, 0.5134056806564331, 0.5054352283477783, 0.49514853954315186, 0.4853479862213135, 0.48295021057128906, 0.47424542903900146, 0.45387208461761475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 1.4936460256576538})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.5952249765396118})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.737821340560913})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.000239372253418})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5404, 'crossentropy': 1.5044833984375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.4755859375, 'crossentropy': 1.5399065017700195})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.5237454175949097})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.4970703125, 'crossentropy': 1.526710033416748})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 34311], ['id', 13753], ['id', 35184], ['id', 8628], ['id', 56559], ['id', 326], ['id', 49662], ['id', 43291], ['id', 26830], ['id', 36761]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.27054810523986816, 0.2671396732330322, 0.26107293367385864, 0.25840914249420166, 0.2543957233428955, 0.2538607120513916, 0.25282955169677734, 0.2516052722930908, 0.2511526346206665, 0.2510141134262085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.4104511737823486})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5880177021026611})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8748831748962402})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.33084774017334})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5676, 'crossentropy': 1.4700302734375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.4681832790374756})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.4466005563735962})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.4173452854156494})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 1033], ['id', 39141], ['ood', 37613], ['id', 34149], ['id', 49376], ['id', 7697], ['id', 1669], ['id', 17886], ['id', 31904], ['id', 18814]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3358818292617798, 0.3169524669647217, 0.30978894233703613, 0.30618858337402344, 0.29833030700683594, 0.2965506315231323, 0.2963085174560547, 0.2959789037704468, 0.2933163046836853, 0.28444433212280273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.5453712940216064})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.537665843963623})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5559396743774414})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.001677989959717})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.514071226119995})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5789, 'crossentropy': 1.60951298828125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.490234375, 'crossentropy': 1.486074686050415})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3903999328613281})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3607065677642822})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3550076484680176})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 36424], ['id', 57268], ['id', 18729], ['id', 50211], ['id', 15298], ['id', 19363], ['id', 22284], ['id', 48453], ['id', 39381], ['id', 15124]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3621760606765747, 0.3558173179626465, 0.35199296474456787, 0.34055066108703613, 0.33385467529296875, 0.3298839330673218, 0.32346975803375244, 0.31782639026641846, 0.31411850452423096, 0.3124321699142456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.5088012218475342})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2954199314117432})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4943748712539673})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6182632446289062})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.7659683227539062})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6337, 'crossentropy': 1.3460447265625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.355082392692566})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2353019714355469})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2169300317764282})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.217207908630371})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 35684], ['id', 37928], ['id', 14157], ['id', 57379], ['id', 49008], ['id', 2731], ['id', 56171], ['id', 51328], ['id', 54405], ['id', 5820]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35190868377685547, 0.35117167234420776, 0.34564208984375, 0.336267352104187, 0.33350467681884766, 0.3282277584075928, 0.3280336856842041, 0.32475054264068604, 0.32370901107788086, 0.32196474075317383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.5487208366394043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.397310733795166})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.469931721687317})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.671156406402588})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7593574523925781})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5994, 'crossentropy': 1.4198439453125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.4224529266357422})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.3652043342590332})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3516159057617188})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.3374258279800415})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 3694], ['id', 42826], ['id', 33012], ['id', 57224], ['id', 37654], ['id', 14945], ['id', 44638], ['id', 52930], ['id', 32800], ['id', 46031]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.359707236289978, 0.33540546894073486, 0.3334779739379883, 0.33017706871032715, 0.32906728982925415, 0.3290000557899475, 0.32892125844955444, 0.32707899808883667, 0.3269510269165039, 0.3267015218734741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.40799880027771})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.297705888748169})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2805581092834473})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5081465244293213})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4974687099456787})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.9654533863067627})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6424, 'crossentropy': 1.3602435546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2789348363876343})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1654682159423828})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1283048391342163})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1420422792434692})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1228570938110352})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 40224], ['id', 44860], ['id', 36884], ['id', 46015], ['id', 19771], ['ood', 2292], ['id', 48933], ['id', 10220], ['id', 23091], ['id', 12155]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5035320520401001, 0.47907108068466187, 0.45487022399902344, 0.45228904485702515, 0.44806432723999023, 0.44131410121917725, 0.44017940759658813, 0.4388478100299835, 0.4314386248588562, 0.42326685786247253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.4729862213134766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3285057544708252})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2610406875610352})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3761025667190552})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4150655269622803})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.5425524711608887})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.65, 'crossentropy': 1.300022265625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2923214435577393})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.202095866203308})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.174625277519226})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1640350818634033})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.125098705291748})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 12467], ['id', 26538], ['id', 23285], ['id', 31444], ['id', 26018], ['id', 48322], ['id', 24108], ['id', 36323], ['id', 7456], ['id', 58130]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4426988363265991, 0.3876785635948181, 0.38332313299179077, 0.3739340305328369, 0.37382614612579346, 0.3685169816017151, 0.36133623123168945, 0.3585779666900635, 0.35457152128219604, 0.3537623882293701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.4831616878509521})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3740570545196533})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.250908374786377})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.347775936126709})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3306089639663696})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.48923921585083})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6597, 'crossentropy': 1.2596970703125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.3230319023132324})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2550022602081299})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1992555856704712})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1799306869506836})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1783502101898193})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49966], ['id', 18783], ['id', 15267], ['ood', 44939], ['ood', 35196], ['ood', 21066], ['ood', 23329], ['id', 30746], ['id', 41355], ['id', 39259]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.34145280718803406, 0.33636152744293213, 0.3228566646575928, 0.3164536952972412, 0.31577515602111816, 0.3120584487915039, 0.3082733154296875, 0.3029111623764038, 0.3020137548446655, 0.30081474781036377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.4595613479614258})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2659878730773926})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3012893199920654})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4365110397338867})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3148123025894165})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6282, 'crossentropy': 1.2776228515625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3955082893371582})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3105978965759277})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3558216094970703})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2521222829818726})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 21901], ['id', 21810], ['id', 59771], ['ood', 44998], ['id', 24172], ['id', 5346], ['ood', 828], ['id', 32578], ['id', 9692], ['ood', 43404]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.411441445350647, 0.3658033609390259, 0.3626655340194702, 0.359657883644104, 0.3563397526741028, 0.34580302238464355, 0.345081090927124, 0.3407604694366455, 0.33734554052352905, 0.33007800579071045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.50443696975708})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3066542148590088})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2689738273620605})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3656432628631592})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3796486854553223})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3338260650634766})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6494, 'crossentropy': 1.23767783203125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3017241954803467})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.199306845664978})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1293957233428955})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.144002079963684})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1334490776062012})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 57174], ['id', 42010], ['id', 10452], ['id', 18138], ['id', 50999], ['id', 41672], ['ood', 47451], ['id', 46777], ['id', 4123], ['ood', 28467]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4396824836730957, 0.4225785732269287, 0.39768481254577637, 0.38542425632476807, 0.380612850189209, 0.37235885858535767, 0.3718022108078003, 0.3654935359954834, 0.3622346520423889, 0.3599574565887451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.4677681922912598})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2491531372070312})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2422890663146973})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1901029348373413})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3480658531188965})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5785259008407593})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3470470905303955})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.654, 'crossentropy': 1.1777181640625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.25335693359375})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.114033579826355})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.067293405532837})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0295441150665283})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.062974214553833})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0688989162445068})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 56628], ['id', 13574], ['id', 377], ['id', 45289], ['id', 21159], ['id', 47549], ['id', 58892], ['id', 22129], ['id', 9208], ['id', 53549]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4814034700393677, 0.47641587257385254, 0.47611480951309204, 0.46408605575561523, 0.45351821184158325, 0.45132315158843994, 0.45098650455474854, 0.450725793838501, 0.4500398635864258, 0.4498879909515381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.443664789199829})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2787091732025146})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2582075595855713})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.231571912765503})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.191962718963623})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2745932340621948})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.326735496520996})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.367584228515625})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6568, 'crossentropy': 1.22738828125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2822020053863525})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.0967354774475098})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.052058458328247})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0408847332000732})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0090842247009277})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 0.997343897819519})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0138630867004395})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 13734], ['id', 30699], ['ood', 5526], ['id', 8455], ['id', 54444], ['id', 33476], ['id', 34452], ['id', 27833], ['id', 33046], ['id', 14252]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4910926818847656, 0.453838586807251, 0.4305626153945923, 0.4283336400985718, 0.42704111337661743, 0.4180667996406555, 0.41575396060943604, 0.4150834083557129, 0.41490185260772705, 0.412911057472229]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.4455602169036865})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2642576694488525})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2622087001800537})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.192884087562561})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2751637697219849})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2347975969314575})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.5854277610778809})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6534, 'crossentropy': 1.225141796875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.279202938079834})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1752660274505615})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1426695585250854})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0858404636383057})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0935306549072266})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1075334548950195})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 40363], ['id', 850], ['id', 36343], ['ood', 39355], ['id', 43346], ['id', 31612], ['id', 44331], ['id', 22836], ['ood', 9651], ['ood', 9641]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3485698699951172, 0.325542151927948, 0.3243716359138489, 0.30699610710144043, 0.3058422803878784, 0.30485451221466064, 0.3037090301513672, 0.3028683066368103, 0.3015977144241333, 0.30013537406921387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.4912109375, 'crossentropy': 1.529653787612915})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.2554539442062378})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1767586469650269})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1793584823608398})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.309295892715454})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3163402080535889})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6279, 'crossentropy': 1.164359765625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2742036581039429})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1861745119094849})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1326026916503906})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.0909903049468994})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1127407550811768})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 26636], ['id', 51127], ['id', 22288], ['id', 55098], ['id', 56769], ['id', 57297], ['id', 12944], ['id', 25963], ['id', 31557], ['id', 36311]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.36797070503234863, 0.3129425048828125, 0.3114943504333496, 0.31094712018966675, 0.3061116933822632, 0.30064475536346436, 0.2993229627609253, 0.29356682300567627, 0.29111504554748535, 0.2889886498451233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.4742186069488525})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.2896987199783325})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1975741386413574})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1849112510681152})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1264216899871826})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2753396034240723})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2987165451049805})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.242653727531433})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6753, 'crossentropy': 1.16139169921875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.345613718032837})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.168377161026001})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.0860247611999512})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.056492567062378})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0803508758544922})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0666240453720093})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0279045104980469})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 58420], ['id', 70], ['id', 55968], ['id', 53338], ['id', 28821], ['id', 12210], ['id', 44619], ['id', 5182], ['id', 7], ['id', 11015]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4500325918197632, 0.4346611499786377, 0.43092644214630127, 0.4272284507751465, 0.40154922008514404, 0.3950974941253662, 0.39482998847961426, 0.39317643642425537, 0.39258384704589844, 0.3914557695388794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3833742141723633})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.1876822710037231})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.077702283859253})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1612650156021118})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1369926929473877})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2465956211090088})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6634, 'crossentropy': 1.09011826171875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.2733936309814453})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.128110408782959})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.0906318426132202})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.0676621198654175})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.0840630531311035})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 32110], ['id', 52150], ['id', 58220], ['id', 17871], ['id', 37251], ['id', 43285], ['id', 54078], ['id', 48595], ['id', 3219], ['id', 3459]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3775056004524231, 0.3436696529388428, 0.33069658279418945, 0.32449591159820557, 0.3235238790512085, 0.32069218158721924, 0.3166658878326416, 0.3102327585220337, 0.3049982786178589, 0.30420076847076416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.4229592084884644})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2179653644561768})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1284029483795166})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0548292398452759})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1181561946868896})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1985777616500854})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2309067249298096})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6827, 'crossentropy': 1.07857861328125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2245908975601196})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.093309760093689})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0825297832489014})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.0578839778900146})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0660400390625})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0108803510665894})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 59858], ['id', 59731], ['ood', 24918], ['ood', 46254], ['ood', 44222], ['ood', 46178], ['ood', 4751], ['ood', 30564], ['ood', 47350], ['ood', 4775]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.36401498317718506, 0.3276330232620239, 0.32560014724731445, 0.31257808208465576, 0.3086667060852051, 0.3083221912384033, 0.30789899826049805, 0.3078228235244751, 0.3075129985809326, 0.305639386177063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.3660078048706055})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1708449125289917})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.093612551689148})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1705431938171387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2203036546707153})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.175550103187561})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6747, 'crossentropy': 1.09892021484375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2333133220672607})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1269053220748901})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0599720478057861})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1103813648223877})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.047744631767273})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 20624], ['id', 2167], ['id', 29147], ['id', 20027], ['id', 10568], ['id', 13137], ['id', 21979], ['id', 33141], ['id', 15841], ['id', 6434]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39294934272766113, 0.3654317855834961, 0.36299097537994385, 0.35899126529693604, 0.3580946922302246, 0.3506932258605957, 0.3499186038970947, 0.3495274782180786, 0.3461529016494751, 0.3461289405822754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.4438858032226562})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2273507118225098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1426467895507812})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1183745861053467})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1272830963134766})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1817831993103027})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2181000709533691})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6662, 'crossentropy': 1.12941494140625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.271338701248169})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1341636180877686})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.0664782524108887})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.0667107105255127})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.0383810997009277})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.0462455749511719})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 2684], ['id', 21683], ['id', 39750], ['id', 46619], ['id', 10063], ['id', 29728], ['id', 47416], ['id', 56884], ['id', 6608], ['id', 11109]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34363073110580444, 0.3317514657974243, 0.3129051923751831, 0.31282925605773926, 0.31265580654144287, 0.31236207485198975, 0.311927855014801, 0.31120848655700684, 0.30907970666885376, 0.30694812536239624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.4543638229370117})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2147696018218994})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.108719825744629})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0664563179016113})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1295521259307861})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0778604745864868})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1815176010131836})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6812, 'crossentropy': 1.07551474609375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2451207637786865})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1093391180038452})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.05816650390625})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0243408679962158})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 0.9950879812240601})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 0.9951668977737427})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 48529], ['id', 12078], ['id', 48494], ['id', 22613], ['id', 16154], ['id', 19281], ['id', 9771], ['ood', 25029], ['ood', 33821], ['id', 10897]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37818217277526855, 0.3583611249923706, 0.3346068263053894, 0.3326607942581177, 0.32215964794158936, 0.31995296478271484, 0.3187750577926636, 0.31419622898101807, 0.3130655288696289, 0.31296002864837646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.4495608806610107})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2083139419555664})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1424310207366943})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1969841718673706})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0981818437576294})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1730929613113403})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2522162199020386})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2642368078231812})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6812, 'crossentropy': 1.1147296875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.225630760192871})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.0993669033050537})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0360747575759888})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.036970615386963})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.0219299793243408})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 0.995491087436676})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 0.9924390316009521})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 16530], ['id', 27719], ['id', 19842], ['id', 12689], ['id', 37650], ['id', 53138], ['id', 54280], ['id', 45863], ['id', 38367], ['id', 32759]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4163188338279724, 0.4002709984779358, 0.39944136142730713, 0.3896713852882385, 0.38204658031463623, 0.37443411350250244, 0.374428391456604, 0.3713442087173462, 0.3687068819999695, 0.3684980273246765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.362612009048462})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1872928142547607})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0763717889785767})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1209288835525513})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1515353918075562})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.17454195022583})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6594, 'crossentropy': 1.0957482421875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2890925407409668})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1836016178131104})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1161613464355469})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1203644275665283})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1012139320373535})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 35913], ['id', 32498], ['id', 20946], ['id', 33674], ['id', 3081], ['ood', 57841], ['id', 3913], ['id', 50403], ['id', 48293], ['id', 56057]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3110005855560303, 0.30250293016433716, 0.2905271053314209, 0.2900298833847046, 0.2849029302597046, 0.28485023975372314, 0.28483080863952637, 0.27888810634613037, 0.276955783367157, 0.2703026533126831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5009765625, 'crossentropy': 1.5258663892745972})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.269000768661499})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1694657802581787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1433346271514893})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1028008460998535})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.136064052581787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2304710149765015})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.286898136138916})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6764, 'crossentropy': 1.1087990234375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2455323934555054})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1427321434020996})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.0674222707748413})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.0512590408325195})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0108530521392822})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0300887823104858})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0051524639129639})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 29457], ['id', 41119], ['id', 31152], ['id', 13191], ['id', 37972], ['id', 1509], ['id', 42723], ['id', 59105], ['id', 922], ['id', 6152]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44118189811706543, 0.3896079659461975, 0.3700557351112366, 0.36781740188598633, 0.3647867441177368, 0.3562830686569214, 0.35581398010253906, 0.34696149826049805, 0.3422684669494629, 0.341344952583313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.4510133266448975})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.202634334564209})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1075830459594727})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.051680088043213})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0795090198516846})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0726711750030518})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.171135663986206})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6685, 'crossentropy': 1.06167177734375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2705631256103516})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.1475961208343506})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.0745238065719604})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0903514623641968})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.063252568244934})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.035172700881958})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 47079], ['id', 7694], ['id', 3301], ['id', 17243], ['id', 46129], ['id', 38392], ['id', 34274], ['id', 14165], ['id', 12346], ['id', 51348]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4192190170288086, 0.3682785630226135, 0.3645409345626831, 0.36115002632141113, 0.3600733280181885, 0.354458212852478, 0.35394322872161865, 0.3528653383255005, 0.3515101671218872, 0.35007011890411377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.466383695602417})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2177565097808838})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1346834897994995})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1180521249771118})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0917047262191772})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1539027690887451})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.070277214050293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.181488275527954})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2039642333984375})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.2281427383422852})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6898, 'crossentropy': 1.0717064453125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2133982181549072})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0659576654434204})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 0.9992305636405945})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9716302156448364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9648827314376831})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.967036783695221})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9516812562942505})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9324740767478943})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9501479268074036})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 33781], ['id', 46812], ['id', 22371], ['id', 56394], ['id', 46613], ['id', 21041], ['id', 32065], ['id', 55367], ['id', 49099], ['id', 15274]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4460340738296509, 0.43152713775634766, 0.42953169345855713, 0.427730917930603, 0.41677534580230713, 0.4136006832122803, 0.40483182668685913, 0.40226948261260986, 0.40029072761535645, 0.3990876078605652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.4259613752365112})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.2113491296768188})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1518893241882324})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1516573429107666})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0811371803283691})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1125648021697998})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1252284049987793})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1793410778045654})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6963, 'crossentropy': 1.06970341796875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.2195088863372803})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.0631133317947388})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 0.9871752262115479})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9737772941589355})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9625070095062256})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.980805516242981})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9783046245574951})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 46563], ['id', 44129], ['id', 28642], ['id', 2096], ['id', 4148], ['id', 54835], ['id', 29672], ['id', 5193], ['id', 35309], ['id', 2938]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3988722562789917, 0.37041062116622925, 0.35139691829681396, 0.3469381332397461, 0.3466916084289551, 0.34462010860443115, 0.343051552772522, 0.34195470809936523, 0.33838677406311035, 0.3376314640045166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.413515329360962})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2598861455917358})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0834741592407227})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0644073486328125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.026427984237671})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1460968255996704})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1261712312698364})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.1428978443145752})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7048, 'crossentropy': 1.0316013671875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.251237392425537})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0800344944000244})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9685981273651123})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9746276140213013})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9174664616584778})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.93137526512146})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.91695237159729})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 16778], ['id', 52509], ['id', 26279], ['id', 20009], ['id', 11374], ['id', 30476], ['id', 56380], ['id', 24728], ['id', 30880], ['id', 25620]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36827826499938965, 0.36321771144866943, 0.3395504951477051, 0.3377408981323242, 0.3367382287979126, 0.33232247829437256, 0.33209097385406494, 0.33160126209259033, 0.3314450979232788, 0.32623231410980225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2893788814544678})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1308504343032837})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9917796850204468})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.978196382522583})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0192430019378662})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9762536287307739})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0600686073303223})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1241668462753296})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.2131860256195068})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 1.0179515625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2458834648132324})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0304570198059082})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9734009504318237})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9189461469650269})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9222440719604492})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9057906866073608})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9037477970123291})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9120463132858276})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 26462], ['id', 45674], ['id', 53617], ['ood', 10884], ['id', 49995], ['id', 2615], ['id', 16844], ['id', 34743], ['id', 9621], ['id', 21066]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4315722584724426, 0.42320215702056885, 0.4196031093597412, 0.41151344776153564, 0.40768367052078247, 0.4060872793197632, 0.3954617381095886, 0.3919351100921631, 0.3916260600090027, 0.38718080520629883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.3844397068023682})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1217546463012695})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0052913427352905})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9907276034355164})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.027014970779419})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0808886289596558})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0795494318008423})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7065, 'crossentropy': 1.01813876953125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1850391626358032})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0557198524475098})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0099780559539795})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9974257946014404})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9660597443580627})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9737036228179932})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 15357], ['ood', 35947], ['id', 5937], ['id', 51450], ['id', 1031], ['id', 1202], ['id', 39951], ['id', 24953], ['id', 16996], ['id', 14609]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.302449107170105, 0.26371586322784424, 0.2630784511566162, 0.26297515630722046, 0.26187145709991455, 0.26186394691467285, 0.26169371604919434, 0.25912022590637207, 0.2562347650527954, 0.2543255090713501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.4892578125, 'crossentropy': 1.3671140670776367})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.1958873271942139})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0928068161010742})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0660204887390137})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.069707989692688})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0690529346466064})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0790042877197266})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6969, 'crossentropy': 1.038998046875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2334849834442139})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1227607727050781})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0489540100097656})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0278147459030151})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0171754360198975})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0381135940551758})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 52961], ['id', 40549], ['id', 57751], ['id', 19088], ['id', 52590], ['id', 2434], ['id', 1342], ['id', 27863], ['id', 14060], ['id', 42949]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33754289150238037, 0.3309452533721924, 0.3109928369522095, 0.30831384658813477, 0.3031039834022522, 0.3030998706817627, 0.3019235134124756, 0.30079084634780884, 0.299416184425354, 0.29559826850891113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3926148414611816})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1712024211883545})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.03700590133667})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0450129508972168})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.023208498954773})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9929832816123962})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.0398255586624146})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0523996353149414})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.088114619255066})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7301, 'crossentropy': 0.96924765625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.249623417854309})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0523256063461304})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 0.9945667386054993})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9177266955375671})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9115815758705139})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9233716130256653})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.8986700773239136})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.8960198163986206})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 54667], ['id', 51071], ['id', 52384], ['id', 57389], ['id', 49988], ['id', 38782], ['id', 20918], ['id', 10400], ['id', 23553], ['id', 53671]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4142691493034363, 0.38872164487838745, 0.35830366611480713, 0.3556128144264221, 0.34938305616378784, 0.34579193592071533, 0.34307265281677246, 0.341220498085022, 0.3411436676979065, 0.3411060571670532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3389462232589722})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2008209228515625})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0725497007369995})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0942718982696533})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0431666374206543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.0755630731582642})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.142329216003418})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.127594232559204})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7134, 'crossentropy': 1.05089013671875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.2791725397109985})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1146767139434814})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0362517833709717})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0230765342712402})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9967902898788452})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0063800811767578})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9656867980957031})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 50210], ['id', 33672], ['id', 18913], ['id', 13588], ['id', 59691], ['id', 15078], ['id', 21184], ['id', 6866], ['id', 39483], ['id', 31587]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3601839542388916, 0.3543037176132202, 0.3505336046218872, 0.3493383526802063, 0.3415706157684326, 0.3357393741607666, 0.3326120376586914, 0.3271247148513794, 0.3250919580459595, 0.32189369201660156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.3842096328735352})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.132617473602295})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0186073780059814})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.001132607460022})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.043067216873169})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.011791467666626})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.063347339630127})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.704, 'crossentropy': 0.9857310546875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2275750637054443})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0744690895080566})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0437040328979492})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.037203311920166})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0306215286254883})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9823025465011597})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 53488], ['id', 27212], ['id', 5092], ['id', 57962], ['id', 10181], ['id', 53033], ['id', 26805], ['id', 23485], ['id', 15599], ['id', 44630]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37555253505706787, 0.2819751501083374, 0.2789797782897949, 0.27811384201049805, 0.269089937210083, 0.2681043744087219, 0.26640069484710693, 0.2610177993774414, 0.2607496976852417, 0.2534288167953491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3749418258666992})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1623433828353882})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.047900676727295})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0564179420471191})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0647022724151611})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0507704019546509})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6841, 'crossentropy': 1.04141826171875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2877198457717896})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1290899515151978})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.085113763809204})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.065548300743103})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0832358598709106})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 31065], ['id', 4194], ['id', 12580], ['id', 35384], ['id', 3800], ['id', 28218], ['id', 56086], ['id', 28159], ['ood', 15137], ['id', 33232]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.31207460165023804, 0.2947104573249817, 0.29071199893951416, 0.27457869052886963, 0.2538025379180908, 0.2505073547363281, 0.24688494205474854, 0.24448621273040771, 0.243125319480896, 0.24264216423034668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.4277117252349854})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1885558366775513})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0647073984146118})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0353453159332275})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0164062976837158})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0307039022445679})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0175447463989258})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9984163045883179})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0538357496261597})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.0658819675445557})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1481378078460693})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7276, 'crossentropy': 1.0187232421875}
