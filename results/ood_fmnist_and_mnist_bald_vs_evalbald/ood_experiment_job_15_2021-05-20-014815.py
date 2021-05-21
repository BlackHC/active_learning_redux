store = {}
store['timestamp']=1621471695
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=15']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=15
store['worker_id']=15
store['num_workers']=80
store['config']={'seed': 1249, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 2.595541000366211})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.1657137870788574})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7094192504882812})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2727322578430176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 4.053597450256348})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.6105568408966064})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.170261383056641})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.025538444519043})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5915, 'crossentropy': 4.1397609375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 14801], ['id', 31847], ['id', 1306], ['id', 14819], ['id', 13428]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.518543117451967, 2.750143974484363, 3.6307427647485646, 4.153721780612339, 4.4117941556387406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.360161781311035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.9483163356781006})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.270195960998535})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3624415397644043})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.541487693786621})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5934, 'crossentropy': 3.2379041015625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 31191], ['id', 47260], ['id', 27393], ['id', 59389], ['id', 41802]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.49864482860945, 2.624465187227023, 3.4440955716119337, 3.9696047079995846, 4.272502894521902]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.1756772994995117})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.240177631378174})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.876330852508545})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2014145851135254})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.297078847885132})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1325764656066895})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.46415638923645})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.7632880210876465})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5617926120758057})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.2545199394226074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.40230655670166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.748072624206543})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.4661409854888916})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.252201557159424})
store['active_learning_steps'][2]['training']['best_epoch']=11
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6034, 'crossentropy': 3.73337734375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 2034], ['id', 42333], ['id', 17736], ['id', 13952], ['id', 20331]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6588136283399582, 2.957272288764446, 3.8467914370335556, 4.2819989000343, 4.472718975768101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.439840316772461})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.910388946533203})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.0789031982421875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.859178304672241})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.751127004623413})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.793333053588867})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.9159011840820312})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.929150104522705})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 4.001773834228516})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.677957773208618})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.582479953765869})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5399222373962402})
store['active_learning_steps'][3]['training']['best_epoch']=9
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5962, 'crossentropy': 4.06428359375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 21931], ['id', 23110], ['id', 6425], ['id', 7621], ['id', 2353]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6011622182750562, 2.797374274249024, 3.6388050534575243, 4.151105823511069, 4.404861311822144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.389259099960327})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.059485673904419})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.647200345993042})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9648327827453613})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5278615951538086})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5917, 'crossentropy': 3.136726171875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 56094], ['id', 13259], ['id', 31046], ['id', 31414], ['id', 55778]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.5630636798623998, 2.673167103606976, 3.540396569376478, 4.057843997157905, 4.338292726084884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.3376779556274414})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.776057243347168})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.2328314781188965})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4879255294799805})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.612868309020996})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5964, 'crossentropy': 2.8914900390625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 18598], ['id', 32504], ['id', 41945], ['id', 23086], ['id', 27419]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3918943125813419, 2.5685882851579693, 3.391209676212098, 3.9036316679719167, 4.217828283469901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.2400636672973633})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.196803092956543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.664616823196411})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6500656604766846})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 2.4165111328125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 14260], ['id', 14661], ['id', 8029], ['id', 19791], ['id', 45018]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1685395412360986, 2.1147616705757426, 2.904052475566349, 3.4902636866370367, 3.8821940139033853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.292771339416504})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.862351417541504})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.167914867401123})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3130550384521484})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0548853874206543})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9315648078918457})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4495973587036133})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.405985116958618})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5903, 'crossentropy': 3.35634375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 32504], ['id', 53479], ['id', 4827], ['id', 11030], ['id', 53038]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4913080409611652, 2.6582120859097227, 3.503660491380094, 4.053020994277341, 4.335216333725857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.2879273891448975})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.9168972969055176})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.141235828399658})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.372370481491089})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.317981719970703})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.373927116394043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8890275955200195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6433863639831543})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.22456693649292})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5946, 'crossentropy': 3.70074765625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 18617], ['id', 36329], ['id', 1865], ['id', 13242], ['id', 22013]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6626987123834955, 2.896320579156071, 3.7523952103852647, 4.21122391325525, 4.4404646633170035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.0851616859436035})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5859508514404297})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.163268566131592})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.306629180908203})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.302478313446045})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 2.682985546875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 57328], ['id', 23421], ['id', 23704], ['id', 9523], ['id', 38365]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4865785166306562, 2.6289402112668103, 3.4592023472940836, 3.987920362601817, 4.289351778639978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.219877243041992})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0340054035186768})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.2968215942382812})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.448615074157715})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 2.41857578125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 54588], ['id', 12263], ['id', 17728], ['id', 26184], ['id', 30123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5266740056105546, 2.6289473012210465, 3.4584215575364396, 3.9674039830851857, 4.234321610547401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.38118314743042})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.499889850616455})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7745895385742188})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.995150566101074})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2427501678466797})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6145, 'crossentropy': 2.8970287109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 488], ['id', 4893], ['id', 14068], ['id', 16911], ['id', 41814]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5974334790564884, 2.8042394580811205, 3.6084715173660538, 4.097632426990221, 4.3547846568651885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.982034683227539})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.548251152038574})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.974562644958496})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1457509994506836})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6054, 'crossentropy': 2.1927056640625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22960], ['id', 11437], ['id', 9202], ['id', 38861], ['id', 59152]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3545144945245093, 2.3733069480199527, 3.1824500736225634, 3.73521763751107, 4.075068340262133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.2022407054901123})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.045429229736328})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9205379486083984})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.256887912750244})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.3462929725646973})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.503453254699707})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.323208808898926})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3391008377075195})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.557445526123047})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.8571534156799316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.2659878730773926})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 3.496357421875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 12906], ['id', 30366], ['id', 51728], ['id', 25315], ['id', 36761]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.543608245858909, 2.8017017385158063, 3.715651304984201, 4.174262599787061, 4.406858889358162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.023301124572754})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.628518581390381})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.689544200897217})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.7912485599517822})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.698679208755493})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.0877926349639893})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7871789932250977})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7513768672943115})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.9996604919433594})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.193113088607788})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.898097515106201})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6428, 'crossentropy': 3.01728046875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 55038], ['id', 14129], ['id', 45294], ['id', 30845], ['id', 52590]], 'labels': [-1, -1, -1, 6, 2], 'scores': [1.5473111941223388, 2.803497839777139, 3.6232228153462103, 4.144110048910074, 4.39979907209338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.043508768081665})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.2955338954925537})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6708531379699707})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1379501819610596})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8167567253112793})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6244, 'crossentropy': 2.4869181640625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 45148], ['id', 224], ['id', 34202], ['id', 12748], ['id', 22643]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3894304874767922, 2.479965534252619, 3.272728528366546, 3.8161559219476553, 4.144930889083029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9514379501342773})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.7143337726593018})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9075608253479004})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.10941743850708})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.865138530731201})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1427626609802246})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.434404134750366})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.474514961242676})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.0302833984375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 18026], ['id', 51004], ['id', 44955], ['id', 51477], ['id', 27413]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5494578283048095, 2.7587060900873537, 3.6461718064188435, 4.129592400443778, 4.388233400641305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.090501070022583})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5468201637268066})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.957399845123291})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.422844886779785})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.078742504119873})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.415839910507202})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3195509910583496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.868610143661499})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1136932373046875})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5779080390930176})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.941791296005249})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5636038780212402})
store['active_learning_steps'][17]['training']['best_epoch']=9
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6117, 'crossentropy': 3.443880078125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 31728], ['id', 24620], ['id', 42251], ['id', 22188], ['id', 47793]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4955477828751786, 2.7414315027046237, 3.5960200311565105, 4.119268561449285, 4.389707677997944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.895404577255249})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5589993000030518})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7979185581207275})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6351022720336914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.1444129943847656})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 2.6999462890625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 20001], ['id', 341], ['id', 47636], ['id', 22679], ['id', 48430]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4648394177557513, 2.6012947900248085, 3.4529276206816544, 3.947565166606955, 4.259920113810418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.299445152282715})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.669433355331421})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.3167192935943604})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.293870449066162})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.9457757472991943})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3698065280914307})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.7707595825195312})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6450300216674805})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8227617740631104})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.091949462890625})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.8604073524475098})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 3.555468359375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 32056], ['id', 51477], ['id', 8074], ['id', 68], ['id', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6177562113904234, 2.7984325070141916, 3.638544776989602, 4.091408862908659, 4.362842122985582]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.028439521789551})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6501665115356445})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2888412475585938})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3207993507385254})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.355564594268799})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1615805625915527})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1788406372070312})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1358895301818848})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.7964792251586914})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.487183094024658})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6061, 'crossentropy': 3.343730078125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 44686], ['id', 17719], ['id', 8509], ['id', 51314], ['id', 44491]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.5520193000878777, 2.7621424870820173, 3.5935491261443957, 4.11027361434761, 4.371416695788255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.930129051208496})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.462583065032959})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8129820823669434})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.9113664627075195})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.865118980407715})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.103055477142334})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0091323852539062})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0091848373413086})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 2.9908955078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 49418], ['id', 28533], ['id', 48176], ['id', 51071], ['id', 43823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6382944071672103, 2.9186941775242197, 3.7695918592665354, 4.221683245326936, 4.419431959953384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.0326271057128906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3363938331604004})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8764472007751465})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.109680414199829})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.125049114227295})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6138, 'crossentropy': 2.5798119140625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 49474], ['id', 31514], ['id', 54134], ['id', 30051], ['id', 43683]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4931465332468548, 2.6912044017001895, 3.5190134481604476, 4.046973301800112, 4.307562845980689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0331833362579346})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.8850269317626953})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.693769931793213})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7228739261627197})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1265430450439453})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1385583877563477})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0632596015930176})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0527710914611816})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2226290702819824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.932422161102295})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.555220603942871})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.614, 'crossentropy': 3.322634765625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 14716], ['id', 906], ['id', 18273], ['id', 36744], ['id', 31020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.59910445277281, 2.7603513417394367, 3.5983113307328347, 4.109153186197755, 4.387523599200681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.099364757537842})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.7701449394226074})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.0381264686584473})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.314332962036133})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5860276222229004})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.4508156776428223})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.8265037536621094})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6025, 'crossentropy': 3.489378515625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 36662], ['id', 14185], ['id', 38861], ['id', 12748], ['id', 4023]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5153288156398572, 2.7124403553710494, 3.5795594243170576, 4.06306106888268, 4.3288252609831925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8620147705078125})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.5410900115966797})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5647847652435303})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.924070119857788})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.8841280937194824})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.825878620147705})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5852737426757812})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 3.1936849609375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 46590], ['id', 27181], ['id', 22626], ['id', 4688], ['id', 55314]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.445905374761657, 2.68635270402097, 3.5636775895347306, 4.059073221782224, 4.329705340809175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.2952990531921387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.772312641143799})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8904292583465576})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.012924909591675})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.373868942260742})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.4065451622009277})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.541219472885132})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.5979, 'crossentropy': 3.4116765625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 28563], ['id', 49418], ['id', 46441], ['id', 46551], ['id', 17542]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5284521876106913, 2.7698109839467686, 3.633065374460193, 4.10444640588969, 4.348534795194185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.043025016784668})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5856618881225586})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8930234909057617})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0356297492980957})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4330344200134277})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1934008598327637})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.337329626083374})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.4409520626068115})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5238535404205322})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1422595977783203})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2021334171295166})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6102, 'crossentropy': 3.632947265625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 4927], ['id', 27344], ['id', 19523], ['id', 19187], ['id', 56866]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.538223037896803, 2.7608634072402385, 3.6603034547231186, 4.144364602037591, 4.395452888295009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.0597875118255615})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.4295413494110107})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.7087578773498535})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2173662185668945})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2750532627105713})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1192851066589355})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2269420623779297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6419246196746826})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.460376501083374})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.494302272796631})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.518496513366699})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 3.52713125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42092], ['id', 39336], ['id', 55490], ['id', 28787], ['id', 43940]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.557606851209729, 2.7886258127834647, 3.627540098800626, 4.134024516800093, 4.380060792306617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.1449615955352783})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.774778366088867})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2079758644104004})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.483822822570801})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.5895, 'crossentropy': 2.2287013671875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 3701], ['id', 17882], ['id', 14163], ['id', 12748], ['id', 17480]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3069389146205426, 2.474595640631028, 3.2129122532346086, 3.751530019661426, 4.088780019164888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.125547409057617})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.69352388381958})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.868856906890869})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8983664512634277})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9599967002868652})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.917717933654785})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.2885537147521973})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2071871757507324})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.296980857849121})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6341, 'crossentropy': 2.9178978515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 18313], ['id', 46711], ['id', 48337], ['id', 15215], ['id', 42325]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5882083550779786, 2.911378000175084, 3.6979748351449615, 4.1533683840018085, 4.373790908078405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.062627077102661})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.764385461807251})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1885786056518555})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.832712173461914})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2207467555999756})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.5294864177703857})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.351109027862549})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6098, 'crossentropy': 3.173050390625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 50388], ['id', 51276], ['id', 15213], ['id', 12254], ['id', 25051]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6842554872343243, 2.945331761514627, 3.7537708603123274, 4.228657692873779, 4.434282447058707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.070911407470703})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.78768253326416})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1350436210632324})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.063063144683838})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.5883, 'crossentropy': 2.1716197265625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 10221], ['id', 9565], ['id', 4216], ['id', 49196], ['id', 52803]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3851072586825084, 2.4576390602235714, 3.206448621528999, 3.69080871467461, 4.043239547490797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.059492826461792})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7363100051879883})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.841359853744507})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9253287315368652})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2766106128692627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3903143405914307})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.8415074348449707})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6154, 'crossentropy': 2.9827943359375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 1258], ['id', 22769], ['id', 12254], ['id', 54357], ['id', 31020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4887333283943334, 2.6688693237609753, 3.515731645364797, 4.039881504357885, 4.309537670974484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9778474569320679})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7396769523620605})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8386075496673584})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.00555419921875})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8952746391296387})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.607429027557373})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.436340808868408})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.131222724914551})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.640439033508301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.307448387145996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3985464572906494})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4432036876678467})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.790410041809082})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6409, 'crossentropy': 3.49619140625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 19983], ['id', 21871], ['id', 32461], ['id', 13890], ['id', 7406]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5375222901887706, 2.7877661905304754, 3.718917740635492, 4.190192527363475, 4.426820251952561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.991020679473877})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.5261616706848145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9301648139953613})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.113677978515625})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.602, 'crossentropy': 2.16068671875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 35312], ['id', 25485], ['id', 48420], ['id', 8031], ['id', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3802212280860382, 2.404547698421541, 3.188205924843107, 3.753304068505975, 4.085763686621471]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.4902870655059814})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3070316314697266})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.808492660522461})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1633903980255127})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0766043663024902})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.3663811683654785})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 2.9654484375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 29166], ['id', 30626], ['id', 47220], ['id', 6364], ['id', 55517]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5138012312433013, 2.72558965054467, 3.5272608810295463, 4.037437875289756, 4.318435414509439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.08789324760437})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.6194238662719727})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.659686803817749})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.8972482681274414})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.116844654083252})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9742069244384766})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.22735595703125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.634510040283203})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.710660457611084})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6247, 'crossentropy': 3.1106333984375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 28900], ['id', 30279], ['id', 3362], ['id', 24620], ['id', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5920450558869967, 2.9275615602945266, 3.7459255434400625, 4.192466628892959, 4.406864942283015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.978118658065796})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.682441234588623})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.894376754760742})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.2756285667419434})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3590970039367676})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.592, 'crossentropy': 3.0700232421875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 13252], ['id', 44939], ['id', 16309], ['id', 20681], ['id', 16929]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5456419330964284, 2.7375719581136444, 3.5099310467478233, 4.004490709332729, 4.28192049955317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.0328330993652344})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.869504928588867})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6882476806640625})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0653793811798096})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.032956600189209})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.537794589996338})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.165274143218994})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.532226085662842})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.072195291519165})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 3.53149375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 32578], ['id', 26333], ['id', 4618], ['id', 55545], ['id', 36449]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.5057595977017706, 2.7331803198793234, 3.616803712377016, 4.125837397685213, 4.363804622344323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.9919464588165283})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.857654571533203})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8309803009033203})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.507509469985962})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.182859420776367})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2797493934631348})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.5968, 'crossentropy': 3.09019921875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 4829], ['id', 23283], ['id', 4765], ['id', 26761], ['id', 23441]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4822553315304328, 2.639152128145092, 3.5256182994752026, 4.042554468748009, 4.319262411120237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.144841432571411})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6582255363464355})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9847073554992676})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0888454914093018})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.4670958518981934})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.9526848793029785})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.5828, 'crossentropy': 3.28028984375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 55519], ['id', 35884], ['id', 7596], ['id', 48201], ['id', 35729]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5520320951860032, 2.853895999116976, 3.6458249997050682, 4.121344946793656, 4.369556710786532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9621143341064453})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.455611228942871})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.762925148010254})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.6964759826660156})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6043, 'crossentropy': 2.0719716796875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 6364], ['id', 2036], ['id', 13600], ['id', 16989], ['id', 56833]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2894766285774288, 2.2788537495041523, 3.0855252189785114, 3.6552558864422586, 3.996456612091208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.0454466342926025})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.7813620567321777})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1683197021484375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.1070899963378906})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6042, 'crossentropy': 2.1502087890625}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 25089], ['id', 39461], ['id', 38925], ['id', 7328], ['id', 54318]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.372279810424894, 2.397020657932064, 3.1715627896721506, 3.710422644205866, 4.0571332074600495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.9748568534851074})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5579662322998047})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.850407838821411})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0983896255493164})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.240750312805176})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.6031906604766846})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8056020736694336})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5306992530822754})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6210274696350098})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 3.54558046875}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 36357], ['id', 16292], ['id', 2880], ['id', 990], ['id', 55490]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4581402650188908, 2.71185410827539, 3.6153358009501444, 4.107420672025409, 4.356847913495316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.0951879024505615})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.412649631500244})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.681286334991455})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.92175555229187})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.953899383544922})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1908681392669678})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.5891363620758057})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6237, 'crossentropy': 3.155326953125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 969], ['id', 5091], ['id', 55546], ['id', 47412], ['id', 27413]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5650074794274893, 2.838432190361699, 3.649561923737105, 4.133255047699793, 4.385065622159154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9694623947143555})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6333017349243164})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9575178623199463})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.0302858352661133})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.5992, 'crossentropy': 2.0968677734375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 40378], ['id', 20894], ['id', 22679], ['id', 4829], ['id', 12748]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.243815207085686, 2.252490284911377, 3.008548814458214, 3.5429820931412106, 3.9105927361997033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.8816313743591309})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.2825517654418945})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.695496082305908})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5852925777435303})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.98321795463562})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6921396255493164})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.887033462524414})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.310718536376953})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.731375217437744})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.090073347091675})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.391132116317749})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.777223587036133})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 2.9661783203125}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 4641], ['id', 27181], ['id', 23982], ['id', 37040], ['id', 22774]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6811903647931947, 2.976293253668606, 3.809752535227852, 4.253923286761217, 4.470375604417516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.245337963104248})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.702791690826416})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7896828651428223})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.9657840728759766})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.4964146614074707})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6109, 'crossentropy': 2.6732900390625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 10236], ['id', 10302], ['id', 18729], ['id', 35158], ['id', 42749]], 'labels': [-1, -1, 3, -1, -1], 'scores': [1.4085715598296948, 2.546190968003595, 3.3718668885939422, 3.9179017364861615, 4.246538985751787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0377912521362305})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.3386261463165283})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.5403027534484863})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1203536987304688})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 2.0783134765625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 9373], ['id', 48216], ['id', 2608], ['id', 47650], ['id', 16357]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2796369578169022, 2.362291101052497, 3.195125395111549, 3.748749371418942, 4.083901834847478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.214655876159668})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.3657286167144775})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7297141551971436})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.924241781234741})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0383901596069336})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.35200834274292})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.999699592590332})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.319664478302002})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6184, 'crossentropy': 3.0958716796875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 31191], ['id', 2036], ['id', 54220], ['id', 16430], ['id', 4103]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5459341985089756, 2.7765960261676277, 3.6551998662770613, 4.132233272009101, 4.373961963007177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0400328636169434})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3397865295410156})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.606652021408081})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.923689365386963})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.070155620574951})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8156940937042236})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 2.7129462890625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 54171], ['id', 37040], ['id', 58078], ['id', 9523], ['id', 19959]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.60111982396361, 2.8164664240304185, 3.6599961201652222, 4.14550606950856, 4.376925796267841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.0188467502593994})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.847759962081909})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4383912086486816})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7146100997924805})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8630905151367188})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2400898933410645})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6237, 'crossentropy': 2.6839494140625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 28517], ['id', 28900], ['id', 30776], ['id', 59726], ['id', 49138]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3868912455391789, 2.593263730733394, 3.449431241117847, 3.9714524781446903, 4.2715514878542304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.0256338119506836})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.844146966934204})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.77432918548584})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.264103889465332})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2413744926452637})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.368192434310913})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.373100757598877})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.773827314376831})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.662506103515625})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.9681434631347656})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.5911, 'crossentropy': 3.7206390625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 38284], ['id', 43279], ['id', 59273], ['id', 24627], ['id', 56574]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5618850109978841, 2.849953905310149, 3.7070089236093153, 4.194816925566187, 4.426216944042848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.986133098602295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.8074934482574463})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.1057486534118652})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.0741117000579834})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6048, 'crossentropy': 2.035691015625}
