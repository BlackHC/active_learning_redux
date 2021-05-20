store = {}
store['timestamp']=1621482233
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=71']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=71
store['worker_id']=71
store['num_workers']=80
store['config']={'seed': 1309, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3496556282043457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.954725742340088})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.889444351196289})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9499411582946777})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5999, 'crossentropy': 2.44541015625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3427412509918213})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.3073267936706543})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3281667232513428})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 26737], ['id', 49197], ['id', 2542], ['id', 13412], ['id', 26863]], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.98152252056116, 1.7615774851791333, 2.248268997507913, 2.5393193026486403, 2.697565801153628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.350341796875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.4015493392944336})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0307044982910156})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.787322759628296})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.943817138671875})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.642, 'crossentropy': 2.5185142578125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2119157314300537})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2270915508270264})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1844725608825684})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1885226964950562})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 39386], ['id', 57549], ['id', 31606], ['id', 15933], ['id', 48067]], 'labels': [-1, -1, -1, 2, 9], 'scores': [1.0588365538582307, 1.7631908388309072, 2.2578318025092017, 2.538685496582353, 2.708809778329286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.2024407386779785})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8298797607421875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.297764301300049})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.4462504386901855})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.7088241577148438})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.645089864730835})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6273, 'crossentropy': 3.41195546875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4810250997543335})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4780247211456299})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.474376916885376})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.607311487197876})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.6080950498580933})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 20356], ['id', 50395], ['id', 42805], ['id', 49254], ['id', 58220]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.1730384744691076, 2.072828406423071, 2.678909239905601, 2.944518783691718, 3.068270584347869]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.4190893173217773})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.759744644165039})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.4203529357910156})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.4781532287597656})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2916488647460938})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.7906033992767334})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.7279133796691895})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 4.131513595581055})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6181, 'crossentropy': 3.564840625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3736705780029297})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.368950605392456})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.382400393486023})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.410595178604126})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4057738780975342})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.403921127319336})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4022821187973022})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 30671], ['id', 55008], ['id', 2324], ['id', 3034], ['id', 20412]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0891826875863613, 1.946975549517382, 2.581069895407788, 2.929028525243927, 3.096711726081625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.2375564575195312})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.7260727882385254})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.010122776031494})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.531635284423828})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5612471103668213})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.052334308624268})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.329797267913818})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.6011953353881836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 4.759437561035156})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.247485160827637})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 4.112977981567383})
store['active_learning_steps'][4]['training']['best_epoch']=8
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.597, 'crossentropy': 3.82422421875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4970965385437012})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4805747270584106})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4476053714752197})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4836264848709106})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5183985233306885})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4864940643310547})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4548568725585938})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 15945], ['id', 43930], ['id', 22595], ['id', 39086], ['id', 51331]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1876970505573463, 2.118904393423189, 2.7033078493873592, 3.015773122373796, 3.1745738100342695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.7592437267303467})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.334348440170288})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.6853151321411133})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9256865978240967})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.909907341003418})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6334, 'crossentropy': 2.4226080078125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1639320850372314})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1938663721084595})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1175041198730469})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1520105600357056})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 52612], ['id', 59383], ['id', 24096], ['id', 50671], ['id', 58912]], 'labels': [-1, -1, -1, 1, 4], 'scores': [1.1648900842346326, 1.9705470455628262, 2.52587086189269, 2.8528181014612475, 3.012412650720507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8957157135009766})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.3556721210479736})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.754444122314453})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6169772148132324})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.76643705368042})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.8477911949157715})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.232510805130005})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6215, 'crossentropy': 2.7859556640625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.320932149887085})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2261512279510498})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2583680152893066})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2125959396362305})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3001022338867188})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2430243492126465})
store['active_learning_steps'][6]['eval_training']['best_epoch']=6
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 36327], ['id', 46027], ['id', 40743], ['id', 46822], ['id', 56323]], 'labels': [-1, -1, 5, 1, 2], 'scores': [1.2322465970055005, 2.023094307086511, 2.562696955971475, 2.8713665071294567, 3.0126485698606773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6950445175170898})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.2965688705444336})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.550772190093994})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.7641489505767822})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.931650161743164})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1143391132354736})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6416, 'crossentropy': 2.6634515625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2112243175506592})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2615087032318115})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2001500129699707})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2157063484191895})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.189084768295288})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 22250], ['id', 25960], ['id', 43353], ['id', 17697], ['id', 17728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2019379264757264, 2.0963833046739957, 2.6839597364425756, 3.023455260589455, 3.1711885077772575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.6248533725738525})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5126452445983887})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4914650917053223})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6471285820007324})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.791456699371338})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.008823871612549})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6367, 'crossentropy': 2.6333505859375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3300422430038452})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2160879373550415})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2499396800994873})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2040961980819702})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2344653606414795})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 58811], ['id', 14004], ['id', 2731], ['id', 1625], ['id', 5893]], 'labels': [-1, -1, 3, 1, 8], 'scores': [1.1154884742764708, 1.9561210053425535, 2.482108981219886, 2.7913253734538666, 2.9710402477233897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.613747239112854})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.185464382171631})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.623673439025879})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7583887577056885})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4457154273986816})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6428933143615723})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6975903511047363})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.8276727199554443})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.116780996322632})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.162109613418579})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.0906178951263428})
store['active_learning_steps'][9]['training']['best_epoch']=8
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6381, 'crossentropy': 3.0891306640625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2620247602462769})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.405555248260498})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4158399105072021})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3263392448425293})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.352942943572998})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3106013536453247})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3320066928863525})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2530782222747803})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 43156], ['id', 341], ['id', 15412], ['id', 37367], ['id', 49494]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.162344904261171, 2.0008963835532843, 2.5646526110544317, 2.8703347244936372, 3.023981804087544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.8422179222106934})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3486595153808594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.251044750213623})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1303794384002686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.717653274536133})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.104707717895508})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6454, 'crossentropy': 2.5473171875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3197064399719238})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2936198711395264})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2696337699890137})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2238940000534058})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2425975799560547})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 30784], ['id', 49187], ['id', 23421], ['id', 26128], ['id', 53426]], 'labels': [8, -1, -1, 6, 8], 'scores': [1.002160325119708, 1.8640597381029336, 2.376449588961414, 2.6242408033262654, 2.7563658649238016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.9154093265533447})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.4729666709899902})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9433021545410156})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0429019927978516})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.096703052520752})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.167520523071289})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.67935848236084})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1950974464416504})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1335322856903076})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6243, 'crossentropy': 3.362291796875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3255021572113037})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4442741870880127})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4486987590789795})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3201375007629395})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 48643], ['id', 14114], ['id', 9692], ['id', 44735], ['id', 13981]], 'labels': [-1, -1, 4, 1, -1], 'scores': [1.0133421600349195, 1.8199050858181258, 2.386096806986041, 2.7140634026985166, 2.8515260970488647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6254414319992065})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1076107025146484})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5078907012939453})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4697911739349365})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8475828170776367})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.056466579437256})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.655017137527466})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6295, 'crossentropy': 2.779254296875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3444724082946777})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.273952841758728})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2445257902145386})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.320401668548584})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3060941696166992})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2893669605255127})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 53494], ['id', 27419], ['id', 24944], ['id', 14679], ['id', 31853]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.096967197163475, 1.9636766341699579, 2.534691665297869, 2.800597809094466, 2.918996875665359]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4575445652008057})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.996018886566162})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2692480087280273})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4651894569396973})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.622642993927002})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6513, 'crossentropy': 2.0764400390625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1568787097930908})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1657545566558838})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.137752652168274})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1238760948181152})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 36858], ['id', 27026], ['id', 10405], ['id', 42692], ['id', 16928]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.8961175396421894, 1.6224482531975801, 2.1318735026764735, 2.491025451952728, 2.670709386344437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4506933689117432})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8785226345062256})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2176384925842285})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.270042896270752})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.78340482711792})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6501, 'crossentropy': 2.0380982421875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1175439357757568})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1206040382385254})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0827139616012573})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0619193315505981})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 32695], ['id', 10984], ['id', 16692], ['id', 20469], ['id', 41337]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9312883969264114, 1.6818705288758902, 2.240210998678646, 2.6040748035445738, 2.84212001922537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.6225841045379639})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9689792394638062})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.3031845092773438})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.400024175643921})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.849292755126953})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6474, 'crossentropy': 1.9660623046875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1293846368789673})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1271133422851562})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1144192218780518})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1143198013305664})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 28335], ['id', 23564], ['id', 30776], ['id', 41455], ['id', 8537]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.9430995676162319, 1.6896013322373769, 2.270914164935551, 2.630589868669033, 2.827685297464928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.627896785736084})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.064380645751953})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.0723838806152344})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.3736162185668945})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5211997032165527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.6134891510009766})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.647, 'crossentropy': 2.32050859375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2033381462097168})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0981900691986084})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1060881614685059})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1280920505523682})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1201996803283691})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 36260], ['id', 52918], ['id', 13633], ['id', 7647], ['id', 5464]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.0117123160066752, 1.8258467019331972, 2.385497941221418, 2.6574028280174193, 2.8218889705078256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4869033098220825})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.053773880004883})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.271127223968506})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.3852758407592773})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5640134811401367})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6804137229919434})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.8038346767425537})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.664, 'crossentropy': 2.612578125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2237368822097778})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2483527660369873})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.243600845336914})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.204473853111267})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2473113536834717})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2544245719909668})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 31497], ['id', 693], ['id', 25016], ['id', 16376], ['id', 15796]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0266913629941272, 1.881515070337778, 2.390418605125897, 2.685171986584228, 2.835502494056609]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3918105363845825})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.011388063430786})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1336605548858643})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3913049697875977})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4971327781677246})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.8728420734405518})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.707642078399658})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.759080410003662})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6604, 'crossentropy': 2.6490634765625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.208828091621399})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.189956545829773})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1594111919403076})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2078800201416016})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1185799837112427})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1621813774108887})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0992944240570068})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 37084], ['id', 27048], ['id', 23323], ['id', 35384], ['id', 53868]], 'labels': [-1, -1, 5, 2, 3], 'scores': [1.1229010674042326, 1.9145492527527268, 2.4077569187347176, 2.73739300407823, 2.9193540567966387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4249274730682373})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.721801996231079})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.17561674118042})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.190462112426758})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.2048897743225098})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.1876068115234375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.369232177734375})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.600468158721924})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.633375406265259})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.5974907875061035})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6803, 'crossentropy': 2.499123828125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1223801374435425})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.038506031036377})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1127586364746094})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0724868774414062})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1100130081176758})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0425574779510498})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1126618385314941})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1150548458099365})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 42934], ['id', 27421], ['id', 33854], ['id', 31631], ['id', 14580]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0597105441585735, 1.9441978632123522, 2.570266391374144, 2.886823041345833, 3.036652239821729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.263688087463379})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.9089112281799316})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.2564518451690674})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.341566562652588})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.242969512939453})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.385545253753662})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.231632709503174})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.628537654876709})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.7195723056793213})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.380274772644043})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6732, 'crossentropy': 2.665057421875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2163097858428955})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1023776531219482})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2058565616607666})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1627010107040405})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1115658283233643})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 13959], ['id', 8965], ['id', 20356], ['id', 31260], ['id', 41015]], 'labels': [-1, -1, -1, 2, 4], 'scores': [1.1008240311187272, 2.0016383033472884, 2.597829285163299, 2.888276841769824, 3.0269866308858377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4507489204406738})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9666543006896973})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9856369495391846})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.387974739074707})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.546966075897217})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.2693090438842773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.352963924407959})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.547393560409546})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.685711622238159})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.691, 'crossentropy': 2.53171875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1400318145751953})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2068612575531006})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.189753532409668})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1657795906066895})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.1264173984527588})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2072629928588867})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.168461799621582})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.095959186553955})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 55525], ['id', 36745], ['id', 33074], ['id', 57172], ['id', 42737]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.116100933869749, 2.0421153868708144, 2.6237371440872175, 2.9386436316335613, 3.0780244880869034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4570814371109009})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.649033784866333})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.1222589015960693})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.359726905822754})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3875880241394043})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.456402063369751})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6867, 'crossentropy': 2.1985787109375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1351114511489868})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1610028743743896})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.161045789718628})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1807359457015991})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1405344009399414})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 56335], ['id', 448], ['id', 43504], ['id', 45627], ['id', 56165]], 'labels': [-1, -1, -1, 7, 3], 'scores': [0.8937089044557349, 1.6205252599758135, 2.127924965295163, 2.4557783397490596, 2.6602511168165472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3439931869506836})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.5086569786071777})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.859466791152954})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.0250980854034424})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.057191848754883})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.364279270172119})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.2579612731933594})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.2691595554351807})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3071417808532715})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.5232412815093994})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.741778612136841})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.730712413787842})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3493614196777344})
store['active_learning_steps'][23]['training']['best_epoch']=10
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7, 'crossentropy': 2.5768189453125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.173511028289795})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.095418930053711})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.1031215190887451})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1051667928695679})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0952868461608887})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1813366413116455})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1727299690246582})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1698806285858154})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1532810926437378})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1064943075180054})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.16432523727417})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.109144687652588})
store['active_learning_steps'][23]['eval_training']['best_epoch']=12
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 40370], ['id', 45505], ['id', 27423], ['id', 33346], ['id', 35796]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0489781620280079, 1.8961177145042094, 2.518519731800456, 2.8969583778912282, 3.120154174785118]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3075356483459473})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6188709735870361})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.1809515953063965})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.102649688720703})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.413184404373169})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4957761764526367})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.593214273452759})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.686190366744995})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.827251434326172})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.6998801231384277})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.7471933364868164})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.654873847961426})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6715, 'crossentropy': 3.063955859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1344213485717773})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1851658821105957})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1127638816833496})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1476764678955078})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1786315441131592})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1217464208602905})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1786186695098877})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2056958675384521})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1653552055358887})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2233855724334717})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2008382081985474})
store['active_learning_steps'][24]['eval_training']['best_epoch']=10
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4999], ['id', 49433], ['id', 25976], ['id', 42308], ['id', 29376]], 'labels': [-1, -1, 5, -1, 5], 'scores': [1.186889280942439, 2.10736018620924, 2.687538420327643, 2.9892152031650765, 3.0901419371865755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3230676651000977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.559563159942627})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9504194259643555})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.0971572399139404})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.0395655632019043})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.013359308242798})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.437835454940796})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.0876834392547607})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.55108642578125})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6875, 'crossentropy': 2.332117578125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0754437446594238})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1047356128692627})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1270129680633545})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.126786470413208})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.107520341873169})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0552417039871216})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1591317653656006})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 49254], ['id', 54314], ['id', 53378], ['id', 38832], ['id', 34435]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.018124026527961, 1.8056688556462945, 2.3517843358492456, 2.670692705280092, 2.804749780888695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.251469373703003})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6557995080947876})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7879621982574463})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.089601516723633})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.1097359657287598})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6897, 'crossentropy': 1.66840625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1244854927062988})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.041477084159851})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0691814422607422})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0624465942382812})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 19231], ['id', 4469], ['id', 36449], ['id', 50738], ['id', 7695]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9858171195882939, 1.6869823072786412, 2.163856692528598, 2.44317961488093, 2.6010189518981246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4061484336853027})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6152100563049316})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.7618545293807983})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.27860164642334})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3660645484924316})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6822, 'crossentropy': 1.6798560546875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1058080196380615})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.048689365386963})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0626410245895386})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0066781044006348})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 1180], ['id', 31778], ['id', 44462], ['id', 6873], ['id', 52039]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.885160019917729, 1.6958064271122744, 2.234361126739935, 2.5895634728447208, 2.7729481402478244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2484968900680542})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6288511753082275})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8024485111236572})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.9115132093429565})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.001951217651367})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.0098822116851807})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.516350030899048})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.4514384269714355})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6871, 'crossentropy': 2.187230859375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1371608972549438})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1996405124664307})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0962023735046387})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1250959634780884})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.097249984741211})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.107506275177002})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.14506995677948})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 39675], ['id', 2880], ['id', 58560], ['id', 14852], ['id', 39301]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0394787007286976, 1.851290599540663, 2.458631369366656, 2.765994451594021, 2.9116838305139368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4815659523010254})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.6388381719589233})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.8914369344711304})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8170416355133057})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2327463626861572})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.331468343734741})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.4581522941589355})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6898, 'crossentropy': 2.041725390625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1420754194259644})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1291427612304688})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0899667739868164})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.095712423324585})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0830888748168945})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0792406797409058})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 2305], ['id', 9840], ['id', 28126], ['id', 13134], ['id', 6753]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0381122888504728, 1.8594361187184802, 2.4021814685679446, 2.736080779159334, 2.934621133832991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.290343999862671})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.6125776767730713})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8109891414642334})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.9980604648590088})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.1107161045074463})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.9596645832061768})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.312490940093994})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.402545928955078})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6914, 'crossentropy': 2.2698865234375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0902968645095825})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1325263977050781})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.094071388244629})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.10284423828125})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0668116807937622})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0862858295440674})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.078206181526184})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 37210], ['id', 33194], ['id', 15560], ['id', 22058], ['id', 53299]], 'labels': [-1, -1, 2, -1, 2], 'scores': [1.145370907056304, 2.111476415696982, 2.675528830942093, 3.0035185164482243, 3.1460803697557065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2259266376495361})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5239241123199463})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8316118717193604})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.8433871269226074})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.172966957092285})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.3236136436462402})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.4079549312591553})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.698, 'crossentropy': 1.9824796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.098235845565796})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0254545211791992})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0646703243255615})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0692696571350098})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0389288663864136})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.072793960571289})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 20314], ['id', 59826], ['id', 55774], ['id', 54881], ['id', 1080]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.9635551303587937, 1.7906049115319744, 2.286756655535637, 2.541242010462156, 2.618921133998599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.314986228942871})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.7054041624069214})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.834031343460083})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.293675661087036})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.1842284202575684})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.3509676456451416})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.7073974609375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.353834629058838})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.617058753967285})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.6545820236206055})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.6601171493530273})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6974, 'crossentropy': 2.5644634765625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0873135328292847})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.164604902267456})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1895371675491333})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1729505062103271})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.172386646270752})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.170056700706482})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.220000982284546})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1706736087799072})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.198869228363037})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1644705533981323})
store['active_learning_steps'][32]['eval_training']['best_epoch']=10
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 54782], ['id', 31683], ['id', 49361], ['id', 44039], ['id', 52797]], 'labels': [-1, -1, -1, 2, 0], 'scores': [1.0227440874072165, 1.8443477585651649, 2.4082887872753247, 2.6765660513165113, 2.8194090556882196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2621963024139404})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6729295253753662})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8037011623382568})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.082170009613037})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.0158145427703857})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6852, 'crossentropy': 1.6613328125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1495704650878906})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1036221981048584})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0387123823165894})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0380256175994873})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 33169], ['id', 43636], ['id', 38760], ['id', 6623], ['id', 40744]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.8575240798877621, 1.5596109033877834, 2.0538595777272786, 2.368125088554349, 2.54075693687325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1928068399429321})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6228022575378418})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.0194599628448486})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.251410722732544})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2452430725097656})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.3438451290130615})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6914, 'crossentropy': 2.1023943359375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1778331995010376})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0656168460845947})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1430423259735107})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1094365119934082})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.075145959854126})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 44466], ['id', 6506], ['id', 14172], ['id', 7584], ['id', 32301]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0187469478952116, 1.8510700732554815, 2.390970007378624, 2.767488381372216, 3.0200710999735794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2746614217758179})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5871027708053589})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8077666759490967})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9060313701629639})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.1827781200408936})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.328732490539551})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.692, 'crossentropy': 1.9230341796875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.086665153503418})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.112946629524231})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1221866607666016})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1306982040405273})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1552801132202148})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 31051], ['id', 58855], ['id', 32349], ['id', 3657], ['id', 50487]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.9499947447121277, 1.6315356859058188, 2.1414250558968897, 2.492344797167301, 2.6536055003004613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2973498106002808})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3697254657745361})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8491034507751465})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.1755547523498535})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.2795400619506836})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.4209680557250977})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.3109445571899414})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.579744338989258})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.8433728218078613})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6896, 'crossentropy': 2.562046484375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2325057983398438})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1979809999465942})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1637893915176392})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1753740310668945})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2650070190429688})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2518658638000488})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.246422290802002})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 40888], ['id', 6871], ['id', 5815], ['id', 11626], ['id', 41951]], 'labels': [-1, -1, -1, 0, 8], 'scores': [1.0093163204637141, 1.8594478265750143, 2.392389845650087, 2.599456418004684, 2.6896507645450844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.298134207725525})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.458075761795044})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0470731258392334})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8271887302398682})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.222114086151123})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.2521936893463135})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.3332676887512207})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.488658905029297})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6912, 'crossentropy': 2.2150044921875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.144644021987915})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1121416091918945})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0888173580169678})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1884065866470337})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0759868621826172})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0889772176742554})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 20414], ['id', 19226], ['id', 22053], ['id', 25156], ['id', 8843]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.203042153073325, 2.0865650746226585, 2.66931716694463, 2.9356958467913765, 3.0387143443664177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2623112201690674})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.511072039604187})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7716189622879028})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.927351474761963})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.8751647472381592})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.1418638229370117})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.108827590942383})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.090536594390869})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7011, 'crossentropy': 1.984575390625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1933369636535645})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1662408113479614})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1414384841918945})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1437714099884033})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.08870267868042})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0574743747711182})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.119432806968689})
store['active_learning_steps'][38]['eval_training']['best_epoch']=7
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 42583], ['id', 39347], ['id', 28506], ['id', 9396], ['id', 2747]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.9024679627498533, 1.662024854021245, 2.203893824676325, 2.535848241241176, 2.6988857488322253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1398329734802246})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6330504417419434})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.920764446258545})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.05224609375})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 1.1787015625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.036501407623291})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9943522214889526})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9658164381980896})
store['active_learning_steps'][39]['eval_training']['best_epoch']=2
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 35709], ['id', 4904], ['id', 21608], ['id', 7019], ['id', 52613]], 'labels': [-1, -1, -1, 6, 5], 'scores': [0.6865478451410696, 1.2019310412509419, 1.5578556781783792, 1.8217349434170798, 2.0101682552346567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2309930324554443})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4762012958526611})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8867945671081543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.139763116836548})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.1662511825561523})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.238426685333252})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.186154365539551})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.593546152114868})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6862, 'crossentropy': 2.365076171875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1487600803375244})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1792808771133423})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1524804830551147})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1029363870620728})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1226131916046143})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2078619003295898})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 51527], ['id', 59377], ['id', 32450], ['id', 34219], ['id', 9144]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0286110911897246, 1.8265015131506563, 2.4287316100411, 2.771879544579112, 2.9396616538752625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.279343605041504})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5105699300765991})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.654538869857788})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.9732980728149414})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9795401096343994})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.246081829071045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.103973388671875})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2746500968933105})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.2640347480773926})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1562623977661133})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6969, 'crossentropy': 2.256078515625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1380910873413086})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0711140632629395})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0679175853729248})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1139068603515625})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.094623327255249})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0261948108673096})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0363209247589111})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.024161458015442})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0123908519744873})
store['active_learning_steps'][41]['eval_training']['best_epoch']=8
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 10984], ['id', 48069], ['id', 20894], ['id', 49060], ['id', 18917]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.070690344642255, 1.9654276038806313, 2.6315497812636592, 2.9828472513596713, 3.1162194680117157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2793773412704468})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.5104386806488037})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9642843008041382})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8720228672027588})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.140204429626465})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.220027208328247})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.4712002277374268})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.3704662322998047})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.464470863342285})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6947, 'crossentropy': 2.2614435546875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1519403457641602})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0643045902252197})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.080126166343689})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0765056610107422})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1102088689804077})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0949676036834717})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0754663944244385})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 55836], ['id', 58249], ['id', 16464], ['id', 57151], ['id', 37015]], 'labels': [-1, -1, -1, 2, 0], 'scores': [1.125259204554697, 1.9220226656487398, 2.47628233213168, 2.711621598731977, 2.8504472359573256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2227833271026611})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4268066883087158})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.532414436340332})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.770115852355957})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8829065561294556})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.097529649734497})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.2790133953094482})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.4383254051208496})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6897, 'crossentropy': 2.076955078125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1520485877990723})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1342871189117432})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.115821123123169})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1173961162567139})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1148321628570557})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.160534381866455})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.138890266418457})
store['active_learning_steps'][43]['eval_training']['best_epoch']=7
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 14763], ['id', 28186], ['id', 25307], ['id', 14774], ['id', 27171]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9829145916023396, 1.837543010859644, 2.387176725808609, 2.707256078607168, 2.8986597204470694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3246960639953613})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.526287317276001})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8088288307189941})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.0577778816223145})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5551843643188477})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.1678903102874756})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.566174030303955})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.5450997352600098})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.52313494682312})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.6203525066375732})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.6614575386047363})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 3.186720371246338})
store['active_learning_steps'][44]['training']['best_epoch']=9
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6837, 'crossentropy': 2.78310859375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0856215953826904})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.163203239440918})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1328617334365845})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.18808913230896})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1533284187316895})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2721710205078125})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2137575149536133})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1770745515823364})
store['active_learning_steps'][44]['eval_training']['best_epoch']=5
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 25915], ['id', 8557], ['id', 47603], ['id', 56526], ['id', 39954]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.082326111145004, 1.9367386348766187, 2.5417825457321084, 2.866587364730516, 3.02683147536695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3143876791000366})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5591429471969604})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.715916395187378})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8485596179962158})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.1708178520202637})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.3983163833618164})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.278965950012207})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6811, 'crossentropy': 2.079002734375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1898034811019897})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1292448043823242})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1159398555755615})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1244277954101562})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1400997638702393})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1054788827896118})
store['active_learning_steps'][45]['eval_training']['best_epoch']=4
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 36429], ['id', 20820], ['id', 10984], ['id', 10010], ['id', 8433]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9821894073123059, 1.739655309279423, 2.290375880596976, 2.580153926285522, 2.733133291289918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2771689891815186})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4440281391143799})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6955368518829346})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.161935567855835})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.3286280632019043})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.132815361022949})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.3079633712768555})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.54382061958313})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.695925235748291})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.65061092376709})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.5853934288024902})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.700981616973877})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6855, 'crossentropy': 2.7040591796875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1540772914886475})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1967546939849854})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1533160209655762})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1560535430908203})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1710796356201172})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1555328369140625})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2363901138305664})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1653037071228027})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1481101512908936})
store['active_learning_steps'][46]['eval_training']['best_epoch']=6
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 36048], ['id', 59296], ['id', 27274], ['id', 28821], ['id', 27714]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.113973283150199, 2.056179112286299, 2.7293745104732308, 3.055083467963116, 3.2045334741791205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2297911643981934})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4666073322296143})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.9113054275512695})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.9462755918502808})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.1664347648620605})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.329582691192627})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.220937967300415})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.450610637664795})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.4950921535491943})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.605790138244629})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.7131102085113525})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.480185031890869})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.7015, 'crossentropy': 2.435503125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0996395349502563})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1373889446258545})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1250741481781006})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2520041465759277})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.189429759979248})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1955578327178955})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.217376947402954})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.173364520072937})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2074335813522339})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 49077], ['id', 19931], ['id', 12528], ['id', 8118], ['id', 52689]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0100410673554103, 1.8169921886080154, 2.386205039849859, 2.7244841068820804, 2.8463992089364147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.206910252571106})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.445139765739441})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8085908889770508})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.005237340927124})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.026524543762207})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.0228431224823})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.1192171573638916})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.346923828125})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.5189547538757324})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.600013256072998})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.697, 'crossentropy': 2.1241716796875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1986815929412842})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0264089107513428})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0795923471450806})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.083488941192627})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1648340225219727})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1254523992538452})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0917153358459473})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1061447858810425})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.125319242477417})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 33785], ['id', 10676], ['id', 10549], ['id', 36875], ['id', 6522]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.1276711016740397, 2.001208092193682, 2.6200513712413094, 2.9640707826462602, 3.135879752437594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2299485206604004})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4678504467010498})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5581893920898438})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7585058212280273})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.2402091026306152})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.202476978302002})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.433596611022949})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.3007700443267822})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.417750358581543})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6839, 'crossentropy': 2.19341015625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2919175624847412})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2859485149383545})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1933695077896118})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.289283037185669})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2830934524536133})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.244992733001709})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.331934928894043})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1933836936950684})
store['active_learning_steps'][49]['eval_training']['best_epoch']=8
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 21507], ['id', 28451], ['id', 23440], ['id', 2512], ['id', 15427]], 'labels': [-1, -1, -1, 5, 0], 'scores': [1.0063702508306254, 1.7275359702431992, 2.274570324929248, 2.574386889752871, 2.7395261829239725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.168095588684082})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.51307213306427})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6681809425354004})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.8122295141220093})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.367985248565674})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.996757984161377})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.268230438232422})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.694, 'crossentropy': 1.9602162109375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0957343578338623})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.108838438987732})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0888373851776123})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0783789157867432})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0375161170959473})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1005604267120361})
store['active_learning_steps'][50]['eval_training']['best_epoch']=4
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 20631], ['id', 31422], ['id', 31702], ['id', 57620], ['id', 35747]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.008571972535278, 1.8254812061726726, 2.3519109648815153, 2.6343895086921343, 2.7935834837664935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.199500322341919})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3592593669891357})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7227578163146973})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8621087074279785})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.9377423524856567})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6807, 'crossentropy': 1.4649466796875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0904816389083862})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0354681015014648})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.02260160446167})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0701696872711182})
store['active_learning_steps'][51]['eval_training']['best_epoch']=3
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 3868], ['id', 30188], ['id', 49267], ['id', 598], ['id', 9445]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9884208492566051, 1.6869475271571055, 2.227661617782924, 2.5592158313428044, 2.7251163727736287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3008497953414917})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3569941520690918})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6147105693817139})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.748866319656372})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.0077710151672363})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.069831132888794})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2479028701782227})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.695, 'crossentropy': 1.8228361328125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1458094120025635})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0805879831314087})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.039054274559021})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0568220615386963})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1164360046386719})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0860679149627686})
store['active_learning_steps'][52]['eval_training']['best_epoch']=3
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 51435], ['id', 49117], ['id', 30380], ['id', 13585], ['id', 10534]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0045660312839917, 1.7367315937766232, 2.2568860345790016, 2.5816831123345416, 2.7521812488402038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3097591400146484})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3597290515899658})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6313936710357666})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8462867736816406})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.976676106452942})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.1212987899780273})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.2699012756347656})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.05595326423645})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6993, 'crossentropy': 2.024421875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.221081256866455})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1285505294799805})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.080751895904541})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0368802547454834})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0860275030136108})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1271969079971313})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1476140022277832})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 8338], ['id', 12712], ['id', 21113], ['id', 4232], ['id', 35947]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9624492853988991, 1.7402066616082656, 2.315697087055554, 2.706206331997066, 2.8969864207459572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.144026279449463})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2670776844024658})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.4542841911315918})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6891645193099976})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.937711477279663})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.055206775665283})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.1883668899536133})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.7029, 'crossentropy': 1.7517345703125}
