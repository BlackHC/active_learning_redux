store = {}
store['timestamp']=1621476203
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=38']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=38
store['worker_id']=38
store['num_workers']=80
store['config']={'seed': 1274, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.509113073348999})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7940356731414795})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4583423137664795})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0745673179626465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.5141797065734863})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.562791347503662})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.6893839836120605})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6597, 'crossentropy': 2.869567578125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1949836015701294})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1445144414901733})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.181879997253418})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1465959548950195})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1668686866760254})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1897541284561157})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36475], ['id', 29246], ['id', 10025], ['id', 8509], ['id', 56775]], 'labels': [2, 3, 0, 0, 0], 'scores': [1.3143153542526393, 2.210102353714558, 2.8654338091634832, 3.2797259177065623, 3.5165619386370057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.30465030670166})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9328551292419434})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.130610942840576})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.3256607055664062})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.411872625350952})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.559330463409424})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3571653366088867})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6615, 'crossentropy': 2.998073046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2361247539520264})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2120096683502197})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.254311203956604})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2557733058929443})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 57456], ['id', 14211], ['id', 32349], ['id', 4066], ['id', 22617]], 'labels': [6, 8, 8, 1, 8], 'scores': [1.1035107845740553, 2.005702547680677, 2.6388706120623837, 3.005826131921485, 3.1585987782817897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7645021677017212})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.041532278060913})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.2039201259613037})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.425689697265625})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.4180688858032227})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.733, 'crossentropy': 1.9271416015625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0106620788574219})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9766435623168945})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9324941635131836})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9642462730407715})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 38064], ['id', 11978], ['id', 8485], ['id', 4743], ['id', 10350]], 'labels': [9, 3, 8, 7, 4], 'scores': [0.9420124007706194, 1.7292380046742064, 2.265798118264609, 2.6665659483899438, 2.902589320374391]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.578952431678772})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8618454933166504})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9886510372161865})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.2712972164154053})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.2242050170898438})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.341221332550049})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7697, 'crossentropy': 1.897067578125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.959145188331604})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9476888179779053})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9274054169654846})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9368655681610107})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.9289065599441528})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 35674], ['id', 21650], ['id', 13061], ['id', 57553], ['id', 57851]], 'labels': [5, 8, 2, 5, -1], 'scores': [1.0706574535101505, 1.9066829321440544, 2.5131971410975646, 2.8580133776406615, 3.0393247354832713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4899189472198486})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.5199623107910156})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8518320322036743})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.750900149345398})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.963780403137207})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 2.216372013092041})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7931, 'crossentropy': 1.5767365234375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.96463942527771})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8702312111854553})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8580722808837891})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8381178379058838})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8181840181350708})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 16860], ['id', 43571], ['id', 8419], ['id', 4684], ['id', 16948]], 'labels': [8, 4, 5, 8, 2], 'scores': [1.0062559830642641, 1.8271814669841775, 2.4243206713196317, 2.783597968637144, 2.9447129374079974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2001469135284424})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.5265960693359375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.4180710315704346})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.411070466041565})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7288399934768677})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.861023187637329})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.972752332687378})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8135, 'crossentropy': 1.45661357421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8825023174285889})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7529851794242859})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7469499111175537})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.7758311629295349})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7348231077194214})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.7553455233573914})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 49991], ['id', 4909], ['id', 43434], ['id', 20451], ['id', 33598]], 'labels': [5, 8, 2, 3, 5], 'scores': [0.8805096827801382, 1.6143498357464923, 2.166739489363364, 2.5346178722345964, 2.7473750767878116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.279963493347168})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.5639421939849854})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.8732799291610718})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.8459527492523193})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.8661037683486938})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.9185311794281006})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7577674388885498})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 2.000917911529541})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 2.0845298767089844})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 2.142368793487549})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8083, 'crossentropy': 1.663012109375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8772007822990417})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.82183837890625})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7893553972244263})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8316196203231812})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.7999753952026367})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8106893301010132})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.7577013969421387})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.7692841291427612})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 13030], ['id', 21306], ['id', 57159], ['id', 51979], ['id', 32211]], 'labels': [0, 3, 9, 4, 6], 'scores': [1.2443396096188102, 2.0470876772498854, 2.661096360790837, 3.0083558982881904, 3.1896976161834862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.125731110572815})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3675638437271118})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.3050085306167603})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3954864740371704})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.5797086954116821})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.5249333381652832})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.848, 'crossentropy': 1.140887109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8307174444198608})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7488121390342712})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7048910856246948})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.733528733253479})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7049334049224854})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 34758], ['id', 39034], ['id', 48811], ['id', 53641], ['id', 19501]], 'labels': [8, 9, 2, 5, 3], 'scores': [0.8437135536386096, 1.5696919962778768, 2.1193268295352325, 2.488433043638098, 2.714659352059334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0948854684829712})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.249393343925476})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3686045408248901})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4722118377685547})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.432271957397461})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.6129494905471802})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.5921638011932373})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.6251506805419922})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8466, 'crossentropy': 1.3484720703125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8594447374343872})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7263855934143066})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.7222017645835876})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7110495567321777})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.6963632106781006})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 26593], ['id', 32702], ['id', 43345], ['id', 30446], ['id', 51846]], 'labels': [-1, 5, 2, 9, -1], 'scores': [0.7924094612325931, 1.5096967302418598, 2.098280983738146, 2.469330329605489, 2.6796661952506824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0584852695465088})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.083823561668396})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.4201321601867676})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3250586986541748})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3455899953842163})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8516, 'crossentropy': 1.0000279296875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8449684381484985})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7363482713699341})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7005715370178223})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.6809201240539551})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 13460], ['id', 37655], ['id', 50632], ['id', 3941], ['id', 16858]], 'labels': [5, 2, 1, 3, -1], 'scores': [0.7043202504176966, 1.3319033651900072, 1.8117194632162432, 2.1511792584829506, 2.370687531501412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0337814092636108})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0808439254760742})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2734498977661133})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2875326871871948})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2713173627853394})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.468862533569336})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.6371204853057861})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.6763861179351807})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8545, 'crossentropy': 1.237628125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8120281100273132})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7081178426742554})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.6545332670211792})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6703305244445801})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6751288771629333})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.660413384437561})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 42263], ['id', 47936], ['id', 51337], ['id', 13890], ['id', 32561]], 'labels': [4, 8, 4, 7, 2], 'scores': [0.7942292356299392, 1.510018762568897, 2.1068506247179126, 2.4929974697696817, 2.7285055711727217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0764808654785156})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2811598777770996})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3400355577468872})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.344713568687439})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3316237926483154})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.619072437286377})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5940322875976562})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5028023719787598})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8469, 'crossentropy': 1.31911796875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8278020620346069})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7431609630584717})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7194056510925293})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.6769644021987915})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.6877357959747314})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.6704514026641846})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.6932610273361206})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 55834], ['id', 56468], ['id', 2852], ['id', 26254], ['id', 38255]], 'labels': [9, 5, 7, -1, 7], 'scores': [0.9153594584107541, 1.6226778629089478, 2.1663830685701395, 2.54784998742511, 2.763656233666733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.003046989440918})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0288605690002441})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.285613775253296})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3898814916610718})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3920466899871826})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.856, 'crossentropy': 0.94638388671875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7648274898529053})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.6964483261108398})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6615293025970459})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.6372895240783691})
store['active_learning_steps'][12]['eval_training']['best_epoch']=1
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 42078], ['id', 26548], ['id', 53298], ['id', 46832], ['id', 40242]], 'labels': [4, 3, 0, 7, -1], 'scores': [0.7493601883690135, 1.3201207547193148, 1.7968286936754474, 2.1523758571801572, 2.3366159534330224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0695087909698486})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.162200689315796})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3083105087280273})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3707414865493774})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.34544038772583})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.540605068206787})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.469759225845337})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.727928876876831})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8514, 'crossentropy': 1.2049494140625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8423510193824768})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7509106397628784})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7113550901412964})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6679856777191162})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6374387145042419})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.6431127786636353})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6407476663589478})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 12345], ['id', 30418], ['id', 1814], ['id', 50391], ['id', 32035]], 'labels': [3, 8, 4, 9, 2], 'scores': [0.8893110739356291, 1.6587805270705234, 2.228865299306876, 2.568926585464479, 2.738169594905685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0703905820846558})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0333547592163086})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1587798595428467})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2641781568527222})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4428205490112305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3775966167449951})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4962968826293945})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.611109972000122})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.4211676120758057})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2618987560272217})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4536105394363403})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.420149803161621})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.354958176612854})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.600707769393921})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.8548824787139893})
store['active_learning_steps'][14]['training']['best_epoch']=12
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 1.31599296875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8555448651313782})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7268595695495605})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6965789794921875})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6959167718887329})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6650335192680359})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6462774276733398})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 35103], ['id', 33035], ['id', 34578], ['id', 30511], ['id', 37111]], 'labels': [8, 6, 6, 3, 9], 'scores': [0.8769927827069224, 1.6584107033977742, 2.2639781317861987, 2.644029035851153, 2.827325126768538]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8886845111846924})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0445334911346436})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.074925184249878})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.215078592300415})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0231189727783203})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2215497493743896})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.4202945232391357})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2808033227920532})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8784, 'crossentropy': 0.991975390625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7309116125106812})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6129828691482544})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6027870178222656})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5704360008239746})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5681842565536499})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 18317], ['id', 46776], ['id', 40987], ['id', 45944], ['id', 12607]], 'labels': [8, 8, -1, 9, -1], 'scores': [0.7994670486084072, 1.5025898572035152, 2.0817670610332364, 2.461890040180311, 2.676784569287232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9162227511405945})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8718092441558838})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0650529861450195})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0366491079330444})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.019441843032837})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0586822032928467})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0975407361984253})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1664751768112183})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1511309146881104})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1831029653549194})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.934726953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.756938099861145})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.648326575756073})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.611247718334198})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5256673097610474})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5130613446235657})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5266008377075195})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.5272709131240845})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 11804], ['id', 19229], ['id', 23546], ['id', 57979], ['id', 56780]], 'labels': [3, 2, 5, 1, 7], 'scores': [0.8092899547461563, 1.5566413675518223, 2.1409138608025495, 2.508472887472972, 2.6915653806382904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9448109865188599})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.780133843421936})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7949299216270447})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.77663654088974})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8142807483673096})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8871362209320068})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9679298400878906})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0523496866226196})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.726332958984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6649404168128967})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5247719883918762})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5362987518310547})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.48045992851257324})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.47816866636276245})
store['active_learning_steps'][17]['eval_training']['best_epoch']=2
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 54106], ['id', 53019], ['id', 40622], ['id', 53696], ['id', 38114]], 'labels': [7, 2, 2, 5, -1], 'scores': [0.8561928726773786, 1.6026105173485408, 2.1737988554838346, 2.478995907450937, 2.640049903652029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8868058919906616})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7518860101699829})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.801246702671051})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8944331407546997})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9101656675338745})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9524767994880676})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0489990711212158})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.71487978515625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6784343719482422})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5607858300209045})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5590776205062866})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5322599411010742})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5156294703483582})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 58840], ['id', 21040], ['id', 34902], ['id', 22505], ['id', 26635]], 'labels': [-1, 9, 2, 9, -1], 'scores': [0.7539226503243013, 1.4507127128536061, 1.9727347805037674, 2.3349477311755846, 2.5102713672002963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8206256628036499})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6972358822822571})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7438109517097473})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9156185388565063})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9032445549964905})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.898, 'crossentropy': 0.63672919921875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7453804016113281})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5496798157691956})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.557128369808197})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5289599895477295})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 56300], ['id', 30764], ['id', 42121], ['id', 3494], ['id', 25706]], 'labels': [9, 7, 5, 7, 9], 'scores': [0.670420481629594, 1.2810508203479256, 1.7795287548453667, 2.156618701245818, 2.4025191258028524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9277684688568115})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7862553000450134})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8151251077651978})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7734056115150452})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8359036445617676})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8075321912765503})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8858500719070435})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.620170654296875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7184037566184998})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5385896563529968})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4884774088859558})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.4980531930923462})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.46565067768096924})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4592519998550415})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 28305], ['id', 18003], ['id', 48102], ['id', 26254], ['id', 8763]], 'labels': [0, 2, 7, -1, 0], 'scores': [0.7452722539060754, 1.4266758670688051, 1.9518987616564605, 2.295075621417956, 2.534184924597689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9387615919113159})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6977494955062866})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6967588663101196})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7305092811584473})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7699509263038635})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7010469436645508})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7017083168029785})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8447257876396179})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8673394918441772})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.61409091796875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7318835854530334})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5447597503662109})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.47030627727508545})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.44778966903686523})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.45089736580848694})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.45013928413391113})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4492641091346741})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 46610], ['id', 5331], ['id', 4058], ['id', 20942], ['id', 39359]], 'labels': [5, 4, 8, 3, 3], 'scores': [0.8388404691134652, 1.579807086893175, 2.1624987235477384, 2.5635915397672555, 2.7895847111366336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.870869517326355})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6242483854293823})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6540331244468689})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6702861785888672})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6187936067581177})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7167999744415283})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7386869788169861})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8434959053993225})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.587017333984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6287708282470703})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5113914608955383})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4620036482810974})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4179975390434265})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4174622893333435})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4469089210033417})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4082585275173187})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 48735], ['id', 36692], ['id', 36141], ['id', 59744], ['id', 5728]], 'labels': [-1, 0, 1, 6, 3], 'scores': [0.7753918968861215, 1.4737612666902296, 2.068228614032664, 2.4575348816481393, 2.7120607852977523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8406684398651123})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6870019435882568})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.679050087928772})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6269720196723938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6407082676887512})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9369287490844727})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7109570503234863})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9156, 'crossentropy': 0.568168310546875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7343711853027344})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5195208787918091})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5386084914207458})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5189369320869446})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4793183207511902})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4480534791946411})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 35864], ['id', 50602], ['id', 44961], ['id', 11146], ['id', 11044]], 'labels': [5, 5, 8, 8, 4], 'scores': [0.6955071511388784, 1.3231949585656602, 1.8172591803297626, 2.1605303873290778, 2.3815468062845957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8378733396530151})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6164746284484863})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6098479628562927})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6693160533905029})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6782528758049011})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6534688472747803})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6479758024215698})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6881502270698547})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6610028743743896})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6753043532371521})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6324048042297363})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7524319887161255})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7390843629837036})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6809672117233276})
store['active_learning_steps'][24]['training']['best_epoch']=11
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.569258642578125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6924164295196533})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5363065004348755})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4658541679382324})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.40880149602890015})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.396125465631485})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3859388530254364})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.38728708028793335})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3788438141345978})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38552549481391907})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3569670021533966})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3626407980918884})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.35795387625694275})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3600561022758484})
store['active_learning_steps'][24]['eval_training']['best_epoch']=10
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 52582], ['id', 55628], ['id', 50111], ['id', 34314], ['id', 20092]], 'labels': [2, 3, 5, 7, -1], 'scores': [0.780926831780071, 1.4946932600342167, 2.1200799427596717, 2.5239820113305758, 2.7636696533930527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8792165517807007})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6071354746818542})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6300911903381348})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6590371131896973})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6923538446426392})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7156288027763367})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7461613416671753})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.5743533203125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.669867217540741})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5200405716896057})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4712024927139282})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.44143056869506836})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40336304903030396})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.41026824712753296})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 30123], ['id', 6574], ['id', 34740], ['id', 43952], ['id', 20232]], 'labels': [0, -1, 3, -1, -1], 'scores': [0.7679082720786643, 1.4697893079405433, 2.027770788626049, 2.4195688427954707, 2.6954676446597787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9408974051475525})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6375077962875366})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6087517738342285})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6428690552711487})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6635602712631226})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6668967008590698})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7156038284301758})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.750527024269104})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.638448876953125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7022703886032104})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5365604758262634})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.46346136927604675})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.46908771991729736})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.42459380626678467})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.4541076421737671})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4170597791671753})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 26852], ['id', 27157], ['id', 59297], ['id', 2622], ['id', 21303]], 'labels': [8, 7, 1, 5, 2], 'scores': [0.7958872654840035, 1.4710722485855885, 2.001478573725035, 2.3767852278808617, 2.6262675175821713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.991483211517334})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7629644274711609})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6757709980010986})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6558560132980347})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6610660552978516})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7987560033798218})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7035472393035889})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7210856676101685})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6728147268295288})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7968766689300537})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.6595623046875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7148799300193787})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5319822430610657})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.46639055013656616})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.45974358916282654})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4195072650909424})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.420806348323822})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.40609073638916016})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 33812], ['id', 50370], ['id', 59509], ['id', 50826], ['id', 11785]], 'labels': [6, 7, 6, 2, 5], 'scores': [0.8023163332791399, 1.4912337726816576, 2.0717787103424685, 2.437119745817923, 2.6386278925856583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.971712589263916})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6568410396575928})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7271371483802795})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6536999940872192})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7116680145263672})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7434519529342651})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6681607961654663})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.695548415184021})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7026292681694031})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7976114749908447})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7232163548469543})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7225775122642517})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.590769287109375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7187110185623169})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5335505604743958})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4405450224876404})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41382068395614624})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.39397597312927246})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.381636381149292})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3763342499732971})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 21601], ['id', 39673], ['id', 54195], ['id', 13680], ['id', 30220]], 'labels': [1, 2, 8, 8, 0], 'scores': [0.9060747415390669, 1.610942985257518, 2.1958666171482255, 2.5748803917801695, 2.781731512578461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8933334350585938})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5701218247413635})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5377066135406494})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6633853316307068})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.646584153175354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.617753267288208})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6917208433151245})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6850392818450928})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7636985778808594})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.558205322265625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.683380126953125})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5114555358886719})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4418855309486389})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46723753213882446})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4075029790401459})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.3864896893501282})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.37446367740631104})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.3941879868507385})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 3719], ['id', 21608], ['id', 58575], ['id', 11625], ['id', 26565]], 'labels': [2, 0, -1, 8, -1], 'scores': [0.7727583991782583, 1.461626732151581, 2.0151275588710194, 2.3530956641679115, 2.5457983509160087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9008787870407104})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5766735672950745})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5908573865890503})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5533046126365662})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5436094403266907})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6266071796417236})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.742164671421051})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6089050769805908})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.49981884765625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6705034971237183})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5600413084030151})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4505753517150879})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4443826377391815})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.39336976408958435})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41241157054901123})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3909265995025635})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 51939], ['id', 41133], ['id', 1497], ['id', 59823], ['id', 39516]], 'labels': [-1, 8, -1, 5, 5], 'scores': [0.7354806980151762, 1.3697620000136177, 1.9075088078037687, 2.3018786835527187, 2.5933521514165383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9198969602584839})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5535348057746887})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5280998349189758})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6050582528114319})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6367287635803223})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.578937828540802})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.48608623046875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6867391467094421})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5090643167495728})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4529808759689331})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.41501420736312866})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4134158790111542})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 18739], ['id', 52099], ['id', 13259], ['id', 45024], ['id', 20500]], 'labels': [3, 2, 1, 5, 3], 'scores': [0.707732287444548, 1.2863221363153459, 1.7618263800229021, 2.121945064448127, 2.3708979707531537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9459028244018555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5772684812545776})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5283319354057312})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5869936943054199})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5558484792709351})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5418675541877747})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6539871692657471})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6635031700134277})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6117606163024902})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.494930517578125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6996973752975464})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.466877818107605})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4137699007987976})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3919801115989685})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37308019399642944})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36689329147338867})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3557594418525696})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3519994616508484})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 18255], ['id', 262], ['id', 24479], ['id', 17076], ['id', 53784]], 'labels': [-1, 2, 8, -1, -1], 'scores': [0.8118166908001627, 1.532170948558516, 2.0501762973781954, 2.364947087777373, 2.5427009536936307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9398585557937622})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5846520662307739})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5422295928001404})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.554006040096283})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5488446950912476})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5969778299331665})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5905771851539612})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.536634716796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6949454545974731})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4695761799812317})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.44669705629348755})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.40898755192756653})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.39301320910453796})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3930874764919281})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 19276], ['id', 11904], ['id', 13573], ['id', 6673], ['id', 2839]], 'labels': [6, 8, -1, -1, 0], 'scores': [0.7208285826110417, 1.3842048714207977, 1.909535599790643, 2.2879744163682396, 2.553822320585839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9329588413238525})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6000697612762451})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5322974324226379})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5788992643356323})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5604445934295654})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5559892058372498})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6582450270652771})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.4938578125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6936883330345154})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4810546040534973})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45353564620018005})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43766820430755615})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3964686095714569})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3872358202934265})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 40766], ['id', 9340], ['id', 3470], ['id', 30932], ['id', 42573]], 'labels': [4, 5, 2, 0, 7], 'scores': [0.7540335425112801, 1.3842010390925195, 1.8910632929037163, 2.229203301833733, 2.4342046705439486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9570069909095764})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5347698926925659})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48817986249923706})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45972251892089844})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49181610345840454})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6159067153930664})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5857880115509033})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.413012890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7297199368476868})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48161977529525757})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42895591259002686})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3940991759300232})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3681376874446869})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34568291902542114})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 8297], ['id', 37048], ['id', 13103], ['id', 10275], ['id', 40370]], 'labels': [7, 9, -1, 6, 7], 'scores': [0.6964188659716566, 1.3464801003701607, 1.8764801786795804, 2.2403436174925133, 2.4988672935915437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9047768115997314})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5550259351730347})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4996801018714905})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5929780602455139})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5345456600189209})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6077432036399841})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.45780703125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7430771589279175})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5132573246955872})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44249117374420166})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4156639873981476})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41231977939605713})
store['active_learning_steps'][36]['eval_training']['best_epoch']=5
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 54556], ['id', 14749], ['id', 23588], ['id', 37750], ['id', 49563]], 'labels': [2, 0, 7, 5, 8], 'scores': [0.738644010129665, 1.389119717005883, 1.9027008512844148, 2.289178928681797, 2.5114773528637233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8756781816482544})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5040508508682251})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5185877084732056})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47724294662475586})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5134370923042297})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5443062782287598})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.518355131149292})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6219050884246826})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5335532426834106})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6138039827346802})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5786459445953369})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5826417207717896})
store['active_learning_steps'][37]['training']['best_epoch']=9
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9464, 'crossentropy': 0.47157041015625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7097393274307251})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4473501443862915})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4338996410369873})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3514912724494934})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35176390409469604})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3277965188026428})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.342958003282547})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 49143], ['id', 39678], ['id', 51991], ['id', 32823], ['id', 34972]], 'labels': [9, 3, 3, -1, -1], 'scores': [0.8150322513033068, 1.5497587598170486, 2.0804696957653848, 2.442854073978754, 2.7012794847469204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9528661966323853})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5153735876083374})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4893122911453247})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.467382550239563})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5051167011260986})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48648330569267273})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5390563011169434})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.398174609375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7164177894592285})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4536895155906677})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4472843110561371})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4039217233657837})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3882167637348175})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3407488465309143})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 34829], ['id', 49890], ['id', 13827], ['id', 45778], ['id', 46230]], 'labels': [5, 5, 3, -1, -1], 'scores': [0.694399526290651, 1.348656658027064, 1.8310432973408064, 2.171135169172371, 2.3967113604060284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9578256607055664})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5343980193138123})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5158222913742065})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4819740653038025})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.501603364944458})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5206844806671143})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5983003377914429})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.544641375541687})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.428444775390625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6918476223945618})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4718654155731201})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41583502292633057})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38834697008132935})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3745284974575043})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3777073323726654})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.35517317056655884})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 26663], ['id', 54316], ['id', 21335], ['id', 24086], ['id', 12379]], 'labels': [9, -1, 7, -1, 8], 'scores': [0.682487242402174, 1.317832277198646, 1.8300738384525133, 2.230810035327888, 2.4873652344442894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8861346244812012})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5399148464202881})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45429956912994385})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45612433552742004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47656601667404175})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4999593496322632})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5371980667114258})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5227145552635193})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.376775146484375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6432057619094849})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46980687975883484})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3829616606235504})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3462725877761841})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.35355281829833984})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.33509352803230286})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 12950], ['id', 57495], ['id', 8678], ['id', 48975], ['id', 21602]], 'labels': [2, -1, 1, 2, 0], 'scores': [0.6945070874113992, 1.3148492564486944, 1.816591161241134, 2.1926295144133308, 2.449262557156815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9716842174530029})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5083606243133545})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44120609760284424})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45440906286239624})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46606725454330444})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4293421506881714})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.3958067138671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6611165404319763})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5037854313850403})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44293248653411865})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41536152362823486})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.406558096408844})
store['active_learning_steps'][41]['eval_training']['best_epoch']=3
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 20208], ['id', 8714], ['id', 24630], ['id', 11889], ['id', 22097]], 'labels': [-1, 9, 5, 5, -1], 'scores': [0.5875943625182618, 1.1375114818412078, 1.605507682554081, 1.9769553601684269, 2.231076551891004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.099257230758667})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.519436240196228})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4768728017807007})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42563438415527344})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4805508852005005})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5295017957687378})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5016490817070007})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48354220390319824})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5070382356643677})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.521672248840332})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5503987669944763})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9514, 'crossentropy': 0.4061818115234375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7576912045478821})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48912739753723145})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.37528854608535767})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3420610725879669})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3403583765029907})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.32341429591178894})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.32426977157592773})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 32178], ['id', 40009], ['id', 2574], ['id', 56086], ['id', 45496]], 'labels': [4, -1, -1, -1, 7], 'scores': [0.7253484178255143, 1.3933648461286503, 1.9188965155912028, 2.3200001293117696, 2.5832728192143897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.891412615776062})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5305955410003662})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5056290030479431})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4926621913909912})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5028502941131592})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5740231871604919})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5989903807640076})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9414, 'crossentropy': 0.4045294921875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7300338745117188})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4761701226234436})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40959417819976807})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36767899990081787})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3970929682254791})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35895437002182007})
store['active_learning_steps'][43]['eval_training']['best_epoch']=6
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 7168], ['id', 51351], ['id', 42515], ['id', 23094], ['id', 20349]], 'labels': [8, -1, 8, 7, 0], 'scores': [0.6881677835970192, 1.2415941705350058, 1.672304863634733, 1.983602966065373, 2.1800064140525706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8497937917709351})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.524900496006012})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41903620958328247})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4614611268043518})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41386914253234863})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45326489210128784})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4551468789577484})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4656757116317749})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47750765085220337})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48068827390670776})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.48149383068084717})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3902189208984375}
