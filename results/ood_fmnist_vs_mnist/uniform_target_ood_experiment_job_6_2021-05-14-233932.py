store = {}
store['timestamp']=1621031972
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=6']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=30
store['config']={'seed': 1242, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.465273857116699})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4610755443573})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9222054481506348})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4325156211853027})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2740731239318848})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6214, 'crossentropy': 2.8212865234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3542624711990356})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2475929260253906})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2593705654144287})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.289900779724121})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 54582], ['ood', 20081], ['ood', 38998], ['ood', 42714], ['ood', 29132], ['ood', 37919], ['ood', 29172], ['ood', 43657], ['ood', 23474], ['ood', 19947]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0464346408843994, 1.0416192412376404, 1.0383065342903137, 1.037478506565094, 1.0337743163108826, 1.0324687361717224, 1.0319822430610657, 1.0277118682861328, 1.0269254446029663, 1.0266642570495605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9246149063110352})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.6225767135620117})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.886298656463623})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.9689435958862305})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5861, 'crossentropy': 1.95794765625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2652990818023682})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.264143943786621})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2404870986938477})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 23869], ['id', 15335], ['id', 42231], ['id', 18860], ['id', 59910], ['id', 11182], ['id', 30693], ['id', 24883], ['id', 44433], ['id', 41131]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6173771023750305, 0.6106871366500854, 0.6098504066467285, 0.6080601811408997, 0.604745090007782, 0.5998885035514832, 0.5983133316040039, 0.5968548059463501, 0.5949614644050598, 0.5944843292236328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.9458526372909546})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.0224146842956543})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.057697296142578})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.7360010147094727})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5615, 'crossentropy': 2.046928125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.3544976711273193})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3206337690353394})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3722045421600342})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 54957], ['id', 25853], ['id', 2142], ['id', 53757], ['id', 19964], ['id', 25781], ['id', 10900], ['id', 36027], ['id', 17060], ['id', 15341]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5642679929733276, 0.5417883396148682, 0.5384982228279114, 0.5322806239128113, 0.5269256830215454, 0.5240195989608765, 0.5217113494873047, 0.5211325883865356, 0.5193609595298767, 0.5181967616081238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.8154513835906982})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.424269676208496})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.084552526473999})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.4721264839172363})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5621, 'crossentropy': 1.9188625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3816888332366943})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3527681827545166})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.4029953479766846})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 15560], ['id', 1776], ['id', 37150], ['id', 479], ['id', 56329], ['id', 28860], ['id', 53784], ['id', 37709], ['id', 28824], ['id', 40155]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6233769655227661, 0.581832230091095, 0.5783351063728333, 0.5701799988746643, 0.5688818693161011, 0.5644991397857666, 0.563062846660614, 0.5543668270111084, 0.5518949031829834, 0.5507549047470093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.5988433361053467})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.3546979427337646})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.572385787963867})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.577448606491089})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5475, 'crossentropy': 1.7306755859375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.4739282131195068})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3676857948303223})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.3370051383972168})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 9459], ['ood', 46227], ['ood', 30547], ['ood', 46273], ['ood', 4347], ['ood', 39224], ['ood', 53487], ['ood', 43497], ['ood', 10599], ['ood', 8979]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.49692320823669434, 0.4754325747489929, 0.45766913890838623, 0.4541506767272949, 0.45337581634521484, 0.4525455832481384, 0.45162367820739746, 0.451599657535553, 0.4514281749725342, 0.45117008686065674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.4790160655975342})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.8939647674560547})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.359117031097412})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.78452205657959})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.566, 'crossentropy': 1.53577685546875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.4212627410888672})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.3704068660736084})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.3549442291259766})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 14410], ['id', 12545], ['id', 52002], ['id', 63], ['id', 58301], ['id', 3095], ['id', 19712], ['id', 13609], ['id', 10886], ['id', 29332]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5564756393432617, 0.5518839359283447, 0.5358967185020447, 0.5320359468460083, 0.5316668748855591, 0.5314074158668518, 0.5290732383728027, 0.5286173224449158, 0.5236040353775024, 0.5233132839202881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 1.4910324811935425})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.7018213272094727})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.1733806133270264})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1734137535095215})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5228, 'crossentropy': 1.53703525390625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.45703125, 'crossentropy': 1.4905389547348022})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.3992226123809814})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5, 'crossentropy': 1.3935329914093018})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 54813], ['id', 43277], ['id', 27260], ['id', 22547], ['id', 4195], ['id', 59324], ['id', 11559], ['id', 27800], ['id', 52509], ['id', 30476]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36451733112335205, 0.3616974353790283, 0.35914015769958496, 0.35885000228881836, 0.3573911190032959, 0.3535677194595337, 0.35127055644989014, 0.34889423847198486, 0.34479427337646484, 0.3429211378097534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.5124938488006592})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.7770100831985474})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.142808437347412})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.7774906158447266})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.524, 'crossentropy': 1.55596474609375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.4775390625, 'crossentropy': 1.5296616554260254})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.4763391017913818})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.4865235090255737})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 5551], ['ood', 20250], ['ood', 30083], ['ood', 36987], ['ood', 36683], ['ood', 42609], ['ood', 33321], ['ood', 50848], ['ood', 56782], ['ood', 33698]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3450998067855835, 0.33774030208587646, 0.3354191780090332, 0.3335036039352417, 0.3320423364639282, 0.3316779136657715, 0.3301973342895508, 0.32944464683532715, 0.3283294439315796, 0.3253939151763916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.5019311904907227})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.6206936836242676})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.9425551891326904})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.281965732574463})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5247, 'crossentropy': 1.6051421875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.4736328125, 'crossentropy': 1.5305163860321045})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4447846412658691})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.4608194828033447})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 50479], ['ood', 50475], ['ood', 45779], ['ood', 20497], ['ood', 50441], ['ood', 56027], ['ood', 25551], ['ood', 2749], ['ood', 37613], ['ood', 21784]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.38906681537628174, 0.38612329959869385, 0.3640943765640259, 0.3598496913909912, 0.3515598773956299, 0.3499472141265869, 0.3449958562850952, 0.3416827917098999, 0.3409963846206665, 0.33614861965179443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.4638671875, 'crossentropy': 1.583833932876587})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4012699127197266})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.6534273624420166})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.208770275115967})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.4717397689819336})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 1.46046279296875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2965588569641113})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2282726764678955})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2413578033447266})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2297065258026123})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 1160], ['id', 26018], ['id', 5821], ['id', 11687], ['id', 19688], ['id', 9622], ['id', 3142], ['id', 21075], ['id', 28297], ['id', 28139]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.37411028146743774, 0.3734617829322815, 0.367734432220459, 0.3532191514968872, 0.3513902425765991, 0.34607136249542236, 0.3438671827316284, 0.34074342250823975, 0.34050118923187256, 0.3343133330345154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.564658284187317})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.525008201599121})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.745683193206787})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.8459854125976562})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.1142144203186035})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5569, 'crossentropy': 1.620480078125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.4170221090316772})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3985586166381836})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.3832191228866577})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.3856489658355713})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 49891], ['id', 49777], ['id', 1344], ['id', 59806], ['ood', 53912], ['id', 35305], ['ood', 2773], ['id', 34701], ['id', 37913], ['id', 50783]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4406334161758423, 0.40674686431884766, 0.38922595977783203, 0.3872804641723633, 0.38534390926361084, 0.3803051710128784, 0.37907421588897705, 0.3731893301010132, 0.37183165550231934, 0.3668738603591919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.4736328125, 'crossentropy': 1.5780996084213257})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.495582103729248})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.617124319076538})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8717057704925537})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9897832870483398})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5753, 'crossentropy': 1.54319951171875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5166015625, 'crossentropy': 1.4770010709762573})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.3938069343566895})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.4013967514038086})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.34034264087677})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 56627], ['id', 32672], ['id', 32244], ['id', 25465], ['id', 48647], ['id', 14502], ['id', 27652], ['id', 53542], ['id', 53015], ['id', 8689]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3580331802368164, 0.3449845314025879, 0.33122384548187256, 0.33033573627471924, 0.32464540004730225, 0.3240795135498047, 0.32028067111968994, 0.3188469409942627, 0.3147852420806885, 0.31426680088043213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.4423828125, 'crossentropy': 1.6663646697998047})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.5278332233428955})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.6467053890228271})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8307756185531616})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.258561611175537})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5109, 'crossentropy': 1.670373828125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.47265625, 'crossentropy': 1.471927285194397})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.4450886249542236})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.4167462587356567})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.3846213817596436})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 32406], ['id', 23586], ['id', 13801], ['id', 1308], ['id', 39264], ['id', 50210], ['id', 8184], ['id', 36674], ['id', 52428], ['id', 25833]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.32538819313049316, 0.3185861110687256, 0.30529558658599854, 0.3026784658432007, 0.29586124420166016, 0.2955503463745117, 0.29325783252716064, 0.29216456413269043, 0.2880697250366211, 0.28654682636260986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.4169921875, 'crossentropy': 1.6097776889801025})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.4780423641204834})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.623114824295044})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.8870534896850586})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.231973648071289})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5816, 'crossentropy': 1.4937888671875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.4500678777694702})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3487484455108643})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3449242115020752})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3334943056106567})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 43510], ['id', 43193], ['id', 7696], ['id', 36110], ['id', 13598], ['id', 42596], ['id', 39699], ['id', 33988], ['id', 27951], ['id', 30218]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.32089507579803467, 0.3155301809310913, 0.30992817878723145, 0.3095513582229614, 0.30798643827438354, 0.2995460629463196, 0.2969013452529907, 0.29626333713531494, 0.2930269241333008, 0.2892810106277466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.3935546875, 'crossentropy': 1.6141464710235596})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.37233567237854})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5106630325317383})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4594188928604126})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.8125922679901123})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5872, 'crossentropy': 1.393496484375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.445949673652649})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.3729008436203003})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.3446290493011475})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3262920379638672})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 37251], ['id', 57297], ['id', 4436], ['id', 49008], ['id', 4135], ['id', 31727], ['id', 32684], ['id', 36424], ['id', 45484], ['id', 12421]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.31956303119659424, 0.2816317081451416, 0.28044241666793823, 0.27795541286468506, 0.27673590183258057, 0.27274656295776367, 0.2725512981414795, 0.27109014987945557, 0.27105581760406494, 0.2707664966583252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.5608832836151123})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.3964102268218994})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.5167831182479858})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.5312676429748535})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5770847797393799})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5857, 'crossentropy': 1.43069501953125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.4172377586364746})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.3465447425842285})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.3119560480117798})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.300344705581665})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 5205], ['id', 59638], ['id', 29980], ['id', 174], ['id', 6797], ['id', 27829], ['id', 19370], ['id', 8276], ['id', 11420], ['id', 1286]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.30579376220703125, 0.2967049479484558, 0.29283589124679565, 0.2916393280029297, 0.29117143154144287, 0.29113978147506714, 0.29108577966690063, 0.28968870639801025, 0.2893573045730591, 0.28925156593322754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.451403021812439})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3080637454986572})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.410074234008789})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5262947082519531})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6555497646331787})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 1.3367341796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.3669925928115845})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3115203380584717})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2244160175323486})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.230802297592163})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 55765], ['id', 37300], ['id', 34314], ['id', 41067], ['id', 2731], ['id', 55157], ['id', 2181], ['id', 47772], ['id', 13454], ['id', 2229]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33259665966033936, 0.32144272327423096, 0.31800591945648193, 0.31775009632110596, 0.31418800354003906, 0.31127679347991943, 0.3003183603286743, 0.2959803342819214, 0.289272665977478, 0.28825557231903076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.541463017463684})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2875100374221802})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2709548473358154})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3201465606689453})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4064321517944336})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4808738231658936})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.642, 'crossentropy': 1.3117048828125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3418233394622803})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2127057313919067})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.167156457901001})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1700739860534668})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.137183427810669})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 30299], ['ood', 21409], ['ood', 27509], ['ood', 47630], ['ood', 18150], ['ood', 37319], ['ood', 35206], ['id', 39880], ['ood', 32393], ['id', 47317]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.37766093015670776, 0.3638548254966736, 0.36230993270874023, 0.3618233799934387, 0.35437464714050293, 0.3486584424972534, 0.34844547510147095, 0.3455176055431366, 0.342393159866333, 0.3413503170013428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4913448095321655})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3217499256134033})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3085353374481201})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2962779998779297})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3540102243423462})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.570783257484436})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.989039659500122})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6515, 'crossentropy': 1.42610478515625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3424885272979736})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2612719535827637})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2127549648284912})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1637181043624878})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1457808017730713})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1584491729736328})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 17345], ['id', 57660], ['id', 55778], ['id', 9692], ['id', 59691], ['id', 29652], ['id', 49032], ['id', 55587], ['id', 56561], ['id', 43342]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4351736307144165, 0.42985665798187256, 0.4270973205566406, 0.4112924337387085, 0.4097033143043518, 0.40627801418304443, 0.40598708391189575, 0.4010692834854126, 0.3998851776123047, 0.3971909284591675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.5206472873687744})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.192012071609497})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2135308980941772})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3096425533294678})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2153162956237793})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6246, 'crossentropy': 1.2461712890625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.3736722469329834})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2710068225860596})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2638156414031982})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.228820562362671})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 34821], ['id', 39750], ['id', 6983], ['id', 28159], ['id', 18284], ['id', 18255], ['id', 55368], ['id', 17267], ['id', 45097], ['id', 52098]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3007098436355591, 0.29251188039779663, 0.2865337133407593, 0.2848987579345703, 0.2798452377319336, 0.27762413024902344, 0.27508533000946045, 0.2746385335922241, 0.27410387992858887, 0.2720900774002075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.5008268356323242})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2646222114562988})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3040204048156738})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3841688632965088})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3139050006866455})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.629, 'crossentropy': 1.32716494140625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3843077421188354})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.338233232498169})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2204616069793701})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2809211015701294})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42521], ['id', 38307], ['id', 51163], ['id', 17160], ['id', 41608], ['id', 6929], ['id', 37367], ['id', 1058], ['id', 33369], ['id', 57416]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2660043239593506, 0.2565159797668457, 0.2541142702102661, 0.2529088854789734, 0.251708447933197, 0.24690991640090942, 0.2462930679321289, 0.24512064456939697, 0.24394679069519043, 0.24239516258239746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.4130859375, 'crossentropy': 1.6264052391052246})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2571650743484497})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.179341197013855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1909767389297485})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3678629398345947})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2852683067321777})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6296, 'crossentropy': 1.27161669921875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2770788669586182})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.208302617073059})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1657707691192627})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.146129846572876})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1024723052978516})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 31065], ['id', 12467], ['id', 10444], ['id', 22613], ['id', 3694], ['id', 27184], ['id', 28880], ['id', 59858], ['id', 37650], ['id', 31587]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3580782413482666, 0.331060528755188, 0.32607054710388184, 0.3225862979888916, 0.3160894513130188, 0.3160390853881836, 0.3142063617706299, 0.3051248788833618, 0.3029524087905884, 0.301660418510437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.4750216007232666})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.278146505355835})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3005883693695068})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.257857084274292})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.288194179534912})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3088147640228271})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4329758882522583})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 1.3300498046875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3050734996795654})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.157996416091919})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.124495267868042})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1450939178466797})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.075390338897705})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.107721209526062})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 41289], ['ood', 8014], ['ood', 54013], ['ood', 49864], ['id', 55098], ['ood', 41091], ['ood', 17526], ['id', 2846], ['ood', 55322], ['ood', 53724]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3625776171684265, 0.34318816661834717, 0.3428869843482971, 0.3359729051589966, 0.33112549781799316, 0.3244882822036743, 0.32095134258270264, 0.3192571997642517, 0.31925129890441895, 0.31882286071777344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.5444424152374268})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.3428583145141602})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2141642570495605})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2024110555648804})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2070248126983643})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3000476360321045})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2757076025009155})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6492, 'crossentropy': 1.23357041015625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.345865249633789})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2213619947433472})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1434595584869385})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1006556749343872})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.108515739440918})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0910371541976929})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 47079], ['id', 9302], ['id', 56948], ['id', 52223], ['id', 24312], ['id', 53522], ['id', 59826], ['id', 326], ['id', 37489], ['id', 24607]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3484989404678345, 0.3467090129852295, 0.3295753002166748, 0.3238004446029663, 0.3226872682571411, 0.32245492935180664, 0.32070159912109375, 0.31436288356781006, 0.3139225244522095, 0.30158746242523193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.5569615364074707})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2460108995437622})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1836903095245361})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1742539405822754})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1901354789733887})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.268786907196045})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.244123101234436})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6495, 'crossentropy': 1.2440564453125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2479420900344849})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1407787799835205})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.078329086303711})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0575141906738281})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.021624207496643})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 0.9831557273864746})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 5346], ['id', 34620], ['id', 16154], ['id', 29629], ['id', 12346], ['id', 801], ['id', 17903], ['id', 24641], ['id', 9924], ['id', 48453]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41671979427337646, 0.3847074508666992, 0.38018113374710083, 0.36689794063568115, 0.36375391483306885, 0.36182117462158203, 0.3602888584136963, 0.36010444164276123, 0.35908639430999756, 0.35739898681640625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.3779296875, 'crossentropy': 1.5739167928695679})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2064534425735474})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0932129621505737})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0856037139892578})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1247532367706299})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0525245666503906})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1401560306549072})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2103757858276367})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1940021514892578})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7106, 'crossentropy': 1.13743916015625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.222591519355774})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0519518852233887})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9701571464538574})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 0.9754772782325745})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9544442892074585})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9294053316116333})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9065126180648804})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9012448191642761})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 41355], ['id', 11611], ['id', 28218], ['id', 20638], ['id', 55855], ['id', 39707], ['id', 53298], ['id', 40549], ['id', 34303], ['id', 13257]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4796183109283447, 0.45442551374435425, 0.44920873641967773, 0.43699514865875244, 0.43180620670318604, 0.4237024784088135, 0.41607046127319336, 0.40988194942474365, 0.40805453062057495, 0.4053844213485718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.544948697090149})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2381877899169922})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1064834594726562})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1634881496429443})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.169804334640503})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1076070070266724})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6641, 'crossentropy': 1.12930576171875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2953777313232422})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1655659675598145})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.134158968925476})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.113090991973877})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.125364065170288})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 57751], ['ood', 56244], ['id', 34817], ['id', 48293], ['id', 38618], ['id', 59771], ['id', 8879], ['ood', 27756], ['ood', 27315], ['id', 15430]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3231925964355469, 0.30338311195373535, 0.2870372533798218, 0.2859005928039551, 0.2812016010284424, 0.27977579832077026, 0.27777743339538574, 0.2717550992965698, 0.2630174160003662, 0.26187920570373535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.5320534706115723})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2821614742279053})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1319981813430786})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0856988430023193})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0282644033432007})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1100656986236572})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1889009475708008})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1836315393447876})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6857, 'crossentropy': 1.10912490234375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.28762948513031})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1033674478530884})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0468649864196777})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9906051158905029})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 0.9709391593933105})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9633967876434326})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9651771783828735})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 32498], ['id', 32110], ['id', 33674], ['id', 10252], ['id', 59835], ['id', 21258], ['id', 50045], ['id', 29088], ['id', 53680], ['id', 53654]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3888200521469116, 0.37644755840301514, 0.37426626682281494, 0.37112295627593994, 0.3619575500488281, 0.3593783378601074, 0.35413241386413574, 0.3505434989929199, 0.3483680486679077, 0.3476449251174927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.455078125, 'crossentropy': 1.585222601890564})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2717435359954834})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1694326400756836})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0840957164764404})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.080804705619812})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1411916017532349})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0713260173797607})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1683473587036133})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.108022928237915})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2019188404083252})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7017, 'crossentropy': 1.1342962890625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2257035970687866})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0793039798736572})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.9788902997970581})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 0.9464154839515686})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9157395958900452})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.924017071723938})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9084445238113403})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9158791303634644})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9233686327934265})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 23515], ['id', 43464], ['id', 35650], ['id', 23414], ['id', 29389], ['id', 45061], ['id', 13941], ['id', 59786], ['id', 10029], ['id', 8534]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5011678338050842, 0.49741649627685547, 0.4950200319290161, 0.4943188428878784, 0.49228525161743164, 0.4921480417251587, 0.4913431406021118, 0.48867881298065186, 0.48467981815338135, 0.4816117286682129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.4939038753509521})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.224440574645996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0278220176696777})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0089244842529297})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0303165912628174})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9956679344177246})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0150989294052124})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.003358244895935})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0783231258392334})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.698, 'crossentropy': 1.08892158203125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.259103775024414})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1082351207733154})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 0.9783766865730286})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9513403177261353})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 0.956026554107666})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.932823657989502})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9304038286209106})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9066159129142761})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20624], ['id', 54405], ['id', 47000], ['id', 39951], ['id', 1807], ['id', 34311], ['id', 3457], ['id', 54661], ['id', 58709], ['id', 9189]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.48089301586151123, 0.44941461086273193, 0.4321540594100952, 0.41963088512420654, 0.4180365204811096, 0.4171346426010132, 0.4031496047973633, 0.4022112488746643, 0.4017760157585144, 0.4015766978263855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.4876511096954346})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2172937393188477})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0479068756103516})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1051957607269287})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0192703008651733})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0214452743530273})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9910336136817932})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0086448192596436})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.0669893026351929})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1253516674041748})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7038, 'crossentropy': 1.07165693359375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2822160720825195})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0222160816192627})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9745802879333496})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9077194929122925})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9117037057876587})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8763751983642578})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9088321924209595})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.8971447944641113})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.8864659070968628})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 24079], ['id', 18675], ['id', 36843], ['id', 6000], ['id', 52556], ['id', 8387], ['id', 46661], ['ood', 40732], ['id', 33801], ['ood', 53298]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5316718816757202, 0.5284252166748047, 0.5183789730072021, 0.49189114570617676, 0.44351446628570557, 0.4314206838607788, 0.4276916980743408, 0.42740148305892944, 0.4246032238006592, 0.4238244295120239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.495681643486023})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2168128490447998})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0564583539962769})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.02167809009552})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9837197661399841})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9756802320480347})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9893423318862915})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.980622410774231})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0522983074188232})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7184, 'crossentropy': 1.01536357421875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3040440082550049})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1378448009490967})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0068917274475098})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9660422801971436})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9250452518463135})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9374686479568481})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8868745565414429})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9046447277069092})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 56166], ['id', 17325], ['id', 32185], ['id', 28967], ['id', 9232], ['id', 43465], ['id', 26516], ['id', 16859], ['id', 11662], ['id', 47851]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.43805456161499023, 0.431662917137146, 0.4012300968170166, 0.38554006814956665, 0.38405001163482666, 0.38168394565582275, 0.3794524073600769, 0.37925004959106445, 0.3764312267303467, 0.3733619451522827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4245965480804443})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.180860996246338})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0454546213150024})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0139819383621216})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9659216403961182})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0088850259780884})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9736535549163818})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9899934530258179})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7154, 'crossentropy': 0.97520205078125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.2890665531158447})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.0828888416290283})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.078136920928955})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0304287672042847})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.982262372970581})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 0.9592854380607605})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.011564016342163})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 49545], ['id', 34043], ['id', 14142], ['id', 36388], ['id', 23339], ['ood', 2292], ['id', 27681], ['id', 27887], ['id', 53157], ['id', 19150]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3996925354003906, 0.38952183723449707, 0.38152432441711426, 0.3726438283920288, 0.3635290861129761, 0.3634803295135498, 0.35887444019317627, 0.3578794002532959, 0.35526180267333984, 0.3552212715148926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.4582074880599976})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.15652334690094})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.03346586227417})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0285277366638184})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9613779783248901})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9599604606628418})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9575239419937134})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.9160448312759399})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9615381956100464})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9950751066207886})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.040048360824585})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.734, 'crossentropy': 1.01131142578125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2741928100585938})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0466318130493164})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9805489778518677})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9108439683914185})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.8909702301025391})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9092291593551636})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.8917940855026245})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9087831974029541})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 19904], ['id', 36120], ['id', 14885], ['id', 15361], ['id', 56015], ['id', 29158], ['id', 24108], ['id', 59559], ['id', 47163], ['id', 13902]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4428175091743469, 0.4265800714492798, 0.41923487186431885, 0.4178730845451355, 0.4163120985031128, 0.40310609340667725, 0.38980942964553833, 0.38524186611175537, 0.3847792148590088, 0.3767143487930298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.413228988647461})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1709662675857544})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0109981298446655})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0147110223770142})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9818497896194458})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0039076805114746})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0360701084136963})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9946221113204956})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.719, 'crossentropy': 1.00869814453125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2657748460769653})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0609080791473389})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9787335395812988})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9563723802566528})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9179291725158691})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9294143915176392})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9000451564788818})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 26636], ['id', 850], ['id', 3301], ['id', 38806], ['id', 46619], ['id', 13464], ['id', 11651], ['id', 49763], ['ood', 57362], ['id', 24338]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37760210037231445, 0.34534263610839844, 0.33855223655700684, 0.3331140875816345, 0.3253632187843323, 0.3198343515396118, 0.3195157051086426, 0.31832772493362427, 0.3176279067993164, 0.3168540596961975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.5180597305297852})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2203370332717896})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0665264129638672})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0278496742248535})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0052714347839355})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9589478969573975})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9721767902374268})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.074263572692871})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0361406803131104})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7072, 'crossentropy': 1.0319068359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.268069863319397})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9801071286201477})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9582809209823608})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9257377982139587})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9036043882369995})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9139947295188904})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.888619601726532})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.8866779804229736})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 5355], ['id', 9771], ['id', 57486], ['id', 27863], ['id', 1033], ['id', 3913], ['id', 58065], ['id', 36400], ['id', 18584], ['id', 56860]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4743168354034424, 0.4474548101425171, 0.43339109420776367, 0.41763293743133545, 0.41232824325561523, 0.4047567844390869, 0.4005228281021118, 0.3962775468826294, 0.3889562487602234, 0.3800492286682129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.5551064014434814})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.229316234588623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0249385833740234})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0045661926269531})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9537254571914673})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9560585021972656})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9352957010269165})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9872593879699707})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0062791109085083})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.0346651077270508})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7246, 'crossentropy': 0.98868935546875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2565944194793701})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0727601051330566})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0371249914169312})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9392489790916443})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9181525111198425})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9026616811752319})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9261095523834229})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9050924777984619})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9138274192810059})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 27477], ['id', 52334], ['id', 22163], ['id', 46613], ['id', 17076], ['id', 43543], ['id', 26823], ['id', 48933], ['id', 14412], ['id', 2502]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.40247273445129395, 0.40087705850601196, 0.38641130924224854, 0.38562172651290894, 0.38305091857910156, 0.3829999566078186, 0.38245004415512085, 0.37846213579177856, 0.37835729122161865, 0.3707238435745239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.4965226650238037})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1965610980987549})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1203687191009521})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.042677640914917})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0105531215667725})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0049322843551636})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0365397930145264})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.01885986328125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.964913547039032})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.007507562637329})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0795695781707764})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.072922945022583})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7262, 'crossentropy': 1.04055771484375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.304976224899292})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.014398455619812})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 0.9344577789306641})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9067493677139282})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.8650164604187012})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8775554299354553})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.8870373368263245})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.8648049831390381})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.8494009375572205})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.843401312828064})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.8370209336280823})
store['active_learning_steps'][37]['eval_training']['best_epoch']=11
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 13384], ['id', 54896], ['id', 23345], ['id', 33232], ['id', 7577], ['id', 20009], ['id', 45262], ['id', 2837], ['id', 49531], ['id', 47494]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5130701065063477, 0.4855967164039612, 0.4713541269302368, 0.45893704891204834, 0.45823919773101807, 0.45327651500701904, 0.4507187604904175, 0.4504285454750061, 0.44638770818710327, 0.44082093238830566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.4414029121398926})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.134516954421997})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9888057708740234})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9816648960113525})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9789211750030518})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9418966770172119})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9500912427902222})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1330980062484741})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9954959154129028})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7295, 'crossentropy': 0.9600533203125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.258385181427002})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.977320671081543})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9460744261741638})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.8786181211471558})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.8932551145553589})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.8769489526748657})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.8720541000366211})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8528999090194702})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 21864], ['id', 33964], ['id', 35336], ['id', 22224], ['id', 27676], ['id', 55165], ['id', 1031], ['id', 12580], ['id', 19842], ['id', 5413]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4148957133293152, 0.41345322132110596, 0.40428006649017334, 0.39344775676727295, 0.3901205062866211, 0.3816238045692444, 0.3771282434463501, 0.3719273805618286, 0.36959755420684814, 0.3627035617828369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.4794921875, 'crossentropy': 1.5675957202911377})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.180433750152588})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0379281044006348})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0097429752349854})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9722833633422852})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9813533425331116})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9651516675949097})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.0029939413070679})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9918328523635864})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0258734226226807})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7289, 'crossentropy': 0.98656806640625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.285430669784546})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.048933744430542})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0102577209472656})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9135591387748718})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9066872596740723})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.862357497215271})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.8895828723907471})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.8588103652000427})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.8501133918762207})
store['active_learning_steps'][39]['eval_training']['best_epoch']=9
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 51688], ['id', 70], ['id', 29672], ['id', 39560], ['id', 12078], ['id', 37827], ['id', 46507], ['id', 8099], ['id', 22637], ['id', 18533]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5080549716949463, 0.4292867183685303, 0.4281117916107178, 0.4278712272644043, 0.41987478733062744, 0.41856932640075684, 0.4168601632118225, 0.4149322509765625, 0.4097086787223816, 0.4065033793449402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.5412218570709229})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1754181385040283})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.02128267288208})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9791924357414246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9435043334960938})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9231646060943604})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.886736273765564})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9440512657165527})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0020345449447632})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9854462146759033})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7293, 'crossentropy': 0.93185185546875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2600071430206299})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0578789710998535})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9137453436851501})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9468950033187866})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8790650367736816})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.8578934669494629})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.8705344200134277})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.8294638991355896})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.8206850290298462})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 3594], ['id', 1254], ['id', 54073], ['id', 59953], ['id', 32393], ['id', 26763], ['id', 55085], ['id', 20959], ['id', 37052], ['id', 3410]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4861396551132202, 0.4285486936569214, 0.42560362815856934, 0.42469727993011475, 0.4043947458267212, 0.3919004201889038, 0.3897383213043213, 0.3874560594558716, 0.38449788093566895, 0.37802016735076904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.5644800662994385})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.1521672010421753})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0177581310272217})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9309960603713989})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9428743124008179})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9376941919326782})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9580360651016235})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7224, 'crossentropy': 0.97576904296875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2973828315734863})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0579705238342285})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0158004760742188})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9835081696510315})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0111902952194214})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9617384672164917})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 3800], ['id', 59981], ['id', 59091], ['id', 48964], ['id', 3510], ['id', 21687], ['id', 12714], ['id', 22069], ['id', 58948], ['id', 10570]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35133618116378784, 0.3340786099433899, 0.3259750008583069, 0.32038968801498413, 0.32034778594970703, 0.3199015259742737, 0.3196406960487366, 0.31958162784576416, 0.31723904609680176, 0.3164978623390198]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.5059874057769775})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1943403482437134})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0247200727462769})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0119376182556152})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9561498165130615})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8663655519485474})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.8970316648483276})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.8986079692840576})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9298263788223267})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.7383, 'crossentropy': 0.91518779296875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2079108953475952})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.027263879776001})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.962215781211853})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8851473927497864})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.883328378200531})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8940485715866089})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8517430424690247})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.861587643623352})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 37979], ['id', 386], ['id', 24433], ['id', 4821], ['id', 59671], ['id', 39952], ['id', 22016], ['id', 55916], ['id', 42536], ['id', 49055]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.33731400966644287, 0.33630311489105225, 0.3287285566329956, 0.3270280361175537, 0.3261268138885498, 0.3255876302719116, 0.3252915143966675, 0.3217918276786804, 0.32097935676574707, 0.3174506425857544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.4455044269561768})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1531342267990112})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0036450624465942})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9335071444511414})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9062181115150452})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9147073030471802})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8569002151489258})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9359207153320312})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 0.8638331294059753})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9343639612197876})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7483, 'crossentropy': 0.89401533203125}
