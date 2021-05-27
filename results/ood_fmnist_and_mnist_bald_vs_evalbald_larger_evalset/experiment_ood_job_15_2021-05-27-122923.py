store = {}
store['timestamp']=1622114963
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=15']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
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
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 14801], ['ood', 31847], ['ood', 1306], ['ood', 14819], ['ood', 13428]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5185431154476094, 2.75014396872235, 3.6307427576967903, 4.153721756435526, 4.411794122702561]}
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
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 31191], ['ood', 47260], ['ood', 27393], ['ood', 59389], ['ood', 41802]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4986448270656076, 2.6244651799317302, 3.4440955610025217, 3.9696046877006275, 4.2725028659029824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.1756772994995117})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.2401773929595947})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.876331090927124})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2014145851135254})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2970786094665527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1325764656066895})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4641566276550293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.7632880210876465})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5617926120758057})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.2545199394226074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.40230655670166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.748072862625122})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.4661412239074707})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.252201557159424})
store['active_learning_steps'][2]['training']['best_epoch']=11
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6034, 'crossentropy': 3.73337734375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 2034], ['ood', 42333], ['ood', 17736], ['ood', 13952], ['ood', 20331]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.658813627299578, 2.9572722793428303, 3.84679143056659, 4.281998889443639, 4.472718958945073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.439840316772461})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.9103891849517822})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.0789031982421875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.859178066253662})
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
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 21931], ['ood', 23110], ['ood', 6425], ['ood', 7621], ['ood', 2353]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6011622170367241, 2.797374273819003, 3.6388050550591107, 4.151105826580276, 4.404861302485344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.389259099960327})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.059485673904419})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.647200345993042})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9648327827453613})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5278615951538086})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5917, 'crossentropy': 3.1367263671875}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 56094], ['ood', 13259], ['ood', 31046], ['ood', 31414], ['id', 55778]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.5630636791732062, 2.6731670956451388, 3.5403965542761444, 4.057843972830623, 4.338292693383659]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.3376779556274414})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.776057243347168})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.2328314781188965})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4879255294799805})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.612868070602417})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5964, 'crossentropy': 2.8914900390625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 18598], ['ood', 32504], ['ood', 41945], ['ood', 23086], ['ood', 27419]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3918943098018597, 2.5685882715589545, 3.3912096565005427, 3.9036316471005037, 4.217828239113893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.2400636672973633})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.196803092956543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.664616823196411})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6500654220581055})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 2.4165111328125}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 14260], ['ood', 14661], ['ood', 8029], ['ood', 19791], ['id', 45018]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1685395411726818, 2.114761663730803, 2.904052457966298, 3.490263668375415, 3.8821939867056408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.2927708625793457})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.862351179122925})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.167914628982544})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3130550384521484})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0548853874206543})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9315648078918457})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4495973587036133})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.405984878540039})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5903, 'crossentropy': 3.35634375}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 32504], ['ood', 53479], ['ood', 4827], ['ood', 11030], ['ood', 53038]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.491308038253579, 2.658212076644494, 3.503660463066712, 4.0530209624554985, 4.335216293430586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.2879273891448975})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.9168970584869385})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.141235828399658})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.3723702430725098})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.317981719970703})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.373927593231201})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8890275955200195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6433863639831543})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.22456693649292})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5946, 'crossentropy': 3.70074765625}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 18617], ['ood', 36329], ['ood', 1865], ['ood', 13242], ['ood', 22013]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6626987113733738, 2.8963205745397955, 3.7523952076095437, 4.21122391334907, 4.440464658940217]}
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
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 57328], ['ood', 23421], ['ood', 23704], ['ood', 9523], ['ood', 38365]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4865785138872178, 2.6289402014175507, 3.459202328572074, 3.9879203334080877, 4.289351740292672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.219877243041992})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0340054035186768})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.2968215942382812})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.448615074157715})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 2.41857578125}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 54588], ['ood', 12263], ['ood', 17728], ['ood', 26184], ['ood', 30123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5266740043628344, 2.628947298021838, 3.458421545306356, 3.967403963833929, 4.234321588376705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.38118314743042})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.499889850616455})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.774589776992798})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.995150566101074})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2427501678466797})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6145, 'crossentropy': 2.8970287109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 488], ['ood', 4893], ['ood', 14068], ['ood', 16911], ['ood', 41814]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5974334785340925, 2.804239458674827, 3.6084715190669705, 4.097632424570874, 4.354784653867895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9820345640182495})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.548251152038574})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.974562644958496})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1457509994506836})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6054, 'crossentropy': 2.1927056640625}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 22960], ['ood', 11437], ['ood', 9202], ['ood', 38861], ['ood', 59152]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.354514494137196, 2.373306941686949, 3.1824500672552922, 3.7352176162278408, 4.075068302166847]}
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
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3391010761260986})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.557445526123047})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.85715389251709})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.2659878730773926})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 3.496357421875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 12906], ['ood', 30366], ['ood', 51728], ['ood', 25315], ['id', 36761]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.543608245112429, 2.8017017346423856, 3.7156513026713593, 4.174262585144975, 4.40685886873477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.023300886154175})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.628518581390381})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.689544200897217})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.7912487983703613})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.698679208755493})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.0877926349639893})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.787179470062256})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7513768672943115})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.9996604919433594})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.193113088607788})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.898097515106201})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6428, 'crossentropy': 3.0172806640625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 55038], ['ood', 14129], ['ood', 45294], ['id', 30845], ['id', 52590]], 'labels': [-1, -1, -1, 6, 2], 'scores': [1.5473111932028383, 2.8034978375376416, 3.623222808903779, 4.144110043700232, 4.399799056523347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.043508768081665})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.2955338954925537})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6708531379699707})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1379499435424805})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8167567253112793})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6244, 'crossentropy': 2.4869181640625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 45148], ['ood', 224], ['ood', 34202], ['ood', 12748], ['ood', 22643]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3894304871917258, 2.4799655301628416, 3.2727285203503556, 3.816155909531914, 4.144930867806666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9514379501342773})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.7143337726593018})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9075608253479004})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.10941743850708})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.865138530731201})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1427628993988037})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.434404134750366})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.474514961242676})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.030283203125}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 18026], ['ood', 51004], ['ood', 44955], ['ood', 51477], ['ood', 27413]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5494578282891318, 2.7587060775052556, 3.6461717854703544, 4.12959237146574, 4.3882333631018335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.090501070022583})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5468201637268066})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.957399845123291})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.422844648361206})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.078742504119873})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4158401489257812})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3195509910583496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.868610143661499})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1136932373046875})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5779080390930176})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.941791534423828})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5636041164398193})
store['active_learning_steps'][17]['training']['best_epoch']=9
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6117, 'crossentropy': 3.4438796875}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 31728], ['ood', 24620], ['ood', 42251], ['ood', 22188], ['ood', 47793]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4955477795787913, 2.7414314916919085, 3.5960200068371515, 4.119268526274496, 4.3897076353962206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.895404577255249})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.558999538421631})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7979187965393066})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6351022720336914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.1444127559661865})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 2.699946484375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 20001], ['ood', 341], ['ood', 47636], ['ood', 22679], ['ood', 48430]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4648394168284655, 2.6012947881346324, 3.452927617619686, 3.9475651601791686, 4.259920094515001]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.299445152282715})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.66943359375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.3167190551757812})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.293870449066162})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.9457757472991943})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3698062896728516})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.7707595825195312})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.6450300216674805})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8227617740631104})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.091948986053467})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.8604073524475098})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 3.555468359375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 32056], ['ood', 51477], ['ood', 8074], ['ood', 68], ['ood', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6177562104304881, 2.7984325009428384, 3.6385447630995547, 4.091408847039057, 4.362842108713735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.028439521789551})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6501665115356445})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2888412475585938})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3207995891571045})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.3555643558502197})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1615805625915527})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1788406372070312})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1358895301818848})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.7964792251586914})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.487183094024658})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6061, 'crossentropy': 3.3437296875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 44686], ['ood', 17719], ['ood', 8509], ['ood', 51314], ['id', 44491]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.552019295473928, 2.7621425076059887, 3.5935491354806723, 4.11027361727642, 4.3714166949139255]}
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
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 2.9908953125}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 49418], ['ood', 28533], ['ood', 48176], ['ood', 51071], ['ood', 43823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6382944058928675, 2.9186941684412147, 3.7695918463021787, 4.2216832322698945, 4.419431938505641]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.0326271057128906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3363938331604004})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8764474391937256})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.109680652618408})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.125048875808716})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6138, 'crossentropy': 2.5798119140625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 49474], ['ood', 31514], ['ood', 54134], ['ood', 30051], ['ood', 43683]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4931465310520018, 2.691204393091749, 3.519013432981054, 4.046973255641808, 4.307562793599325]}
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
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.614, 'crossentropy': 3.32263515625}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 14716], ['ood', 906], ['ood', 18273], ['ood', 36744], ['ood', 31020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5991044533448253, 2.7603513422107016, 3.598311330459193, 4.10915317602659, 4.387523581166816]}
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
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 36662], ['ood', 14185], ['ood', 38861], ['ood', 12748], ['ood', 4023]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5153288163796605, 2.7124403516009767, 3.5795594172129137, 4.063061053202796, 4.328825243762242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8620147705078125})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.5410900115966797})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5647847652435303})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.924070119857788})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.8841280937194824})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.825878858566284})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5852737426757812})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 3.1936849609375}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 46590], ['ood', 27181], ['ood', 22626], ['ood', 4688], ['ood', 55314]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4459053739073542, 2.686352696727349, 3.5636775810978376, 4.059073199463281, 4.329705315149064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.2952990531921387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.772312641143799})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8904290199279785})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.012925148010254})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.373868942260742})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.4065451622009277})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.541219711303711})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.5979, 'crossentropy': 3.4116765625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 28563], ['ood', 49418], ['ood', 46441], ['ood', 46551], ['ood', 17542]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5284521864352596, 2.769810973234953, 3.6330653505631245, 4.104446367232385, 4.348534746036769]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.043025016784668})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5856618881225586})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.893023729324341})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0356297492980957})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4330341815948486})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1934008598327637})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.337329387664795})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.4409518241882324})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5238535404205322})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1422595977783203})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2021336555480957})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6102, 'crossentropy': 3.632947265625}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 4927], ['ood', 27344], ['ood', 19523], ['ood', 19187], ['ood', 56866]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5382230378338484, 2.7608634038664848, 3.6603034507676497, 4.144364586997721, 4.395452896409789]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.0597877502441406})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.4295413494110107})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.7087578773498535})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2173659801483154})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2750535011291504})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1192851066589355})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2269420623779297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6419248580932617})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.460376501083374})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4943017959594727})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.518496513366699})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 3.52713125}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 42092], ['ood', 39336], ['ood', 55490], ['ood', 28787], ['id', 43940]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.5576068505128733, 2.7886258099624976, 3.627540079205204, 4.134024485899639, 4.380060745035661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.1449618339538574})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.774778366088867})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2079761028289795})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.483822822570801})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.5895, 'crossentropy': 2.2287013671875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 3701], ['ood', 17882], ['ood', 14163], ['ood', 12748], ['ood', 17480]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.306938914184921, 2.4745956339475192, 3.2129122440993, 3.751530008568162, 4.088780012100257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.125547409057617})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.69352388381958})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.868856906890869})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8983664512634277})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9599967002868652})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.917717933654785})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.288553237915039})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2071871757507324})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.296980857849121})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6341, 'crossentropy': 2.917898046875}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 18313], ['ood', 46711], ['ood', 48337], ['ood', 15215], ['ood', 42325]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5882083564915765, 2.9113779972665403, 3.6979748276112288, 4.1533683586650545, 4.3737908762382025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.062627077102661})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.764385461807251})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1885786056518555})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.832712173461914})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2207465171813965})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.5294864177703857})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.351109027862549})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6098, 'crossentropy': 3.173050390625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 50388], ['ood', 51276], ['ood', 15213], ['ood', 12254], ['ood', 25051]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.684255487326244, 2.9453317621401953, 3.7537708572418307, 4.228657715201684, 4.434282468049139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.070911169052124})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.78768253326416})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1350436210632324})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.063063144683838})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.5883, 'crossentropy': 2.1716197265625}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 10221], ['ood', 9565], ['ood', 4216], ['ood', 49196], ['ood', 52803]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3851072563394515, 2.45763905290215, 3.2064486005299884, 3.690808668754861, 4.043239480643113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.059493064880371})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7363100051879883})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.8413596153259277})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9253287315368652})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2766106128692627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3903143405914307})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.8415074348449707})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6154, 'crossentropy': 2.9827943359375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 1258], ['ood', 22769], ['ood', 12254], ['ood', 54357], ['ood', 31020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4887333275296535, 2.668869321271381, 3.5157316409827475, 4.039881472552949, 4.309537632243303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9778474569320679})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7396769523620605})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8386075496673584})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.00555419921875})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8952746391296387})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.607429027557373})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.436340570449829})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.131222724914551})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.640439033508301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.307448625564575})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3985462188720703})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4432036876678467})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.790409564971924})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6409, 'crossentropy': 3.49619140625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 19983], ['ood', 21871], ['ood', 32461], ['ood', 13890], ['ood', 7406]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5375222896007295, 2.787766188722648, 3.7189177302043586, 4.190192510701747, 4.42682022563833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9910205602645874})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.5261616706848145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9301648139953613})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.113677978515625})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.602, 'crossentropy': 2.16068671875}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 35312], ['ood', 25485], ['ood', 48420], ['ood', 8031], ['ood', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3802212246478018, 2.4045476900420124, 3.188205899333761, 3.753304031364303, 4.085763640726864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.4902870655059814})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3070316314697266})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.808492660522461})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1633903980255127})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.076604127883911})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.3663811683654785})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 2.9654484375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 29166], ['ood', 30626], ['ood', 47220], ['ood', 6364], ['ood', 55517]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.513801231709127, 2.7255896455994266, 3.527260871359019, 4.037437857154103, 4.31843538525957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.08789324760437})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.6194238662719727})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.659687042236328})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.8972482681274414})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.116844654083252})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9742069244384766})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.22735595703125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.634510040283203})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.710660457611084})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6247, 'crossentropy': 3.11063359375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 28900], ['ood', 30279], ['ood', 3362], ['ood', 24620], ['ood', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5920450556685684, 2.92756155956826, 3.745925544271911, 4.192466622629379, 4.406864948279174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9781185388565063})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.682441234588623})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.894376754760742})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.2756288051605225})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3590970039367676})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.592, 'crossentropy': 3.0700232421875}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 13252], ['ood', 44939], ['ood', 16309], ['ood', 20681], ['ood', 16929]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.545641936075926, 2.737571963631321, 3.509931049411903, 4.00449070537376, 4.281920490904975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.0328330993652344})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.869504928588867})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6882476806640625})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0653791427612305})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.032956600189209})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.537794589996338})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.165274143218994})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.5322258472442627})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.072195529937744})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 3.53149375}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 32578], ['ood', 26333], ['id', 4618], ['ood', 55545], ['ood', 36449]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.5057595968804485, 2.733180317902089, 3.6168037072919237, 4.125837392457987, 4.363804604254263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.9919464588165283})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.857654094696045})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8309803009033203})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.507509231567383})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.182859420776367})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2797493934631348})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.5968, 'crossentropy': 3.09019921875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 4829], ['ood', 23283], ['ood', 4765], ['ood', 26761], ['ood', 23441]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.482255329169562, 2.6391521151419175, 3.525618274904474, 4.042554438220307, 4.319262368962001]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.1448416709899902})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6582255363464355})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9847073554992676})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0888454914093018})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.4670958518981934})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.9526848793029785})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.5828, 'crossentropy': 3.28028984375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 55519], ['ood', 35884], ['ood', 7596], ['ood', 48201], ['ood', 35729]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5520320636076654, 2.8538959663129897, 3.6458249657214656, 4.12134491638162, 4.369556669035287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9621143341064453})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.455611228942871})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.762925386428833})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.6964759826660156})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6043, 'crossentropy': 2.0719716796875}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 6364], ['ood', 2036], ['ood', 13600], ['ood', 16989], ['ood', 56833]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2894766244087772, 2.278853735422768, 3.0855251992391857, 3.655255868836468, 3.996456591641035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.0454466342926025})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.7813620567321777})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1683197021484375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.1070902347564697})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6042, 'crossentropy': 2.1502087890625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 25089], ['ood', 39461], ['ood', 38925], ['ood', 7328], ['ood', 54318]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3722798099884868, 2.397020653299047, 3.1715627751618607, 3.7104226203970994, 4.057133156404136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.9748568534851074})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5579659938812256})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8504080772399902})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0983893871307373})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2407500743865967})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.6031906604766846})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8056020736694336})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5306992530822754})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6210272312164307})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 3.54558046875}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 36357], ['ood', 16292], ['ood', 2880], ['ood', 990], ['ood', 55490]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4581402661782477, 2.7118541068930107, 3.6153358020913586, 4.107420667715674, 4.356847909704507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.0951879024505615})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.412649631500244})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.681286334991455})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.921755313873291})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.953899383544922})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1908681392669678})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.5891366004943848})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6237, 'crossentropy': 3.155326953125}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 969], ['ood', 5091], ['ood', 55546], ['ood', 47412], ['ood', 27413]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.565007477940135, 2.8384321821193805, 3.6495619075762384, 4.133255019899934, 4.385065583548983]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9694623947143555})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6333017349243164})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9575178623199463})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.030285596847534})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.5992, 'crossentropy': 2.0968677734375}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 40378], ['ood', 20894], ['ood', 22679], ['ood', 4829], ['ood', 12748]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.243815207039316, 2.2524902855908535, 3.008548811007275, 3.542982090385328, 3.9105927363472803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.8816314935684204})
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
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 2.966178125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 4641], ['ood', 27181], ['ood', 23982], ['ood', 37040], ['ood', 22774]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6811903651913145, 2.976293251770245, 3.809752529130356, 4.253923358629822, 4.470375659590353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.245337963104248})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.702791690826416})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7896828651428223})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.9657840728759766})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.4964144229888916})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6109, 'crossentropy': 2.6732900390625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 10236], ['ood', 10302], ['id', 18729], ['ood', 35158], ['ood', 42749]], 'labels': [-1, -1, 3, -1, -1], 'scores': [1.408571559462958, 2.546190970092441, 3.37186688391167, 3.917901726962687, 4.2465389690315405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.0377910137176514})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.3386261463165283})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.5403027534484863})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1203536987304688})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 2.0783134765625}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 9373], ['ood', 48216], ['ood', 2608], ['ood', 47650], ['ood', 16357]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2796369564490564, 2.3622910960776666, 3.1951253775627935, 3.748749359517583, 4.083901824196713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.214656114578247})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.3657288551330566})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7297141551971436})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.924241542816162})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0383901596069336})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.35200834274292})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.999699592590332})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.319664716720581})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6184, 'crossentropy': 3.0958716796875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 31191], ['ood', 2036], ['ood', 54220], ['ood', 16430], ['ood', 4103]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5459341983552788, 2.776596021208911, 3.6551998595308177, 4.132233251052119, 4.373961938352341]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0400328636169434})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3397865295410156})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.606651782989502})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.923689365386963})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.070155620574951})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8156943321228027})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 2.7129462890625}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 54171], ['ood', 37040], ['ood', 58078], ['ood', 9523], ['ood', 19959]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6011198234386956, 2.8164664204763765, 3.6599961101264133, 4.145506056812806, 4.376925787698383]}
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
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 28517], ['ood', 28900], ['ood', 30776], ['ood', 59726], ['ood', 49138]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3868912451996402, 2.593263718202291, 3.449431224706524, 3.9714524492993837, 4.271551445602175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.0256338119506836})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.844146966934204})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.77432918548584})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.264103889465332})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2413744926452637})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.368192672729492})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.373100757598877})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.773827314376831})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.662506341934204})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.9681434631347656})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.5911, 'crossentropy': 3.720638671875}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 38284], ['ood', 43279], ['ood', 59273], ['ood', 24627], ['ood', 56574]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5618850106809719, 2.8499538988417297, 3.707008906726709, 4.194816905175355, 4.426216925332804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.986133098602295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.8074934482574463})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.1057486534118652})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.0741117000579834})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6048, 'crossentropy': 2.035691015625}
