store = {}
store['timestamp']=1620908044
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=2']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=20
store['config']={'seed': 1237, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.198180675506592})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.1555979251861572})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.2054734230041504})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6942601203918457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.9050188064575195})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7039, 'crossentropy': 2.0665068359375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1332035064697266})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0794700384140015})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0738472938537598})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1270103454589844})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [21758, 11575, 2363, 35481, 14480, 3690, 48055, 6276, 25430, 31682], 'labels': [7, 8, 5, 0, 8, 8, 8, 5, 6, 5], 'scores': [0.8126699924468994, 0.8059306740760803, 0.6581794023513794, 0.9628654718399048, 0.7293745279312134, 0.9265619516372681, 0.828623354434967, 0.9447749853134155, 0.8187962770462036, 0.6168034672737122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.5651977062225342})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.8299864530563354})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.177867889404297})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.1083950996398926})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7472, 'crossentropy': 1.53489228515625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9942127466201782})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.955019474029541})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9801942706108093})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [56004, 5573, 37503, 40588, 20853, 18992, 42392, 34020, 13464, 31456], 'labels': [8, 3, 3, 3, 5, 3, 5, 8, 0, 9], 'scores': [0.905135989189148, 0.4686681926250458, 0.5331235527992249, 0.6223965287208557, 0.5615962743759155, 0.447695255279541, 0.7273262143135071, 0.6277303695678711, 0.6592990159988403, 0.7683140635490417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3604350090026855})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2946691513061523})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.5176162719726562})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5231090784072876})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.6784671545028687})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.805, 'crossentropy': 1.30198818359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.849456787109375})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.7960721254348755})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.7731636762619019})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.743926465511322})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [39398, 22610, 25173, 19369, 59522, 10229, 53570, 41036, 13030, 109], 'labels': [2, 9, -1, 0, 4, -1, -1, 4, 0, -1], 'scores': [0.6256583333015442, 0.5306309759616852, 0.5636135339736938, 0.6840027570724487, 0.5428725481033325, 0.5743430852890015, 0.6140124797821045, 0.4965561032295227, 0.897537887096405, 0.7117140293121338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1094474792480469})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.4153342247009277})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.240128993988037})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4050540924072266})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8189, 'crossentropy': 0.9944736328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8475205898284912})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7665931582450867})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7361688613891602})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [4949, 30107, 53386, 44031, 34437, 4678, 14484, 54044, 47842, 29258], 'labels': [9, 2, 9, 1, 8, 9, 2, 5, 2, 4], 'scores': [0.38903188705444336, 0.43570441007614136, 0.49506300687789917, 0.3360546827316284, 0.555009663105011, 0.3640215992927551, 0.683002233505249, 0.5191921591758728, 0.5048624277114868, 0.38570845127105713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9905929565429688})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0690417289733887})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1852843761444092})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1338244676589966})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8571, 'crossentropy': 0.87483515625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8270509839057922})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7627855539321899})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7268882989883423})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [11991, 19774, 5214, 30630, 4457, 36498, 635, 16638, 18346, 827], 'labels': [9, 0, -1, -1, 2, 7, 5, 2, 7, 9], 'scores': [0.45928341150283813, 0.3719092607498169, 0.40477144718170166, 0.2642907500267029, 0.5795314311981201, 0.4916020631790161, 0.5780906677246094, 0.579318642616272, 0.5030051469802856, 0.4192442297935486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.954643964767456})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1492040157318115})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1170854568481445})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2561464309692383})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8524, 'crossentropy': 0.84128525390625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8099591732025146})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7526217699050903})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.689659595489502})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [49312, 55912, 21779, 47628, 49992, 42793, 40212, 28209, 3890, 50449], 'labels': [3, 2, 5, 3, 5, 4, 2, 5, 2, 2], 'scores': [0.5335561037063599, 0.6518850326538086, 0.652278482913971, 0.5302908420562744, 0.7273091077804565, 0.610992968082428, 0.618716299533844, 0.5143151879310608, 0.636264443397522, 0.5169459581375122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8116875290870667})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8955899477005005})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9030920267105103})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9598627686500549})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.7263466796875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7661139965057373})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7417407035827637})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7119412422180176})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [28371, 58470, 53450, 42383, 46397, 11550, 4373, 0, 38565, 48004], 'labels': [3, 9, -1, 8, -1, 9, 3, 5, 3, 5], 'scores': [0.6420924663543701, 0.6266424655914307, 0.33415520191192627, 0.6547901034355164, 0.39504730701446533, 0.48495590686798096, 0.403444766998291, 0.588092565536499, 0.6118783950805664, 0.6473527550697327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8590160608291626})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8030350804328918})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9071420431137085})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9168591499328613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0663139820098877})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.6808662109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6995127201080322})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6093579530715942})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5445418357849121})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5609667301177979})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [57150, 15815, 42650, 29212, 40593, 40825, 12277, 44932, 21086, 13061], 'labels': [7, 3, 7, 7, 4, 0, 9, 6, 7, 2], 'scores': [0.5521886348724365, 0.41376447677612305, 0.3824840784072876, 0.4725828170776367, 0.4710313081741333, 0.5654265284538269, 0.5015270113945007, 0.5862961411476135, 0.4199063777923584, 0.564635694026947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8509330153465271})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8893231153488159})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0439729690551758})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9321373701095581})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8587, 'crossentropy': 0.797683349609375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9108927249908447})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8381059765815735})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7730900049209595})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [27027, 56674, 27891, 47403, 59468, 30539, 13011, 18240, 13333, 57772], 'labels': [8, 0, 8, 9, 7, 8, 6, 3, 7, 8], 'scores': [0.455233097076416, 0.4086545705795288, 0.27238988876342773, 0.24722206592559814, 0.408846914768219, 0.3623545169830322, 0.44825756549835205, 0.3828244209289551, 0.2829306721687317, 0.37102723121643066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.766506552696228})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6797167062759399})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7481810450553894})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7430553436279297})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8208990097045898})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.576265234375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6723650693893433})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5413888692855835})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5225110650062561})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.527307391166687})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [58258, 8261, 6272, 50992, 28226, 1293, 16971, 37466, 9762, 12650], 'labels': [7, -1, 9, 7, 8, 1, 1, -1, 8, 5], 'scores': [0.4240589141845703, 0.4096437692642212, 0.4563184976577759, 0.3304963707923889, 0.616190493106842, 0.24174946546554565, 0.440687358379364, 0.25022435188293457, 0.43627792596817017, 0.47785061597824097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8257660269737244})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7532457709312439})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8311874866485596})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8329677581787109})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8573942184448242})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.636985498046875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7473713159561157})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6313802003860474})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5043050050735474})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5232542753219604})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [10126, 49683, 48811, 6238, 2226, 11563, 33704, 40707, 54388, 19338], 'labels': [-1, 4, 2, 9, -1, -1, 6, -1, 1, -1], 'scores': [0.3901192545890808, 0.5158003568649292, 0.6254044771194458, 0.4705631732940674, 0.5549805760383606, 0.4821532964706421, 0.44749653339385986, 0.4021678566932678, 0.4794628620147705, 0.38576990365982056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7417570352554321})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6806292533874512})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6725901365280151})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.786988377571106})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7286956906318665})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8701468706130981})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.56566875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.696395993232727})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5263839960098267})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5122869610786438})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.502579927444458})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4789123833179474})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [46727, 13079, 17714, 9290, 43893, 42504, 19430, 35834, 14728, 19396], 'labels': [2, 8, 7, 9, -1, 8, 5, -1, 8, 5], 'scores': [0.4823485016822815, 0.5506734251976013, 0.24198320508003235, 0.628155529499054, 0.28332221508026123, 0.672158420085907, 0.433876633644104, 0.2409663200378418, 0.6468026638031006, 0.7228150367736816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8264582753181458})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6656663417816162})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7040201425552368})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7293452024459839})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8843121528625488})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.577350634765625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7937158942222595})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5849522352218628})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5665359497070312})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5636515617370605})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [55368, 28954, 43620, 17079, 35338, 33388, 8765, 8736, 26444, 10992], 'labels': [8, 2, -1, 6, 8, 8, 3, 9, 1, 0], 'scores': [0.4309382438659668, 0.4846418499946594, 0.2801166772842407, 0.5776691436767578, 0.3500075340270996, 0.4246827960014343, 0.3667445182800293, 0.43929845094680786, 0.5545989274978638, 0.38939833641052246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8548742532730103})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6944808959960938})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6762464046478271})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6570919752120972})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7447918653488159})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7553962469100952})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8134503364562988})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.54962421875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7641408443450928})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5468281507492065})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4696105718612671})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.465811550617218})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4251263737678528})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4266766905784607})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [59271, 41299, 34819, 52053, 10930, 50348, 54019, 7498, 23467, 27226], 'labels': [3, 3, 8, -1, -1, 2, -1, 5, 9, 9], 'scores': [0.52928027510643, 0.638556957244873, 0.7515051960945129, 0.5172523260116577, 0.30780404806137085, 0.6400068402290344, 0.47406840324401855, 0.3647505044937134, 0.4766647219657898, 0.5494022369384766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8243643045425415})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5913926362991333})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5461618304252625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5568971633911133})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6596801280975342})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5668483972549438})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.47340283203125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7663137912750244})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5354651212692261})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4743023216724396})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4922143220901489})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4716157913208008})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [42287, 5173, 18693, 29248, 51570, 14825, 21517, 50258, 3030, 35578], 'labels': [5, -1, -1, 5, 6, 3, 4, -1, 9, 6], 'scores': [0.5127735733985901, 0.2766813039779663, 0.2700001001358032, 0.32756927609443665, 0.511027604341507, 0.44561076164245605, 0.3420732617378235, 0.2883484363555908, 0.5464994311332703, 0.5055333375930786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.851914644241333})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5771594643592834})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5593629479408264})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6979644298553467})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5912129878997803})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6210780739784241})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.482978076171875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6525865793228149})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5342239141464233})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4554431438446045})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4623732566833496})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45128095149993896})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [57308, 46736, 49049, 50433, 25596, 9476, 6279, 3824, 22866, 24567], 'labels': [3, 3, -1, 4, 1, -1, 0, 3, 5, -1], 'scores': [0.5014864206314087, 0.45277106761932373, 0.32592999935150146, 0.4937818646430969, 0.33148205280303955, 0.42848217487335205, 0.41221463680267334, 0.5263501405715942, 0.4845666289329529, 0.36174869537353516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9342803955078125})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6618732213973999})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5618098974227905})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6055976152420044})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6323122382164001})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6055222749710083})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.527359423828125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7707408666610718})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5258287191390991})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5211265683174133})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4503013789653778})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47489526867866516})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [21402, 26358, 46017, 14093, 5691, 18480, 623, 39304, 30856, 41371], 'labels': [-1, 3, 0, 8, 1, 2, 6, 4, 6, 0], 'scores': [0.2864201068878174, 0.5487087368965149, 0.6317983269691467, 0.5100247859954834, 0.4816722869873047, 0.3799130916595459, 0.3832749128341675, 0.43838053941726685, 0.5220198035240173, 0.596657395362854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8793063163757324})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5842703580856323})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5579982995986938})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6764545440673828})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6361432075500488})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6067781448364258})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.52562880859375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6976531744003296})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5018479824066162})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.47572898864746094})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.46765631437301636})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4732467830181122})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [9279, 55245, 326, 44095, 36375, 36861, 28953, 9435, 15963, 26150], 'labels': [3, -1, -1, 2, -1, 8, -1, -1, 8, 5], 'scores': [0.5210767388343811, 0.47335952520370483, 0.5056871175765991, 0.5595037937164307, 0.32258981466293335, 0.5748463273048401, 0.42529046535491943, 0.39903438091278076, 0.7042317390441895, 0.6487118601799011]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8433054685592651})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5738823413848877})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5733778476715088})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5902570486068726})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5696578025817871})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7156713604927063})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5870881676673889})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6397137641906738})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.4934681640625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7720478773117065})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4590685963630676})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4375546872615814})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42599284648895264})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40257543325424194})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3760468661785126})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3991621732711792})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [42209, 23112, 13347, 16800, 26673, 37567, 29110, 20828, 22147, 33096], 'labels': [9, 8, 0, -1, -1, 5, -1, -1, 5, -1], 'scores': [0.4989558458328247, 0.5437518358230591, 0.5008034110069275, 0.39791882038116455, 0.2930278778076172, 0.690120279788971, 0.5572506189346313, 0.39873480796813965, 0.4436240494251251, 0.26843082904815674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.922890305519104})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5200722813606262})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5138545036315918})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48487722873687744})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.566277027130127})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5726698637008667})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5985298156738281})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.4077343017578125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7614045739173889})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46895191073417664})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42063120007514954})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.43339288234710693})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.39268749952316284})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.375085711479187})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [24424, 2737, 47568, 24426, 26389, 622, 38331, 14098, 28218, 55410], 'labels': [1, -1, -1, 5, 0, -1, -1, -1, -1, -1], 'scores': [0.6348260641098022, 0.3603999614715576, 0.36864209175109863, 0.4895269572734833, 0.5161529779434204, 0.30928468704223633, 0.3009161949157715, 0.3348119258880615, 0.4744468927383423, 0.467496395111084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9379479885101318})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5197303295135498})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5672885775566101})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5810985565185547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6137964725494385})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9267, 'crossentropy': 0.483351904296875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7219381928443909})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5158059000968933})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5375179052352905})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.49429550766944885})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [13538, 5616, 16769, 10438, 37386, 21766, 28853, 19988, 16909, 40894], 'labels': [5, 3, 6, 9, 2, 0, 9, 8, 2, 6], 'scores': [0.5852166414260864, 0.26407772302627563, 0.2448209524154663, 0.2957206964492798, 0.34347695112228394, 0.29247891902923584, 0.23689967393875122, 0.3916487693786621, 0.47087907791137695, 0.3365507125854492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.980242133140564})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6500053405761719})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4868774116039276})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5396974086761475})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5677200555801392})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5903616547584534})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.444747412109375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6741432547569275})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5429806709289551})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4507986307144165})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.44876712560653687})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43197983503341675})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [3768, 659, 2426, 47066, 1143, 134, 9081, 37816, 32393, 20037], 'labels': [5, 3, 1, -1, 2, 1, 9, 1, 5, 8], 'scores': [0.5506182312965393, 0.47769641876220703, 0.45803457498550415, 0.4789137840270996, 0.42413127422332764, 0.5091969966888428, 0.5238101482391357, 0.4685248136520386, 0.4718783497810364, 0.601618230342865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9481284618377686})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5474386215209961})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4996369481086731})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5635461807250977})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5124667882919312})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.542719841003418})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.406901953125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7654293775558472})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5439823865890503})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45694783329963684})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4096227288246155})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3997159004211426})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [56503, 966, 37352, 58661, 14679, 3738, 35952, 29179, 52838, 29132], 'labels': [-1, 3, 9, -1, 8, 4, 4, 8, 4, 8], 'scores': [0.2942895293235779, 0.4664255976676941, 0.3811134099960327, 0.37217211723327637, 0.4975045323371887, 0.43777990341186523, 0.47027117013931274, 0.37605297565460205, 0.397854745388031, 0.4730547070503235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9091264009475708})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5692633390426636})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5422481298446655})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.495901882648468})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5628949999809265})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5457690954208374})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5806374549865723})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9395, 'crossentropy': 0.445619189453125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7369518280029297})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5371369123458862})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4984346330165863})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43102404475212097})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4112067222595215})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3919578492641449})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [15817, 37460, 9912, 32022, 57506, 49607, 59388, 3470, 39305, 31108], 'labels': [8, 8, 2, 2, 2, 3, -1, 2, -1, 3], 'scores': [0.265365332365036, 0.5748618841171265, 0.5812376141548157, 0.6431742906570435, 0.5567589402198792, 0.6705997586250305, 0.2997362017631531, 0.4367644190788269, 0.44083893299102783, 0.4096094071865082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9533788561820984})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.592488169670105})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4745100736618042})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4804233908653259})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44541090726852417})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5123640298843384})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4792636036872864})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4974237084388733})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.4218203125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7448256611824036})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4803508520126343})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4181140065193176})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38837844133377075})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.360548198223114})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.401927649974823})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35707640647888184})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [39427, 41319, 29725, 56586, 418, 16362, 51231, 25798, 32426, 51939], 'labels': [5, 4, 6, 5, 8, -1, 5, 6, 8, -1], 'scores': [0.3992418646812439, 0.4062652587890625, 0.7662103176116943, 0.34364041686058044, 0.3414562940597534, 0.33708226680755615, 0.5619329810142517, 0.6069676876068115, 0.4570234417915344, 0.5034542083740234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8661671876907349})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5515966415405273})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4777703285217285})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43342599272727966})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45404553413391113})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45239949226379395})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5006905794143677})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.3594083984375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.744385838508606})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4898477792739868})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4199897050857544})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36804041266441345})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3822551369667053})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3743398189544678})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [8409, 43575, 50665, 53585, 1600, 30027, 28539, 29018, 25480, 38617], 'labels': [-1, -1, -1, 2, 0, -1, -1, -1, -1, -1], 'scores': [0.45360398292541504, 0.4086742401123047, 0.3944661617279053, 0.650216281414032, 0.46082162857055664, 0.39564287662506104, 0.433315634727478, 0.43307191133499146, 0.43888378143310547, 0.2832900285720825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9942528605461121})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.551417350769043})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47050926089286804})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4526004195213318})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4420527517795563})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4437254071235657})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.416080504655838})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4372626841068268})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4626708924770355})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49678462743759155})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9519, 'crossentropy': 0.405952783203125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8241262435913086})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4708656370639801})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3859426975250244})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3573882579803467})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3552730083465576})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3295165002346039})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34402787685394287})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34406739473342896})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3330981433391571})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [14764, 54236, 32346, 5171, 49519, 24084, 47219, 21207, 57505, 58105], 'labels': [6, 1, 7, 2, 1, -1, 6, -1, 1, 4], 'scores': [0.46791666746139526, 0.3313305974006653, 0.5744912028312683, 0.5233466923236847, 0.5760921835899353, 0.3553318977355957, 0.6020225882530212, 0.4088401794433594, 0.7081522941589355, 0.5230480432510376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8842809200286865})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5332750082015991})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47149354219436646})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48243051767349243})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4827813506126404})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47188448905944824})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.44395927734375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7506245970726013})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5768328309059143})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4726906716823578})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4441016912460327})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.42552027106285095})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [8093, 12655, 19971, 34407, 6314, 46126, 35652, 7125, 53976, 19111], 'labels': [0, 9, -1, 3, 4, 3, 2, 7, 9, 4], 'scores': [0.4858344793319702, 0.5674898028373718, 0.3097749948501587, 0.5415447354316711, 0.40075385570526123, 0.5141686797142029, 0.3452138304710388, 0.40022456645965576, 0.507368266582489, 0.4900718331336975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9198436737060547})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4952853322029114})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47270476818084717})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45848384499549866})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4281649589538574})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47627347707748413})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44380682706832886})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45739617943763733})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.376835595703125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7788864374160767})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4951869547367096})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.44930827617645264})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3861299455165863})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37356239557266235})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3338482081890106})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3476114869117737})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [31531, 44196, 27504, 44837, 11749, 43588, 59747, 7768, 27685, 52834], 'labels': [7, 8, 6, 3, 8, 8, 5, 8, 6, 2], 'scores': [0.4710812270641327, 0.4023054838180542, 0.4050906300544739, 0.43087196350097656, 0.4403287172317505, 0.4852672219276428, 0.6372529566287994, 0.5212406516075134, 0.3179229497909546, 0.5983298420906067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9692806005477905})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5417931079864502})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41499170660972595})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3942973017692566})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44536131620407104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3782443404197693})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4327959716320038})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44099029898643494})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4538429379463196})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.380096826171875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6919414401054382})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4225989282131195})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.382163941860199})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34828615188598633})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34818416833877563})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3232431709766388})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3213423490524292})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3330623507499695})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [59392, 36324, 40022, 59335, 37341, 22199, 19111, 109, 17393, 31313], 'labels': [-1, 3, 8, 4, -1, -1, -1, 2, -1, -1], 'scores': [0.3792923092842102, 0.40296417474746704, 0.6721482276916504, 0.5214579105377197, 0.4275662899017334, 0.6091799736022949, 0.28489142656326294, 0.7417941093444824, 0.4798872470855713, 0.39613330364227295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1171352863311768})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5545863509178162})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4421859681606293})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4393230080604553})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.398337721824646})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41168737411499023})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4109119176864624})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3900167942047119})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4128398299217224})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4477997422218323})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43449607491493225})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9532, 'crossentropy': 0.39026650390625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8215355277061462})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45312392711639404})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3645997941493988})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3576204478740692})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31263595819473267})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3088897466659546})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.336587131023407})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3021419048309326})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3127710223197937})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3155699670314789})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [20275, 26080, 4313, 48378, 51245, 26910, 33859, 27729, 50054, 868], 'labels': [-1, -1, -1, 2, -1, -1, -1, 8, 8, -1], 'scores': [0.3789329528808594, 0.37588584423065186, 0.4897153377532959, 0.44374486804008484, 0.44248223304748535, 0.4241105318069458, 0.26205313205718994, 0.42778855562210083, 0.232820063829422, 0.6883565187454224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9052327275276184})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5031427145004272})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.422035276889801})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3882695436477661})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38681405782699585})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39263176918029785})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3964167833328247})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3931666612625122})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.357772119140625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8377838134765625})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4158889055252075})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3989458382129669})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3503876328468323})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33314067125320435})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32228147983551025})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33017200231552124})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [2011, 57054, 32653, 34752, 27891, 30457, 56632, 7829, 26733, 29955], 'labels': [3, -1, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.45203933119773865, 0.39266085624694824, 0.33107829093933105, 0.43126893043518066, 0.43436264991760254, 0.38921844959259033, 0.3219865560531616, 0.550100564956665, 0.5618754029273987, 0.4984067678451538]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0149140357971191})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5032155513763428})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4029558598995209})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35752564668655396})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3979262709617615})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36949247121810913})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37250426411628723})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.36323271484375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6920226812362671})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4527058005332947})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4060335159301758})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31941089034080505})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30949634313583374})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3275699019432068})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [16860, 3762, 8693, 36761, 31801, 4604, 28512, 12270, 55184, 16882], 'labels': [8, 8, 3, -1, 8, -1, 5, -1, 5, 7], 'scores': [0.4198490381240845, 0.6464408040046692, 0.4570184350013733, 0.4087749719619751, 0.48312780261039734, 0.38206279277801514, 0.560128927230835, 0.33393561840057373, 0.32687416672706604, 0.3518543839454651]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.947356104850769})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46461376547813416})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45132941007614136})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39811626076698303})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3816165328025818})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4178416132926941})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3720654845237732})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4001700282096863})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40688443183898926})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3855471909046173})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3614284423828125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.751225471496582})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4815351366996765})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3948724865913391})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3156687021255493})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3279714584350586})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2795405983924866})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2914777398109436})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.281268835067749})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2779610753059387})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [45510, 11545, 5718, 26724, 39536, 59616, 21901, 19404, 8447, 56027], 'labels': [-1, 3, 9, -1, 4, -1, -1, 4, 3, -1], 'scores': [0.4969538450241089, 0.42422211170196533, 0.5597098469734192, 0.35730743408203125, 0.6352141201496124, 0.47040265798568726, 0.3612842559814453, 0.41939622163772583, 0.5825299024581909, 0.3257981538772583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.981752336025238})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5606677532196045})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.457960844039917})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40936970710754395})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4439961314201355})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37557703256607056})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39791032671928406})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4311756491661072})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3718295991420746})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4174463152885437})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4277861714363098})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4410862624645233})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.3591322265625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8839558362960815})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4637853503227234})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38154786825180054})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35920462012290955})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3255467414855957})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3605114221572876})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3216616213321686})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2957211136817932})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2788452208042145})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31249165534973145})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3179410398006439})
store['active_learning_steps'][34]['eval_training']['best_epoch']=9
store['active_learning_steps'][34]['acquisition']={'indices': [59757, 24860, 52173, 55883, 38998, 17651, 38902, 57683, 9428, 14385], 'labels': [2, 9, 7, -1, -1, -1, -1, 9, 9, 8], 'scores': [0.5437061786651611, 0.5984068512916565, 0.6905502080917358, 0.3490332365036011, 0.2391514778137207, 0.44356298446655273, 0.4856224060058594, 0.4364698529243469, 0.4666670560836792, 0.5313573479652405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 1.0139381885528564})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4786912202835083})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4026094079017639})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38171350955963135})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3840508759021759})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4163448214530945})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4091021418571472})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9564, 'crossentropy': 0.35052333984375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7426250576972961})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4956815838813782})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39250311255455017})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36448073387145996})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34240198135375977})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3490063548088074})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [21495, 44713, 26410, 33340, 4185, 54935, 8654, 2765, 28194, 58644], 'labels': [9, -1, -1, 5, 2, 8, 9, 0, -1, -1], 'scores': [0.5509374141693115, 0.2482661008834839, 0.3598436117172241, 0.448433518409729, 0.46116310358047485, 0.29290664196014404, 0.439464807510376, 0.5326601266860962, 0.38438475131988525, 0.33456742763519287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0862929821014404})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5106231570243835})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46339619159698486})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40464943647384644})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4132586717605591})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4027673602104187})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4000101685523987})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4294830560684204})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4242270588874817})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5088396072387695})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.3911413330078125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8276776075363159})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4989701509475708})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4178880453109741})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3855990171432495})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33678126335144043})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35996925830841064})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3337209224700928})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3202967643737793})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.301047682762146})
store['active_learning_steps'][36]['eval_training']['best_epoch']=9
store['active_learning_steps'][36]['acquisition']={'indices': [12663, 28920, 13520, 40399, 49531, 3814, 29377, 49750, 49933, 56561], 'labels': [8, 2, 4, -1, 7, 6, 1, -1, -1, -1], 'scores': [0.47482264041900635, 0.6724945902824402, 0.3560875952243805, 0.4443396329879761, 0.5173168182373047, 0.6541133522987366, 0.5445568561553955, 0.42175644636154175, 0.3298985958099365, 0.5732412338256836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9639682769775391})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.526273787021637})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.43509018421173096})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43062329292297363})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4069819450378418})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4032087028026581})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3866978585720062})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44175684452056885})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40945500135421753})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.412700891494751})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.36522958984375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8242433071136475})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49598246812820435})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41171085834503174})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3362891376018524})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3407692313194275})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3133277893066406})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3076117932796478})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3285730481147766})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3041442036628723})
store['active_learning_steps'][37]['eval_training']['best_epoch']=9
store['active_learning_steps'][37]['acquisition']={'indices': [46623, 57552, 59460, 46262, 9940, 50959, 6206, 16637, 44753, 21936], 'labels': [4, 1, 1, -1, 4, -1, -1, -1, 5, 4], 'scores': [0.26280051469802856, 0.4524638056755066, 0.5326648950576782, 0.18746131658554077, 0.5456960797309875, 0.4480311870574951, 0.2923848628997803, 0.401938259601593, 0.6469849944114685, 0.4563067555427551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9878594875335693})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5181230306625366})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3989344835281372})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41261184215545654})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4444260597229004})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3867909014225006})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4106954336166382})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4022742509841919})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4544881284236908})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9501, 'crossentropy': 0.3551862548828125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7569198608398438})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49716007709503174})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39036449790000916})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34317725896835327})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3257831931114197})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3068600296974182})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3218402862548828})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.30713701248168945})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [40704, 21981, 13088, 57385, 54888, 21243, 31094, 48742, 45847, 17507], 'labels': [5, -1, -1, -1, -1, -1, 9, -1, -1, 2], 'scores': [0.546509861946106, 0.5725386142730713, 0.38795018196105957, 0.48336249589920044, 0.2833990454673767, 0.3632768392562866, 0.4622430205345154, 0.48395252227783203, 0.3449972867965698, 0.5600352883338928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9504467248916626})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47700661420822144})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.423099160194397})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4007854461669922})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3913845419883728})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42101046442985535})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3982389569282532})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4420276880264282})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9561, 'crossentropy': 0.34497607421875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7981297969818115})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4154525101184845})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3785640597343445})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.358825147151947})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34743010997772217})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32377731800079346})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31852439045906067})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [29926, 19007, 14405, 38082, 42136, 13093, 44927, 17545, 2445, 38223], 'labels': [-1, 9, 6, 9, 0, 3, 7, -1, -1, 3], 'scores': [0.21681511402130127, 0.36335790157318115, 0.45356035232543945, 0.441281795501709, 0.4692625403404236, 0.5454617738723755, 0.4087368845939636, 0.33090901374816895, 0.2514353394508362, 0.6645378172397614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.131436824798584})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5769398212432861})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40993452072143555})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3989938497543335})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36516475677490234})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3588438034057617})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3676750063896179})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35453933477401733})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3808887004852295})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4097091555595398})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4151473641395569})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.3123688720703125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7152972221374512})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48558416962623596})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34262657165527344})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30414116382598877})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29772210121154785})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2750844955444336})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2895508408546448})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2678590416908264})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.27119970321655273})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2622517943382263})
store['active_learning_steps'][40]['eval_training']['best_epoch']=10
store['active_learning_steps'][40]['acquisition']={'indices': [56195, 33440, 41276, 56552, 46189, 32419, 35761, 16780, 15812, 40462], 'labels': [-1, -1, 2, -1, -1, 4, -1, 5, -1, -1], 'scores': [0.4309720993041992, 0.22864556312561035, 0.3814857602119446, 0.42940014600753784, 0.5032267570495605, 0.486483633518219, 0.4949178695678711, 0.46338197588920593, 0.3892509341239929, 0.26151424646377563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.1916923522949219})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5839135646820068})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46211111545562744})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3838568925857544})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37905412912368774})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39634016156196594})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3825053870677948})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3981086015701294})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9513, 'crossentropy': 0.3644578857421875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8038453459739685})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46287187933921814})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4047122597694397})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35315394401550293})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33884483575820923})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37632203102111816})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36022546887397766})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [12188, 49590, 25859, 45822, 56343, 43386, 50239, 3268, 7074, 16756], 'labels': [-1, 7, 8, -1, -1, -1, 9, 6, 1, 7], 'scores': [0.5291339159011841, 0.47822660207748413, 0.30444449186325073, 0.3987147808074951, 0.1850452423095703, 0.32340073585510254, 0.43455368280410767, 0.35624468326568604, 0.3936346769332886, 0.3787790536880493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9751995205879211})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4607001841068268})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4042566418647766})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38658246397972107})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3711608052253723})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3412184715270996})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3666950464248657})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3924627900123596})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35903090238571167})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.333858056640625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7944754958152771})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4531489610671997})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4101909399032593})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3352709412574768})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3573225438594818})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30325329303741455})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31048089265823364})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2925378084182739})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [17760, 8927, 4034, 11579, 30838, 16690, 47888, 2369, 24303, 96], 'labels': [8, -1, -1, -1, -1, -1, 8, -1, -1, -1], 'scores': [0.48353973031044006, 0.4479472041130066, 0.5225770473480225, 0.3657197952270508, 0.5132344961166382, 0.5152331590652466, 0.5580149292945862, 0.450753390789032, 0.3820408582687378, 0.39673852920532227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0731208324432373})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.561265230178833})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3954247236251831})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3916480541229248})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3352877199649811})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3527612090110779})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41221335530281067})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35716065764427185})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.3464287109375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7721165418624878})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5050737857818604})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38311105966567993})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33791691064834595})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2986947298049927})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34513750672340393})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31335657835006714})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [45602, 34294, 52294, 33824, 45097, 42472, 36065, 16070, 33538, 8283], 'labels': [5, 4, 0, 4, 7, 2, 5, 6, 0, 7], 'scores': [0.5879815220832825, 0.46094295382499695, 0.6055189371109009, 0.5193414688110352, 0.3352864384651184, 0.3921661376953125, 0.43862009048461914, 0.460193932056427, 0.633594810962677, 0.31941038370132446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9903582334518433})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5573105216026306})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35944536328315735})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3585370182991028})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3559618890285492})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3031494617462158})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3224231004714966})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3163856863975525})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31428262591362})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.2921541748046875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8069740533828735})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49484503269195557})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35270848870277405})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30718672275543213})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2861664891242981})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29294538497924805})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30344468355178833})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28158971667289734})
store['active_learning_steps'][44]['eval_training']['best_epoch']=8
store['active_learning_steps'][44]['acquisition']={'indices': [7806, 2530, 57620, 31090, 50736, 31345, 34681, 29294, 36818, 44171], 'labels': [-1, -1, -1, -1, -1, 3, -1, 3, 7, -1], 'scores': [0.49519073963165283, 0.44296014308929443, 0.47145360708236694, 0.41095662117004395, 0.4759786128997803, 0.5723390579223633, 0.3433448076248169, 0.5313795208930969, 0.518705427646637, 0.45592427253723145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.084660291671753})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5772626399993896})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38962188363075256})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36549854278564453})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3545079231262207})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36698630452156067})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3350040912628174})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3544369637966156})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38686174154281616})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3595125079154968})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.32338173828125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.832511305809021})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4658195972442627})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4125312566757202})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.373803973197937})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30909523367881775})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3108002543449402})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2931828498840332})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27954375743865967})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2669539153575897})
store['active_learning_steps'][45]['eval_training']['best_epoch']=9
store['active_learning_steps'][45]['acquisition']={'indices': [34920, 14062, 49634, 34414, 7146, 18637, 26629, 18398, 47343, 54035], 'labels': [9, 8, 8, 8, 2, 4, 3, 4, -1, 7], 'scores': [0.6858972907066345, 0.39721107482910156, 0.36361217498779297, 0.5289943814277649, 0.46647703647613525, 0.6734766960144043, 0.35814863443374634, 0.584661066532135, 0.34085917472839355, 0.2616356611251831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0585510730743408})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48110124468803406})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3730394244194031})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.344347208738327})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30567753314971924})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30551373958587646})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3373562693595886})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31737154722213745})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3135962188243866})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.2876803466796875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8615881204605103})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49772337079048157})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3626056909561157})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34431198239326477})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34146854281425476})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3194996118545532})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3023543655872345})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31036651134490967})
store['active_learning_steps'][46]['eval_training']['best_epoch']=7
store['active_learning_steps'][46]['acquisition']={'indices': [10715, 20960, 8387, 5684, 18164, 23942, 5070, 24479, 3002, 26026], 'labels': [-1, -1, -1, 6, -1, -1, -1, 8, -1, -1], 'scores': [0.14170634746551514, 0.3789933919906616, 0.49425041675567627, 0.46767115592956543, 0.3993077278137207, 0.3146202564239502, 0.24377942085266113, 0.4211080074310303, 0.36319196224212646, 0.422305703163147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0823931694030762})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5685209035873413})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3887197971343994})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3779430389404297})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3547056317329407})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3619384467601776})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3228021264076233})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3683023452758789})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36157870292663574})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3578571677207947})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.320721337890625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8465897440910339})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4796980619430542})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3922402858734131})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3042007088661194})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3031061887741089})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.289093554019928})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3039872348308563})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26337382197380066})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2539590895175934})
store['active_learning_steps'][47]['eval_training']['best_epoch']=9
store['active_learning_steps'][47]['acquisition']={'indices': [13980, 24061, 20976, 7886, 28020, 7806, 59083, 29376, 26863, 57221], 'labels': [3, -1, 5, 9, -1, -1, 7, -1, -1, -1], 'scores': [0.3195600211620331, 0.49001622200012207, 0.5055079460144043, 0.8315505981445312, 0.47476494312286377, 0.4086500406265259, 0.3118577003479004, 0.6267756223678589, 0.517993688583374, 0.555220901966095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1234303712844849})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5472031831741333})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4047667384147644})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38234126567840576})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33682143688201904})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31935638189315796})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33032089471817017})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3197097182273865})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.317227303981781})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3182605504989624})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3595438599586487})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3550938665866852})
store['active_learning_steps'][48]['training']['best_epoch']=9
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.3202220458984375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9275854825973511})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4663121998310089})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4004974365234375})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3332595229148865})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33954888582229614})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2983357310295105})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28124088048934937})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2578791677951813})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23422610759735107})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2559739053249359})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26404234766960144})
store['active_learning_steps'][48]['eval_training']['best_epoch']=9
store['active_learning_steps'][48]['acquisition']={'indices': [28306, 41186, 57652, 27386, 10716, 43181, 36357, 15450, 38064, 11453], 'labels': [-1, -1, -1, -1, 7, -1, 3, 6, -1, 0], 'scores': [0.5738720893859863, 0.3233206272125244, 0.4374018907546997, 0.5352487564086914, 0.39085865020751953, 0.6500620245933533, 0.5210540592670441, 0.41391175985336304, 0.24892449378967285, 0.3615309000015259]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0893309116363525})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5228707194328308})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40363022685050964})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3246905207633972})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3146401643753052})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32200825214385986})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30683255195617676})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3252941071987152})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3274464011192322})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.343618780374527})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2874827880859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7984223365783691})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43510663509368896})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3645698130130768})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3298901915550232})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2947961091995239})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28517216444015503})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25534525513648987})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2693907618522644})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25657811760902405})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [25587, 11322, 48397, 3758, 8303, 42199, 25180, 9176, 18279, 29537], 'labels': [-1, 8, 5, -1, -1, 3, -1, -1, -1, -1], 'scores': [0.2919696569442749, 0.36426877975463867, 0.4391341209411621, 0.544675886631012, 0.3582186698913574, 0.5055866837501526, 0.3670893907546997, 0.3842196464538574, 0.3915358781814575, 0.43450212478637695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1601548194885254})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.590855598449707})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4266960620880127})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3819519281387329})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3249913454055786})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3327227830886841})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3206033706665039})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3076545000076294})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3138953447341919})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33530041575431824})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3389028310775757})
store['active_learning_steps'][50]['training']['best_epoch']=8
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.2965460693359375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7604323625564575})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5360015630722046})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36546969413757324})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30579236149787903})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30502718687057495})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2692250609397888})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27653634548187256})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2872920334339142})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26803454756736755})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2554396390914917})
store['active_learning_steps'][50]['eval_training']['best_epoch']=10
store['active_learning_steps'][50]['acquisition']={'indices': [27052, 31397, 21293, 18501, 31272, 22651, 38749, 1958, 56366, 14100], 'labels': [-1, -1, -1, 4, -1, -1, -1, -1, 5, 5], 'scores': [0.5507091283798218, 0.6093804836273193, 0.5733420848846436, 0.6017196774482727, 0.5530047416687012, 0.5265932083129883, 0.5405639410018921, 0.4099169969558716, 0.49348413944244385, 0.6008970141410828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1394400596618652})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5305781364440918})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36750829219818115})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3173251450061798})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3376750349998474})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30890998244285583})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3321044147014618})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32253628969192505})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29733869433403015})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3332105278968811})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2717837989330292})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3230799734592438})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3165978193283081})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3346995711326599})
store['active_learning_steps'][51]['training']['best_epoch']=11
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2885017333984375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8040491342544556})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4836966395378113})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3508933484554291})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3045530617237091})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27881503105163574})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29362621903419495})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27980875968933105})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24121853709220886})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24839666485786438})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25042396783828735})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2328139990568161})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23585021495819092})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23792368173599243})
store['active_learning_steps'][51]['eval_training']['best_epoch']=11
store['active_learning_steps'][51]['acquisition']={'indices': [5390, 16925, 33664, 49977, 29132, 34301, 16611, 29895, 44612, 56292], 'labels': [-1, -1, 8, -1, -1, -1, -1, 0, -1, 9], 'scores': [0.3295520544052124, 0.3460378646850586, 0.3804123103618622, 0.5326277017593384, 0.46288472414016724, 0.35183781385421753, 0.3545093536376953, 0.45718538761138916, 0.34085947275161743, 0.489754319190979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.959113597869873})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4803115725517273})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38179296255111694})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3288722634315491})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33244699239730835})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3314438462257385})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30683085322380066})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3044043481349945})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3284311890602112})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29541146755218506})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30388614535331726})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3517957329750061})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3288382291793823})
store['active_learning_steps'][52]['training']['best_epoch']=10
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.287657763671875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8867706060409546})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48685386776924133})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3355896472930908})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32804712653160095})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2964918911457062})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2922492027282715})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25886231660842896})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25549572706222534})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.240138441324234})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26404786109924316})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23446395993232727})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2399711310863495})
store['active_learning_steps'][52]['eval_training']['best_epoch']=11
store['active_learning_steps'][52]['acquisition']={'indices': [20641, 20742, 57827, 27873, 38912, 34477, 40667, 42920, 3830, 2758], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5971071720123291, 0.34636223316192627, 0.4614936113357544, 0.4725576639175415, 0.6764911413192749, 0.3598182201385498, 0.46434998512268066, 0.7022923231124878, 0.5072349309921265, 0.3883563280105591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1687250137329102})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5387876033782959})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39734506607055664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3644430637359619})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3185024559497833})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32205361127853394})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2745524048805237})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3037733733654022})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29594606161117554})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33546411991119385})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9605, 'crossentropy': 0.3020325439453125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8678444027900696})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4537399411201477})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41797637939453125})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3283236026763916})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3184395432472229})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2978675365447998})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.303932249546051})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26993322372436523})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2699146270751953})
store['active_learning_steps'][53]['eval_training']['best_epoch']=9
store['active_learning_steps'][53]['acquisition']={'indices': [34029, 4955, 37048, 32776, 47291, 6580, 57841, 54885, 58007, 21944], 'labels': [-1, 2, 9, 4, 1, -1, -1, 6, -1, 1], 'scores': [0.2935214042663574, 0.6135445833206177, 0.3665205240249634, 0.6592383980751038, 0.4109078645706177, 0.24056923389434814, 0.2989480495452881, 0.4114561080932617, 0.2579892873764038, 0.42656242847442627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2313777208328247})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5851411819458008})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42910727858543396})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32453253865242004})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34027189016342163})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3336421549320221})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35933834314346313})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.33812841796875}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9006955027580261})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5948566198348999})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4847942888736725})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44084280729293823})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36271363496780396})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3738589882850647})
store['active_learning_steps'][54]['eval_training']['best_epoch']=5
store['active_learning_steps'][54]['acquisition']={'indices': [43787, 21867, 50729, 45387, 44895, 21910, 8254, 22518, 25732, 36055], 'labels': [-1, -1, 0, -1, -1, -1, 3, 4, 2, -1], 'scores': [0.25136446952819824, 0.31585538387298584, 0.27990543842315674, 0.36643147468566895, 0.1919800043106079, 0.5213044881820679, 0.3689802885055542, 0.41856473684310913, 0.4775053858757019, 0.3384343385696411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1150259971618652})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5190496444702148})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44543254375457764})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36356431245803833})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3359718918800354})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3126239776611328})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3039896786212921})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37587419152259827})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3224896788597107})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3851633667945862})
store['active_learning_steps'][55]['training']['best_epoch']=7
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.3123827392578125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8659566640853882})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46872538328170776})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39302539825439453})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31379321217536926})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31580036878585815})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27907466888427734})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2698957920074463})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2960880994796753})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29951947927474976})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [33485, 36988, 2376, 9315, 16156, 46035, 27502, 25703, 48080, 1356], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, 5], 'scores': [0.29228007793426514, 0.4280126094818115, 0.34781643748283386, 0.6450589299201965, 0.42509543895721436, 0.47350841760635376, 0.530239462852478, 0.3874242305755615, 0.37540650367736816, 0.3384222984313965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0520213842391968})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5001251697540283})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3789091408252716})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3282299041748047})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36495256423950195})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3465166687965393})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3170543313026428})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3151806890964508})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32486119866371155})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32552698254585266})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3027612268924713})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.345602810382843})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3332054615020752})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.310647189617157})
store['active_learning_steps'][56]['training']['best_epoch']=11
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2874179931640625}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8677090406417847})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5277968049049377})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33239495754241943})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34698402881622314})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2836608290672302})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28283265233039856})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.272433876991272})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26336389780044556})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2624652087688446})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.273418128490448})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27485203742980957})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2267487347126007})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2553202509880066})
store['active_learning_steps'][56]['eval_training']['best_epoch']=12
store['active_learning_steps'][56]['acquisition']={'indices': [34597, 254, 40040, 13003, 27685, 53979, 41555, 25092, 51130, 57022], 'labels': [3, -1, 0, -1, -1, 8, -1, 0, -1, -1], 'scores': [0.34901992976665497, 0.4660227298736572, 0.5568794310092926, 0.5879517793655396, 0.44033873081207275, 0.560252845287323, 0.5527361631393433, 0.5038592219352722, 0.4589160680770874, 0.32439327239990234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0530998706817627})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5983425974845886})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42096132040023804})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35933759808540344})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40234142541885376})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.314439594745636})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3358399271965027})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3546086549758911})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3335781693458557})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.31281259765625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8503241539001465})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4630793333053589})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39865046739578247})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3503491282463074})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35690557956695557})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3431850075721741})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33864444494247437})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33408939838409424})
store['active_learning_steps'][57]['eval_training']['best_epoch']=8
store['active_learning_steps'][57]['acquisition']={'indices': [59336, 38605, 1696, 14728, 31407, 13012, 2789, 17433, 15079, 55486], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.43143516778945923, 0.3743981122970581, 0.34792524576187134, 0.3338336944580078, 0.376528799533844, 0.32661211490631104, 0.3508197069168091, 0.2710222005844116, 0.3682440519332886, 0.2627512216567993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1272577047348022})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5285840034484863})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41653162240982056})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37820929288864136})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3301985263824463})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34134185314178467})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.325023353099823})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32644122838974})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3715762495994568})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3774792551994324})
store['active_learning_steps'][58]['training']['best_epoch']=7
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2778233642578125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9900870323181152})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4993759095668793})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4020371437072754})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34163495898246765})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33585089445114136})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2961282730102539})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26151496171951294})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28224921226501465})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27786505222320557})
store['active_learning_steps'][58]['eval_training']['best_epoch']=7
store['active_learning_steps'][58]['acquisition']={'indices': [43352, 45451, 59396, 8712, 15303, 12584, 59575, 18440, 52844, 25642], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4099920988082886, 0.3271244764328003, 0.4123854637145996, 0.29672789573669434, 0.5862643718719482, 0.40578722953796387, 0.4508540630340576, 0.38983118534088135, 0.4639158248901367, 0.5176070928573608]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0757255554199219})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.531731128692627})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3695877492427826})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29433146119117737})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2876151502132416})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3129275441169739})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2988666296005249})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29335272312164307})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.291742529296875}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9190908670425415})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4690670371055603})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40574437379837036})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.335136353969574})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30979782342910767})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3240649104118347})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30222225189208984})
store['active_learning_steps'][59]['eval_training']['best_epoch']=7
store['active_learning_steps'][59]['acquisition']={'indices': [13259, 18487, 21636, 51242, 11823, 20404, 10624, 51590, 41116, 20685], 'labels': [1, 4, 2, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.5787079334259033, 0.43750154972076416, 0.5243746042251587, 0.29082775115966797, 0.31478047370910645, 0.3120136260986328, 0.39196258783340454, 0.3629637360572815, 0.3583737015724182, 0.3816303014755249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1380468606948853})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5220769643783569})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.379097044467926})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3180505633354187})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31561794877052307})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28342288732528687})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29207560420036316})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33221226930618286})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3070187568664551})
store['active_learning_steps'][60]['training']['best_epoch']=6
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2651755859375}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.836142897605896})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4708392024040222})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3872618079185486})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31952446699142456})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2990131974220276})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2919015884399414})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2750810980796814})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2900446057319641})
store['active_learning_steps'][60]['eval_training']['best_epoch']=7
store['active_learning_steps'][60]['acquisition']={'indices': [11600, 34906, 43950, 14290, 18256, 56949, 14765, 38621, 4077, 33010], 'labels': [-1, 3, 9, 4, -1, -1, 3, -1, -1, -1], 'scores': [0.5975209474563599, 0.32079482078552246, 0.6055638194084167, 0.4330195188522339, 0.47461652755737305, 0.4421989917755127, 0.5725665092468262, 0.41371655464172363, 0.40246254205703735, 0.5586471557617188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1097158193588257})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5490474104881287})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40874600410461426})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3536452651023865})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.326846718788147})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31669580936431885})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3249051570892334})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30711495876312256})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3089359998703003})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33832401037216187})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.39201104640960693})
store['active_learning_steps'][61]['training']['best_epoch']=8
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2778145263671875}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9391189813613892})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47784626483917236})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37360161542892456})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2870776951313019})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2831745743751526})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2727075219154358})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2650794982910156})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2631482779979706})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2515377402305603})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24186167120933533})
store['active_learning_steps'][61]['eval_training']['best_epoch']=10
store['active_learning_steps'][61]['acquisition']={'indices': [4804, 4547, 52688, 55092, 37648, 23350, 11622, 39856, 55190, 40877], 'labels': [0, -1, 6, -1, -1, 8, -1, -1, 3, -1], 'scores': [0.5047141909599304, 0.5571246147155762, 0.381665974855423, 0.36403846740722656, 0.47501492500305176, 0.6460970044136047, 0.5535446405410767, 0.49667251110076904, 0.4963417649269104, 0.4537496566772461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0851383209228516})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5152468681335449})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35659968852996826})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3557335138320923})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3265089690685272})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3307257890701294})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31099650263786316})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25455737113952637})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28769606351852417})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3017137348651886})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3059301972389221})
store['active_learning_steps'][62]['training']['best_epoch']=8
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2649875244140625}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9209951162338257})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47128206491470337})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3970765471458435})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3528948426246643})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30108314752578735})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2844052314758301})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2710731029510498})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29451984167099})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2679203152656555})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2650735378265381})
store['active_learning_steps'][62]['eval_training']['best_epoch']=10
store['active_learning_steps'][62]['acquisition']={'indices': [44270, 9161, 53839, 57222, 36850, 2030, 18522, 51815, 1294, 46817], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.44437819719314575, 0.3969050645828247, 0.26519644260406494, 0.5339453816413879, 0.4887391924858093, 0.563298225402832, 0.30051112174987793, 0.43542635440826416, 0.3257620334625244, 0.4644196033477783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1387460231781006})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.47618597745895386})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36259815096855164})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3172836899757385})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30582308769226074})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3030329942703247})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30191555619239807})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30935990810394287})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3015240430831909})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31303825974464417})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31403839588165283})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3431520164012909})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2798512939453125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8717225193977356})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44423261284828186})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36290842294692993})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3197740316390991})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25493696331977844})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2760448157787323})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26974982023239136})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27862873673439026})
store['active_learning_steps'][63]['eval_training']['best_epoch']=5
store['active_learning_steps'][63]['acquisition']={'indices': [18607, 14296, 53640, 15265, 57552, 43549, 49262, 51889, 4296, 301], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.49619024991989136, 0.3261359930038452, 0.4113270044326782, 0.40848493576049805, 0.5032117366790771, 0.4781275987625122, 0.44982075691223145, 0.47072142362594604, 0.37318146228790283, 0.37812340259552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1127285957336426})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.500421404838562})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4246267080307007})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3198251724243164})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34041285514831543})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32983410358428955})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29837557673454285})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2953259348869324})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31898465752601624})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3127240836620331})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31504881381988525})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.2996796142578125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8592725992202759})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5011072158813477})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37519049644470215})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35466834902763367})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2885775566101074})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30658024549484253})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2771463990211487})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2643861770629883})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2585136592388153})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24689708650112152})
store['active_learning_steps'][64]['eval_training']['best_epoch']=10
store['active_learning_steps'][64]['acquisition']={'indices': [36157, 42345, 32527, 33091, 16541, 14667, 23956, 38912, 868, 56298], 'labels': [7, -1, -1, -1, -1, -1, 4, -1, -1, -1], 'scores': [0.586813747882843, 0.3667426109313965, 0.4408339262008667, 0.30186760425567627, 0.3784698247909546, 0.279178261756897, 0.4794253706932068, 0.6101409196853638, 0.5139150619506836, 0.37704527378082275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.0497653484344482})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5100491046905518})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3829289674758911})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3249818682670593})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28228864073753357})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28570303320884705})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30255430936813354})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27075934410095215})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2698809504508972})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2735861539840698})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33361852169036865})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2997610569000244})
store['active_learning_steps'][65]['training']['best_epoch']=9
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.270973583984375}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8319441676139832})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49425584077835083})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42629140615463257})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33613044023513794})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3186400830745697})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2941814064979553})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26877811551094055})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2637338638305664})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2888142764568329})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25635993480682373})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2512170672416687})
store['active_learning_steps'][65]['eval_training']['best_epoch']=11
store['active_learning_steps'][65]['acquisition']={'indices': [29814, 45660, 32823, 22272, 36704, 47424, 55986, 40166, 47797, 10109], 'labels': [-1, -1, -1, 5, 2, -1, -1, -1, -1, -1], 'scores': [0.4442932605743408, 0.39318162202835083, 0.5027108788490295, 0.5663472414016724, 0.5604077577590942, 0.46985340118408203, 0.3871278762817383, 0.47784674167633057, 0.4315299987792969, 0.4392824172973633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1075936555862427})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6106252670288086})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36074692010879517})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.360994428396225})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30691447854042053})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30203673243522644})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2889229953289032})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30355143547058105})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30862706899642944})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31767037510871887})
store['active_learning_steps'][66]['training']['best_epoch']=7
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2575096923828125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8298788070678711})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.453727126121521})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34007930755615234})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33536410331726074})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2967924475669861})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27546823024749756})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25002220273017883})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2699892222881317})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3033515214920044})
store['active_learning_steps'][66]['eval_training']['best_epoch']=7
store['active_learning_steps'][66]['acquisition']={'indices': [25261, 39942, 43838, 54959, 55148, 44148, 57175, 26241, 54950, 57221], 'labels': [-1, 9, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.3822232484817505, 0.49120938777923584, 0.4225572347640991, 0.311565101146698, 0.4010046720504761, 0.4117244482040405, 0.3012058734893799, 0.4987814426422119, 0.42773115634918213, 0.6275599598884583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3812289237976074})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5935981273651123})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4360837936401367})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3138114809989929})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3156372904777527})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2899320125579834})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28771382570266724})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28111332654953003})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26840102672576904})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29782918095588684})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2704187035560608})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28805556893348694})
store['active_learning_steps'][67]['training']['best_epoch']=9
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2501826171875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8931567668914795})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.47277185320854187})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36719152331352234})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2873796224594116})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2721484899520874})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27125436067581177})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24734047055244446})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24815118312835693})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24360120296478271})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24401263892650604})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23822161555290222})
store['active_learning_steps'][67]['eval_training']['best_epoch']=11
store['active_learning_steps'][67]['acquisition']={'indices': [58681, 40310, 17733, 46545, 37485, 57035, 14004, 25990, 46214, 43267], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.49261701107025146, 0.5307210087776184, 0.6029273867607117, 0.6717265248298645, 0.4011591672897339, 0.6208323240280151, 0.5801156759262085, 0.44057393074035645, 0.3720884919166565, 0.449837327003479]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0920335054397583})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5362929105758667})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3860596716403961})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.36939549446105957})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30308157205581665})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27356356382369995})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2631392478942871})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3150297701358795})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30090734362602234})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.29546546936035156})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.27010107421875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9282627105712891})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5133538842201233})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37374231219291687})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3266880512237549})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3088732659816742})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30021366477012634})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2902567982673645})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2527253329753876})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2664525508880615})
store['active_learning_steps'][68]['eval_training']['best_epoch']=8
store['active_learning_steps'][68]['acquisition']={'indices': [31252, 41378, 43567, 4767, 40390, 37184, 37124, 21279, 14266, 49311], 'labels': [5, -1, -1, 8, 0, -1, 3, 0, 3, 0], 'scores': [0.6930199265480042, 0.42769503593444824, 0.23569393157958984, 0.43846213817596436, 0.5022828578948975, 0.40200042724609375, 0.34853899478912354, 0.3625585436820984, 0.5375926494598389, 0.46840137243270874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0566856861114502})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5881772041320801})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3342534303665161})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31680208444595337})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2959839105606079})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2568889260292053})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31296610832214355})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.283586323261261})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25684988498687744})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30448096990585327})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2592795491218567})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3414947986602783})
store['active_learning_steps'][69]['training']['best_epoch']=9
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2530791259765625}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9131752252578735})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45806437730789185})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38449227809906006})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3203290104866028})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2871520519256592})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27262765169143677})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2884848117828369})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.242728590965271})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.250972718000412})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2558530271053314})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2576374411582947})
store['active_learning_steps'][69]['eval_training']['best_epoch']=8
store['active_learning_steps'][69]['acquisition']={'indices': [30457, 2591, 26554, 16825, 54363, 9557, 38400, 55203, 55827, 33451], 'labels': [-1, -1, -1, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.3925609588623047, 0.5490344762802124, 0.4666016697883606, 0.28905290365219116, 0.3548862934112549, 0.47913604974746704, 0.3587149381637573, 0.3511788845062256, 0.5130264759063721, 0.38585853576660156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3318203687667847})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5666923522949219})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40159863233566284})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4084315896034241})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34974706172943115})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33495479822158813})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30223265290260315})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3202696442604065})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2965810298919678})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31720802187919617})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3200724720954895})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.343929260969162})
store['active_learning_steps'][70]['training']['best_epoch']=9
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.273884130859375}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9203275442123413})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5059241652488708})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3559035360813141})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2811851501464844})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29180651903152466})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26980963349342346})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26004558801651})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24168655276298523})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25255468487739563})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2653246223926544})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23320433497428894})
store['active_learning_steps'][70]['eval_training']['best_epoch']=11
store['active_learning_steps'][70]['acquisition']={'indices': [55910, 52508, 39778, 17248, 55737, 14461, 22097, 17804, 37969, 19537], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.5784561634063721, 0.3330923318862915, 0.44619089365005493, 0.543820321559906, 0.4057549238204956, 0.2871652841567993, 0.44446420669555664, 0.4456954002380371, 0.37949031591415405, 0.5907559990882874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1965230703353882})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6641969084739685})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3815494179725647})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3396311104297638})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31904423236846924})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3057408630847931})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3126734495162964})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2881389856338501})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32382652163505554})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28891998529434204})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3162863254547119})
store['active_learning_steps'][71]['training']['best_epoch']=8
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.2715465087890625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8197476863861084})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45382773876190186})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40525296330451965})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32246267795562744})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3074614703655243})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3065638542175293})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3145194947719574})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.286058247089386})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28550612926483154})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2970861792564392})
store['active_learning_steps'][71]['eval_training']['best_epoch']=9
store['active_learning_steps'][71]['acquisition']={'indices': [32573, 25120, 50617, 36029, 12689, 3756, 2992, 28833, 28600, 48804], 'labels': [8, 8, -1, -1, -1, 3, -1, -1, -1, -1], 'scores': [0.39385855197906494, 0.2534852623939514, 0.5775125622749329, 0.534538745880127, 0.689428448677063, 0.653103232383728, 0.43599390983581543, 0.4359546899795532, 0.39875757694244385, 0.6866121292114258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2047314643859863})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.550230085849762})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.38200026750564575})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3300415277481079})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3301469087600708})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32297319173812866})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30811816453933716})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31153208017349243})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31033098697662354})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31001895666122437})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.2882921630859375}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9965957403182983})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5023530721664429})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3649371862411499})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3450378179550171})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3320646286010742})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30056214332580566})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2724512219429016})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27503466606140137})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29051706194877625})
store['active_learning_steps'][72]['eval_training']['best_epoch']=7
store['active_learning_steps'][72]['acquisition']={'indices': [42438, 30365, 28609, 20172, 38642, 23053, 44698, 59731, 1017, 59662], 'labels': [9, -1, -1, 4, -1, -1, 1, 5, -1, -1], 'scores': [0.6618338227272034, 0.40787893533706665, 0.2673078775405884, 0.626168966293335, 0.4293797016143799, 0.27671003341674805, 0.4296354651451111, 0.4504849314689636, 0.36888420581817627, 0.34727025032043457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1737459897994995})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6001499891281128})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3956184387207031})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3360854387283325})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26513779163360596})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2934403419494629})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2834565043449402})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27607253193855286})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.28718359375}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9659432172775269})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5875642895698547})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4632648825645447})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41003286838531494})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3848615288734436})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3715161085128784})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29393649101257324})
store['active_learning_steps'][73]['eval_training']['best_epoch']=7
store['active_learning_steps'][73]['acquisition']={'indices': [54880, 31776, 37427, 15852, 43008, 25125, 26877, 35171, 23632, 27791], 'labels': [5, -1, 2, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.34690937399864197, 0.25253963470458984, 0.5628013014793396, 0.5052344799041748, 0.4330419898033142, 0.42799633741378784, 0.3609752655029297, 0.4397801160812378, 0.4454461336135864, 0.41713380813598633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0791985988616943})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5284106731414795})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3778093159198761})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3201586604118347})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33200564980506897})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3076680302619934})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3367208242416382})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29697853326797485})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2984980642795563})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28518402576446533})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3155432343482971})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31215494871139526})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3198872208595276})
store['active_learning_steps'][74]['training']['best_epoch']=10
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.266643701171875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9883284568786621})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5486832857131958})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3867807388305664})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35616129636764526})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.334414005279541})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27293500304222107})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24831122159957886})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25811436772346497})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2669011950492859})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2569265067577362})
store['active_learning_steps'][74]['eval_training']['best_epoch']=7
store['active_learning_steps'][74]['acquisition']={'indices': [40647, 40502, 18682, 32544, 18736, 41555, 59014, 17271, 18056, 43647], 'labels': [-1, -1, 7, -1, -1, -1, -1, -1, 4, -1], 'scores': [0.4557437002658844, 0.48258018493652344, 0.3942255675792694, 0.30391645431518555, 0.4346579313278198, 0.31749463081359863, 0.35955512523651123, 0.44837427139282227, 0.38180750608444214, 0.4361863136291504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1946446895599365})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5608073472976685})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34591144323349})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36533498764038086})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28028666973114014})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2722291946411133})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28441381454467773})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2810432016849518})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27410179376602173})
store['active_learning_steps'][75]['training']['best_epoch']=6
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.27194609375}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8146986365318298})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4521750211715698})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33472979068756104})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33760130405426025})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33919236063957214})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2782217562198639})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27866312861442566})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3052656054496765})
store['active_learning_steps'][75]['eval_training']['best_epoch']=6
store['active_learning_steps'][75]['acquisition']={'indices': [37583, 27751, 39373, 44969, 52133, 12327, 29530, 35360, 18966, 30088], 'labels': [-1, -1, 8, -1, 0, -1, 4, 1, 7, 0], 'scores': [0.5059982538223267, 0.2917199730873108, 0.49579286575317383, 0.326473593711853, 0.4566305875778198, 0.3847956657409668, 0.319428026676178, 0.3420150876045227, 0.43953394889831543, 0.38300812244415283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.322722315788269})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5808447599411011})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4540098309516907})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3408288359642029})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3341822028160095})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3203772306442261})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34390178322792053})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34710708260536194})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3348817825317383})
store['active_learning_steps'][76]['training']['best_epoch']=6
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.302288671875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9500212669372559})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5639129877090454})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4297640323638916})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3845713138580322})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3546449542045593})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3336283564567566})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3098970353603363})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34599077701568604})
store['active_learning_steps'][76]['eval_training']['best_epoch']=7
store['active_learning_steps'][76]['acquisition']={'indices': [4058, 52280, 12784, 17666, 43901, 17209, 30686, 31767, 42112, 45915], 'labels': [8, 8, -1, 9, -1, -1, -1, -1, 8, 4], 'scores': [0.5467194318771362, 0.30707085132598877, 0.41580313444137573, 0.24365079402923584, 0.3968573808670044, 0.3598439693450928, 0.35848569869995117, 0.18841314315795898, 0.39240002632141113, 0.6495411396026611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2369942665100098})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5745166540145874})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42105162143707275})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3624160885810852})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3112749457359314})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3649894595146179})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2918316423892975})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2885514497756958})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29727959632873535})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34785956144332886})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28343701362609863})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3092963695526123})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2803647518157959})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3018151521682739})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31833842396736145})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30206233263015747})
store['active_learning_steps'][77]['training']['best_epoch']=13
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.255856689453125}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9941242933273315})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6128078699111938})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3603024184703827})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35642343759536743})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2831681966781616})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28152233362197876})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25213855504989624})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23135292530059814})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23813781142234802})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23970825970172882})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2492915689945221})
store['active_learning_steps'][77]['eval_training']['best_epoch']=8
store['active_learning_steps'][77]['acquisition']={'indices': [58310, 55320, 35670, 24918, 4285, 42058, 35401, 3426, 56726, 4542], 'labels': [-1, -1, -1, -1, -1, -1, 3, -1, 9, -1], 'scores': [0.34783434867858887, 0.49408042430877686, 0.4687885046005249, 0.4407116174697876, 0.30388498306274414, 0.3452826738357544, 0.5791535377502441, 0.3665430545806885, 0.47977185249328613, 0.4254164695739746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2605617046356201})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.630131721496582})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40469005703926086})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3388029932975769})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29962706565856934})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3179723620414734})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2943764925003052})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27981337904930115})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28188085556030273})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29674822092056274})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27013498544692993})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27721408009529114})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2891421914100647})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27229613065719604})
store['active_learning_steps'][78]['training']['best_epoch']=11
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.2686142578125}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0255098342895508})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5514163374900818})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3791097104549408})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34791457653045654})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3112792670726776})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2953531742095947})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28738000988960266})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27335238456726074})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2609790861606598})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26293885707855225})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2654867172241211})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24987053871154785})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26162800192832947})
store['active_learning_steps'][78]['eval_training']['best_epoch']=12
store['active_learning_steps'][78]['acquisition']={'indices': [45954, 50212, 7806, 5216, 44543, 21671, 56587, 2665, 51863, 1075], 'labels': [8, 3, -1, 2, -1, -1, -1, -1, 9, 7], 'scores': [0.6099462509155273, 0.4585278034210205, 0.48772257566452026, 0.44339531660079956, 0.3562331199645996, 0.4423114061355591, 0.22711044549942017, 0.3368173837661743, 0.5113292336463928, 0.5198968052864075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2702717781066895})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6767210960388184})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4474267363548279})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35624659061431885})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3119567632675171})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2998143136501312})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2958233058452606})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30845487117767334})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27030622959136963})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2993509769439697})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32176491618156433})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3079524040222168})
store['active_learning_steps'][79]['training']['best_epoch']=9
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2698658447265625}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1254509687423706})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6033669710159302})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4372539222240448})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32978197932243347})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30037814378738403})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31935882568359375})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2976313829421997})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27417585253715515})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27251380681991577})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2630877196788788})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.263868123292923})
store['active_learning_steps'][79]['eval_training']['best_epoch']=10
store['active_learning_steps'][79]['acquisition']={'indices': [8673, 48975, 42546, 30429, 51161, 32880, 27888, 52487, 19078, 16743], 'labels': [-1, 2, -1, 2, -1, 0, -1, -1, -1, 3], 'scores': [0.4829155206680298, 0.46404457092285156, 0.436975359916687, 0.5120138823986053, 0.4391433000564575, 0.6499223709106445, 0.4705633521080017, 0.657106339931488, 0.4566922187805176, 0.3578210771083832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2238094806671143})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5244738459587097})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4229368567466736})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3849390149116516})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33567169308662415})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32746821641921997})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3168683648109436})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2917192876338959})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30785512924194336})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2949100434780121})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31172502040863037})
store['active_learning_steps'][80]['training']['best_epoch']=8
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2781470947265625}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8952128887176514})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5891529321670532})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4173107147216797})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35031622648239136})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31953054666519165})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2939871847629547})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27783167362213135})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.286119669675827})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25769656896591187})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27218928933143616})
store['active_learning_steps'][80]['eval_training']['best_epoch']=9
store['active_learning_steps'][80]['acquisition']={'indices': [29332, 9641, 14507, 30656, 44585, 23911, 1517, 11743, 25624, 12636], 'labels': [-1, 8, -1, -1, -1, 1, -1, -1, -1, 6], 'scores': [0.46771955490112305, 0.40118318796157837, 0.3638153076171875, 0.442594051361084, 0.35557615756988525, 0.32216453552246094, 0.35046517848968506, 0.2669299840927124, 0.6671110391616821, 0.6410278975963593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.225575566291809})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5653833150863647})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4430997371673584})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3801732659339905})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3357732892036438})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3398400545120239})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30858099460601807})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2861517071723938})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29296332597732544})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2926255464553833})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2936675250530243})
store['active_learning_steps'][81]['training']['best_epoch']=8
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.2725429443359375}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.9336001873016357})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49939119815826416})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3905554413795471})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.331097811460495})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30233222246170044})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31334173679351807})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2793300449848175})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24933023750782013})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26223224401474})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25618278980255127})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [424, 59160, 23732, 1972, 54925, 11074, 10513, 53217, 58064, 8619], 'labels': [9, 5, 9, -1, -1, 9, -1, -1, 3, 8], 'scores': [0.5897010564804077, 0.4484476149082184, 0.5771526098251343, 0.29874467849731445, 0.2894275188446045, 0.31119775772094727, 0.18469470739364624, 0.44014233350753784, 0.33556485176086426, 0.35507649183273315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2562501430511475})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5856661796569824})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4143778681755066})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36352837085723877})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28368261456489563})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2647717595100403})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2656894326210022})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2711557149887085})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30405449867248535})
store['active_learning_steps'][82]['training']['best_epoch']=6
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.254543310546875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.937950074672699})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5313912630081177})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4358063340187073})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3238108456134796})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29983121156692505})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2975984811782837})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28162235021591187})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2777245044708252})
store['active_learning_steps'][82]['eval_training']['best_epoch']=8
store['active_learning_steps'][82]['acquisition']={'indices': [38926, 39086, 8711, 36867, 16462, 9788, 49664, 30508, 29511, 43276], 'labels': [-1, -1, -1, -1, 3, 7, -1, -1, -1, -1], 'scores': [0.39361023902893066, 0.42878258228302, 0.32349491119384766, 0.4090331792831421, 0.37652671337127686, 0.39969444274902344, 0.35468459129333496, 0.5285667181015015, 0.43458282947540283, 0.39385104179382324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0041435956954956})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5882623791694641})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.39410459995269775})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30727964639663696})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2816600501537323})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2925081253051758})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27308300137519836})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27039578557014465})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2991962134838104})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26112478971481323})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2645784616470337})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2738421857357025})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28408417105674744})
store['active_learning_steps'][83]['training']['best_epoch']=10
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.2327066650390625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8986350297927856})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5501205325126648})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35004594922065735})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3224368095397949})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31842267513275146})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2809656262397766})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.248806893825531})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26698458194732666})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24296215176582336})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25845757126808167})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25217205286026})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23584365844726562})
store['active_learning_steps'][83]['eval_training']['best_epoch']=12
store['active_learning_steps'][83]['acquisition']={'indices': [52800, 1241, 55513, 55131, 39822, 51358, 50435, 45443, 41770, 53627], 'labels': [9, -1, 5, -1, 9, -1, -1, 5, -1, -1], 'scores': [0.5916515588760376, 0.4056839942932129, 0.6044158935546875, 0.36365020275115967, 0.32769593596458435, 0.3609057664871216, 0.49650537967681885, 0.49759984016418457, 0.34464097023010254, 0.43177568912506104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4489054679870605})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6957764625549316})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46267205476760864})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3510390520095825})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32457342743873596})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2993449568748474})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33122849464416504})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28977277874946594})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3180432915687561})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33054810762405396})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34094083309173584})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2638099365234375}
