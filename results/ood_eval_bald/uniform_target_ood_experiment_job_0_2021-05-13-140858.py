store = {}
store['timestamp']=1620911338
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=0']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=20
store['config']={'seed': 1234, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.173092842102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.45434308052063})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.655754566192627})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6076624393463135})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6905, 'crossentropy': 1.99090078125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.174839973449707})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1219029426574707})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0926287174224854})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 35521], ['id', 34136], ['id', 17454], ['ood', 21219], ['id', 50381], ['id', 34678], ['ood', 5645], ['id', 7790], ['id', 54795], ['id', 48102]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8353060483932495, 0.7496199011802673, 0.8796994090080261, 0.5031688213348389, 0.7512497901916504, 0.9299537539482117, 0.47745537757873535, 0.9259240627288818, 0.6692615151405334, 0.8443500995635986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5223102569580078})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.9423129558563232})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1397128105163574})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2006473541259766})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6983, 'crossentropy': 1.5420947265625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1217377185821533})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0582661628723145})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.059912919998169})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 16593], ['id', 51761], ['id', 47539], ['id', 8569], ['id', 23999], ['id', 46890], ['id', 10473], ['id', 54635], ['id', 44882], ['ood', 13924]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.40847980976104736, 0.4321730136871338, 0.3956106901168823, 0.4459404945373535, 0.3500387668609619, 0.3670696020126343, 0.40705323219299316, 0.3648033142089844, 0.49720990657806396, 0.3372492790222168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1154985427856445})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2406032085418701})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3555964231491089})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.398321509361267})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7713, 'crossentropy': 1.0393173828125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9333921074867249})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.8747769594192505})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.8693829774856567})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 56669], ['id', 39468], ['id', 37983], ['id', 14787], ['id', 47741], ['id', 45753], ['id', 48045], ['id', 19868], ['id', 36939], ['id', 20228]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5547901391983032, 0.4131959080696106, 0.38359129428863525, 0.40461063385009766, 0.5547593832015991, 0.49752575159072876, 0.3482252359390259, 0.4015389680862427, 0.4972488284111023, 0.2808123826980591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2389631271362305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.4863426685333252})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.640207290649414})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.7347339391708374})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7759, 'crossentropy': 1.0881056640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.9844801425933838})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.875257134437561})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.8988948464393616})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 224], ['id', 23177], ['id', 30600], ['id', 54521], ['id', 50965], ['id', 26294], ['id', 57726], ['id', 28045], ['id', 41092], ['id', 28932]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.28512346744537354, 0.40131890773773193, 0.3827831745147705, 0.4501587152481079, 0.4182875156402588, 0.39784252643585205, 0.3901609182357788, 0.39893460273742676, 0.4891526699066162, 0.38479650020599365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.242218255996704})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.5508390665054321})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3213425874710083})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.567802906036377})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7769, 'crossentropy': 1.08709609375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0318961143493652})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9944596886634827})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.9056072235107422})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 32017], ['id', 15845], ['id', 58026], ['id', 15947], ['id', 53255], ['id', 49639], ['id', 34698], ['id', 6819], ['id', 20166], ['id', 30]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46566736698150635, 0.40827739238739014, 0.43236488103866577, 0.38299763202667236, 0.48308271169662476, 0.46240293979644775, 0.2965419292449951, 0.30475425720214844, 0.30069148540496826, 0.48162662982940674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.097386360168457})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2611979246139526})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1616265773773193})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.5251719951629639})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8153, 'crossentropy': 0.98675390625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9991503953933716})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8773578405380249})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8710851669311523})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 32370], ['id', 36744], ['id', 51522], ['id', 48874], ['id', 20277], ['id', 27167], ['id', 28141], ['id', 47965], ['id', 53517], ['id', 17261]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.37183916568756104, 0.5633779764175415, 0.4210594892501831, 0.1933135986328125, 0.2815050482749939, 0.42511171102523804, 0.4195767045021057, 0.49279820919036865, 0.6050225496292114, 0.44438910484313965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0225415229797363})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9465960264205933})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0866961479187012})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1031088829040527})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1494710445404053})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8559, 'crossentropy': 0.8407466796875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8709584474563599})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7258763313293457})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6826566457748413})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6332101821899414})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 53530], ['ood', 57221], ['id', 3266], ['id', 56882], ['id', 33451], ['id', 8691], ['id', 7768], ['id', 14644], ['id', 48751], ['id', 19945]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5354342460632324, 0.5898997783660889, 0.5295193791389465, 0.3396012783050537, 0.44180887937545776, 0.4933764338493347, 0.5212455987930298, 0.46925902366638184, 0.3614959716796875, 0.5049493312835693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9395098686218262})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9349607825279236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9317367672920227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9981644153594971})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0356948375701904})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.049279808998108})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.757852587890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7826043367385864})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6495791673660278})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6279057264328003})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6282821297645569})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.638319730758667})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 11950], ['id', 3447], ['id', 13025], ['id', 2852], ['ood', 15605], ['id', 47913], ['id', 51457], ['id', 50777], ['id', 35503], ['id', 44281]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36648106575012207, 0.3605673909187317, 0.5230391025543213, 0.4441038966178894, 0.31418561935424805, 0.4533756971359253, 0.3965928256511688, 0.3510861396789551, 0.49771809577941895, 0.5323448181152344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8794573545455933})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7880878448486328})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8192898035049438})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8830882906913757})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8835573196411133})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.884, 'crossentropy': 0.681511328125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7960466146469116})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6270362138748169})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.565112829208374})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5814476609230042})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 45240], ['id', 37974], ['id', 28359], ['id', 37877], ['id', 1248], ['id', 43692], ['id', 2765], ['id', 12581], ['id', 12377], ['id', 38770]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3323850631713867, 0.5973835587501526, 0.42875999212265015, 0.4185534119606018, 0.4571407437324524, 0.3816724419593811, 0.5595099329948425, 0.44047248363494873, 0.5547361373901367, 0.3443254232406616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.83717942237854})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7183970212936401})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7750672101974487})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.829380452632904})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8194785118103027})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.59230322265625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8079748153686523})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6591340899467468})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5851140022277832})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5904370546340942})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 59388], ['id', 14333], ['id', 41489], ['id', 37721], ['id', 28128], ['id', 22830], ['id', 12972], ['id', 12017], ['id', 8847], ['id', 15551]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.43059659004211426, 0.4478514790534973, 0.5419367551803589, 0.4001585841178894, 0.48240500688552856, 0.4493944048881531, 0.45282232761383057, 0.3499611020088196, 0.3936010003089905, 0.46514761447906494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9293862581253052})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7522468566894531})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7939242720603943})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6785038709640503})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7655491828918457})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8626115918159485})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7718619108200073})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.563153369140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.746268630027771})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5730648040771484})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5279471278190613})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4804501533508301})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4797302782535553})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.46820276975631714})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 80], ['id', 41897], ['id', 58560], ['id', 47100], ['id', 37822], ['id', 19298], ['ood', 14745], ['id', 18042], ['id', 8780], ['id', 42100]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5695421695709229, 0.43755871057510376, 0.4130536615848541, 0.5235681533813477, 0.5101062655448914, 0.6258935928344727, 0.25915956497192383, 0.5556135177612305, 0.62962406873703, 0.5469220876693726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8888116478919983})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5881140232086182})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6156312823295593})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6388100385665894})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6257179975509644})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.533245703125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7386350631713867})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.582634449005127})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5186138153076172})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5249838829040527})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 47628], ['id', 14791], ['id', 25357], ['id', 49576], ['id', 17958], ['id', 52314], ['id', 50342], ['id', 49728], ['id', 47936], ['id', 20820]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.46482616662979126, 0.4238690137863159, 0.3708686828613281, 0.4702030420303345, 0.41296517848968506, 0.3026834726333618, 0.33192551136016846, 0.4630196690559387, 0.4294549822807312, 0.49750322103500366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.898323655128479})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6732795238494873})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6639047861099243})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.667350709438324})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5946648716926575})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6057133674621582})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6146734356880188})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8124550580978394})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.55309375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.803027868270874})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5687167644500732})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5284556150436401})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.474090039730072})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46320027112960815})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4651060104370117})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4496462643146515})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 41334], ['ood', 44581], ['id', 22420], ['id', 18324], ['id', 58471], ['id', 22083], ['ood', 45163], ['id', 59332], ['id', 35351], ['id', 30074]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4513416886329651, 0.5340383648872375, 0.5525210499763489, 0.6953052878379822, 0.3909890055656433, 0.49718064069747925, 0.48091816902160645, 0.5797983407974243, 0.45343300700187683, 0.465385377407074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8522850871086121})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5403900146484375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5357004404067993})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48460161685943604})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5821044445037842})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5298547148704529})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5541232824325562})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9285, 'crossentropy': 0.473242333984375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8249847888946533})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5678966045379639})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4655420184135437})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47652649879455566})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41407501697540283})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4669923782348633})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 12431], ['id', 32215], ['id', 2803], ['id', 2559], ['id', 46132], ['id', 50387], ['id', 53115], ['id', 58384], ['id', 1776], ['id', 12950]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3810573220252991, 0.5684476494789124, 0.6698290705680847, 0.35863828659057617, 0.6889399886131287, 0.48694396018981934, 0.3983982801437378, 0.4413992166519165, 0.30308210849761963, 0.6168452501296997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9477514028549194})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5894755125045776})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.535488486289978})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4780997335910797})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.502742350101471})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5339803695678711})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5440782904624939})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.408374560546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.787270188331604})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5121859312057495})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4316755533218384})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43539339303970337})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37328869104385376})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37625718116760254})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 14726], ['id', 25920], ['id', 4107], ['id', 36818], ['id', 47782], ['id', 29630], ['id', 32909], ['id', 47557], ['id', 51241], ['id', 44502]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.43180370330810547, 0.46917203068733215, 0.4466533064842224, 0.49564915895462036, 0.3721431791782379, 0.5967075228691101, 0.4533558487892151, 0.40859919786453247, 0.4412347674369812, 0.46233007311820984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9141561985015869})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5478225946426392})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4857742190361023})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45234739780426025})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47181329131126404})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5221401453018188})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46425172686576843})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.414761328125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7169047594070435})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5031685829162598})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.405667245388031})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3822705149650574})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3504704236984253})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3500674366950989})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 54264], ['id', 3950], ['id', 37168], ['id', 8202], ['id', 40909], ['id', 33505], ['id', 37986], ['id', 41108], ['id', 23526], ['id', 47365]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4621160626411438, 0.43446213006973267, 0.47224295139312744, 0.4502522945404053, 0.21233493089675903, 0.4745965003967285, 0.43979549407958984, 0.4540954828262329, 0.37012892961502075, 0.4901597499847412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8981665372848511})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.535119891166687})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4491773247718811})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44494837522506714})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41577425599098206})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45149871706962585})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45221996307373047})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4810332655906677})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.948, 'crossentropy': 0.3630560302734375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8667026162147522})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5058809518814087})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42117300629615784})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37902602553367615})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3867655098438263})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36170005798339844})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3355257511138916})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 33162], ['id', 44736], ['ood', 5316], ['id', 37431], ['id', 31103], ['id', 25654], ['id', 8940], ['id', 36686], ['id', 45911], ['id', 10800]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4001423716545105, 0.5018627643585205, 0.2716597318649292, 0.34800857305526733, 0.39653003215789795, 0.4878726005554199, 0.34102416038513184, 0.6220698952674866, 0.2975289821624756, 0.4519096612930298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0110647678375244})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5950206518173218})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46945932507514954})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4919579029083252})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49211910367012024})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4678940176963806})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4889485239982605})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5413224697113037})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4982989430427551})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9444, 'crossentropy': 0.40838076171875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6848081350326538})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5037060379981995})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42250558733940125})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3944503366947174})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3587384819984436})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34836190938949585})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34307119250297546})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3522706627845764})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 22498], ['id', 23388], ['id', 17792], ['id', 20636], ['id', 49563], ['id', 22531], ['id', 21040], ['id', 5422], ['id', 32002], ['id', 28305]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39965158700942993, 0.5508089065551758, 0.5161682367324829, 0.5284389853477478, 0.47978997230529785, 0.5589586496353149, 0.48100459575653076, 0.396557092666626, 0.6421889066696167, 0.4196951389312744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9577310085296631})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5635228157043457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4606979787349701})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40665847063064575})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41218286752700806})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4420880079269409})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4123762845993042})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9471, 'crossentropy': 0.3632045166015625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7376047372817993})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5131187438964844})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40858227014541626})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4049447178840637})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4305077791213989})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36734268069267273})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 21601], ['id', 32835], ['id', 20045], ['ood', 10513], ['id', 23730], ['id', 23350], ['id', 58707], ['id', 2292], ['id', 16722], ['id', 14697]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.45428407192230225, 0.5657761096954346, 0.31914329528808594, 0.3447476625442505, 0.5759971737861633, 0.47107744216918945, 0.3201616406440735, 0.4607166051864624, 0.48061472177505493, 0.4536607265472412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9189603924751282})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5204250812530518})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4719086289405823})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4690816402435303})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4553316831588745})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.444324254989624})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4142836034297943})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42977792024612427})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.493627667427063})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.539162278175354})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.354244775390625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8162730932235718})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46308404207229614})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4017243981361389})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38733533024787903})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3267095685005188})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.33733507990837097})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34285086393356323})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.33881646394729614})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 46493], ['id', 40618], ['ood', 1436], ['id', 3336], ['id', 57714], ['id', 38287], ['id', 39135], ['ood', 11465], ['id', 32994], ['id', 52800]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.27181652188301086, 0.6134098470211029, 0.20652461051940918, 0.4126952290534973, 0.5407348275184631, 0.3765277862548828, 0.44785791635513306, 0.3155592679977417, 0.4579612612724304, 0.516247034072876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9583225250244141})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5271437168121338})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41462084650993347})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4071888327598572})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4174392819404602})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4282512664794922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4115660488605499})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.361024609375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7771879434585571})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5039345026016235})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41458675265312195})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44562655687332153})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3893078565597534})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35419178009033203})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 30123], ['id', 41453], ['id', 27448], ['id', 41553], ['id', 43696], ['id', 9390], ['id', 5000], ['id', 29253], ['id', 29472], ['id', 52727]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5181384086608887, 0.3293619155883789, 0.46339190006256104, 0.3825780153274536, 0.29145359992980957, 0.3619515299797058, 0.2503461241722107, 0.2745097875595093, 0.3086252212524414, 0.478071391582489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0001341104507446})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4732475280761719})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3964443802833557})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3863743543624878})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3557475805282593})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3750547766685486})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39339542388916016})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4009101688861847})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.321129541015625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.842748761177063})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5010573863983154})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38793763518333435})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3629789352416992})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34947970509529114})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3316333591938019})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3501388132572174})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 59913], ['id', 35051], ['id', 24990], ['id', 43745], ['id', 24223], ['ood', 3382], ['id', 38315], ['id', 16113], ['id', 8228], ['id', 55612]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.37323814630508423, 0.5236359238624573, 0.4698050022125244, 0.5972825884819031, 0.43588846921920776, 0.3176257610321045, 0.3982256054878235, 0.4332733154296875, 0.38875341415405273, 0.47115665674209595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9982296228408813})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5345315933227539})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39664459228515625})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3879163861274719})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3873458504676819})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39298442006111145})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39491891860961914})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4201211631298065})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.951, 'crossentropy': 0.340589306640625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7329089641571045})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46388760209083557})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42420485615730286})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3709033131599426})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.32703983783721924})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3136439323425293})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33463960886001587})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 817], ['id', 59957], ['id', 35997], ['ood', 48037], ['id', 8093], ['id', 8759], ['id', 31738], ['id', 20792], ['id', 14749], ['id', 7074]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4954763650894165, 0.6856386661529541, 0.4234347343444824, 0.15603983402252197, 0.5100355744361877, 0.3912390470504761, 0.4964299201965332, 0.6217817664146423, 0.44289880990982056, 0.2740812301635742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0457388162612915})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5697791576385498})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4442788362503052})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39219582080841064})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40596672892570496})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4101695418357849})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4212784171104431})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9526, 'crossentropy': 0.349722900390625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8286528587341309})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5372934341430664})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40223702788352966})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39802640676498413})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3998405337333679})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42409294843673706})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 43454], ['id', 32908], ['id', 17908], ['id', 43767], ['id', 20265], ['id', 21130], ['id', 56457], ['id', 39778], ['id', 27337], ['id', 23747]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.22789525985717773, 0.39512014389038086, 0.39037591218948364, 0.45668065547943115, 0.45062536001205444, 0.23456770181655884, 0.3097389340400696, 0.45804333686828613, 0.3955807685852051, 0.316788911819458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0410709381103516})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.554290235042572})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4021133482456207})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37122684717178345})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3852076530456543})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3783628046512604})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3616950809955597})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3759717345237732})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40268027782440186})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3698849081993103})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.339605029296875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8317671418190002})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47586482763290405})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4238818287849426})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35796600580215454})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34923824667930603})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3276072144508362})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.31688907742500305})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3344886898994446})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3096752166748047})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 11068], ['id', 19138], ['ood', 28020], ['id', 46300], ['id', 10716], ['id', 11734], ['id', 20756], ['ood', 12461], ['id', 16823], ['id', 38267]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.29410073161125183, 0.5232514142990112, 0.32713449001312256, 0.3791801333427429, 0.32771819829940796, 0.43767786026000977, 0.5919902920722961, 0.29802536964416504, 0.5511156320571899, 0.49262064695358276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9849699139595032})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5110421776771545})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42778071761131287})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37638720870018005})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40211641788482666})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3714783787727356})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36356011033058167})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37403231859207153})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4294500946998596})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4375699460506439})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9539, 'crossentropy': 0.3241119140625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8229405283927917})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.502521276473999})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4133755564689636})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32996344566345215})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34315264225006104})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33268463611602783})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32233214378356934})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30971503257751465})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3200747072696686})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 48837], ['id', 17047], ['id', 38165], ['id', 14896], ['id', 13305], ['id', 7142], ['id', 18501], ['id', 59460], ['id', 11206], ['id', 6289]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38462263345718384, 0.45066699385643005, 0.5549537539482117, 0.5959301888942719, 0.31594985723495483, 0.3614646792411804, 0.39337462186813354, 0.3143106698989868, 0.33418089151382446, 0.5941113829612732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0320141315460205})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4823596477508545})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39579343795776367})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36927342414855957})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3452712297439575})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36311691999435425})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3545939028263092})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3882531523704529})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.3092283203125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.816963791847229})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47349274158477783})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40631505846977234})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3604016900062561})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36093011498451233})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3392041325569153})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3360805809497833})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 26629], ['id', 6582], ['id', 38774], ['id', 4066], ['id', 18816], ['id', 57808], ['ood', 33774], ['id', 22053], ['id', 52524], ['id', 3136]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3967881202697754, 0.38627684116363525, 0.3355214595794678, 0.5631809234619141, 0.33725112676620483, 0.47242188453674316, 0.19850099086761475, 0.49104106426239014, 0.24088943004608154, 0.39344239234924316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.994243860244751})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5303553342819214})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39903944730758667})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4289053678512573})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4332181215286255})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4235503673553467})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.3902282470703125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8151164650917053})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5386584401130676})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5014795064926147})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4588806629180908})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42751121520996094})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 17153], ['id', 29310], ['id', 21370], ['id', 30072], ['id', 16911], ['id', 3719], ['id', 28468], ['id', 10481], ['id', 42763], ['id', 15412]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3868366479873657, 0.41425859928131104, 0.3044043779373169, 0.32010769844055176, 0.40383362770080566, 0.5564577579498291, 0.3488842844963074, 0.34817177057266235, 0.3311506509780884, 0.32947635650634766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.066473364830017})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5510691404342651})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42273277044296265})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39320918917655945})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3272044360637665})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3238488435745239})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3139544725418091})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33334481716156006})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30786657333374023})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35185712575912476})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3543233573436737})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3708168864250183})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.280885302734375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9084553718566895})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5136281251907349})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38802534341812134})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31046557426452637})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30594056844711304})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2987830638885498})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2872527837753296})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3024941086769104})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27065497636795044})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28515106439590454})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27075886726379395})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 31200], ['id', 26742], ['id', 38122], ['id', 56623], ['id', 8690], ['id', 30461], ['ood', 36648], ['id', 52151], ['id', 29890], ['id', 40876]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.48596978187561035, 0.33875805139541626, 0.3641223609447479, 0.4128309190273285, 0.42628514766693115, 0.36269062757492065, 0.38305962085723877, 0.5747393369674683, 0.38255828619003296, 0.7334533929824829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9996237754821777})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5660558938980103})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40498995780944824})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.343139111995697})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3237335979938507})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3564631938934326})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32055404782295227})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3643549680709839})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34859389066696167})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3548462986946106})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.2836806396484375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9256643056869507})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.49685049057006836})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41761231422424316})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35967785120010376})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37196797132492065})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3195545971393585})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3047937750816345})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31786951422691345})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2839488387107849})
store['active_learning_steps'][29]['eval_training']['best_epoch']=9
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 14325], ['id', 41643], ['id', 14405], ['id', 58832], ['id', 47079], ['id', 41485], ['id', 6466], ['id', 440], ['id', 15574], ['id', 41445]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4954995810985565, 0.4455157518386841, 0.5653284788131714, 0.6042909622192383, 0.5085455179214478, 0.5101714134216309, 0.4604344367980957, 0.6254135072231293, 0.43782296776771545, 0.4445565938949585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1365187168121338})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5716181397438049})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39590999484062195})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36402326822280884})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33488720655441284})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33141010999679565})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3590433597564697})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34556591510772705})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37601685523986816})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.306715869140625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8813905715942383})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.496155321598053})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3849572539329529})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3861837089061737})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31351977586746216})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33489179611206055})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33049601316452026})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.322632372379303})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 40226], ['id', 23733], ['id', 12587], ['id', 46354], ['id', 41426], ['id', 34486], ['id', 29179], ['ood', 40428], ['id', 44113], ['id', 6050]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.33498936891555786, 0.599929690361023, 0.289875328540802, 0.34057456254959106, 0.46024036407470703, 0.30484187602996826, 0.3971487283706665, 0.24823856353759766, 0.47301506996154785, 0.6193205714225769]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0831286907196045})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5622695684432983})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3986191749572754})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4103090763092041})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37716400623321533})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3627713918685913})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38694489002227783})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3564239740371704})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39905205368995667})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3786720335483551})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37288758158683777})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.30555537109375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7972471714019775})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48044538497924805})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3813377022743225})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32006099820137024})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3262213468551636})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2927783727645874})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33116692304611206})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2968564033508301})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31705111265182495})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 13992], ['id', 25988], ['id', 42668], ['id', 37712], ['id', 12484], ['id', 37276], ['id', 21495], ['id', 528], ['id', 22803], ['id', 52937]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.2569007873535156, 0.4092332720756531, 0.4241907596588135, 0.33299124240875244, 0.36855775117874146, 0.40739041566848755, 0.47121357917785645, 0.4040212035179138, 0.27797096967697144, 0.3513942360877991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0498239994049072})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5527576208114624})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.422635555267334})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3532099723815918})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.315984308719635})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35949963331222534})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3300023674964905})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32686740159988403})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.28736787109375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.880050778388977})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5121303796768188})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35986995697021484})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34124693274497986})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34748542308807373})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30414485931396484})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32477083802223206})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 44149], ['id', 55268], ['id', 32747], ['id', 14608], ['id', 635], ['id', 35232], ['id', 2761], ['id', 9608], ['id', 37810], ['id', 6098]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47601842880249023, 0.3694307804107666, 0.47592055797576904, 0.17383573949337006, 0.3674967288970947, 0.5493124127388, 0.4060554504394531, 0.3636021614074707, 0.314994215965271, 0.2882551848888397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.089051604270935})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5533460378646851})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3724370002746582})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3703630268573761})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38194507360458374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3316856026649475})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3021780550479889})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31774359941482544})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3249399960041046})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3161383271217346})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.260814990234375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8230791091918945})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.529798686504364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39024361968040466})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36899739503860474})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31451237201690674})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3200923502445221})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3358091711997986})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3281431794166565})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 7168], ['id', 37397], ['id', 8765], ['id', 17777], ['id', 13440], ['id', 24426], ['id', 48382], ['id', 48842], ['ood', 1707], ['id', 28469]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5112956762313843, 0.4715036153793335, 0.5152616500854492, 0.3002365231513977, 0.4908297657966614, 0.3065037727355957, 0.3831087350845337, 0.3537256717681885, 0.1912226676940918, 0.41329312324523926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1151883602142334})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5704513192176819})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4401072561740875})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3625645935535431})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3187757134437561})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37978875637054443})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33813178539276123})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3016880750656128})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37501320242881775})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3414595127105713})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3473818898200989})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2749855712890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9239445924758911})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47175776958465576})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4091992974281311})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34339749813079834})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34396523237228394})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2765582799911499})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29239001870155334})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3037438988685608})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27994754910469055})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49488], ['id', 16964], ['id', 51464], ['id', 21102], ['id', 12840], ['id', 17712], ['id', 37552], ['id', 39668], ['id', 4124], ['id', 33594]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4367486238479614, 0.425753653049469, 0.32519739866256714, 0.5113800764083862, 0.5731952786445618, 0.40521371364593506, 0.45530271530151367, 0.5878669023513794, 0.5608328580856323, 0.5471774935722351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0387721061706543})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5590720176696777})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3833072781562805})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3245302438735962})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34662431478500366})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34768009185791016})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3202749490737915})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3412317633628845})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3298822343349457})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3272753953933716})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.27218046875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8445433974266052})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.546573281288147})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4043869376182556})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36474576592445374})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3405166268348694})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.305159330368042})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31397122144699097})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28776612877845764})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.278520405292511})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41160], ['id', 55630], ['id', 2184], ['id', 5896], ['id', 28770], ['id', 54218], ['id', 1455], ['id', 13538], ['id', 882], ['id', 43921]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3837403655052185, 0.3537498116493225, 0.3858335018157959, 0.344066858291626, 0.31185537576675415, 0.3656580448150635, 0.38121140003204346, 0.36869460344314575, 0.20773684978485107, 0.2496192455291748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2455847263336182})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.582913875579834})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41093820333480835})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.356831431388855})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34476351737976074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3358851671218872})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2986178696155548})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3089457154273987})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3455156683921814})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3282442092895508})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2603218505859375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9348587393760681})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5129984021186829})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44541457295417786})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3542299270629883})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3173101544380188})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3228415846824646})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28665927052497864})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29891008138656616})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28961795568466187})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 36603], ['id', 45954], ['id', 49517], ['id', 41367], ['id', 40335], ['id', 30900], ['id', 17741], ['id', 28136], ['id', 40312], ['id', 59520]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4447473883628845, 0.42180871963500977, 0.451809823513031, 0.6318087577819824, 0.41018328070640564, 0.46695220470428467, 0.3691600561141968, 0.45548439025878906, 0.4703220725059509, 0.41707050800323486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.149404764175415})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.551638662815094})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3948656916618347})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3127240240573883})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3344298005104065})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.303584486246109})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3002452254295349})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30913209915161133})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3182348608970642})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2875620722770691})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30566900968551636})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29295971989631653})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3192231357097626})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.241732080078125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9890202283859253})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4846593141555786})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39675217866897583})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3520544767379761})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34111225605010986})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3150196373462677})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30661338567733765})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2957785129547119})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2787961959838867})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29637065529823303})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30879849195480347})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27282440662384033})
store['active_learning_steps'][37]['eval_training']['best_epoch']=12
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 37077], ['id', 38920], ['ood', 25264], ['id', 12392], ['id', 14096], ['id', 57311], ['id', 24630], ['id', 16959], ['id', 48355], ['id', 26588]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5327907800674438, 0.4615669846534729, 0.2665764093399048, 0.49489396810531616, 0.6550783514976501, 0.4667842388153076, 0.6153128743171692, 0.6662374138832092, 0.5784227252006531, 0.3808831572532654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.064819574356079})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5167624950408936})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.379244327545166})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3230450749397278})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2948739528656006})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30327731370925903})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29655036330223083})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2891677916049957})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28284597396850586})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28769606351852417})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31226712465286255})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2944220304489136})
store['active_learning_steps'][38]['training']['best_epoch']=9
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.24005234375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9222655296325684})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5301245450973511})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42011892795562744})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35726070404052734})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32264238595962524})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3112768530845642})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2794111967086792})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28662270307540894})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28394848108291626})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2807762026786804})
store['active_learning_steps'][38]['eval_training']['best_epoch']=7
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 48880], ['id', 5042], ['id', 11208], ['id', 45422], ['id', 37632], ['id', 49474], ['id', 36224], ['id', 55015], ['id', 34252], ['id', 33364]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.410533607006073, 0.36520159244537354, 0.3735184967517853, 0.4349243640899658, 0.5616359710693359, 0.6374415159225464, 0.3112497329711914, 0.3950379490852356, 0.25377708673477173, 0.34539657831192017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0972354412078857})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6311217546463013})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40702003240585327})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33663761615753174})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3282921314239502})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28829988837242126})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.317649245262146})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34292876720428467})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31113511323928833})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2591743896484375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8888228535652161})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.542802095413208})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.42360180616378784})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33068788051605225})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33744993805885315})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3139590919017792})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30524325370788574})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30608028173446655})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 34430], ['id', 42298], ['id', 22530], ['id', 46126], ['id', 50946], ['id', 16290], ['id', 40208], ['id', 15112], ['id', 38407], ['id', 19031]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2864767909049988, 0.25654837489128113, 0.5043968558311462, 0.5039147138595581, 0.43263840675354004, 0.3295556306838989, 0.5187468826770782, 0.2548121213912964, 0.41608303785324097, 0.3319740891456604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2420576810836792})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6492996215820312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4748833179473877})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35370686650276184})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36346864700317383})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3385128080844879})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3035510182380676})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32750242948532104})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3284885883331299})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3339821696281433})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.27021025390625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9862606525421143})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5334757566452026})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4588458240032196})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36257314682006836})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.35843563079833984})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33734095096588135})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2959074378013611})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3323248624801636})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3312717378139496})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 11304], ['id', 43636], ['id', 25482], ['id', 46249], ['id', 45073], ['id', 25262], ['id', 33860], ['id', 54002], ['id', 8655], ['id', 27986]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.46002399921417236, 0.46979546546936035, 0.35467565059661865, 0.3712018132209778, 0.27441346645355225, 0.3654080033302307, 0.4986013174057007, 0.524365246295929, 0.45824867486953735, 0.6139285564422607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3330035209655762})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6011372804641724})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3829880654811859})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37576401233673096})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35999035835266113})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3376842737197876})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.300923228263855})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3097808361053467})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3307555317878723})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32076334953308105})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.26728388671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.919980525970459})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46120887994766235})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4102814197540283})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34107354283332825})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3397839665412903})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2946636974811554})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3237828016281128})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2917780876159668})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2634612023830414})
store['active_learning_steps'][41]['eval_training']['best_epoch']=9
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 57308], ['id', 33055], ['id', 24688], ['id', 20989], ['id', 18460], ['id', 29662], ['id', 52550], ['id', 18946], ['id', 39734], ['id', 35482]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4399617910385132, 0.2761017680168152, 0.505649745464325, 0.4698152542114258, 0.3222838342189789, 0.7171767354011536, 0.46605613827705383, 0.4539194703102112, 0.5194605588912964, 0.46338504552841187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0845613479614258})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6050047874450684})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.41283637285232544})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33993101119995117})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2756313681602478})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28803589940071106})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26735353469848633})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2814673185348511})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26369184255599976})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2874147891998291})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2673342227935791})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3168677091598511})
store['active_learning_steps'][42]['training']['best_epoch']=9
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9751, 'crossentropy': 0.224683349609375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9680249094963074})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5190093517303467})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39035841822624207})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.350846529006958})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31797653436660767})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.299665629863739})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3062601685523987})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2758861184120178})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2812656760215759})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27994823455810547})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2727673649787903})
store['active_learning_steps'][42]['eval_training']['best_epoch']=11
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 46724], ['id', 13831], ['id', 7851], ['id', 9344], ['id', 20120], ['id', 45761], ['ood', 52836], ['id', 47669], ['id', 36118], ['id', 47471]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5890386998653412, 0.33851248025894165, 0.6539327502250671, 0.3452586531639099, 0.5139342546463013, 0.4437817931175232, 0.253437876701355, 0.338340163230896, 0.6512879133224487, 0.35085320472717285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1641924381256104})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6092811822891235})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4025837481021881})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.340289831161499})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30462974309921265})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2777211666107178})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2824622392654419})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.284676194190979})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2492465376853943})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2817334830760956})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2582046389579773})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2733907103538513})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2277568115234375}
