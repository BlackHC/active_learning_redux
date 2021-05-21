store = {}
store['timestamp']=1621474862
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=33']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=33
store['worker_id']=33
store['num_workers']=80
store['config']={'seed': 1269, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.4352903366088867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.0573983192443848})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.4619040489196777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1190996170043945})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.505178689956665})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2118725776672363})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.94419527053833})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5896, 'crossentropy': 3.47516171875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.8857399225234985})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9719297885894775})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.9736194610595703})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.8494101762771606})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.897611379623413})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 25887], ['id', 2835], ['id', 20905], ['id', 8380], ['id', 36158]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0135865569885696, 1.785554135384912, 2.2450430136262, 2.5389407917530615, 2.6945975594844045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.8079921007156372})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.5961523056030273})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.0458168983459473})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.9207866191864014})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5797, 'crossentropy': 1.798627734375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.4779918193817139})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.397444725036621})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.344482660293579})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 33141], ['id', 29923], ['id', 44952], ['id', 5560], ['id', 58030]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4644496988987301, 0.8941979404951974, 1.2529531745528035, 1.537528759108608, 1.763898522916766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.7735382318496704})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.7688632011413574})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.8966310024261475})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.753760576248169})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.448594808578491})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.472238779067993})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.4303183555603027})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5827, 'crossentropy': 3.27396171875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.7124974727630615})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.7858593463897705})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.7231385707855225})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.832632303237915})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.729580283164978})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.7342286109924316})
store['active_learning_steps'][2]['eval_training']['best_epoch']=5
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 59772], ['id', 50210], ['id', 32992], ['id', 12632], ['id', 10570]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6542387602866779, 1.2503188767674738, 1.7127359028992846, 2.0588780195296046, 2.2885823175953837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.7197048664093018})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.2301511764526367})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.527751922607422})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 3.096724510192871})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.144261360168457})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6013, 'crossentropy': 2.285278125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.4443678855895996})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.5019779205322266})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.482372522354126})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.4666491746902466})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 3913], ['id', 8302], ['id', 44], ['id', 23357], ['id', 46975]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5602002522561598, 1.0710443962765703, 1.493845437945562, 1.7843443641216545, 1.9808496673859457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.8097450733184814})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 2.47466778755188})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.5908451080322266})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 3.4811019897460938})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 3.615753173828125})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.4586286544799805})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.5320277214050293})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.2596869468688965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 4.324830055236816})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5695, 'crossentropy': 3.76195625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.589951515197754})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.0360586643218994})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.0617876052856445})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.210564136505127})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.9778518676757812})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.119558334350586})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.094851016998291})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 274], ['id', 872], ['id', 30837], ['id', 24153], ['id', 20644]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.683133478849286, 1.223978139802202, 1.6817408627643715, 2.0280235350636993, 2.2553665314408295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.680261254310608})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 2.471367835998535})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.7907114028930664})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.067999839782715})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.3258323669433594})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 3.616856098175049})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.5773274898529053})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.889594078063965})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5924, 'crossentropy': 3.278112890625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.5707201957702637})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8037199974060059})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.72219979763031})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8261197805404663})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.9059784412384033})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7881174087524414})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 49164], ['id', 50075], ['id', 1361], ['id', 51113], ['id', 6963]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7199553091184229, 1.2664393552203386, 1.7141819722827325, 2.0539155989610296, 2.281222280623374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.4676992893218994})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.854423999786377})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.0735137462615967})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2204039096832275})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6291260719299316})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.602884292602539})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6621108055114746})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6381, 'crossentropy': 2.2527486328125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.4991261959075928})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.575865626335144})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6435070037841797})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.6004581451416016})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.510094404220581})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.6278553009033203})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 10217], ['id', 48222], ['id', 53134], ['id', 5413], ['id', 16724]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5460843131022652, 1.0490920397777135, 1.510033565036351, 1.8167851647141413, 2.03941866114687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.342942714691162})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5476547479629517})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.773478388786316})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.8474349975585938})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.200131416320801})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.1064670085906982})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.29783296585083})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.296840190887451})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.2093582153320312})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4692630767822266})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6618571281433105})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6366, 'crossentropy': 2.337933984375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.3077881336212158})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.402488112449646})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4625458717346191})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4050712585449219})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3984730243682861})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3930909633636475})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3662492036819458})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3796570301055908})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 57132], ['id', 26395], ['id', 38573], ['id', 59634], ['id', 35697]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7242129715464545, 1.3049801886213899, 1.7867739125448, 2.1645262932616056, 2.4442644060194914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1908668279647827})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3545341491699219})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.575889229774475})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.632310152053833})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8150900602340698})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9145478010177612})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0594334602355957})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6863, 'crossentropy': 1.703403125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1816719770431519})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.263798713684082})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2146191596984863})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1707360744476318})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1614892482757568})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1918320655822754})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 54813], ['id', 51318], ['id', 4175], ['id', 36775], ['id', 5188]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5477233707368871, 1.001293285514404, 1.3606672054793698, 1.6418606784318248, 1.8411431371129865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.262742280960083})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.335799217224121})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5803251266479492})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9726901054382324})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.9448397159576416})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.0702221393585205})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9258719682693481})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.0180630683898926})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.072133779525757})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.24198055267334})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.393749952316284})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.153684616088867})
store['active_learning_steps'][9]['training']['best_epoch']=9
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6752, 'crossentropy': 2.120584765625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2953323125839233})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.4354753494262695})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3178870677947998})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3869463205337524})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3242746591567993})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.324295997619629})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2407801151275635})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3030833005905151})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.258477807044983})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3412772417068481})
store['active_learning_steps'][9]['eval_training']['best_epoch']=7
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 45164], ['id', 8617], ['id', 24702], ['id', 3301], ['id', 41879]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5860268341315026, 1.1320174512363907, 1.5607274462811098, 1.8663406424808358, 2.1058160173683342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.3104496002197266})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2900800704956055})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.554890751838684})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6084043979644775})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.015735149383545})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.901268720626831})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.0585992336273193})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6645, 'crossentropy': 1.7141380859375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.3301178216934204})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2119213342666626})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2335225343704224})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.207242727279663})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.180748701095581})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2231764793395996})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 13650], ['id', 29478], ['id', 39750], ['id', 36424], ['id', 12188]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5130811441067478, 0.9930258463370127, 1.3977825027331239, 1.6782864418399353, 1.8863418162832346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.304711103439331})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4320564270019531})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6815294027328491})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.8132011890411377})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9079782962799072})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.1153759956359863})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3374807834625244})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1546096801757812})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6629, 'crossentropy': 1.9237658203125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3317174911499023})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2140798568725586})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2132933139801025})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2529001235961914})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.278536319732666})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2129379510879517})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59703], ['id', 58451], ['id', 44063], ['id', 45826], ['id', 50143]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41064165684207365, 0.8065054331688017, 1.1492072178998685, 1.428945003007894, 1.6320902754232751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.3502792119979858})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3124723434448242})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4683761596679688})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5818105936050415})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9939680099487305})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.058102607727051})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0764522552490234})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.2239174842834473})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.0284459590911865})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6696, 'crossentropy': 2.072009765625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3067511320114136})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.264446496963501})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2357420921325684})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.33334481716156})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.366998553276062})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.366459608078003})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2482271194458008})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 38551], ['id', 22352], ['id', 10299], ['id', 46547], ['id', 23326]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5118608920561749, 0.9661582942401461, 1.3296741155117369, 1.589703565589872, 1.7869144319919723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3012821674346924})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3727151155471802})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.404510498046875})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5682064294815063})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7596527338027954})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.9693183898925781})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8997697830200195})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6922, 'crossentropy': 1.581430078125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3257930278778076})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1352784633636475})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1534582376480103})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1107765436172485})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.11687433719635})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.119004726409912})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37251], ['id', 53306], ['id', 34821], ['id', 9495], ['id', 14622]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4647529641761883, 0.8709305275271979, 1.2276674794113855, 1.5234890941128985, 1.7345499268714129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.3113459348678589})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2605719566345215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.332756519317627})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.559553623199463})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6075401306152344})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.014221429824829})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8838183879852295})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.029696464538574})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.249479055404663})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.317711353302002})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.684, 'crossentropy': 1.9603857421875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.304178237915039})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1802818775177002})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2649105787277222})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2733993530273438})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3185698986053467})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.3187321424484253})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2263858318328857})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3177199363708496})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1972315311431885})
store['active_learning_steps'][14]['eval_training']['best_epoch']=9
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 7238], ['id', 20270], ['id', 15420], ['id', 501], ['id', 4785]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.600687144508274, 1.0855947280033131, 1.5006890644868816, 1.830560131642975, 2.093635591335186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.242319941520691})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2515287399291992})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4873595237731934})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5780436992645264})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7529160976409912})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.0578665733337402})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6864, 'crossentropy': 1.39499013671875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3772510290145874})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1917665004730225})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0844101905822754})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1047669649124146})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1142895221710205})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14667], ['id', 21935], ['id', 31662], ['id', 55968], ['id', 3293]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5065081582530035, 0.8939813526251106, 1.2268139045611957, 1.502476524516192, 1.7338669099513622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.4887549877166748})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1955894231796265})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2808480262756348})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.440834641456604})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.7161364555358887})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.7509504556655884})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.843583583831787})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.976067066192627})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6749, 'crossentropy': 1.6751994140625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.3194338083267212})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2648265361785889})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2169430255889893})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2240900993347168})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1801550388336182})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1825060844421387})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1720139980316162})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 25465], ['id', 18126], ['id', 108], ['id', 55906], ['id', 27131]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.601912092687614, 1.1314410148532574, 1.5674715472739518, 1.9358017962461878, 2.224625862435853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.372178316116333})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.232985019683838})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.378807783126831})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.443648338317871})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.641196370124817})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9516918659210205})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.045875072479248})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.010251998901367})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3979005813598633})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6687, 'crossentropy': 1.9564841796875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.3489105701446533})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1649372577667236})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2070882320404053})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2215080261230469})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2565070390701294})
store['active_learning_steps'][17]['eval_training']['best_epoch']=2
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 36117], ['id', 48480], ['id', 2682], ['id', 49864], ['id', 34446]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5427371366418758, 1.0129074435755134, 1.4218912991121222, 1.7382002118804705, 1.9817669741200143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3707878589630127})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2132288217544556})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3363215923309326})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5905789136886597})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.762242078781128})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.1416382789611816})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.9324634075164795})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6737, 'crossentropy': 1.602178125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.216630458831787})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1693795919418335})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1364967823028564})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1407818794250488})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.205507755279541})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1579982042312622})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 58301], ['id', 22734], ['id', 28632], ['id', 41922], ['id', 48841]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5143382942815924, 0.955062427014786, 1.3552532021932011, 1.6900873315965965, 1.9532604265153326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.4075253009796143})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1819541454315186})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1893324851989746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4203310012817383})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4574627876281738})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7172635793685913})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8611528873443604})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0528793334960938})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6631, 'crossentropy': 1.5089509765625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.4047966003417969})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.1296088695526123})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1000313758850098})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0905961990356445})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0645822286605835})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0768721103668213})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.030097484588623})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27863], ['id', 27800], ['id', 20624], ['id', 10539], ['id', 52331]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6367070560291557, 1.1525693673209831, 1.526189001986351, 1.8324721626804985, 2.0685325868298516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.4146530628204346})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1871737241744995})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2848765850067139})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.3219316005706787})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4627971649169922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5084874629974365})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7183490991592407})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.774296522140503})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8166943788528442})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7039, 'crossentropy': 1.7111642578125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3154211044311523})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1660187244415283})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.155604600906372})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1469173431396484})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2297942638397217})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1414501667022705})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1356618404388428})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1594271659851074})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 36504], ['id', 34743], ['id', 28367], ['id', 59448], ['id', 57315]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.501373959677347, 0.9581021548430146, 1.351615874618013, 1.6717060802867323, 1.9198767141915658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.407716989517212})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1599016189575195})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2277028560638428})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.5390138626098633})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.498896837234497})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.717850923538208})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7482800483703613})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7826573848724365})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8695111274719238})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.130218744277954})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.260615348815918})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7067, 'crossentropy': 1.8397837890625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.346171498298645})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1480391025543213})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1263587474822998})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1118545532226562})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.150418996810913})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1556880474090576})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1169487237930298})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.222337007522583})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 8904], ['id', 47079], ['id', 16370], ['id', 1595], ['id', 21586]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5898524231246491, 1.0532999079234422, 1.452342612540133, 1.7553105886916018, 1.9636500917266284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.408888816833496})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2148652076721191})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2308456897735596})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.393970012664795})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4539196491241455})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4842233657836914})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6929186582565308})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.180199146270752})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9684314727783203})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.171501636505127})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.1524040699005127})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9816780090332031})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7072, 'crossentropy': 2.09211015625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3522007465362549})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1514050960540771})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1181809902191162})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.136042833328247})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2405552864074707})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1349143981933594})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1667712926864624})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2210159301757812})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1622779369354248})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 9297], ['id', 10651], ['id', 19169], ['id', 47158], ['id', 38618]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.58158111302046, 1.081519151850792, 1.5129817524837152, 1.8464282017846694, 2.080276821749342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3785042762756348})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1454508304595947})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2746047973632812})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3856923580169678})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.453395962715149})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.71695876121521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.031339168548584})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.2774136066436768})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0661988258361816})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.093148708343506})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.263401508331299})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.3185782432556152})
store['active_learning_steps'][23]['training']['best_epoch']=9
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7006, 'crossentropy': 1.992790234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3027775287628174})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0830745697021484})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0699927806854248})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1864404678344727})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.219201683998108})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0972208976745605})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1606429815292358})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.10795259475708})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.153170108795166})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.102875828742981})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1121299266815186})
store['active_learning_steps'][23]['eval_training']['best_epoch']=9
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 34172], ['id', 33461], ['id', 36568], ['id', 59674], ['id', 31449]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6411393839272155, 1.201203046668144, 1.6989083332869939, 2.0685197261550705, 2.326750592419719]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.4431877136230469})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1340038776397705})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.030164122581482})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.356783390045166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2789011001586914})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6667544841766357})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.5757887363433838})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6971561908721924})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.718, 'crossentropy': 1.4235890625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3017268180847168})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0047621726989746})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9333192110061646})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9457733631134033})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9598608016967773})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.8808566331863403})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.8981592655181885})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 33781], ['id', 55037], ['id', 25069], ['id', 13598], ['id', 38003]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6232351479418439, 1.1459726183499295, 1.5962195241980823, 1.9557340639405716, 2.201161575400901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.345774531364441})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1175639629364014})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.104438066482544})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1100229024887085})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3115731477737427})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.4638898372650146})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.4447011947631836})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.7325010299682617})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5713164806365967})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6543327569961548})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.7541754245758057})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.7600350379943848})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6941003799438477})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.8430836200714111})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.9712646007537842})
store['active_learning_steps'][25]['training']['best_epoch']=12
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7158, 'crossentropy': 1.9684509765625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2286736965179443})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0085999965667725})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0457638502120972})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0234386920928955})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0506315231323242})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0575227737426758})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0187621116638184})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0179672241210938})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0449246168136597})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0201135873794556})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 51688], ['id', 4554], ['id', 10960], ['id', 8488], ['id', 42160]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6346145147785681, 1.1771984818463572, 1.6437358900084087, 2.0235485508873996, 2.28904445128845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3576769828796387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1062281131744385})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.231520414352417})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3206655979156494})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5399394035339355})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4441053867340088})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5119285583496094})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.801408290863037})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.8820128440856934})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5850012302398682})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8882591724395752})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7291, 'crossentropy': 1.8351845703125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2838704586029053})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0527009963989258})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0021135807037354})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.098597526550293})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1217656135559082})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1108181476593018})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.1320222616195679})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0118582248687744})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.064465045928955})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0563284158706665})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 34238], ['id', 14412], ['id', 31037], ['id', 51952], ['id', 44088]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7195626813105513, 1.2881267244742405, 1.7559333312744112, 2.108715389336809, 2.3638509354700767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3230795860290527})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0944507122039795})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.133875846862793})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1435039043426514})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.259401559829712})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3782594203948975})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4986679553985596})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7158, 'crossentropy': 1.2188298828125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1981663703918457})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0169909000396729})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9629287123680115})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9339390993118286})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9023720026016235})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9310221672058105})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 39766], ['id', 1381], ['id', 2574], ['id', 2181], ['id', 25057]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5329589327762949, 1.0121256953334576, 1.3723242193547796, 1.6854168521981778, 1.9285072661632956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.280095100402832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0782639980316162})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1015887260437012})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.225031852722168})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.2738958597183228})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4093403816223145})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5475578308105469})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.614424228668213})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5903284549713135})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7269, 'crossentropy': 1.46464443359375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2141971588134766})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0730652809143066})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0622318983078003})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0208706855773926})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.033093810081482})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0509382486343384})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0481369495391846})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0154082775115967})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 31242], ['id', 40168], ['id', 372], ['id', 17481], ['id', 49996]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4700682546697378, 0.907289490102035, 1.2742544696989198, 1.5846701259082128, 1.8384650346056617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2758126258850098})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0544116497039795})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.127563714981079})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1886709928512573})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.365886926651001})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3725783824920654})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3850622177124023})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.4435756206512451})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6335396766662598})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7302, 'crossentropy': 1.41666767578125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2729804515838623})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0040298700332642})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9833354949951172})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9656237363815308})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0193355083465576})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9921878576278687})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.020298957824707})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.9972109794616699})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20302], ['id', 56086], ['id', 15800], ['id', 56860], ['id', 40506]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5567737891345474, 1.0302447347328738, 1.4469063203003545, 1.7885391992042718, 2.0194568151816066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4595595598220825})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0880359411239624})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0559334754943848})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1373810768127441})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.182450771331787})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.233393907546997})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3929202556610107})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4709652662277222})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.480884075164795})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7201, 'crossentropy': 1.355422265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3347668647766113})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.108452558517456})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0098447799682617})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9636765718460083})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9719298481941223})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9791252613067627})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9593960046768188})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9445284605026245})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 32065], ['id', 7949], ['id', 4147], ['id', 39951], ['id', 12963]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5593705652250431, 1.0443232100925355, 1.451890358650389, 1.789249512680576, 2.0334825383785455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3603806495666504})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.089469075202942})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0680742263793945})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1504406929016113})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3035457134246826})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3615789413452148})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7182, 'crossentropy': 1.1449189453125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2345116138458252})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0590953826904297})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0130376815795898})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9791304469108582})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.95988929271698})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 51167], ['id', 52223], ['id', 32882], ['id', 10350], ['id', 52168]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.45557713128547683, 0.8596550634697153, 1.206033209998525, 1.5086610581416675, 1.7519893970516591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.3467110395431519})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0542415380477905})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0812197923660278})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2348592281341553})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1683251857757568})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.2621538639068604})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4031667709350586})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.4287166595458984})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.722917079925537})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.4036169052124023})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.7152364253997803})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.8206236362457275})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.9143729209899902})
store['active_learning_steps'][32]['training']['best_epoch']=10
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7339, 'crossentropy': 1.59994755859375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3319344520568848})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0740392208099365})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0478085279464722})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.045060396194458})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0384080410003662})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0456956624984741})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.066077470779419})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0319410562515259})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.027742862701416})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9751771092414856})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 40395], ['id', 14500], ['id', 628], ['id', 15605], ['id', 9227]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4944058695847129, 0.9404742084710218, 1.3452513391398142, 1.6707015359964847, 1.9217872628056494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.4539268016815186})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1008535623550415})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0291621685028076})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.079554557800293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.155450463294983})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2340961694717407})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.365842342376709})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3672373294830322})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.482184886932373})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.47491455078125})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.602036476135254})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6506471633911133})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.8151261806488037})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7296, 'crossentropy': 1.60165224609375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2970950603485107})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0920422077178955})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0786292552947998})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0562725067138672})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9941304326057434})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.037748098373413})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0260746479034424})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0000625848770142})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9912847876548767})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 54352], ['id', 16870], ['id', 34503], ['id', 13663], ['id', 39615]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5338166673267424, 0.9974085247138555, 1.4000251947071285, 1.7203070198095478, 1.948133246493203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.4960116147994995})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1704277992248535})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0746994018554688})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0431349277496338})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0512218475341797})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1112972497940063})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1684060096740723})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.263670802116394})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.345454216003418})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.527258276939392})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4545087814331055})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.508582592010498})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7295, 'crossentropy': 1.42764208984375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.4689593315124512})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0723204612731934})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9987263679504395})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0277235507965088})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9735334515571594})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0264803171157837})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0088833570480347})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9398459792137146})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9712391495704651})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.981458306312561})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9438058137893677})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 34744], ['id', 46619], ['id', 44011], ['id', 20328], ['id', 45570]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7005309351729931, 1.2359700447439401, 1.7145409447497766, 2.076040108273701, 2.346312059543407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3230500221252441})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1058149337768555})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1087148189544678})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1189597845077515})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1603779792785645})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4008524417877197})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.402920126914978})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5941581726074219})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7292, 'crossentropy': 1.25982177734375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3403434753417969})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0680863857269287})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9558488130569458})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9247158169746399})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8835685849189758})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9022156000137329})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8713037967681885})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 35668], ['id', 34358], ['id', 32052], ['id', 9711], ['id', 47927]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47175402636254027, 0.9117929445344557, 1.296454640424093, 1.6119601706901623, 1.8543630583241821]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.4090802669525146})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1504619121551514})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1269268989562988})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0463687181472778})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2397902011871338})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.2570804357528687})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3067772388458252})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3524292707443237})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.5729851722717285})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.5990277528762817})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7276, 'crossentropy': 1.412781640625}
