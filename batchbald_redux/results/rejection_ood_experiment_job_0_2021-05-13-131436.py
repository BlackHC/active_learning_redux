store = {}
store['timestamp']=1620908076
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=0']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=20
store['config']={'seed': 1234, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [41981, 28419, 16257, 55906, 49926, 16268, 46788, 6456, 11984, 13489], 'labels': [4, 8, 5, -1, 3, 5, 6, 6, 8, 8], 'scores': [0.5798690915107727, 0.7967948913574219, 0.5968843698501587, 0.6874239444732666, 0.8539624810218811, 0.5238154828548431, 0.7077624797821045, 0.6868482828140259, 0.5578749179840088, 0.7906135320663452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6355912685394287})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.1223273277282715})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.196366786956787})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.110318899154663})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7433, 'crossentropy': 1.5073380859375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0005064010620117})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9565363526344299})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9232338070869446})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [1948, 11599, 32221, 12625, 14817, 30290, 24195, 50659, 41515, 13258], 'labels': [8, 5, 0, 3, 0, 7, -1, 9, 3, 8], 'scores': [0.6708747744560242, 0.5390775203704834, 0.6052490472793579, 0.3678770065307617, 0.9099697470664978, 0.47315317392349243, 0.46978437900543213, 0.6372729539871216, 0.613676905632019, 0.43611472845077515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.748197317123413})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.130690813064575})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.223201274871826})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.393677234649658})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7501, 'crossentropy': 1.52726328125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.07149076461792})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.050825595855713})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0219494104385376})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [7322, 52125, 22543, 35279, 17989, 53193, 19294, 57245, 12024, 7779], 'labels': [3, 6, 8, 2, 9, 5, 4, 2, 3, 4], 'scores': [0.5673470497131348, 0.7081416845321655, 0.6495977640151978, 0.5203104019165039, 0.45328837633132935, 0.5540341138839722, 0.6805610060691833, 0.5976160764694214, 0.45341259241104126, 0.5872189998626709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2577338218688965})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.526862621307373})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.804260015487671})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6626042127609253})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8012, 'crossentropy': 1.17344970703125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9100062847137451})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.8071334362030029})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.8242698907852173})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [38376, 18114, 37918, 12305, 44350, 41002, 28371, 11025, 31546, 12223], 'labels': [6, 8, -1, 9, 3, 7, 3, 5, 2, 2], 'scores': [0.41677236557006836, 0.5214463472366333, 0.30189359188079834, 0.6748956441879272, 0.8417869210243225, 0.5669064521789551, 0.7367310523986816, 0.7083348035812378, 0.50493985414505, 0.6910239458084106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2128751277923584})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.465970516204834})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.416368007659912})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.7194836139678955})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7938, 'crossentropy': 1.09844267578125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9089323282241821})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.8558616042137146})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8141368627548218})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [25402, 12098, 5316, 50078, 22717, 12406, 24050, 46649, 9184, 24452], 'labels': [5, 4, 9, 9, 3, 9, 2, 8, -1, 3], 'scores': [0.5091168284416199, 0.39269542694091797, 0.5596901774406433, 0.50837242603302, 0.406890332698822, 0.5635926127433777, 0.5129148960113525, 0.49821847677230835, 0.35035014152526855, 0.4051784873008728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9300068020820618})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0514625310897827})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1000549793243408})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.4108598232269287})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.812285302734375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8261955976486206})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6943253874778748})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6809183359146118})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [24347, 20709, 52012, 41200, 46175, 8444, 2135, 56653, 31440, 19976], 'labels': [2, 8, 8, 8, 8, 7, 8, 7, 8, 3], 'scores': [0.5004291534423828, 0.4471083879470825, 0.6104023456573486, 0.45861560106277466, 0.39141952991485596, 0.3815511465072632, 0.4943612813949585, 0.47333604097366333, 0.537838339805603, 0.45820534229278564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.972083330154419})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8816392421722412})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8485946655273438})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.963420033454895})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0020251274108887})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.048593521118164})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8713, 'crossentropy': 0.825519921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7838242053985596})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6115891933441162})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5624951720237732})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.554766058921814})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5582849383354187})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [36254, 46286, 55691, 47507, 5324, 24409, 18187, 4058, 2166, 22533], 'labels': [-1, 2, -1, -1, 4, -1, 9, 8, 1, 1], 'scores': [0.5920702815055847, 0.4432567358016968, 0.3910769820213318, 0.4550480246543884, 0.506958544254303, 0.4032552242279053, 0.60100919008255, 0.7225463390350342, 0.4793255925178528, 0.4115109443664551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8501181602478027})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7113332748413086})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8314895629882812})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8566421866416931})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8495975732803345})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.649245654296875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6796495914459229})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.551419734954834})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5281160473823547})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5087903141975403})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [15058, 24589, 39320, 11964, 40584, 15261, 19369, 9428, 38567, 7557], 'labels': [4, 8, 6, 6, 9, 3, 0, 9, 4, 0], 'scores': [0.4330531060695648, 0.5163758993148804, 0.4426921606063843, 0.40981000661849976, 0.3847910165786743, 0.49117177724838257, 0.5237451791763306, 0.6033768653869629, 0.5720844268798828, 0.44635647535324097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7720947861671448})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.742385983467102})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7109293341636658})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8019792437553406})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8350809812545776})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8410751223564148})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.66622783203125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7267668843269348})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5467599630355835})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5431596040725708})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.48377978801727295})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4863632917404175})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [19939, 16290, 25257, 29694, 46640, 36686, 15947, 48409, 58491, 52646], 'labels': [-1, 4, -1, 7, 5, 6, -1, -1, -1, 9], 'scores': [0.5508652925491333, 0.6881330609321594, 0.3834261894226074, 0.4006791114807129, 0.734087347984314, 0.8336098790168762, 0.4365413784980774, 0.34181201457977295, 0.39088284969329834, 0.4232999086380005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.797094464302063})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7863035202026367})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7251062393188477})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8714301586151123})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9392577409744263})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9436386227607727})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9011, 'crossentropy': 0.6961287109375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7070038318634033})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5552819967269897})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.506689727306366})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5377058982849121})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4949522614479065})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [19662, 37912, 12663, 3719, 33161, 52978, 12984, 31535, 52511, 30177], 'labels': [-1, 3, 8, 2, 3, 0, 8, -1, -1, 7], 'scores': [0.5544160604476929, 0.5265419483184814, 0.7726714611053467, 0.6161288619041443, 0.5051963925361633, 0.5550322532653809, 0.5477002263069153, 0.5293877124786377, 0.2763972878456116, 0.5565572381019592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.902677059173584})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6956554651260376})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6998392343521118})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.867485761642456})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9111123085021973})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9034, 'crossentropy': 0.60917119140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7324139475822449})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5911787152290344})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5795297622680664})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5488747358322144})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [55540, 44345, 23546, 28013, 43057, 45032, 13047, 30775, 45118, 12748], 'labels': [2, 4, 5, 2, 9, 1, 6, 8, 5, 0], 'scores': [0.5513601303100586, 0.5519958138465881, 0.5983830690383911, 0.3808465898036957, 0.46137160062789917, 0.5687643885612488, 0.4685670733451843, 0.3746275305747986, 0.5217624306678772, 0.42607665061950684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8010984659194946})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6493476629257202})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.789269208908081})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7112572193145752})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7632921934127808})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.61081083984375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7606085538864136})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5627001523971558})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5001283288002014})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5637113451957703})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [644, 18003, 52025, 38560, 49658, 43648, 18102, 670, 48952, 37270], 'labels': [7, 2, 2, 2, 5, 5, 0, 3, 7, 5], 'scores': [0.4816848039627075, 0.4330388903617859, 0.5177949070930481, 0.306050181388855, 0.5891793370246887, 0.6133273839950562, 0.3902178406715393, 0.5299506783485413, 0.44850218296051025, 0.549708366394043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8231030106544495})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.618862509727478})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6484595537185669})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6614069938659668})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6630232334136963})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.584042236328125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7722997069358826})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5681668519973755})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5322202444076538})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5165078639984131})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [26703, 29027, 11675, 57369, 12188, 49058, 54885, 31706, 42201, 54556], 'labels': [9, 5, 0, 5, 7, 7, 6, 8, 3, 2], 'scores': [0.40589380264282227, 0.3098694682121277, 0.45156610012054443, 0.28084874153137207, 0.6157554388046265, 0.517631471157074, 0.5095287561416626, 0.5519419312477112, 0.47765856981277466, 0.553824245929718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9521200656890869})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.682809591293335})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6335139274597168})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7333225011825562})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.751010537147522})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8237566351890564})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.557855126953125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6640850901603699})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5100979804992676})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4846099019050598})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4250301718711853})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4469224810600281})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [3336, 42317, 39545, 28853, 35842, 18519, 50757, 6405, 28412, 52035], 'labels': [3, 5, 2, 9, 7, 4, -1, -1, 0, 3], 'scores': [0.6278442144393921, 0.5861050486564636, 0.7242829203605652, 0.4297716021537781, 0.39957499504089355, 0.44503986835479736, 0.46417009830474854, 0.4223670959472656, 0.48894211649894714, 0.6735547184944153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8205548524856567})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5919065475463867})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5786914825439453})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5764082670211792})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6267302632331848})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6067602634429932})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6143362522125244})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.5294677734375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7003321647644043})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.513634204864502})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.44437605142593384})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4381897449493408})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4384952485561371})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.3862159848213196})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [47142, 31148, 33412, 28196, 45101, 57254, 4873, 11708, 47260, 55388], 'labels': [2, 2, 3, -1, 5, 6, 8, 3, 6, -1], 'scores': [0.6273165941238403, 0.5897777676582336, 0.34581097960472107, 0.505706787109375, 0.5164086222648621, 0.5735578536987305, 0.6496251821517944, 0.5914658308029175, 0.4367067217826843, 0.3169444799423218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8175557851791382})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5447455644607544})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5891056060791016})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6155229806900024})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6135740280151367})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.499633447265625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7547348737716675})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5849138498306274})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48639899492263794})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4926277995109558})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [23112, 50509, 43931, 20322, 47655, 49235, 42690, 41291, 55011, 39445], 'labels': [8, 6, -1, 1, 3, 7, 1, 0, 2, 3], 'scores': [0.571800947189331, 0.2965323328971863, 0.25223565101623535, 0.5269609093666077, 0.48206114768981934, 0.23150479793548584, 0.41322261095046997, 0.4729727506637573, 0.4154622554779053, 0.3821483850479126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.874906063079834})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5389710664749146})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.543290376663208})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5286906361579895})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5480364561080933})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5758953094482422})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5843542814254761})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.48647333984375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7321667671203613})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5138798952102661})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4485362768173218})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40903812646865845})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.39551955461502075})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.39354953169822693})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [34189, 49529, 56795, 52053, 4156, 12116, 27754, 23138, 28388, 21880], 'labels': [-1, 3, 2, -1, 3, -1, 2, 2, 2, 2], 'scores': [0.4696180820465088, 0.3418234586715698, 0.44730594754219055, 0.5116082429885864, 0.50213623046875, 0.38059520721435547, 0.5482878088951111, 0.5342352390289307, 0.5268053412437439, 0.5675238966941833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9323449730873108})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5508610010147095})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49993932247161865})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5432889461517334})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5526062250137329})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.503872811794281})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.486002734375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7334052324295044})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5150940418243408})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45934629440307617})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4509594440460205})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43411093950271606})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [14651, 33026, 10409, 13334, 43034, 15754, 14266, 14665, 28838, 24086], 'labels': [-1, -1, 1, -1, -1, -1, 3, 8, 9, -1], 'scores': [0.3702516555786133, 0.5245687961578369, 0.3164823055267334, 0.3444579243659973, 0.39708471298217773, 0.5649778842926025, 0.5231559872627258, 0.654680609703064, 0.3595273494720459, 0.40365874767303467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9080706834793091})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5246776342391968})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6033025979995728})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5276780724525452})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.553634524345398})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.474025048828125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7407363653182983})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5325140953063965})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5044370293617249})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46302086114883423})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [22343, 24740, 49545, 25376, 11091, 34542, 45438, 26252, 14015, 38256], 'labels': [-1, -1, 8, -1, 0, 1, -1, 6, 9, 2], 'scores': [0.2699747085571289, 0.458920955657959, 0.4780687093734741, 0.2587391138076782, 0.31089144945144653, 0.35000622272491455, 0.4454681873321533, 0.38917917013168335, 0.3288804292678833, 0.4881508946418762]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8898202180862427})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5124161839485168})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5003157258033752})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5065887570381165})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46410709619522095})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.561132550239563})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4721812605857849})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5131222605705261})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.443021728515625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7524911761283875})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.47608447074890137})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3674710690975189})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37098926305770874})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.369594007730484})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3670693635940552})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3596625328063965})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [23140, 15333, 1707, 22409, 4557, 35025, 19468, 52641, 37472, 35418], 'labels': [7, -1, -1, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.7005150318145752, 0.4834277629852295, 0.5242152214050293, 0.3636378049850464, 0.42439669370651245, 0.502615749835968, 0.37964707612991333, 0.4817161560058594, 0.4671062231063843, 0.3532235026359558]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.781387448310852})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5179415345191956})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4930325746536255})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49891141057014465})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5043634176254272})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48273420333862305})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5787227153778076})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5501559972763062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4815731942653656})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5450447797775269})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49164631962776184})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.563602089881897})
store['active_learning_steps'][20]['training']['best_epoch']=9
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.946, 'crossentropy': 0.41339365234375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7230955362319946})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4639067053794861})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39384812116622925})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35790854692459106})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3501747250556946})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3205524981021881})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33111199736595154})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30057746171951294})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30689120292663574})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31714898347854614})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3029661178588867})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [59875, 38150, 134, 33882, 59208, 36744, 7485, 16951, 14580, 37450], 'labels': [-1, 4, 1, -1, -1, 1, -1, 8, 9, 4], 'scores': [0.5364254713058472, 0.5713742971420288, 0.7495952248573303, 0.37474286556243896, 0.45234379172325134, 0.7329931855201721, 0.4721582531929016, 0.40697091817855835, 0.42283278703689575, 0.5443186163902283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.855389416217804})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5255969762802124})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4926998019218445})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4729940593242645})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4886500835418701})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4816637635231018})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.570008397102356})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.420139013671875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7506211996078491})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4928149878978729})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4053214490413666})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3779376149177551})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38000214099884033})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37560003995895386})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [35503, 26756, 7900, 7168, 47673, 34244, 8693, 40208, 50461, 19945], 'labels': [-1, 7, 5, 8, -1, -1, 3, -1, 7, 5], 'scores': [0.3270125389099121, 0.5341010689735413, 0.44519469141960144, 0.5591840147972107, 0.2526780366897583, 0.3860666751861572, 0.4705529808998108, 0.29309165477752686, 0.56379234790802, 0.5083574652671814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8165633082389832})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45741719007492065})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4622964859008789})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4698248505592346})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41609668731689453})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47777679562568665})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.410713791847229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38496625423431396})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43385645747184753})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4764884114265442})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43453437089920044})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.3605264404296875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7217402458190918})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.43799272179603577})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3681667447090149})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34348517656326294})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33001309633255005})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34468209743499756})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31956759095191956})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3032784163951874})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3042553663253784})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2885945439338684})
store['active_learning_steps'][22]['eval_training']['best_epoch']=10
store['active_learning_steps'][22]['acquisition']={'indices': [40688, 59439, 11494, 3613, 44661, 12327, 22505, 30515, 15174, 21264], 'labels': [-1, 0, -1, -1, 1, -1, 9, 3, -1, -1], 'scores': [0.5589426755905151, 0.380601167678833, 0.3639335036277771, 0.6040606498718262, 0.4651912748813629, 0.5739652514457703, 0.4262382984161377, 0.42679524421691895, 0.39523613452911377, 0.37971770763397217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8349335789680481})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4219364821910858})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44453680515289307})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4072418212890625})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3944636583328247})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45313796401023865})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43158066272735596})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43141958117485046})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9517, 'crossentropy': 0.36743740234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.789251446723938})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4517673850059509})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41910219192504883})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36763766407966614})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.352469265460968})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.31026262044906616})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32040339708328247})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [30047, 50369, 29570, 6446, 42897, 15878, 56021, 48520, 48742, 59297], 'labels': [1, 3, 0, -1, 7, -1, -1, 4, -1, 1], 'scores': [0.5462630391120911, 0.43466466665267944, 0.45641863346099854, 0.3013582229614258, 0.3101425766944885, 0.46551841497421265, 0.28553497791290283, 0.3277176320552826, 0.474612832069397, 0.6711089015007019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9347355365753174})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46560394763946533})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3848647475242615})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41600245237350464})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4348570704460144})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4473613500595093})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9501, 'crossentropy': 0.3617375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7620729804039001})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47705310583114624})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3887128233909607})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38354557752609253})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34827613830566406})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [14484, 14062, 54083, 37588, 34495, 17469, 47662, 14337, 55496, 37770], 'labels': [2, 8, 0, 2, 2, -1, 9, -1, 9, 7], 'scores': [0.5380378365516663, 0.49168717861175537, 0.47222912311553955, 0.5702264904975891, 0.47564834356307983, 0.33438611030578613, 0.3515286445617676, 0.31790316104888916, 0.4084049463272095, 0.2842676043510437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8747166395187378})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4601263999938965})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4044151306152344})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.363031268119812})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36441606283187866})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36707162857055664})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3750365376472473})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.348209716796875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7982189655303955})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47632041573524475})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4067898690700531})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37008053064346313})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38181251287460327})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36058294773101807})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [4285, 24637, 37432, 58720, 52550, 3289, 29501, 46133, 2054, 360], 'labels': [-1, 4, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.3439664840698242, 0.47364699840545654, 0.525112509727478, 0.6062608361244202, 0.5451034307479858, 0.39857029914855957, 0.45719438791275024, 0.5591968297958374, 0.3197101354598999, 0.43388545513153076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8854806423187256})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4878832697868347})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40839067101478577})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3886367380619049})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4473523795604706})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4607715606689453})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44878149032592773})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.951, 'crossentropy': 0.3697593994140625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7855597734451294})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41317179799079895})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38530147075653076})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36891603469848633})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37453293800354004})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30512499809265137})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [45084, 42175, 41481, 57687, 56999, 50651, 58840, 57589, 48093, 278], 'labels': [-1, -1, -1, -1, 5, -1, -1, -1, -1, 5], 'scores': [0.4802957773208618, 0.34717392921447754, 0.23788118362426758, 0.2560691833496094, 0.5681043863296509, 0.3647122383117676, 0.5404659509658813, 0.3018038272857666, 0.29286670684814453, 0.46945345401763916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9788956642150879})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48897433280944824})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4315529465675354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4257452189922333})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4193410873413086})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47158682346343994})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41900861263275146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4361191689968109})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4525085985660553})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4785177409648895})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9541, 'crossentropy': 0.389253076171875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7225134372711182})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4570029079914093})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35586434602737427})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33885273337364197})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3269931972026825})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3018118739128113})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32136672735214233})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3160364627838135})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2911020517349243})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [54739, 25604, 57493, 29730, 14295, 15767, 39674, 30553, 33812, 52788], 'labels': [-1, 4, -1, 7, 2, -1, 4, -1, 6, -1], 'scores': [0.3604707717895508, 0.6168249845504761, 0.39935189485549927, 0.5605687499046326, 0.5928659439086914, 0.3548870086669922, 0.5821458697319031, 0.459087610244751, 0.6360167860984802, 0.30457139015197754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9022226333618164})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.495068222284317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4463505744934082})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3935452699661255})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3803137242794037})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4265766441822052})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3993847966194153})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3752322793006897})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45732271671295166})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4435909390449524})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4143427014350891})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.369571484375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6615684628486633})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3998492360115051})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3378760516643524})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30369997024536133})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2863926291465759})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2881619930267334})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2819330096244812})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2811264991760254})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2754923105239868})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2724398970603943})
store['active_learning_steps'][28]['eval_training']['best_epoch']=10
store['active_learning_steps'][28]['acquisition']={'indices': [37720, 22553, 43504, 59280, 6466, 59314, 42425, 49494, 46087, 56172], 'labels': [8, -1, -1, 8, 2, 9, 4, -1, -1, -1], 'scores': [0.6443955302238464, 0.3466308116912842, 0.4324120283126831, 0.5163230895996094, 0.6246569156646729, 0.5813890695571899, 0.47644539177417755, 0.4640693664550781, 0.4826662540435791, 0.4098772406578064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9861940741539001})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5181611776351929})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4090287387371063})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42707329988479614})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42612969875335693})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4324023723602295})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9502, 'crossentropy': 0.372175390625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8075822591781616})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5052502155303955})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41223961114883423})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38752633333206177})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37480658292770386})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [25868, 40889, 3210, 52952, 29439, 45451, 41617, 18029, 828, 1568], 'labels': [-1, -1, -1, 7, -1, -1, -1, 0, 4, 4], 'scores': [0.5627167224884033, 0.19867610931396484, 0.44725120067596436, 0.20835387706756592, 0.5434916615486145, 0.3673180341720581, 0.39533525705337524, 0.39428025484085083, 0.5141942501068115, 0.4504709243774414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8650996685028076})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45420920848846436})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3690875172615051})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3868667483329773})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39458078145980835})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35925400257110596})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3673914670944214})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4025791883468628})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.424255907535553})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9554, 'crossentropy': 0.3640404541015625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6959928274154663})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43213385343551636})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35058432817459106})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3190443515777588})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3404834270477295})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2937929630279541})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3094441890716553})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29023993015289307})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [24575, 34495, 21554, 8768, 5034, 49863, 21671, 57087, 8726, 18291], 'labels': [-1, -1, -1, -1, -1, -1, -1, 8, -1, -1], 'scores': [0.34752506017684937, 0.3858751058578491, 0.37118077278137207, 0.44076764583587646, 0.2858870029449463, 0.3098750114440918, 0.41546499729156494, 0.4406067132949829, 0.4417308568954468, 0.42986321449279785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8517323732376099})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4675087034702301})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4250769019126892})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3400696814060211})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.355419784784317})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3893815875053406})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3307415544986725})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3951112627983093})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4451240003108978})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4133889973163605})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.321576318359375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8100957274436951})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47275224328041077})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36153361201286316})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33443683385849})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3213396370410919})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2865673899650574})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31081622838974})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2825753390789032})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2671959102153778})
store['active_learning_steps'][31]['eval_training']['best_epoch']=9
store['active_learning_steps'][31]['acquisition']={'indices': [37149, 42838, 9290, 41578, 25314, 56454, 43876, 54030, 16658, 50517], 'labels': [-1, 9, 9, 8, -1, 0, -1, 8, 8, -1], 'scores': [0.34881412982940674, 0.46372222900390625, 0.46473175287246704, 0.46135419607162476, 0.25758469104766846, 0.542087972164154, 0.35103511810302734, 0.35277944803237915, 0.5033319592475891, 0.43437838554382324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9418460726737976})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4711464047431946})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3347449004650116})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.360248863697052})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3532679080963135})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42160269618034363})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3611279052734375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6901336908340454})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4682942032814026})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4275190532207489})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37385067343711853})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3457474708557129})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [35384, 24432, 26436, 38626, 49094, 250, 17222, 39297, 37397, 49537], 'labels': [-1, -1, -1, 5, 5, 3, 8, 1, 3, 2], 'scores': [0.4455595016479492, 0.26956450939178467, 0.2300269603729248, 0.46525007486343384, 0.3980047106742859, 0.375418484210968, 0.34923529624938965, 0.2670987844467163, 0.5630447864532471, 0.6016027331352234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.010000228881836})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.48290687799453735})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3736070990562439})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3430686593055725})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3545794188976288})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37902307510375977})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32074612379074097})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3583464026451111})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36088985204696655})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3904363811016083})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.327159619140625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8632654547691345})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44109833240509033})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3496723175048828})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33892524242401123})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.282283216714859})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3093482255935669})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26196587085723877})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25824037194252014})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2534743547439575})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [54036, 55244, 10147, 5073, 17966, 13745, 11597, 32640, 48735, 21012], 'labels': [9, 7, -1, -1, -1, 3, -1, 2, -1, 2], 'scores': [0.367959201335907, 0.49758094549179077, 0.40575718879699707, 0.37398457527160645, 0.44407451152801514, 0.18808704614639282, 0.4562600255012512, 0.4652566909790039, 0.6748170852661133, 0.6106615364551544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0997905731201172})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5446768999099731})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39293569326400757})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3967055082321167})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.397294282913208})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37501397728919983})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4317639470100403})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3828338384628296})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4496488571166992})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9557, 'crossentropy': 0.3585478759765625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.793342649936676})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4938220977783203})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38667047023773193})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33818918466567993})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31649142503738403})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31858599185943604})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3147902488708496})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2808731198310852})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [5647, 10162, 7971, 15696, 3811, 58114, 7695, 12372, 14649, 12934], 'labels': [2, -1, -1, -1, 1, 2, 2, 2, 0, 8], 'scores': [0.5555565059185028, 0.3356403112411499, 0.5997387766838074, 0.5105075836181641, 0.5253149271011353, 0.7184582948684692, 0.579714298248291, 0.526963859796524, 0.3259239196777344, 0.5263729691505432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9639082551002502})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5159655809402466})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.422793984413147})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3637339174747467})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3444706201553345})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35938793420791626})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37798893451690674})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3465723693370819})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.316150341796875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7569043636322021})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4132128357887268})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33781659603118896})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34016019105911255})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33911818265914917})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3197553753852844})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2923109233379364})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [26742, 52780, 18049, 27079, 5315, 17748, 40410, 33733, 15771, 49242], 'labels': [7, -1, 3, 5, 3, -1, -1, -1, 5, 7], 'scores': [0.5118969678878784, 0.15861034393310547, 0.504449725151062, 0.34320005774497986, 0.6187854409217834, 0.40326356887817383, 0.33889830112457275, 0.4120621681213379, 0.5520780682563782, 0.3920666575431824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.951116681098938})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4875430762767792})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4102925658226013})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34107163548469543})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31259194016456604})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36479878425598145})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.371407151222229})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3483956456184387})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.3080985107421875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7764527797698975})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46800440549850464})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3713507652282715})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35286515951156616})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3448980152606964})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3095402419567108})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3130836486816406})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [16606, 53133, 29923, 25105, 2957, 55958, 29250, 2662, 44, 5335], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.5108366012573242, 0.33477115631103516, 0.47322845458984375, 0.30513787269592285, 0.36801910400390625, 0.37975430488586426, 0.32879638671875, 0.36469876766204834, 0.3929424285888672, 0.31443631649017334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0858094692230225})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4785797894001007})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39577150344848633})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34987103939056396})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35321786999702454})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.333278089761734})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3414708077907562})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3779938220977783})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37818223237991333})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.3132282958984375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7219340801239014})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4420560598373413})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3573746681213379})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3397066593170166})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31173667311668396})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29981523752212524})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.291393518447876})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3030446767807007})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [148, 38932, 49009, 16972, 13841, 58588, 37223, 59747, 49714, 42437], 'labels': [7, 5, 2, -1, -1, -1, -1, 5, 9, -1], 'scores': [0.4246099591255188, 0.4429553747177124, 0.5996557474136353, 0.45366787910461426, 0.2724039554595947, 0.34597694873809814, 0.4391871690750122, 0.8126052618026733, 0.49652114510536194, 0.46279555559158325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9182319641113281})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5209196209907532})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3821874260902405})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3375404179096222})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33064597845077515})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3093559145927429})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3309987485408783})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33753538131713867})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31820520758628845})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3198108642578125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8090524673461914})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4620668888092041})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36322593688964844})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3330863118171692})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30083853006362915})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28263044357299805})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30393970012664795})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28816133737564087})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [788, 20554, 48801, 29282, 37441, 59166, 14619, 26538, 58628, 58050], 'labels': [9, -1, -1, -1, 1, -1, 3, 5, -1, 6], 'scores': [0.49460411071777344, 0.48758262395858765, 0.5042642951011658, 0.4052518606185913, 0.4929352402687073, 0.4983198642730713, 0.45888251066207886, 0.5977824330329895, 0.5485390424728394, 0.35138657689094543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0594019889831543})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49281060695648193})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4317847490310669})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32571160793304443})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39201200008392334})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33770552277565})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34960734844207764})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.31395458984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8226532936096191})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5455843210220337})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42295461893081665})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3698742389678955})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3363091051578522})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37272119522094727})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
