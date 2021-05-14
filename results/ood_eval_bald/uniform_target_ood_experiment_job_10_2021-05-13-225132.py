store = {}
store['timestamp']=1620942692
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=10']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=20
store['config']={'seed': 1249, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1137166023254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2941315174102783})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.829442024230957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3553199768066406})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6785, 'crossentropy': 1.9317615234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1459364891052246})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.18696928024292})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1400997638702393})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 5486], ['id', 6153], ['id', 14851], ['id', 42595], ['id', 10025], ['ood', 12366], ['ood', 25465], ['id', 8297], ['id', 46715], ['id', 5711]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6827659606933594, 0.726731538772583, 0.714920699596405, 0.6350863575935364, 0.6132357120513916, 0.5316828489303589, 0.5191422700881958, 0.38137757778167725, 0.6815872192382812, 0.8656435608863831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.569091558456421})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8951419591903687})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8810923099517822})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.1923375129699707})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7243, 'crossentropy': 1.4212876953125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.08586585521698})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0285829305648804})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0457977056503296})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 16157], ['id', 3980], ['id', 17972], ['id', 7159], ['id', 41776], ['id', 13517], ['id', 31530], ['id', 50142], ['id', 52959], ['id', 22772]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.583393931388855, 0.5162453055381775, 0.7422826886177063, 0.5171471834182739, 0.3568055033683777, 0.5671390295028687, 0.5916718244552612, 0.5612674951553345, 0.7089097499847412, 0.4167674779891968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6717321872711182})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6626784801483154})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9168038368225098})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.326716184616089})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.157680034637451})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7341, 'crossentropy': 1.49359169921875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9906495809555054})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9581224918365479})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9126400947570801})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.8934146165847778})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43217], ['id', 52708], ['id', 13526], ['id', 50010], ['id', 20157], ['id', 38608], ['id', 41865], ['id', 11590], ['id', 41319], ['id', 42438]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7164140939712524, 0.5699144601821899, 0.5445595979690552, 0.7703139185905457, 0.596558690071106, 0.7674157619476318, 0.6117537021636963, 0.5459882020950317, 0.5946512818336487, 0.5823221206665039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3955552577972412})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7703676223754883})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.930132269859314})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.8997788429260254})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7516, 'crossentropy': 1.33278779296875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1356732845306396})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0735788345336914})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0102390050888062})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 2953], ['id', 59393], ['id', 47539], ['id', 8827], ['id', 17477], ['id', 46347], ['id', 39708], ['id', 48946], ['id', 52707], ['id', 46085]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42960983514785767, 0.48709380626678467, 0.5371201634407043, 0.5455123782157898, 0.40222370624542236, 0.45899343490600586, 0.5586166381835938, 0.568187952041626, 0.5956699848175049, 0.30515456199645996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0367082357406616})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9475651979446411})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1933940649032593})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3542966842651367})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3827478885650635})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.849, 'crossentropy': 0.93070830078125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.9242805242538452})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7010310888290405})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7105339765548706})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7478480339050293})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 7933], ['id', 44149], ['id', 55011], ['id', 42509], ['id', 49830], ['id', 20352], ['id', 5611], ['id', 37160], ['id', 31409], ['id', 2636]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3351578712463379, 0.5315693616867065, 0.5353206396102905, 0.49582111835479736, 0.4103514552116394, 0.5312982797622681, 0.6041980981826782, 0.5258895754814148, 0.5143722891807556, 0.6188535094261169]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1107938289642334})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0670514106750488})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1246235370635986})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2041598558425903})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3917275667190552})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8365, 'crossentropy': 1.07874267578125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7940231561660767})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6986712217330933})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6410494446754456})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6297979950904846})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 31904], ['id', 31153], ['id', 8826], ['id', 48811], ['id', 46412], ['id', 2423], ['id', 7254], ['id', 50802], ['id', 57542], ['id', 57735]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3676171600818634, 0.37621182203292847, 0.5295815467834473, 0.6095059514045715, 0.6550195813179016, 0.46913594007492065, 0.63984814286232, 0.5421203374862671, 0.7358631491661072, 0.37636619806289673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.301516056060791})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.290489912033081})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.4578397274017334})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.488692283630371})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5559470653533936})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8014, 'crossentropy': 1.2129822265625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8936014771461487})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7931994199752808})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7285830974578857})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7520336508750916})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 54598], ['id', 40839], ['id', 19546], ['id', 3140], ['id', 8632], ['id', 50144], ['id', 12194], ['id', 54954], ['id', 34013], ['id', 19188]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5385575890541077, 0.4762248992919922, 0.44525569677352905, 0.5557878017425537, 0.5292233228683472, 0.6506171226501465, 0.36243700981140137, 0.44167596101760864, 0.4371638894081116, 0.3564896583557129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9956837892532349})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0332386493682861})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0625381469726562})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1188796758651733})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.815, 'crossentropy': 0.91692255859375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.9230461120605469})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8278717994689941})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8653522729873657})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 36417], ['id', 4066], ['id', 1241], ['id', 55310], ['id', 59664], ['id', 25861], ['id', 54426], ['id', 36694], ['id', 35176], ['id', 1338]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4051651954650879, 0.41597139835357666, 0.3739556074142456, 0.4513680934906006, 0.37159764766693115, 0.30682575702667236, 0.46909064054489136, 0.38029658794403076, 0.317355751991272, 0.40441256761550903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8971326351165771})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8361740112304688})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9729032516479492})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9848728775978088})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1076140403747559})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8542, 'crossentropy': 0.777175341796875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7874436974525452})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6197805404663086})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5889748334884644})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.5584964156150818})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 38275], ['id', 6710], ['id', 23873], ['id', 29094], ['id', 17756], ['id', 42213], ['id', 11463], ['id', 3082], ['id', 40241], ['id', 39336]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6127999424934387, 0.562985897064209, 0.5893165469169617, 0.49880850315093994, 0.5790354013442993, 0.5771102905273438, 0.482114315032959, 0.43681901693344116, 0.36034172773361206, 0.37131768465042114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8949916362762451})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7907031774520874})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8053855895996094})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7141175866127014})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8164094090461731})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8615972399711609})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9351651668548584})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.700870068359375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6949131488800049})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5606478452682495})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5125555992126465})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5101000070571899})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.4968528747558594})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.48115503787994385})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 39722], ['id', 1404], ['id', 4295], ['id', 34284], ['id', 14580], ['ood', 58047], ['id', 5126], ['id', 20560], ['id', 41134], ['id', 37070]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6563343405723572, 0.48282378911972046, 0.684842050075531, 0.4972715973854065, 0.535480260848999, 0.3957270383834839, 0.6119609475135803, 0.5595332980155945, 0.4813109040260315, 0.48489242792129517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8334752321243286})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7146250009536743})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7400740385055542})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7814589142799377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8036693334579468})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8879, 'crossentropy': 0.657081591796875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6900163292884827})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5697988867759705})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5400745868682861})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5072939395904541})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 31940], ['id', 47732], ['id', 25117], ['id', 52092], ['id', 18143], ['id', 40066], ['id', 26872], ['id', 19953], ['id', 24660], ['id', 54488]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6132267713546753, 0.5545840859413147, 0.5931313037872314, 0.5479143261909485, 0.35296630859375, 0.5420352816581726, 0.4140365719795227, 0.5067122280597687, 0.5712353587150574, 0.42710262537002563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7865085601806641})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6007834672927856})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6717160940170288})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6769375801086426})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6388713121414185})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.60622841796875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6398504972457886})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5466892123222351})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5001848340034485})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.44794678688049316})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 44881], ['id', 33849], ['id', 37347], ['id', 7984], ['ood', 19378], ['id', 11675], ['id', 15713], ['id', 49141], ['id', 39309], ['id', 33694]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5985578298568726, 0.2955784201622009, 0.3713838458061218, 0.45057928562164307, 0.2346593141555786, 0.4443069100379944, 0.585260272026062, 0.33735501766204834, 0.3002391457557678, 0.48933207988739014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7267728447914124})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6096557378768921})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5694018602371216})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6191055774688721})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6476775407791138})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6578469276428223})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.56611259765625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.692933201789856})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5413942337036133})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43697959184646606})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.45139026641845703})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43157368898391724})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 19106], ['id', 24533], ['id', 3636], ['id', 28420], ['id', 43383], ['id', 30451], ['id', 26852], ['id', 59433], ['id', 28512], ['id', 16354]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3563784956932068, 0.6704197824001312, 0.2787410020828247, 0.4762367010116577, 0.2551625669002533, 0.5572274327278137, 0.47622478008270264, 0.5382561683654785, 0.5613561272621155, 0.2994602918624878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7449764013290405})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5802550315856934})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5333266258239746})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5361714959144592})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5297838449478149})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.574371337890625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5861690640449524})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.553264856338501})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.50638681640625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7143043279647827})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49563920497894287})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4159717857837677})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4114636778831482})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.37841761112213135})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.392148494720459})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.37633901834487915})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 9180], ['id', 13265], ['id', 4767], ['id', 32835], ['id', 21306], ['id', 5580], ['id', 30069], ['id', 16003], ['id', 39713], ['id', 2465]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5547434091567993, 0.5109468102455139, 0.645143449306488, 0.42748379707336426, 0.45720458030700684, 0.5214600563049316, 0.43156981468200684, 0.33574461936950684, 0.5612684488296509, 0.4314427971839905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8294016122817993})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4818696081638336})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4554142653942108})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4718233048915863})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5050153136253357})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4899556636810303})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9322, 'crossentropy': 0.451480322265625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6483878493309021})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.47501426935195923})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4254729449748993})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.38684481382369995})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39349600672721863})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 34708], ['id', 24235], ['id', 47628], ['id', 33338], ['id', 54721], ['id', 56014], ['id', 7924], ['id', 53937], ['id', 17010], ['id', 52514]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5425407886505127, 0.32966357469558716, 0.5521751046180725, 0.3486887216567993, 0.32970237731933594, 0.3992137312889099, 0.3817538619041443, 0.4845306873321533, 0.5174975991249084, 0.3904109299182892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7910944223403931})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4980866312980652})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.460482120513916})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5186440944671631})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4872473478317261})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4768425524234772})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.470648681640625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7356280088424683})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4811088442802429})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4135724902153015})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42496442794799805})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3702605962753296})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 32747], ['id', 13716], ['id', 34770], ['id', 32093], ['id', 2064], ['id', 4111], ['id', 11621], ['id', 32190], ['id', 59321], ['id', 16528]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.63371741771698, 0.40805941820144653, 0.37438732385635376, 0.28387659788131714, 0.42850416898727417, 0.4215558171272278, 0.4673253893852234, 0.5262764692306519, 0.5317279696464539, 0.6472668051719666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8072429895401001})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5363464951515198})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46592140197753906})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4795722961425781})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5186090469360352})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.511003315448761})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.50351640625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7651162147521973})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48513951897621155})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.422882616519928})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.426242470741272})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39051586389541626})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 30184], ['id', 41415], ['ood', 44538], ['ood', 3049], ['id', 22053], ['id', 22112], ['id', 45306], ['ood', 2226], ['id', 40259], ['id', 53993]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5247570276260376, 0.37870335578918457, 0.4245717525482178, 0.4227781295776367, 0.5904513597488403, 0.3863353133201599, 0.3407840132713318, 0.4258742332458496, 0.4047151803970337, 0.5198764204978943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8937439918518066})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5465565919876099})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43906018137931824})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4280959665775299})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48224133253097534})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46287357807159424})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45151764154434204})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.439318701171875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7788968682289124})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5214377641677856})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43418508768081665})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4191367030143738})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40049201250076294})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3872724175453186})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 4290], ['id', 59314], ['id', 46435], ['ood', 55038], ['id', 5910], ['id', 46242], ['id', 16282], ['id', 53567], ['id', 42526], ['ood', 10020]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.546857625246048, 0.5595815777778625, 0.38418981432914734, 0.3248281478881836, 0.29629287123680115, 0.4923837184906006, 0.32511037588119507, 0.46561938524246216, 0.4541168212890625, 0.38452088832855225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.823133111000061})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4949527382850647})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.46095511317253113})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3879472017288208})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4235500693321228})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4280318319797516})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41931042075157166})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.412117431640625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8022321462631226})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5360217690467834})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.45409727096557617})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3749470114707947})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3910718560218811})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.38289159536361694})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 53906], ['id', 37676], ['id', 50025], ['id', 18782], ['id', 42838], ['id', 42810], ['id', 14604], ['id', 8790], ['id', 49579], ['id', 28368]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.1934586763381958, 0.3398101329803467, 0.37999260425567627, 0.49453315138816833, 0.3912581205368042, 0.3137369751930237, 0.3115115761756897, 0.4524537920951843, 0.3816545605659485, 0.3498554229736328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9842432737350464})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49799636006355286})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45366281270980835})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41730910539627075})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3990708589553833})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4249577522277832})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4636092185974121})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43945080041885376})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.39589140625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8361543416976929})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5178398489952087})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4467352032661438})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37087902426719666})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36886486411094666})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3625006079673767})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3657503128051758})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 41358], ['id', 16029], ['id', 52140], ['id', 53904], ['id', 31576], ['id', 56229], ['id', 23863], ['id', 57295], ['id', 43126], ['id', 36822]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2905980944633484, 0.30504441261291504, 0.5182146430015564, 0.3236638903617859, 0.4618695378303528, 0.3256898820400238, 0.6156036257743835, 0.39134567975997925, 0.5058650374412537, 0.4748367667198181]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9620417356491089})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4737650156021118})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40477490425109863})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4263860583305359})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4286178946495056})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4337800145149231})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9395, 'crossentropy': 0.422120654296875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7579255700111389})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5373775362968445})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.442175030708313})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4080522656440735})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36715608835220337})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 23041], ['id', 29365], ['id', 37191], ['id', 12497], ['id', 57890], ['id', 51414], ['id', 24716], ['ood', 34620], ['id', 37352], ['id', 51904]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3702797293663025, 0.28242963552474976, 0.3133053779602051, 0.4008595943450928, 0.41431665420532227, 0.43573182821273804, 0.3858996033668518, 0.2827718257904053, 0.3269934058189392, 0.4327892065048218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8578363656997681})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4413604736328125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34721171855926514})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3946947157382965})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3692352771759033})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3692892789840698})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9548, 'crossentropy': 0.32798076171875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7301960587501526})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4610315263271332})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3960997760295868})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3616734445095062})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3696744441986084})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 39304], ['id', 3762], ['id', 41998], ['id', 30952], ['id', 5127], ['id', 21315], ['ood', 12904], ['id', 27883], ['id', 19945], ['id', 54191]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3895840048789978, 0.34401631355285645, 0.26933467388153076, 0.4173080325126648, 0.3463979959487915, 0.3828856348991394, 0.14299511909484863, 0.30906856060028076, 0.3595674932003021, 0.5569921731948853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9709064960479736})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5158179998397827})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41222187876701355})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38242843747138977})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37063315510749817})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37043535709381104})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3979825973510742})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38960838317871094})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3940505087375641})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9512, 'crossentropy': 0.3634953857421875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7364445924758911})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4656108617782593})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34838420152664185})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34706491231918335})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3531557321548462})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32295846939086914})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2828814387321472})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3284280002117157})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 39480], ['id', 1518], ['id', 44672], ['id', 18324], ['id', 3803], ['id', 55496], ['id', 52462], ['id', 13942], ['id', 26338], ['id', 4278]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6957433223724365, 0.7887805700302124, 0.345916211605072, 0.5910216569900513, 0.425259530544281, 0.6643175482749939, 0.40537041425704956, 0.5337827801704407, 0.4547710418701172, 0.1935734748840332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9395143985748291})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5421634912490845})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4711906611919403})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39681845903396606})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4071817398071289})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4174576699733734})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4106994569301605})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.3936413818359375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7762799263000488})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5005995631217957})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43707019090652466})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3880208134651184})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3826602101325989})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3702992796897888})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 46734], ['id', 28335], ['id', 6058], ['id', 384], ['id', 21134], ['id', 31415], ['id', 21601], ['id', 55428], ['id', 41960], ['id', 39534]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5222136974334717, 0.22262179851531982, 0.21700343489646912, 0.5457711815834045, 0.3559366464614868, 0.3665691614151001, 0.4887140989303589, 0.4074770212173462, 0.3193960189819336, 0.2920360565185547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9460756182670593})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49366915225982666})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4050673842430115})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3782595694065094})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38046741485595703})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4103040397167206})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39517003297805786})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.369039794921875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7521649599075317})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4805877208709717})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4221404790878296})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4391557574272156})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39867162704467773})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3870440125465393})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 52201], ['id', 43378], ['id', 55591], ['id', 80], ['id', 31371], ['id', 22083], ['id', 36008], ['ood', 58351], ['id', 8552], ['id', 52949]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3610647916793823, 0.42559272050857544, 0.3742830157279968, 0.4443114995956421, 0.3050950765609741, 0.5113494396209717, 0.45870769023895264, 0.366829514503479, 0.4509614109992981, 0.45991677045822144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9324200749397278})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4788190722465515})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3663458526134491})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3979816436767578})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40182414650917053})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3457982540130615})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37150686979293823})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3704032599925995})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3873451054096222})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9553, 'crossentropy': 0.3257173828125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7377451062202454})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4607616066932678})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36063438653945923})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3178170323371887})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3044525384902954})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3183788061141968})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29536259174346924})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30609869956970215})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 54036], ['id', 14294], ['id', 44432], ['id', 16992], ['id', 11734], ['id', 30584], ['id', 11510], ['id', 50840], ['id', 54628], ['id', 29286]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5107877850532532, 0.48924148082733154, 0.48793506622314453, 0.5542433261871338, 0.49525463581085205, 0.46469664573669434, 0.23882129788398743, 0.4849574565887451, 0.36746305227279663, 0.5198177099227905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0872349739074707})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.48968422412872314})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45031535625457764})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3598215579986572})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37091290950775146})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3694044053554535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3431951701641083})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3810029625892639})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41575610637664795})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37064462900161743})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9633, 'crossentropy': 0.293052294921875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8444938659667969})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4605764150619507})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.388298362493515})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.342934250831604})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32159316539764404})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2930726408958435})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3107343316078186})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31652534008026123})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2899865210056305})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 24767], ['id', 24426], ['id', 45972], ['id', 32016], ['id', 27348], ['id', 31157], ['id', 33297], ['id', 1277], ['id', 8816], ['id', 30764]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4167061448097229, 0.44582492113113403, 0.5148287415504456, 0.4390835762023926, 0.3579215407371521, 0.35120606422424316, 0.36662906408309937, 0.36407625675201416, 0.43879127502441406, 0.5920059084892273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9237045645713806})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4858355224132538})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3559427261352539})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.343254029750824})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35900580883026123})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3438670039176941})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32723960280418396})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35423052310943604})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3774314522743225})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3595394194126129})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.3080154052734375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7679874897003174})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4419964551925659})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3558054566383362})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3412250876426697})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29716312885284424})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3053005337715149})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28596413135528564})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29743659496307373})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31117239594459534})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 27653], ['id', 13259], ['id', 39776], ['id', 39778], ['id', 48890], ['id', 59294], ['id', 58649], ['ood', 54159], ['id', 39383], ['id', 6695]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5702616572380066, 0.5154055953025818, 0.31137293577194214, 0.4953343868255615, 0.5605323910713196, 0.5508803129196167, 0.3523132801055908, 0.35761940479278564, 0.4245041012763977, 0.43403929471969604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0641429424285889})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5280650854110718})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37480974197387695})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3510938882827759})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3586500883102417})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3573007583618164})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32731062173843384})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34498095512390137})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3235311806201935})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39453500509262085})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37733349204063416})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36513280868530273})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.307811767578125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8889340162277222})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5217373371124268})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39142972230911255})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3567299246788025})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3195990324020386})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33077168464660645})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3076172471046448})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2970341742038727})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3083631992340088})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.29374441504478455})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2911706268787384})
store['active_learning_steps'][28]['eval_training']['best_epoch']=11
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 35670], ['id', 32129], ['id', 52101], ['id', 38315], ['ood', 33063], ['id', 10726], ['id', 53556], ['id', 33594], ['id', 46764], ['id', 46088]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.2529035806655884, 0.3349952697753906, 0.32302671670913696, 0.44324618577957153, 0.34998220205307007, 0.5374084115028381, 0.507486879825592, 0.5099170207977295, 0.42711108922958374, 0.29754579067230225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.0048511028289795})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4836848974227905})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39481914043426514})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32433992624282837})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3470193147659302})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31384333968162537})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32276731729507446})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3323709964752197})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35158771276474})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.287393896484375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.769511342048645})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49275118112564087})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4280846118927002})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3450712561607361})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33601731061935425})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32519644498825073})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31189584732055664})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30181407928466797})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 7130], ['id', 54190], ['id', 39305], ['id', 55906], ['id', 48512], ['ood', 27940], ['ood', 26589], ['id', 23089], ['ood', 50403], ['id', 788]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.19196999073028564, 0.3365015387535095, 0.35804659128189087, 0.39339685440063477, 0.34211379289627075, 0.42148327827453613, 0.252535343170166, 0.4313768148422241, 0.44999033212661743, 0.3744690418243408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.206817865371704})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6206470131874084})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4139294922351837})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37568527460098267})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3944896459579468})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35750681161880493})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3399428129196167})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3677677810192108})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3584401607513428})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34583139419555664})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.302540283203125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9790120124816895})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48586463928222656})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3958243727684021})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35122328996658325})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3221423923969269})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3363121747970581})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3138314485549927})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29723840951919556})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.292783260345459})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 39877], ['id', 46790], ['id', 7732], ['id', 54994], ['id', 424], ['id', 20959], ['id', 14307], ['id', 39316], ['id', 52225], ['id', 41424]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.445198118686676, 0.2866052985191345, 0.47162342071533203, 0.5120425224304199, 0.311909556388855, 0.3582683205604553, 0.3002035319805145, 0.4240613579750061, 0.38993024826049805, 0.4544229507446289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1002432107925415})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.520595133304596})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35307347774505615})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3404427766799927})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32839226722717285})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3279117941856384})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3034213185310364})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3235953748226166})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3113322854042053})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3187152147293091})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.2735235595703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9090334177017212})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5482033491134644})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3811221122741699})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40057337284088135})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3461883068084717})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33814096450805664})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3069911301136017})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32151487469673157})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28624844551086426})
store['active_learning_steps'][31]['eval_training']['best_epoch']=9
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 47914], ['ood', 50727], ['id', 45739], ['id', 10256], ['id', 48681], ['id', 12764], ['id', 31688], ['id', 22149], ['id', 58022], ['id', 52133]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7208251059055328, 0.3076103925704956, 0.2927706837654114, 0.5918825268745422, 0.33147817850112915, 0.45593953132629395, 0.4099090099334717, 0.29397261142730713, 0.3133159577846527, 0.4067472815513611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1012756824493408})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5021293759346008})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39181363582611084})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3274291753768921})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3180725574493408})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.348794162273407})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32065969705581665})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3569198250770569})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.2951945556640625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8344874382019043})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.50417160987854})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3966923654079437})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3853137493133545})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3414672315120697})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33460819721221924})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34588056802749634})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 49200], ['id', 2859], ['id', 32766], ['id', 44698], ['id', 32323], ['id', 25210], ['id', 50026], ['id', 47475], ['id', 1682], ['id', 8447]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.268020361661911, 0.5213617086410522, 0.44464099407196045, 0.367692768573761, 0.5036522150039673, 0.5042945742607117, 0.22877174615859985, 0.42395853996276855, 0.3438315987586975, 0.5175574421882629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0326502323150635})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4649743139743805})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39777541160583496})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35833510756492615})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3142516016960144})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3169240951538086})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3422815799713135})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2999769449234009})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34863966703414917})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.310398131608963})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35071200132369995})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.264396630859375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8480266332626343})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4988560676574707})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37238776683807373})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3379989266395569})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2973041534423828})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28990471363067627})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29959386587142944})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2580876350402832})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2730015814304352})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26225054264068604})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 14296], ['id', 37758], ['id', 44690], ['id', 26640], ['id', 24850], ['id', 2818], ['id', 24440], ['id', 12559], ['id', 17709], ['id', 48137]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42674580216407776, 0.35370659828186035, 0.29958105087280273, 0.36294829845428467, 0.2287089228630066, 0.3458055257797241, 0.3525538444519043, 0.3770512640476227, 0.2997737526893616, 0.35029464960098267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1574897766113281})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5923641920089722})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42891964316368103})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.389956533908844})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.339546799659729})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32845696806907654})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34127840399742126})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3362279236316681})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3161524534225464})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34744369983673096})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37612783908843994})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3319447636604309})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.285827685546875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9216669797897339})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5384248495101929})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42997318506240845})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3367564082145691})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3208554685115814})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.300017774105072})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28286439180374146})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28999853134155273})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2814335227012634})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2588120102882385})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2568581700325012})
store['active_learning_steps'][34]['eval_training']['best_epoch']=11
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 44202], ['id', 47631], ['id', 22292], ['id', 29294], ['id', 29254], ['id', 17079], ['id', 137], ['id', 21690], ['id', 59731], ['id', 36076]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4531390070915222, 0.4125325083732605, 0.48805755376815796, 0.6194078326225281, 0.6507219076156616, 0.6574768424034119, 0.5623201727867126, 0.5246753096580505, 0.7241087555885315, 0.21437600255012512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.084245204925537})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5506471395492554})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4095917046070099})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33999067544937134})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30258628726005554})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3045037090778351})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29180553555488586})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2948143482208252})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3068159222602844})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3041927218437195})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2657220703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.916595458984375})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5209635496139526})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34952694177627563})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.362339049577713})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3014010787010193})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30913347005844116})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31221073865890503})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2827993631362915})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24770812690258026})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 27696], ['id', 32450], ['id', 13838], ['id', 27770], ['id', 974], ['id', 24589], ['id', 1380], ['id', 48360], ['id', 55090], ['id', 23629]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4228004217147827, 0.400388240814209, 0.29432982206344604, 0.3823474943637848, 0.362079381942749, 0.4214284420013428, 0.38033759593963623, 0.32698047161102295, 0.47876042127609253, 0.37952136993408203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.0685368776321411})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46946871280670166})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36280637979507446})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2857775092124939})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2945571541786194})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26817744970321655})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2612132728099823})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2608080804347992})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2689571976661682})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3040498197078705})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2731912434101105})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2430320068359375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8154116272926331})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48095887899398804})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37289753556251526})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29990535974502563})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29689499735832214})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2653563618659973})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25717052817344666})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2694453001022339})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26614394783973694})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28175050020217896})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 49242], ['id', 30493], ['id', 42161], ['ood', 41739], ['id', 41933], ['id', 11534], ['id', 40448], ['id', 37588], ['id', 34101], ['ood', 6336]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.36699581146240234, 0.5806963443756104, 0.3646102547645569, 0.18271517753601074, 0.42484015226364136, 0.3694174885749817, 0.3837057650089264, 0.5763356685638428, 0.4158250391483307, 0.2407151460647583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.093965768814087})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4669296145439148})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3640156388282776})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27738454937934875})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2860901355743408})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2992425560951233})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27047157287597656})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24066713452339172})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24492591619491577})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28025907278060913})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2939164340496063})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.23342978515625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9738423824310303})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5170949101448059})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3725653886795044})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3179623484611511})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3118654489517212})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28263843059539795})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33507561683654785})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2670113742351532})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2444663643836975})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2779654860496521})
store['active_learning_steps'][37]['eval_training']['best_epoch']=9
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 49109], ['id', 29320], ['id', 58776], ['id', 6838], ['id', 11708], ['id', 224], ['id', 25566], ['id', 20002], ['id', 14405], ['id', 31308]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5326252579689026, 0.4672498106956482, 0.3703111410140991, 0.31926196813583374, 0.5951898694038391, 0.5401933193206787, 0.3581947684288025, 0.42471519112586975, 0.5085470080375671, 0.4123390316963196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0661436319351196})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5137078762054443})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3384701907634735})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3131313920021057})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28039705753326416})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24295786023139954})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2408163845539093})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24918171763420105})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27315622568130493})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2563247084617615})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.232332763671875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8486640453338623})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49646681547164917})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36252903938293457})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3244991898536682})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2791966199874878})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2513357996940613})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27207615971565247})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26410725712776184})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2551349401473999})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 35996], ['id', 19868], ['id', 19148], ['id', 39123], ['id', 30861], ['id', 39942], ['id', 7833], ['id', 10738], ['id', 12692], ['id', 32387]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4494667649269104, 0.42488914728164673, 0.37424325942993164, 0.42270416021347046, 0.4212130308151245, 0.2478346824645996, 0.27475160360336304, 0.39568018913269043, 0.3692760467529297, 0.5647497773170471]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1391198635101318})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5493698120117188})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36075514554977417})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34348607063293457})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28430986404418945})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.298626184463501})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.273108571767807})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2800586521625519})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29762187600135803})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2914162874221802})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2573591552734375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0726757049560547})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5572218894958496})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4261491894721985})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36405789852142334})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3048545718193054})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3087277412414551})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3249245882034302})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29232534766197205})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2789984941482544})
store['active_learning_steps'][39]['eval_training']['best_epoch']=9
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 39668], ['id', 14385], ['id', 50090], ['id', 49202], ['id', 58832], ['id', 29061], ['id', 854], ['id', 28362], ['id', 53872], ['id', 49656]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.49899935722351074, 0.3968433737754822, 0.441675066947937, 0.43842101097106934, 0.4627682566642761, 0.5393937826156616, 0.3739827275276184, 0.39596301317214966, 0.5935276746749878, 0.4138445258140564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.194730281829834})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5615148544311523})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4390109181404114})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3080345690250397})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.329878568649292})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3316024839878082})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29384517669677734})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2697110176086426})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2811717391014099})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2970817983150482})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2862795889377594})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2532559326171875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.020543098449707})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6007462739944458})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4504343271255493})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34951892495155334})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31601405143737793})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3513716459274292})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2937658429145813})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3044993579387665})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3032313287258148})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2631371021270752})
store['active_learning_steps'][40]['eval_training']['best_epoch']=10
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 39526], ['id', 11647], ['id', 19362], ['id', 34756], ['id', 26752], ['id', 46828], ['ood', 20941], ['id', 29872], ['id', 52886], ['id', 17747]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3392143249511719, 0.5250823497772217, 0.6098372936248779, 0.37489932775497437, 0.2813289761543274, 0.4422510266304016, 0.2032696008682251, 0.3243776559829712, 0.41765260696411133, 0.4368109703063965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0875211954116821})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.562688946723938})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4226958155632019})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3436053395271301})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2860471308231354})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3074268102645874})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28340792655944824})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31225892901420593})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2856033444404602})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2698981761932373})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27327921986579895})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2705032527446747})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26646655797958374})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2857089936733246})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29934239387512207})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31095054745674133})
store['active_learning_steps'][41]['training']['best_epoch']=13
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.25499833984375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0121599435806274})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.583317756652832})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38464099168777466})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29266390204429626})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28289270401000977})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25413286685943604})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2608291506767273})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24532350897789001})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.236716628074646})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24024170637130737})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23122555017471313})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22291181981563568})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2205338478088379})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22887557744979858})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23232579231262207})
store['active_learning_steps'][41]['eval_training']['best_epoch']=13
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 5155], ['id', 25332], ['id', 18135], ['id', 42353], ['id', 56106], ['id', 21636], ['id', 14201], ['id', 37900], ['id', 23468], ['id', 16007]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4950007200241089, 0.8215892016887665, 0.7995699644088745, 0.769421249628067, 0.5637069344520569, 0.673898458480835, 0.36418819427490234, 0.43653786182403564, 0.7799403369426727, 0.7555744349956512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1159183979034424})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5537300705909729})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40653181076049805})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33425503969192505})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28864428400993347})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29129278659820557})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2692466676235199})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2811460793018341})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2877957820892334})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28664079308509827})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2371341552734375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.980493426322937})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.519522488117218})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41501384973526})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33233171701431274})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33626794815063477})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3170618414878845})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32055339217185974})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2906743288040161})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2993426024913788})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 42472], ['id', 27537], ['id', 39208], ['id', 41453], ['id', 6706], ['id', 9450], ['id', 52727], ['id', 59681], ['id', 46640], ['id', 50017]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.481370747089386, 0.27762359380722046, 0.6054916381835938, 0.39779746532440186, 0.3882771134376526, 0.39943933486938477, 0.3928336501121521, 0.4149453639984131, 0.36776381731033325, 0.41277480125427246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2009767293930054})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5477944016456604})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3514210283756256})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30653810501098633})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2937979996204376})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26408326625823975})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2991377115249634})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27300816774368286})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2831202745437622})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2414700439453125}
